import itertools
from typing import Callable, Set


def get_n_practices_brute_force(
    practice_score_f: Callable[[str, str], int],
    practices_available: Set[str],
    sub_chars: Set[str],
    num_practices: int,
    covered_score: int,
) -> Set[str]:
    """
    :param practice_score_f:
        Function returning the score for a sub characteristic and practice. Needs to return
        a score for each of `sub_chars`x`practices_available`
    :param practices_available:
        Set of all available practices.
    :param sub_chars:
        Set of selected sub characteristic we wish to cover
    :param num_practices:
        Budget of practices we can implement
    :param covered_score:
        The score we consider as covering a given sub characteristic.
    :return:
        A set of practices. Caution: the resulting list is not necessarily a feasible solution covering
        all sub-characteristics. If a feasible solution does not exist, the next best is returned.
    """
    best_solution = None
    best_solution_score = None

    for selected_practices in itertools.combinations(
        practices_available, num_practices
    ):
        sub_char_points = {sub_char: covered_score for sub_char in sub_chars}

        for practice in selected_practices:
            for sub_char in sub_chars:
                sub_char_points[sub_char] -= practice_score_f(sub_char, practice)
                sub_char_points[sub_char] = max(0, sub_char_points[sub_char])

        score_achieved = sum(sub_char_points.values())

        if best_solution_score is None:
            best_solution = selected_practices
            best_solution_score = score_achieved
        else:
            if best_solution_score > score_achieved:
                best_solution_score = score_achieved
                best_solution = selected_practices

    return set(best_solution)


def get_n_practices_greedy(
    practice_score_f: Callable[[str, str], int],
    practices_available: Set[str],
    sub_chars: Set[str],
    num_practices: int,
    covered_score: int,
) -> Set[str]:
    """
    :param practice_score_f:
        Function returning the score for a sub characteristic and practice. Needs to return
        a score for each of `sub_chars`x`practices_available`
    :param practices_available:
        Set of all available practices.
    :param sub_chars:
        Set of selected sub characteristic we wish to cover
    :param num_practices:
        Budget of practices we can implement
    :param covered_score:
        The score we consider as covering a given sub characteristic.
    :return:
        A set of practices. Caution: the resulting list is not necessarily a feasible solution covering
        all sub-characteristics. If a feasible solution does not exist, the next best is returned.
    """
    covered: Set[str] = set()
    selected_practices: Set[str] = set()
    left_to_cover = {sub_char: covered_score for sub_char in sub_chars}
    num_rounds = 0

    while covered != sub_chars and num_rounds < num_practices:
        num_rounds += 1

        scored_practices = []

        for practice in practices_available:
            scaled_score = 0
            for sub_char in sub_chars.difference(covered):
                scaled_score += practice_score_f(sub_char, practice)
            scored_practices.append((practice, scaled_score)),

        # greedy selection by the most r points a practice achieves on all sub characteristics
        selected_practice, _ = sorted(scored_practices, key=lambda x: -x[1])[0]

        # Apply the selected practice to each sub-characteristic
        for sub_char in list(left_to_cover.keys()):
            left_to_cover[sub_char] -= practice_score_f(sub_char, selected_practice)

            # Once a sub characteristic is covered, add it to the set of covered once,
            # we do not need to improve it further
            if left_to_cover[sub_char] <= 0:
                covered.add(sub_char)
                del left_to_cover[sub_char]

        practices_available.remove(selected_practice)
        selected_practices.add(selected_practice)

    return selected_practices
