 TaskForge – Azure-Powered Task Workflow API

TaskForge is a scalable, cloud-native API for managing asynchronous task workflows using Azure Functions, Durable Functions, and Azure Table Storage. Built for speed and modularity, it features clean, JSON-based endpoints ideal for automation and frontend integration.

🚀 Features

- Stateless HTTP-triggered Azure Functions for CRUD task operations  
- Durable Function chaining for orchestrating task workflows  
- Azure Table Storage for lightweight, fast task persistence  
- Async support with robust state tracking  
- Environment-based configuration for dev/prod parity

📁 Project Structure

`
TaskForge/
│
├── task_functions/          # Azure Function apps (create, update, complete)
├── shared/                  # Shared helpers and models
├── host.json                # Global Azure Functions config
├── local.settings.json      # Local environment variables
└── requirements.txt         # Python dependencies
`

🛠️ Tech Stack

- Azure Functions (Python)  
- Durable Functions  
- Azure Table Storage  
- Python 3.10+  
- VS Code + Azure Tools Extension

🧪 Running Locally

1. Clone the repo  
2. Install dependencies:  
   `bash
   pip install -r requirements.txt
   `
3. Start the function app:  
   `bash
   func start
   `

> ⚠️ Make sure Azure Storage Emulator or Azurite is running locally for testing Table Storage.

📦 Deployment

You can deploy directly via:

- Azure CLI (func azure functionapp publish)
- GitHub Actions (optional CI/CD integration)
- Azure DevOps Pipelines

📌 Future Enhancements

- JWT-based authentication  
- Pagination and filtering  
- Integration with frontend UI (React/Vue)  
- CI/CD pipeline with GitHub Actions

👤 Author

Connor F.  
Cloud Computing Student @ Purdue Global  
GitHub • LinkedIn
# TaskForge