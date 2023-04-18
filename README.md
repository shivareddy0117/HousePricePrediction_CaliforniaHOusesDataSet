# HousePricePrediction_CaliforniaHOusesDataSet
For this project, we'll be predicting house prices using a dataset, and we'll use Python, Pandas, Scikit-learn, and Spark. Here is an outline of the procedure:

Collect the dataset
Explore and preprocess the data
Train a machine learning model
Evaluate the model
Save the model (linear_regression_model.pkl' and 'scaler.pkl' files are saved) #above(step 4 to 8) is done in app2.py
extend this project by adding more advanced models, feature engineering, or by deploying it as a web service using FastAPI.
Let's create a simple REST API using FastAPI to serve predictions from the trained model. First, ensure you have FastAPI and Uvicorn installed
You can install them using the following command: pip install fastapi uvicorn
To run the application, execute the following command in your terminal: uvicorn app:app --reload
FastAPI application is now running successfully. Your application is listening on http://0.0.0.0:8000, 
which means it is accessible from any IP address on port 8000.

used common HTTP methods you can use with FastAPI:

GET: Retrieve information from the server (read-only).
POST: Send data to the server to create a new resource.
PUT: Update an existing resource on the server.
DELETE: Remove a resource from the server.

Then created a simple web application interface using HTML, CSS, and JavaScript to interact with your FastAPI backend.
This interface will allow users to input house features and then send GET, PUT, and POST requests to the FastAPI server 
to get predictions and perform other operations.

Due to CORS (Cross-Origin Resource Sharing) restrictions,  enabled CORS on FastAPI server
To enable CORS in your FastAPI application, follow these steps:

Install FastAPI's CORS middleware package fastapi.middleware.cors: pip install fastapi[all]
Import CORSMiddleware and add it to your FastAPI application. In your main FastAPI application file (where you define your API routes)

FastAPI application is now running on http://0.0.0.0:8000. You can access the auto-generated API documentation by opening your web browser and navigating to http://127.0.0.1:8000/docs.
From there, you can interact with the API endpoints.
To test your application, you can use a tool like Postman or Insomnia, or you can write Python scripts to make requests to the API.

