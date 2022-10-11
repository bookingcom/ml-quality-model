Below we provide the internal set of 41 best practices created from a survey to the ML community about which 
ML best practices the ML practitioners they are most familiar with. The practices have been splitted into categories 
for easier comprehension.


## Reproducible ML lifecycle

### 1. Logging of metadata and artifacts (hyperparams, code version, data used to train, model binary, etc)
Logging of all the relevant information which can help to reproduce the ML model. 
This can be helpful to reproduce a build model artefact, and also understand what went wrong in case of issues. 
Extra thought should be given to versioning the actual runtime environment (see Use of containerized environment) 
and any randomness seeds.


### 2. Code versioning
You make use of software configuration management tools, such as Git, to version your code and be able to go back to 
previous versions at any given point in time. If using more volatile code like notebooks, make sure to save the actual 
code or the latest committed version and diff.


### 3. Data versioning
You version your data at different stages of processing (i.e. raw, after train/test split, after preprocessing), 
 automatically. You can retrieve it easily using a unique identifier to a storage system. 
You don’t overwrite versioned data and keep it for as long as the model’s lifetime.


### 4. Model versioning
Keep track of model versions in production, to understand which model achieved which predictions and evaluation results.

### 5. Documentation
You document your ML system and make the documentation discoverable 
(using a centralized portal or inside the code itself). 
You document both the modeling assumptions and the rationale for them, 
e.g. the reasoning for certain decisions (why certain features are bucketized, why some of the features are excluded, 
what is the intuition behind a custom loss function). 
On top of that, you also document engineering and installation instructions, e.g. all the necessary information that a 
practitioner needs to know in order to be able to train, evaluate, deploy, etc. the ML system. 


### 6. Ownership
Having clear scope around which aspects of the ML system are owned by each individual or team. For example if an
ML system is being used by multiple teams for a variety of use cases, who owns the monitoring of the system’s 
performance for each of those use cases?

### 7. Use of containerized environment 
You use virtualization to create reproducible environments for both training and deployment. 
Any change to the environment is written in the configuration file (Dockerfile/environment.yml), 
and pinned if necessary. This ensures that all the necessary dependencies and settings for both training and deployment 
are pre-installed in the environment, so no extra effort is required for this.




## Monitoring & Alerting

### 8. Model Performance Monitoring
Monitor the ML and business related aspects of your model in production, including:
- Predictions are created and are similar to the testing distribution
- Predictions are correlated with business metrics
- Any proxy metric which can be relevant

### 9. Monitor Feature Drift
You hold invariants of your features as they were distributed when the model was created, 
and monitor production data for any drift that can cause your model to under-perform.


### 11. Monitor Feature Parity
You monitor parity between online and offline features in real-time and alert when changes occur.

### 12. Alerting
Make sure to have alerts (with carefully chosen alerting thresholds) for all the key indicators of an ML system.

## Continuous Integration & Continuous Delivery
### 12. Automate the ML Lifecycle
Every time a change is made in an ML system and the model needs to be re-deployed, the whole ML lifecycle needs to be 
repeated. If this includes many manual steps, there are chances for errors and hence deploying a problematic system 
version. Moreover, running steps manually takes time and leads to resource waste. A way to mitigate these issues is to 
automate the whole ML lifecycle, e.g. data collection, feature engineering, training, evaluation, prediction threshold 
setting and deployment. Whenever a change is made in the system’s code, the pipeline is triggered and a new version of 
the system is automatically deployed into production. Of course there are cases where it is desired to manually inspect 
the model before deployment (possible in business critical applications) so in such cases, it is fine to leave the 
evaluation and deployment step outside of the automated pipeline.

### 13. Automated tests
You test your code and data, both for acceptance and for code correctness. 
You use tools like code coverage to validate your code is well-tested. You unit test the system’s components 
to make sure each of them functions properly in isolation and you create integration tests for the whole pipeline 
to make sure all the components work well together. Every time you make changes to the code, you run the tests to 
make sure that the system works properly.


### 14. Fast development feedback loops
It is preferable to develop an ML system in small iterations without too many changes happening in each iteration. 
This helps with debugging as there are fewer things that can go wrong and it is also simpler to understand what 
worked and what did not when AB testing a certain ML system version. In order to have fast development cycles, 
it is important that we can make fast changes, for example quickly add features or change models and retrain the system. 

## High Quality Features
### 15. Achieve Feature Parity
You make sure that online feature calculation yields the same results as your offline features.
### 16. Keeping the historical features up to date
Regularly update historical features that might need pre-computations, such that the model always uses up-to-date 
features.

### 17. Remove redundant features
In Machine Learning, unnecessary complexity is not desirable as it makes the maintainability of the ML systems harder, 
without improving their performance.  One typical way to add complexity in an ML system without improving the 
performance is by adding redundant features, e.g. features which do not add predictive value. To avoid that, 
feature selection procedures should be applied to make sure the system is as simple as possible without compromising 
the performance.

### 18. Input Data Validation
You apply sanity checks on the data with which the ML model is being trained and evaluated on, to make sure they are
 as expected. 

### 19. Degenerate Feedback Loops
For the cases where the ML system’s features are constantly updated and when those features are influenced by the model 
itself, we might end up with wrong experimentation results if we do not do preventive actions.  


### 20. Dealing with and preventing the consequences of the dependencies created when using an output of a model as input to another.
When a model’s output is being used as input to another model, a small error can be propagated from the source to the 
target model and have a large negative impact. 

Practices which help to deal with and prevent such negative consequences:
- Alerting to the target model that the input of the source model might be broken
- If you own the target model, monitor your feature (the one coming from the source model) distribution 
- Automated retraining and deployment pipeline (in case of an error, fix it quickly)


