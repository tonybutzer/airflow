# Quests

## Shinbashi DAG

### WBS

1. Stac Search Task
	- People - Adrian Gould
	- Code Study
		- https://smartgitlab.com/blacksky/smartflow/-/blob/main/dags/Demo_Shinbashi.py
		- clone the repo 
	- Stub out Noops for main tasks in devcode
		- DEPLOY TO airflow - with makefile

## Docker Compose Trial Airflow - Celery

### Quickstart

- https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html


## 1 Airflow Study

1. airflow book - Data Pipelines with Apache Airflow - Harenslak

### Prerequisites *args and *kwargs

- https://code.tutsplus.com/articles/understanding-args-and-kwargs-in-python--cms-29494

- What Are Args?

*args are used to pass non-keyword arguments. Examples of non-keyword arguments are fun(3,4), fun("foo","bar").

*args are usually used as a measure to prevent the program from crashing if we don’t know how many arguments will be passed to the function. This is used in C++ as well as other programming languages.
What Are Kwargs?

- **kwargs is a dictionary of keyword arguments. 
The ** allows us to pass any number of keyword arguments. A keyword argument is basically a dictionary.

An example of a keyword argument is fun(foo=2,bar=7).


- You can call the function with any arguments you want.
	

``` python
def capital_cities(**kwargs): 
    # initialize an empty list to store the result
    result = []
    for key, value in kwargs.items():
        result.append("The capital city of {} is {} .format (key,value)
 
    return result
print capital_city(China = "Beijing",Cairo = "Egypt",Rome = "Italy"))
```

