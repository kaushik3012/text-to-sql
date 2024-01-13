import sqlalchemy as sa

def create_database(database_name):
    engine_str = (
        "mysql+pymysql://{user}:{password}@{server}"
        .format(user="root", password="root", server="localhost"))

    # Create a SQLAlchemy engine without specifying the database
    engine = sa.create_engine(engine_str)
    conn = engine.connect()
    if conn:
        print("MySQL Connection is Successful ... ... ...")
    else:
        print("MySQL Connection is not Successful ... ... ...")

    # Create 'Assignment' database if it doesn't exist
    conn.execute(sa.text(f"CREATE DATABASE IF NOT EXISTS {database_name}"))
    conn.close()
    