## Ensure long-lasting commercial value
### 21. Peer Code Review
You request your peers to review your code before going to production. This includes both data processing 
and model training code.

### 22. Bot Detection
You detect and filter out instances made by bots from training and production data.


### 23. ML evaluation metric correlates with the business metric
When developing and deploying an ML system we need to make sure that the offline evaluation metric is a good proxy 
for the business metric used to evaluate the model in production. This means that if we observe a certain improvement 
in the offline evaluation metric, we should also observe this improvement on the production metric. In this way we are 
able to know which of the improvements we apply in the model might be promising, before AB testing them. 


### 24. Mimic production setting in offline evaluation
The offline evaluation of an ML system should mimic the production environment. For example, if a certain feature 
during production has null values, then the same feature should also have null values in the offline test set. If 
online assumptions are not imposed during offline evaluation, we risk having an optimistic offline performance.

### 25. Compare with a baseline
You compare your model with a simple baseline to ensure ML techniques are actually valuable as well as to benchmark
the ML system. 
The simple baseline depends on your model, but it can range anything from a simple heuristic through a 
regular expression to a simple ML model.

### 26. Impact of model staleness is known [[source](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/aad9f93b86b7addfea4c419b9100c6cdd26cacea.pdf)]
Many production ML systems encounter rapidly changing, non-stationary data. Examples include content recommendation 
systems and financial ML applications. For such systems, if the pipeline fails to train and deploy sufficiently 
up-to-date models, we say the model is stale. Understanding how model staleness affects the quality of predictions 
is necessary to determine how frequently to update the model. If predictions are based on a model trained yesterday 
versus last week versus last year, what is the impact on the live metrics of interest? Most models need to be updated 
eventually to account for changes in the external world; a careful assessment is important to decide how often to 
perform the updates


### 27. Code Modularity and Reusability
You write modular and reusable code, doing your best at breaking up large processes into smaller, cohesive chunks. You enable others to re-use your code fragments by generalizing them and pushing them to a centralized code repository.
To promote reusability of your code, make sure you create your functions in ways that enable extensibility, not just modification; these include:
- Program by interface (e.g. array-like) and not by implementation (e.g. using `isinstance`)
- Use the [Dependency Injection](https://en.wikipedia.org/wiki/Dependency_injection) pattern and follow the [Open-Closed Principle](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle)
- Prefer meaningful arguments (e.g. a callable, data structure) over booleans (e.g. use_new_schema) when extending functionality

### 28. Bias Assessment
You assess the differences in the prediction error of the ML systems across sensitive variables (such as country) to 
detect any bias issues.

### 29. Bias Mitigation
You take actions to mitigate the differences in prediction errors across sensitive variables of interest, to make sure
that they are within acceptable thresholds.

### 30. Establish clear success metric before model design
The success criterion for an ML system is something that directly affects the model design choices taken during 
development. For example, the optimal hyper-parameters for a given success metric might be suboptimal for a 
different metric and need to be re-tuned. This is why it is important to think about the evaluation metrics 
(both offline and online) before the design of the model, and take them into account in all the modeling choices. 

### 31. Error analysis
Analyze all the error types in the ML system to understand why it failed and what fixes need to be done to prevent such 
errors in the future.

### 32. Keep the model up to date
Make sure that the ML system is trained on data points that are representative of the current production environment. 

### 33. ML system audit by domain experts
Domain experts periodically audit the ML system to make sure that it complies with any applicable standards. 

## A/B testing

### 34. AB test all model changes
Assess the impact of all the model changes through an AB test.

### 35. Do not test a model which is not promising in offline evaluation
Avoid conducting redundant and costly AB tests when the offline evaluation does not indicate significant differences 
with the current production model. 

### 36. Understand when AB assumptions are violated and seek alternative experimentation framework
Always make sure that key AB testing assumptions 
(for example the [independence assumption](https://www.statisticshowto.com/assumption-of-independence/)) 
are met before conducting an experiment. In case they are not met, find alternative experimentation methods. 

## Infrastructure
### 37. Unified environment for all lifecycle steps
If all the lifecycle steps of a certain ML system are developed in a unified environment it simplifies code reuse, 
shared engineering techniques and patterns, as well as shared code style conventions, development tools, etc. 
For instance, if the training and serving environments are developed in different languages, we risk re-implementing 
the same functionality (e.g. pre or post-processing) in both environments separately.

### 38. Reuse data, supported internal tooling and solutions
Prefer to use org-supported tooling and solutions for your ML needs 
(e.g. serving platforms, features stores, model registries).
This enables better sharing of your work with others, makes managing of infrastructure easier and keeps you 
updated with any enhancements. Moreover, data re-usage especially in the case of costly annotated labels is 
quite beneficial and avoids unnecessary effort and cost.

### 39. Turn experimental code into production code
You move your experimental code (usually notebooks) to a runnable, organized and git-committed code when you're done 
training and before/while you go to production. Bonus point if you validate that the production code you ported 
actually re-creates the model as expected.
In the case of using Jupyter notebook as an exploration environment, there are simple ways to 
[turn the notebooks 
into scripts](https://stackoverflow.com/questions/17077494/how-do-i-convert-a-ipython-notebook-into-a-python-file-via-commandline) 
and then further re-design the software.

### 40. Shadow Deployment
Ability to deploy an ML system without exposing its predictions to the users. 
One way this can be useful is to understand the technical performance impact of deploying a model, 
e.g. is there any delay on the page load where the model is being used, what is the monetary impact of the delay 
to the customer?

### 41. Canary Deployment
Ability to gradually roll out an ML system, such that any negative impact due to its deployment is mitigated. 
