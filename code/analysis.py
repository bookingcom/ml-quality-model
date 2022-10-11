import os
from typing import Callable, Dict, List, Set

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import pearsonr
from sklearn.metrics import cohen_kappa_score
from tqdm import notebook
import random

from prioritization_framework import get_n_practices_brute_force, get_n_practices_greedy


def read_public_scores(csv_path: str) -> pd.DataFrame:
    scores = pd.read_csv(csv_path, sep="\t")

    scores.loc[:, "Score Annotator A"] = scores.loc[:, "Score Annotator A"].astype(int)
    scores.loc[:, "Score Annotator B"] = scores.loc[:, "Score Annotator B"].astype(int)
    scores["Score"] = scores[["Score Annotator A", "Score Annotator B"]].mean(axis=1)

    return scores


def read_public_and_private_scores(csv_path: str, normalise: bool = True) -> pd.DataFrame:

    scores = pd.read_csv(csv_path, sep="\t", header=0)

    if normalise:
        return normalize_scores(dataframe_w_scores=scores, max_score=4.0)
    else:
        return scores


def compute_agreement_between_practitioners(
    weights: pd.DataFrame,
    prefix: str,
    agreement_func: callable,
) -> pd.DataFrame:
    data = {}
    cols = sorted(col for col in weights.columns if col.startswith(prefix))
    for col1 in cols:
        name1 = col1[len(prefix) :]
        pers = {}
        for col2 in cols:
            if col1 == col2:
                continue
            name2 = col2[len(prefix) :]
            pers[name2] = agreement_func(weights[col1], weights[col2])
        pers["mean"] = sum(pers.values()) / len(pers)
        data[name1] = pers
    return pd.DataFrame(data)


def kappa_(y1, y2):
    map_unsupported_floats = lambda x: int(x * 4)
    y1 = y1.map(map_unsupported_floats)
    y2 = y2.map(map_unsupported_floats)
    return cohen_kappa_score(y1, y2)


def kappa_large_gap(y1, y2):
    """Compute Cohen's Kappa with only meaningful gaps (a difference of more than 1 step).

    In order to do so correctly, whenever we see a difference of 1 step (0.25 in our vector of range [0,1])
    we randomly choose one of the scores and overwrite the other one, so they would be the same.

    By choosing at random we would approximate the same distribution of scores as the original so the Kappa
    score would still be meaningful (as it takes the score distribution as prior).
    """
    y1, y2 = y1.tolist(), y2.tolist()
    for i, (val1, val2) in enumerate(zip(y1, y2)):
        if abs(val1 - val2) < 0.5:
            new_val = random.choice([val1, val2])
            y1[i], y2[i] = new_val, new_val
    return kappa_(pd.Series(y1), pd.Series(y2))


def normalize_scores(dataframe_w_scores: pd.DataFrame, max_score: float) -> pd.DataFrame:
    dataframe_w_scores[dataframe_w_scores.columns[2:]] = dataframe_w_scores[dataframe_w_scores.columns[2:]].apply(
        lambda x: x / max_score
    )
    return dataframe_w_scores


def create_df_from_csvs(
    csvs: List[str],
    header_row_number: int,
    practice_col: str,
    weights_col: str,
    subchar_col: str,
) -> pd.DataFrame:
    """
    Creates dataframe from a list of csv files. It is important that the name of practice, weights and quality
    sub-characteristic columns are the same among the csvs.
    """
    dataframes = []
    for csv_file in csvs:
        loaded_df = create_dataframe_from_csv(
            csv_file,
            header_row_number=header_row_number,
            practice_col=practice_col,
            subchar_col=subchar_col,
            weights_col=weights_col,
        )
        dataframes.append(loaded_df)

    merged = dataframes[0]
    for dataframe in dataframes[1:]:
        merged = merged.join(dataframe, how="left")

    return merged


def create_dataframe_from_csv(
    vectors: str,
    header_row_number: int,
    practice_col: str,
    weights_col: str,
    subchar_col: str,
) -> pd.DataFrame:
    vectors_df = pd.read_csv(vectors, header=header_row_number)

    csv_name = extract_name_from_csv_path(vectors)
    new_weight_col_name = "weights_" + csv_name
    vectors_df.rename(columns={weights_col: new_weight_col_name}, inplace=True)

    vectors_df.set_index([subchar_col, practice_col], verify_integrity=True, inplace=True)

    return vectors_df[[new_weight_col_name]]


