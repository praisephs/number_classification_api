## FastAPI Number Classification API

# Overview

This project is a FastAPI-based web application that classifies numbers based on various properties such as prime, perfect, and Armstrong numbers. The API is deployed on Azure App Service and accessible via:

You can access the live API URL here: [Classify Number API](https://no-class-app-dshhaserdmh8cagk.eastus2-01.azurewebsites.net/api/classify-number?number=371)

# Features

Classifies numbers as prime, perfect, Armstrong, or other propert

Provides a structured JSON response with number analysis

Uses FastAPI for high-performance API development

Deployed on Azure App Service with GitHub Actions for CI/CD

# Prerequisites

Ensure you have the following installed:

Python 3.8+

pip (Python package manager)

Virtual environment module (venv)

# Project Setup

1. Create a Virtual Environment

To maintain an isolated environment for dependencies, create a virtual environment:

                  `python3 -m venv venv`

# Explanation

python -m venv invokes Python's built-in module for virtual environments

venv (last argument) is the directory where the virtual environment will be created

2. Activate the Virtual Environment

On macOS/Linux:

          'source venv/bin/activate'

On Windows (Command Prompt):

          'venv\Scripts\Activate.ps1'


3. Install Dependencies

Install FastAPI, Uvicorn (ASGI server), and any other required packages:

           'pip install fastapi uvicorn'

4. Save Dependencies

To ensure all dependencies can be reinstalled easily, generate a requirements.txt file:

            'pip freeze > requirements.txt'

5. Create FastAPI Application

Inside the app/ directory, create main.py:

![Image](https://github.com/user-attachments/assets/2c63eb46-1a71-4ae6-9a7f-1df5f01fa718)

![Image](https://github.com/user-attachments/assets/8081d759-3190-409e-bcdc-31d9f4c93272)

![Image](https://github.com/user-attachments/assets/5fe5850e-dfe9-48d6-943d-96c4a031dea5)

6. Run Locally Using Uvicorn

To test the API locally before deployment:

            'uvicorn app.main:app --host 0.0.0.0 --port 8000 --rDeployment on Azure App Service

  Access the API at: http://localhost:8000           

7. Push Code to GitHub

Ensure your code is pushed to a GitHub repository:eload'
   

         'git init
          git add .
          git commit -m "Initial commit"'
          git branch -M main
          git remote add origin <your-repo-url>
          git push -u origin main'

8. Create an Azure App Service

Log in to Azure Portal

Navigate to App Services → Create a new App Service

Select Python 3.8+ as the runtime stack

Choose GitHub as the deployment source

Authorize your GitHub account and select the repository

Enable GitHub Actions for continuous deployment

9. Configure Startup Command

Go to Azure App Service → Settings → Configuration → General Settings, then set the startup command:

          'gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --log-level debug'

 10. Access Deployed API

Once the deployment is complete, access the API at:       

            'https://<your-app-name>.azurewebsites.net/'

 ## API Endpoints

  # Health Check           
              
               'GET /'

  For example to check the health status of your API App, simply open the web browser and enter your URL:

            'https://<your-app-name>.azurewebsites.net/'

  Response:

  ![Image](https://github.com/user-attachments/assets/870c6791-8bb3-48d5-a605-542d1da05bae)

  
  # Number Classification
  
            'https://<your-app-name>.azurewebsites.net/api/classify-number?number=371'
            

  Response: 

    
  ![Image](https://github.com/user-attachments/assets/5d6cda82-19c2-4b8b-9950-cc090d87ebc7)     


  # Error Handling (Invalid Input)

          'https://<your-app-name>.azurewebsites.net/api/classify-number?number=abc'


 Response:

 
  ![Image](https://github.com/user-attachments/assets/ef701602-916a-41bf-8d36-6183e69b7511)

  # Conclusion

  This FastAPI project demonstrates how to classify numbers and deploy an API using Azure App Service with CI/CD via GitHub Actions

             
           
          


          
          







