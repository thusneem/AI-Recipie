🍳 AI Recipe Assistant

An AI-powered recipe generation web application built using Angular, Python, and AWS Bedrock. The app allows users to generate personalized recipes based on ingredients, dietary preferences, and cuisine types using generative AI.

🚀 Features

Generate recipes from available ingredients

Personalized suggestions (dietary needs, cuisine preferences)

Step-by-step cooking instructions

AI-powered responses using AWS Bedrock foundation models

Scalable cloud-based architecture

🏗️ Architecture Overview

Frontend: Angular (hosted on Amazon S3)

Backend: Python (Flask/FastAPI) running on Amazon EC2

AI Service: AWS Bedrock (Claude / Titan models)

Hosting:

S3 for static frontend hosting

EC2 for backend API services

IAM roles for secure Bedrock access

🔄 Application Flow

User enters ingredients or preferences in the Angular UI

Frontend sends request to the Python backend API

Backend constructs a prompt and calls AWS Bedrock

Bedrock generates recipe content

Backend returns formatted results to the frontend

🧠 AI Integration (AWS Bedrock)

Uses AWS Bedrock to access managed foundation models

No model training or hosting required

Supports:

Recipe generation

Ingredient substitutions

Cooking tips and variations

🛠️ Tech Stack
Layer	Technology
Frontend	Angular, TypeScript, HTML, CSS
Backend	Python, Flask / FastAPI
AI Models	AWS Bedrock
Cloud	Amazon EC2, Amazon S3
Security	AWS IAM
📂 Project Structure
ai-recipe-assistant/
├── frontend/          # Angular application
├── backend/           # Python API (Flask/FastAPI)
│   ├── app.py
│   ├── requirements.txt
│   └── bedrock_client.py
├── README.md

⚙️ Setup Instructions
Backend (Python on EC2)
pip install -r requirements.txt
python app.py


Ensure your EC2 instance has an IAM role with Bedrock access.

Frontend (Angular)
npm install
ng build --configuration production


Upload the build files to an S3 bucket configured for static website hosting.

🔐 Security

IAM roles used instead of hardcoded credentials

Bedrock access restricted by least-privilege policies

🌱 Future Enhancements

User authentication

Saved and favorite recipes

Nutrition and calorie breakdown

Multi-language support

Voice-based recipe assistant

📌 Use Cases

Home cooking assistance

Meal planning applications

AI-powered food recommendation systems

Cloud + Generative AI demos
