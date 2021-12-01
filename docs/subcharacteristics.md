# Subcharacteristics - details

This section contains the following information for each subcharacteristic:

- Definition
- Why is this subcharacteristic important?
- Relationship to other subcharacteristics
- Fulfilled example

## Utility

### Accuracy

#### Definition
The size of the observational error (systematic and random) of an ML system.

#### Why is Accuracy important?

An ML system needs to model the reality close enough to deliver value.

#### Fulfilled example

For a supervised binary classification scenario, the ML system makes predictions with precision and recall 
according to the specified requirements (e.g. comparable with a human baseline). 

### Effectiveness

#### Definition
The ability of an ML system to produce a desired result on the business task it is being used for.

#### Why is Effectiveness important?

An effective system produces expected results for a given business task, achieving commercial impact.

#### Fulfilled example

1. An ML system that is built to reduce email spam, managed to decrease the spam percentage by 3% during an AB experiment.
2. An ML system used to rank search results manages to generate incremental revenue (compared to a baseline).

Please note that a system might be accurate (e.g. achieve the desired precision and recall) but not effective.
This could be due to an invalid business hypothesis, where we use the model predictions in a way which 
does not contribute at all to the business metrics (e.g. we predict properly a CS agent response time, but
surface this information in an unhelpful way).


### Responsiveness

#### Definition
The ability of an ML system to complete the desired task in an acceptable time frame.


#### Why is Responsiveness important?

An ML system is always used in an end product which comes with requirements to the systems' responsiveness. If the system
makes very accurate predictions, but too slow, its impact might be dramatically reduced. The end user will simply not wait
for the prediction or will not have a chance to notice it.

#### Fulfilled example

The ML system is able to provide a prediction within 100ms 99% of the time. It is being used on the front end, 
where we know (by experimentation) that the impact is positive if we keep this number below 200ms.

### Reusability

#### Definition
The ability to reuse the same ML system without any change, for another business case.

#### Why is Reusability important?

An ML system which can be reused for different products enables to scale fast and deliver more value.

#### Fulfilled example

The ML system used to predict if user generated accommodation reviews are offensive can be reused for a 
different business unit for different types of user generated content.

## Robustness

### Recoverability	

#### Definition
The degree to which an ML system can be promptly restored to a previous functioning state.

#### Why is Recoverability important?

An ML system might need to be reverted to a previous version quickly when problems with a new version arise.
It should not require retraining, lengthy redeployment, and manual intervention needs to be reduced to a
minimum. 

#### Fulfilled example

A newly deployed version of the ML system produces errors. 
It can be switched to the previous version within 5 minutes after the error is observed.

### Availability

#### Definition
The probability that the system will be up and running and able to deliver useful services to users.

#### Why is Availability important?

For an ML system to maintain an active user base it needs to be available for use. 
If an ML system randomly stops working, it will not be used in the long run and will fail to deliver value.

#### Fulfilled example

The ML system is expected to be serving predictions 99.99% of the time, or any other percent, in line with the business requirements

### Resilience

#### Definition
The degree to which an ML system can provide and maintain an acceptable level of service in the face of 
technical challenges to normal operation.

#### Why is Resilience important?

ML systems are deployed in an environment with many external dependencies (other systems, databases). 
Failure of external dependencies is always possible, and the more resilient to failure the ML system is, 
the more value to the end user it brings.

#### Fulfilled example

The ML system keeps running with an acceptable accuracy, even when some features become unavailable (e.g. due to a database outage)

### Adaptability

#### Definition
The extent to which an ML system can adapt to changes in the production environment, always providing the same functioning level.

#### Why is Adaptability important?

ML systems are deployed in a constantly changing environment: customer behaviour can change due to economic changes, 
trends, fashion, or new products being available. An ML system should be able to adapt to change.

#### Fulfilled example

1. The ML system is periodically retrained on new data.
1. The ML system is updated online with each new training instances.

### Scalability

