🍳 AI Recipe Assistant
An AI-powered recipe generation web application built with Angular, Python, AWS Bedrock, and Docker.
The app generates personalized recipes based on ingredients, dietary preferences, and cuisine types using generative AI.
________________________________________
🚀 Features
```
•	Generate recipes from available ingredients
•	Personalized suggestions (dietary needs, cuisine preferences)
•	Step-by-step cooking instructions
•	AI-powered responses using AWS Bedrock foundation models
•	Retrieval-Augmented Generation (RAG) support
•	Dockerized backend for consistent deployments
•	Scalable cloud-based architecture
________________________________________
🏗️ Architecture Overview
•	Frontend: Angular (hosted on Amazon S3)
•	Backend: Python (Flask / FastAPI) running in Docker on Amazon EC2
•	AI Service: AWS Bedrock (Claude / Titan models)
Hosting & Security
•	Amazon S3 for static frontend hosting
•	Amazon EC2 for backend containers
•	IAM roles for secure Bedrock access
________________________________________
🔄 Application Flow
1.	User enters ingredients or preferences in the Angular UI
2.	Frontend sends a request to the backend API
3.	Backend (Docker container) constructs a prompt
4.	Backend calls AWS Bedrock
5.	AI-generated recipe is returned to the frontend
________________________________________
🧠 AI Integration (AWS Bedrock)
•	Uses AWS Bedrock to access managed foundation models
•	No model training or hosting required
Supported Capabilities
•	Recipe generation
•	Ingredient substitutions
•	Cooking tips and variations
________________________________________
🛠️ Tech Stack
```
|   Layer     |   Technology   | 
|------------ |--------------- | 
| Frontend    | Angular        | 
| Backend     | Python (Flask) | 
| AI          | AWS Bedrock    |
| Cloud       | EC2, S3        |
| DevOps      | Docker, GitHub Actions|
| Security    | AWS IAM        |
```


________________________________________
📂 Project Structure
```
AI-recipe/
├── .github/
│   └── workflows/
│       ├── deploy-backend.yml
│       └── deploy-frontend.yml
│
├── recipe-ai-assistant-backend/
│   ├── Rag/
│   │   ├── documents.py
│   │   ├── rag_pipeline.py
│   │   └── vector_store.py
│   ├── bedrock.py
│   ├── recipe_api.py
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .gitignore
│
├── recipe-ai-assistant-frontend/
│   └── browser/
│       └── index.html
│
└── README.md
```
___________________________________
🐳 Docker Support (Backend)
The backend is fully containerized using Docker for consistent development and deployment.
Build Docker Image
docker build -t backend .
Run Backend Container
docker run -d -p 8000:8000 recipe-ai-backend
________________________________________
Frontend (Angular)
npm install
ng build --configuration production
Upload the generated build files to an S3 bucket configured for static website hosting.
________________________________________
🚀 Deployment
•	Backend is deployed to EC2 as a Docker container using GitHub Actions
•	Frontend is deployed to Amazon S3 on every push to the main branch
•	CI/CD ensures consistent and repeatable deployments
________________________________________
🔐 Security
•	IAM roles used instead of hardcoded credentials
•	AWS Bedrock access restricted by least-privilege policies
________________________________________
🌱 Future Enhancements
•	User authentication
•	Saved and favorite recipes
•	Nutrition and calorie breakdown
•	Multi-language support
•	Voice-based recipe assistant
•	Container orchestration (ECS / EKS)
________________________________________
📌 Use Cases
•	Home cooking assistance
•	Meal planning applications
•	AI-powered food recommendation systems
•	Cloud and Generative AI demonstrations
```
