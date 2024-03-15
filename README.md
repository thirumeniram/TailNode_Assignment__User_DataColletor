# User and Posts Data Collector

This project is designed to fetch users and their corresponding posts data from [dummyapi.io](https://dummyapi.io/) and store it in a postgres database . 

## Functional Requirements implemented

- Obtained an `app_id` by registering on the [dummyapi.io](https://dummyapi.io/) website.
- Used the provided `app_id` to authenticate API requests.
- Fetched users' data and store it in the `new_users` table in the database.
- Fetch each user's posts data and store it in the `new_posts` table in the database.

# Folder Structure

src/
   components/
      App.js
      TodoItem.js
      AddTodo.js
      Todos.js
   index.js
   index.css

## Installation

Follow these steps to set up and run the project:

1. **Clone the Repository**
   
    Clone the project to your local machine:https://github.com/thirumeniram/TailNode_Assignment__User_DataColletor.git2
  
2. cd TailNode_Assignment_part_A_User_DataColleto

3. Create and activate a virtual environment:
   - For Windows:
     - python -m venv venv
     - \venv\Scripts\activate
       
   - For macOS/Linux:
     - python3 -m venv venv
     - source venv/bin/activate
       
4. Install Dependencies
    - pip install -r requirements.txt
   
5. Run the application
    - python app.py


