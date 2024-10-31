# Flask and MongoDB Student Data API

This project is a simple Flask web application that connects to a MongoDB database to manage student data. It allows you to insert and fetch data using RESTful API endpoints.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [License](#license)

## Features
- Connects to a MongoDB database to store and retrieve student data.
- Provides a RESTful API to insert and fetch data.
- Simple and easy-to-use interface.

  ## Technologies Used

- ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)  
  Flask is a micro web framework for Python.

- ![PyMongo](https://img.shields.io/badge/PyMongo-4DB33D?style=for-the-badge&logo=mongodb&logoColor=white)  
  PyMongo is a Python library for MongoDB.

- ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)  
  MongoDB is a NoSQL database for storing data.



## Setup Instructions

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install Flask pymongo
   ```

4. **Set Up MongoDB**
   - Create a MongoDB Atlas account (if you haven't already).
   - Set up a cluster and get your connection string.
   - Replace the connection string in the `MongoClient` instantiation in `app.py`.

5. **Run the Application**
   ```bash
   python app.py
   ```
   The server will start on `http://127.0.0.1:5000/`.


## API Endpoints

### Fetch Student Data
- **Endpoint**: `/fetch`
- **Method**: POST
- **Description**: Fetches all student data from the database.

### Example Request
```bash
curl -X POST http://127.0.0.1:5000/fetch
```

## Usage
1. **Inserting Data**
   - When you run the application, it automatically inserts a sample student record.
   - You can modify the `insert_data` function in `app.py` to add more records as needed.

2. **Fetching Data**
   - Send a POST request to `/fetch` to retrieve the student data stored in the MongoDB database.
   - The data will be returned in JSON format.

## Screenshots
1. **Application Running**
   ![App Running](https://github.com/Deepak8260/fetch-data-from-mongoDB-using-api/blob/main/images/app%20running.jpeg)

2. **Fetching Data**
   ![Fetching Data](https://github.com/Deepak8260/fetch-data-from-mongoDB-using-api/blob/main/images/server%20fetching.jpeg)

## License
This project is licensed under the MIT License. See the LICENSE file for details.
