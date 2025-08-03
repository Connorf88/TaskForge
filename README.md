# 🛠️ TaskForge

**TaskForge** is a modular backend for cloud-ready task orchestration built with Azure Functions and Durable Functions. It powers APIs for retrieving, updating, and automating task completion workflows — ideal for scalable productivity apps.

---

## 🚀 Features

- 🔍 **Get Task**: Retrieve task details using `GET /tasks/{id}`
- 📝 **Update Task**: Modify task fields with `PUT /tasks/{id}`
- 🧩 **Durable Orchestration**: Automate task completion workflows
- 🔧 **Activity Functions**: Handle granular task operations
- 📦 **Shared Layer**: Common models and table services for clean architecture

---

## 📂 Project Structure

```bash
task_functions/
├── get_task/
├── update_task/
├── start_orchestrator/
├── orchestrator/
├── activity_get_task/
├── activity_complete_task/
└── shared/
    ├── models.py
    └── table_service.py

⚙️ Setup
Install dependencies:

bash
pip install -r requirements.txt
Start the Azure Functions host:

bash
func start
🌐 API Reference
Method	Endpoint	Purpose
GET	/tasks/{id}	Fetch a task
PUT	/tasks/{id}	Update a task
POST	/tasks/{id}/complete	Trigger orchestration
🔁 Orchestration Flow
text
start_orchestrator → orchestrator
     └── activity_get_task
     └── activity_complete_task
start_orchestrator triggers the flow.

orchestrator delegates work to two activity functions.

Task is marked completed in Table Storage.

✏️ Customization Ideas
⏰ Add due dates or reminders

📬 Integrate email or Slack alerts

🧠 Build predictive models for task prioritization

📊 Connect with dashboards like Power BI
