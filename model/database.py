import psycopg2
from config.postgres import DATABASE_URL

#connecting to the PostgreSQL database using the connection string defined in DATABASE_URL.
def get_connection():
    return psycopg2.connect(DATABASE_URL)

#Initializing the database by creating a new tables for storing the users and user's post.
def initialize_db():
    conn=get_connection()
    cur=conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS new_users (
        db_id SERIAL PRIMARY KEY,
        id VARCHAR(50) UNIQUE NOT NULL,
        title VARCHAR(10),
        firstName VARCHAR(100),
        lastName VARCHAR(100),
        picture VARCHAR(255)
    );
    ''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS new_posts (
    db_id SERIAL PRIMARY KEY,
    post_id VARCHAR(50) UNIQUE NOT NULL,
    user_id VARCHAR(50),
    text TEXT,
    likes INTEGER,
    publishDate TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES new_users(id)
    );
    ''')
    conn.commit()
    cur.close()
    conn.close()