#### Definition
The ability of an ML system to handle a growing amount of work by adding resources to the system.

#### Why is Scalability important?

As business grows, new users can arrive at an exponentially fast pace. The ML system should be ready to handle 
new traffic and accommodate business growth.

#### Fulfilled example

1. The ML system can be scaled to an increased traffic by adding more resources. Adding more resources scales linearly: each new box added can help 1000 new customers.
1. Counter example: The bottleneck of the ML system is a O(N^2) computation (N - number of users) which cannot be computed out of core and needs to be run on one box.

## Economy

### Cost-effectiveness

#### Definition
The extent to which an ML system achieves the desired relationship between costs and overall impact.

#### Why is Cost-effectiveness important?

It is important to keep a healthy cost to impact ratio. An ML system which costs more to train, maintain, 
and serve predictions than the impact of these predictions should not be deployed. 
This can be hard to measure but should never be left out of consideration.

#### Fulfilled example

The ML system "makes money". The ML system uses resources worth $1000 per month while generating additional $2000 worth of bookings per month.

### Efficiency

#### Definition
Efficiency is the ability to avoid wasting resources (computational, human, financial, etc.) in order to perform the desired task effectively.

#### Why is Efficiency important?

It is important to maintain an acceptable level of resources while reaching the desired objective. This also helps maintain cost-effectiveness.

#### Fulfilled example

1. The ML system accomplishes its objective by using the least amount of compute resources possible.
2. The ML system accomplishes its objective by using the least amount of data annotation possible (think active learning).
3. The ML system reuses existing components and features to speed up development.

## Modifiability

### Extensibility

#### Definition
The ease with which an ML system can be modified, in order to be used for another purpose.

#### Why is Extensibility important?
The more use cases an ML system can be used for, with the minimal amount of change, the more the commercial impact it
will have on the long term. 

#### Fulfilled example

An ML model trained to identify phone numbers in images can be quickly extended to identify email addresses 
in the same image dataset.

### Maintainability

#### Definition
The ease with which activities aiming at keeping an ML system functional in the desired regime, can be performed. 

#### Why is Maintainability important?
The ease and speed with which certain activities can be performed to an ML system in order for this to function 
properly, directly affect the downtime of the system and hence its commercial impact. At the same time, ease of 
maintenance means less development time spent for the required activities and thus, higher efficiency of 
human resources.

#### Fulfilled example
A unit, integration, and e2e tested and modular ML system, in which changes can be made quickly 
without risk of breaking it.

### Modularity

#### Definition
The extent to which an ML system consists of components of limited functionality that interrelate with each other. 

#### Why is Modularity important?
Highly modular ML systems allow for changes to be performed in one part of the system without the risk to break another 
part of it. This translates to faster development time to maintain or extend the functionality of the system. 

#### Fulfilled example
An ML system for which the code for each of the steps in the ML lifecycle (data collection, feature engineering, 
training, etc) is separate in different scripts, and changes in one step do not affect the rest.

### Testability

#### Definition
The degree to which the code of an ML system can be tested for failures.

#### Why is Testability important?
The ease of testing the functionality of an ML system highly depends on its testability. Highly testable systems require
less development time for the testing and have more chances of providing the expected output due to the higher testing 
coverage, which testability entails.

#### Fulfilled example
A highly modular ML system where each piece of functionality has a narrow scope which is easy to be tested for its 
expected output and edge cases as well.

## Productionizability

### Deployability

#### Definition
The extent to which an ML system can be deployed in production when needed.

#### Why is Deployability important?

In order for an ML system to bring value, its predictions should be used in production for the task at hand. Hence, 
one must be able to deploy the system in a production environment when necessary, 
otherwise its predictions cannot be used.  

#### Fulfilled example
An ML system that is supposed to predict real-time, can be uploaded in a company central ML deployment platform and serve requests for 
prediction.

### Repeatability

#### Definition
The ease with which the ML lifecycle can be repeated.

