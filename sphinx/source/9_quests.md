# Quests

## Shinbashi DAG

### WBS

### 0. Stac Search Task
	- People - Adrian Gould
	- Code Study
		- https://smartgitlab.com/blacksky/smartflow/-/blob/main/dags/Demo_Shinbashi.py
		- clone the repo 
	- Stub out Noops for main tasks in devcode
		- DEPLOY TO airflow - with makefile

### Building the Docker smartflow
- clone adrians github
- build in ~/work
- add tony additions
- capture all this in build_docker/Makefile

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


### Source

References to elements in the code, scripts, or specific Airflow classes/variables/values are often in italics to help distinguish them from the surrounding text. Source code for all examples and instructions to run them using Docker and Docker Compose are available in our GitHub repository (
- https://github.com/BasPH/data-pipelines-with-apache-airflow) and can be downloaded via the book’s website (
- www.manning.com/books/data-pipelines-with-apache-airflow).


### Getting Started

- data pipelines
- airflow's role
- compare to other technologies
- scheduling semantics
- templating
- then on to part 2

- airflow is an orchetrator - the spider in the web
- weather task example
	- fetch weather data via ap
	- clean and organize weather data
	- push cleanded data to weather dashboard

> This type of graph is typically called a directed acyclic graph (DAG), as the graph contains directed edges and does not contain any loops or cycles (acyclic).


Name Originated at1 Workflows defined in Written in Scheduling Backfilling User interface2 Installation platform Horizontally scalable 
- Airflow Airbnb Python Python Yes Yes Yes Anywhere Yes 
- Argo Applatix YAML Go Third party3 Yes Kubernetes Yes 
- Azkaban LinkedIn YAML Java Yes No Yes Anywhere Conductor Netflix JSON Java No Yes Anywhere Yes 
- Luigi Spotify Python Python No Yes Yes Anywhere Yes 
- Make Custom DSL C No No No Anywhere No 
- Metaflow Netflix Python Python No No Anywhere Yes 
- Nifi NSA UI Java Yes No Yes Anywhere Yes Oozie

de Ruiter, Julian; Harenslak, Bas. Data Pipelines with Apache Airflow (p. 9). Manning. Kindle Edition. 

### Introducing Airflow

- define DAGS using python code.
	- set of tasks
	- metadata
	- scheduling

- airflow extensions - 
	- databases
	- cloud services
	- notification linkages

#### 3 main components - scheduler; workers; webserver

- airflow metastore(database) key component for linkages
