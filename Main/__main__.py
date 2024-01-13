from database import create_database
from params import database_name
from load_data import load_data
from llm import get_answer
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--model', type=str, default='GPT3',
                        help='Model to use for answer generation')
    parser.add_argument('--filename', type=str, default='data.csv',
                        help='Name of CSV file to load data from')
    return parser.parse_args()

def main():
    # Parse arguments
    args = parse_args()
    model = args.model
    filename = args.filename

    # Create database
    create_database(database_name)

    # Load data
    df = load_data(file_name=filename)

    # Get answer
    answer = get_answer(model=model, df=df)

    print(answer)

if __name__ == '__main__':
    main()