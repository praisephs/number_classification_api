## FastAPI Number Classification API

# Overview

This project is a FastAPI-based web application that classifies numbers based on various properties such as prime, perfect, and Armstrong numbers. The API is deployed on Azure App Service and accessible via:

You can access the live API URL here: [Classify Number API](https://no-class-app-dshhaserdmh8cagk.eastus2-01.azurewebsites.net/api/classify-number?number=371)

# Features

Classifies numbers as prime, perfect, Armstrong, or other propert

Provides a structured JSON response with number analysis

Uses FastAPI for high-performance API development

Deployed on Azure App Service with GitHub Actions for CI/CD

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

            'uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload'

Access the API at: http://localhost:8000            
            
           
           
          


          
          







