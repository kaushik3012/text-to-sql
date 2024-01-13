
# Text-to-SQL with Live User Interaction

The primary objective of this project is to create an efficient Text-to-SQL system by integrating MySQL, LangChain, and Language Models (LLM). The ultimate goal is to establish a seamless pipeline that enables users to interact with a database effortlessly through natural language queries. The project aims to handle real-time user-input questions, employing advanced Language Models to generate database queries, and subsequently retrieve accurate answers.
## Installation

First, install the dependencies

```bash
  pip install -r requirements.txt
```
Use Python 3.8 or above

#### MySQL Setup

Install MySQL on your local computer and create its username and password.
Use this username and password in the params.py file.
## Run Locally

Go to the project directory
and add the data file in CSV format

In the same directory open the terminal and run the following code:

```bash
  python Main --filename=FILENAME --model=MODEL
```

By default, filename='data.csv' and model='GPT3'.

You can change the following variables in the params.py file:

* Database Name 
* SQL username
* SQL password
* MySQL server IP address
* API Key

The API key can be of OpenAI model or hugging face model.
## Authors

- [Raj Vardhan Singh](https://www.github.com/rajvs20)
- [Kaushik Raj V Nadar](https://www.github.com/kaushik3012)

