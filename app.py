from model.database import initialize_db
from controller.user_controller import fetch_and_store_users, fetch_and_store_posts

def main():
    initialize_db() #Initializing the database and create table if not exists
    print("Database initialized successfully.")
    fetch_and_store_users() #Fetching and storing users data
    print("User data stored successfully.")
    fetch_and_store_posts()#Fetching and storing user's post data
    print("Post data stored successfully.")

if __name__ == '__main__':
    main()
