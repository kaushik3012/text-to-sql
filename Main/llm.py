from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
import sqlalchemy as sa
from langchain import HuggingFaceHub
import os
from langchain_openai import OpenAI
from params import engine_str, database_name, openai_api_key, hf_api_token

def get_answer(model, df):

    # Now, create a new engine with the specified database
    engine = sa.create_engine(f"{engine_str}/{database_name}")
    conn = engine.connect()

    # Write DataFrame to MySQL database
    df.to_sql(name="products", con=engine,
            if_exists="replace", chunksize=1000,
            index=False)

    if model == 'T5':

        # add path to HF repo
        # using the google flan-t5-xxl model
        repo_id = 'cssupport/t5-small-awesome-text-to-sql'

        # establish llm model
        llm = HuggingFaceHub(repo_id=repo_id, huggingfacehub_api_token=hf_api_token,
                             model_kwargs={"temperature": 0.1, "max_length": 256})
        
    elif model == 'GPT3':
        os.environ['OPENAI_API_KEY'] = openai_api_key
        llm = OpenAI(temperature=0)
        
    # Replace the database_name with an instance of SQLDatabase
    db_instance = SQLDatabase.from_uri(
        f'mysql+mysqlconnector://root:root@localhost/{database_name}')
    db_agent = SQLDatabaseChain(llm=llm, database=db_instance, verbose=True)

    query = input("Enter your query: ")
    answer = db_agent.run(query)

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    return answer