#### Why is Repeatability important?

A system which requires many manual steps in order for its ML lifecycle to be repeated, has among others the following
risks: The contributor of the system will spend time to run the necessary commands to repeat the system's cycle and 
there is the chance for human error. Due to the aforementioned, the contributor might hesitate to repeat the system's 
lifecycle which means that a code quality improvement might not be rolled out, or that the system will not be retrained 
frequently. To avoid such risks, it is important to be able to repeat the system's lifecycle as easy as possible. 

#### Fulfilled example

The system is associated with a continuous deployment pipeline, in which data collection, feature engineering, 
training and deployment are executed automatically.

### Operability

#### Definition
The extent to which an ML system can be controlled (disable, upload new version, etc.).

#### Why is Operability important?

When an ML system is being used in production for a particular task, there might be cases where the state of the system 
must be altered. For example, if the system starts causing problems with its deployment or its predictions it might 
need to be disabled, or if a bug in the model is found then it has to be updated. Operability is about being able to 
perform such actions, and it is crucial for the system's value.

#### Fulfilled example
An ML system that is deployed in a central ML deployment platform and which can be easily disabled or updated without any changes required
from its clients.

### Monitoring

#### Definition
The degree to which relevant indicators of an ML system are effectively observed/monitored and integrated in 
the operation of the system.

#### Why is Monitoring important?

Since most of the ML systems are complex and non-deterministic, there might be many points of failure during the ML 
lifecycle. Hence, it is crucial to have monitors for all the relevant indicators of the system in order to understand
how the system operates and be able to spot degradation of certain components.

#### Fulfilled example

An ML system that is serving in production, and for which monitors are in place in order to observe feature drift and model performance on an ongoing basis.

## Comprehensibility

### Discoverability

#### Definition
The degree to which an ML system can be found (by means of performing a search in a database or any other 
information retrieval system).

#### Why is Discoverability important?

An ML system can only have value if it is possible to be found and used. An excellent ML system which is 
hard to be found by potential users, will have limited commercial value.

#### Fulfilled example
An ML system which can be successfully found with a search by its name or owner: e.g. in a 
central ML deployment platform or a version control system.

### Learnability

#### Definition
The capability of an ML system to enable the user to learn how to use it.

#### Why is Learnability important?

An intuitive ML system with a smooth learning curve, makes it easy for its users to learn how to use it, something
that can increase the adoption and hence the value of the system itself.

#### Fulfilled example
An ML system with an elaborate documentation and intuitive implementation, which users can learn how to use without
   much effort.

### Readability

#### Definition
The ease with which the code of an ML system can be understood.

#### Why is Readability important?

In order for an ML system to be maintained, modified and extended, the contributors should be able to easily 
understand the system's code with the least possible friction. In this way a contributor will easily understand how the 
system is built and also will be able to spot any potential mistakes in the logic.

#### Fulfilled example
An ML system's code with intention-revealing names for variables, functions and classes, for which the functionality
can be quickly understood with a glance at the code and its documentation and without the need to contact the owner.

### Traceability

#### Definition
The ability to relate artifacts created during the development of an ML system to describe the system from 
different perspectives and levels of abstraction with each other, the stakeholders that have contributed to the 
creation of the artifacts, and the rationale that explains the form of the artifacts.

#### Why is Traceability important?

ML systems are usually complex non-deterministic systems with several stakeholders who might have made certain 
assumptions during the system's implementation. In order for the system to be easily understood, debugged or audited, it
is important to be able to trace back certain created artifacts, along with the rationale and stakeholders 
behind those artifacts.

#### Fulfilled example
1. An ML system with extensive logging, in which we can have visibility among others, on the date ranges and 
   hyper-parameters used for training, at any given point in the past. 
2. An ML system for which code development happens in Git, and for which we have the ability to attribute code changes 
   to contributors.
   

### Understandability

#### Definition
The ease with which the implementation and design choices of an ML system can be understood.

