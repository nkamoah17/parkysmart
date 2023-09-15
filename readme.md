Parking Lot Occupancy Detection System

This repository contains the code for an AI-powered parking lot occupancy detection system. The system uses a trained machine learning model to predict the occupancy of a parking lot from an image.
Overview

The system is composed of a React frontend and a Flask backend. The frontend allows users to upload an image of a parking lot, and displays the predicted occupancy. The backend handles the image upload, runs the prediction model, and returns the results.

The system also includes a caching layer using Redis, and a blob storage layer using S3 for storing the uploaded images. It uses PostgreSQL for database operations.
Getting Started

To get started with the project, clone the repository and install the required dependencies.

For the frontend, you will need Node.js and npm. Navigate to the src directory and run npm install to install the dependencies.

For the backend, you will need Python and pip. Navigate to the root directory and run pip install -r requirements.txt to install the dependencies.

You will also need to set up the following environment variables for the backend:

DB_NAME, DB_USER, DB_PASSWORD for the PostgreSQL database
S3_BUCKET, S3_ACCESS_KEY, S3_SECRET_KEY for the S3 storage
REDIS_HOST, REDIS_PORT for the Redis caching layer
SECRET_KEY for the Flask application

These can be set in the config.py file or as environment variables.
Running the Application

To run the frontend, navigate to the src directory and run npm start.

To run the backend, navigate to the root directory and run python app.py.
Contributing

We welcome contributions to this project. If you would like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

Before submitting your pull request, please ensure your changes do not break any existing functionality, and add tests for your new features where possible.
License

This project is licensed under the MIT License. See the LICENSE file for more details.