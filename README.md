# User and Posts Data Collector

This project is designed to fetch users and their corresponding posts data from [dummyapi.io](https://dummyapi.io/) and store it in a postgres database . 



## Functional Requirements implemented

- Obtained an `app_id` by registering on the [dummyapi.io](https://dummyapi.io/) website.
- Used the provided `app_id` to authenticate API requests.
- Fetched users' data and stored it in the `new_users` table in the database.
- Fetch each user's posts data and stored it in the `new_posts` table in the database.

## Tech Stack 

- **Python**: 
- **PostgreSQL**



## Data Stored in ElephantSQL

- This section shows  how the scraped user and users' data is organized and stored within the ElephantSQL database.
  
- The user database schema includes tables for users ,capturing attributes like db_id, id, FirstName, LastName and picture.
  
- The users' post database schema includes tables for users' post, capturing attributes like db_id, post_id, user_id, text, like, publisheddate.

Below are screenshots from the ElephantSQL database interface showing examples of the stored data:

user data:

![users data](https://github.com/thirumeniram/TailNode_Assignment__User_DataColletor/assets/66516937/0708f63f-200b-40dd-9654-b4657739ca30)

users' post data

![users' post data](https://github.com/thirumeniram/TailNode_Assignment__User_DataColletor/assets/66516937/b119dd06-6175-44dc-8d34-0a76c6c696bf)

The images above demonstrate the structured storage of scraped data.


## Folder structure

TailNode_Assignment_part_A_User_DataColletor/
│
├── config/
│ └── postgres.py
|
|──controllers/
│ └── user_controller.py
│
├── model/
│ └── database.py
│
└── app.py


## Installation

Follow these steps to set up and run the project:

1. **Clone the Repository**
   
    Clone the project to your local machine:https://github.com/thirumeniram/TailNode_Assignment__User_DataColletor.git
  
2. cd TailNode_Assignment_part_A_User_DataColletor

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