def extract_name_from_csv_path(csv_path: str):
    return os.path.basename(csv_path).partition(".")[0]


def get_cumulative_scales(weights: List[int]) -> List[int]:
    return np.insert(np.cumprod(weights), 0, 0)


def score_sub_chars(
    practice_score_f: Callable[[str, str], int],
    practices_available: Set[str],
    sub_chars: Set[str],
) -> Dict[str, int]:
    score_for_sub_char = {sub_char: 0 for sub_char in sub_chars}
    for sub_char in sub_chars:
        for practice in practices_available:
            score_for_sub_char[sub_char] += practice_score_f(sub_char, practice)
    return score_for_sub_char


def which_are_covered(
    score_per_subchar: Dict[str, int],
    covered_score: int,
) -> Dict[str, bool]:
    return {practice: score >= covered_score for practice, score in score_per_subchar.items()}


def plot_set_contributions(points_for_all_practices: dict, title: str, index: str) -> None:
    scale_cumulative = get_cumulative_scales(weights=[1, 2, 3, 4])

    plt.subplots(figsize=[12, 12])
    sns.set_context("poster")

    points_for_all_practices[index]["Sum of scores"].plot.barh(color="black")
    plt.axvline(
        scale_cumulative[-1],
        color="red",
        ls="--",
        label=f"Covered at {scale_cumulative[-1]} points",
    )
    title = title + "\n"
    plt.title(title)
    plt.xlabel("Weighted contribution score")
    plt.ylabel("")
    sns.despine()

    plt.legend()


def plot_quality_coverage(merged_practices: pd.Series) -> None:
    sub_chars = set(list(merged_practices.index.get_level_values(0).unique()))
    practices = set(merged_practices.index.get_level_values(1))
    covered_score = get_cumulative_scales(weights=[1, 2, 3, 4])[-1]

    practice_score_f = lambda sub_char, practice: merged_practices.loc[(sub_char, practice)]
    xs = []
    ys = []
    for num_practices in range(1, len(practices)):
        practices_to_adopt = get_n_practices_greedy(
            practice_score_f=practice_score_f,
            practices_available=practices.copy(),
            sub_chars=sub_chars.copy(),
            num_practices=num_practices,
            covered_score=covered_score,
        )

        scores = score_sub_chars(practice_score_f, practices_to_adopt, sub_chars)
        coverage_results = which_are_covered(scores, covered_score)
        not_covered = [sub_char for sub_char, is_covered in coverage_results.items() if not is_covered]

        xs.append(num_practices)
        ys.append((len(sub_chars) - len(not_covered)) / len(sub_chars))

        if len(not_covered) == 0:
            break

    plt.subplots(figsize=[12, 7.5])
    sns.set_context("poster")

    plt.plot(xs, ys, color="black")
    title = "Quality Coverage"
    plt.title(title)
    plt.xlabel("Number of practices chosen by greedy")
    plt.ylabel("Coverage Fraction")
    sns.despine()


def piecewise_linear_function(x: float) -> float:
    if x > 4 or x < 0:
        raise ValueError(f"Not supported domain of x = {x}")

    if x >= 0 and x <= 2:
        return x
    if x >= 2 and x <= 3:
        return x * 4 - 6
    if x >= 3:
        return x * 18 - 48


piecewise_linear_function = np.vectorize(piecewise_linear_function)


def convert(series: pd.Series) -> pd.Series:
    return piecewise_linear_function(series)


def randomly_permute(x: int, lb: int, up: int) -> int:
    return max(0, min(4, x + np.random.randint(lb, up)))


def sensitivity_analysis(
    N: int, name: str, permutation_f: Callable[[str, str], float], practices: pd.DataFrame
) -> np.array:
    results = []
    for i in notebook.tqdm(range(N), desc=name):
        randomly_permuted_score = practices["Score"].apply(lambda x: permutation_f(x))

        permuted_merged = practices.copy()
        permuted_merged["Score_Scaled"] = convert(randomly_permuted_score)

        sum_permuted = permuted_merged.groupby("Subcharacteristics")["Score_Scaled"].agg([np.sum]).sort_values(by="sum")

        sum_original = practices.groupby("Subcharacteristics")["Score_Scaled"].agg([np.sum]).sort_values(by="sum")

        ranked = sum_permuted[["sum"]].join(sum_original[["sum"]], rsuffix="_original").rank()
        results.append(pearsonr(ranked["sum"], ranked["sum_original"])[0])

    results = np.array(results)

    return results