#### Why is Understandability important?

Usually, during the development of ML systems, certain design choices are being made which have an important impact 
on the system's output. In order for a contributor to use or build on top of an existing system, it is particularly 
important to understand the reasoning behind all the choices which were made regarding the implementation or the 
design of the system.

#### Fulfilled example

A system with documented explanations of the rationale behind certain choices, e.g. why some features have been 
bucketized, why those specific buckets were chosen, why certain count features are windowed, etc.

### Usability

#### Definition
The degree to which an ML system can be effectively used by users.

#### Why is Usability important?

An ML system can have value only if it can be effectively used by its potential users. Thus, it is very important for 
the system to be easy and intuitive to use.

#### Fulfilled example
1. An ML system which is containerized and can run on any machine and does not have any (hidden) special requirements.
2. An ML system deployed in a central ML deployment platform available to everyone.  

### Debuggability

#### Definition
The extent to which the inner workings of the ML system can be analyzed in order to understand why it behaves the way it does.

#### Why is Debuggability important?

In order for ML systems to be maintained, modified or extended, it is essential for the contributors to be able 
to analyze their inner workings, to understand how they behave and be able to debug them. 

#### Fulfilled example
An ML system with modular code, unit tests and extensive logging, for which it is easy to understand what went wrong
in case of an error.

## Responsibility

### Explainability

#### Definition
The ability to explain the output of an ML system.

#### Why is Explainability important?

There are cases when certain predictions of the ML system need to be justified to the affected customers, auditors or 
other stakeholders. In such cases, being able to explain the mechanism with which the system outputs its predictions, is 
key for gaining the stakeholders' trust.

#### Fulfilled example

An ML system with a linear regression model for which we can explain how each feature contributes to the 
final prediction.
   

### Fairness

#### Definition
The extent to which an ML system prevents unjust predictions towards protected attributes (race, gender, income, etc).

#### Why is Fairness important?

In many cases, ML systems' predictions are being used to take irreversible decisions on behalf of customers. In order
for an ML system to be ethical, its performance should not be affected by protected variables, such as country, race 
or gender.

#### Fulfilled example

A binary classifier which yields equal False Positive rates, for instances of different booker countries (or other
sensitive variable).
   

### Ownership

#### Definition
The extent to which there exists people appointed to maintaining the ML system and supporting all the relevant stakeholders.

#### Why is Ownership important?
It is hard for an ML system to have long-term commercial impact, unless there is a person or team being responsible for 
maintaining the system and supporting its stakeholders with various requests. Due to this, having clear ownership 
is an essential part of the system's success.


#### Fulfilled example

An ML system which is deployed in a central ML deployment platform with details and contact information of its owner.

### Standards Compliance

#### Definition
The extent to which applicable standards are followed in the ML system.

#### Why is Standards Compliance important?

Depending on the organization or the use case that an ML system is operating, there might be certain standards which 
need to be followed and could add transparency, ensure protection of personal information or standardize certain 
processes. Adherence to such standards is particularly important for the long-term viability of an ML system. 

#### Fulfilled example
An ML system which is trained with PII and has a clear documentation of the process that is followed in order to 
ensure the PII data are not accessible by developers without permission and that the PII used for training 
is not extractable from the system. Please note that if PII is used as features in this ML system any logging functionality
must also respect the requirements of handling PII data as well.

### Vulnerability

#### Definition

The ease with which the system can be (ab)used to achieve malicious purposes.

#### Why is Vulnerability important?

It is common for ML systems operating on a lot of traffic or on sensitive applications, to fall victims of abuse by 
malicious users who try to exploit the system. The risks of such cases of abuse might be very big for the organization 
itself and its customers, thus it is critical for the ML system to be immune against such attacks.

#### Fulfilled example

An ML system that has high test coverage, with test cases both for the happy path and edge cases as well, 
and which has its code reviewed for vulnerability issues by multiple developers.
