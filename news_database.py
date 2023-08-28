import sqlite3
import json
import datetime

def create_database():
    # Connect to the database
    conn = sqlite3.connect("app_data/news_database.db")
    cursor = conn.cursor()

    # Create a table to store news articles
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            time TEXT
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()



def create_news_table(cursor):
    # Create a table to store news articles
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            time TEXT
        )
    ''')

def insert_article(title):
    # Insert the data into the table
    conn = sqlite3.connect('app_data/news_database.db')
    cursor = conn.cursor()
    time=datetime.datetime.now()

    cursor.execute('''
        INSERT INTO news (title, time)
        VALUES (?, ?)
    ''', (title, time))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def load_data_into_database(file_path):
    # Connect to the database (creates a new database if it doesn't exist)
    conn = sqlite3.connect('app_data/news_database.db')
    cursor = conn.cursor()

    create_news_table(cursor)

    # Load data from JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    insert_article(cursor, data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Example usage
# load_data_into_database('app_data/data.json')
# create_database()


def check_title_exists(title):
    # Connect to the database
    conn = sqlite3.connect('app_data/news_database.db')
    cursor = conn.cursor()

    # Execute a query to check if the title exists
    cursor.execute('''
        SELECT EXISTS (
            SELECT 1
            FROM news
            WHERE title = ?
        )
    ''', (title,))

    result = cursor.fetchone()[0]  # Fetch the result of the query

    # Close the connection
    conn.close()

    return bool(result)


# val=check_title_exists("The Impact of NYC’s Anti-Bias Law on Hiring Algorithms")
# print(val)

# insert_article("abcs")