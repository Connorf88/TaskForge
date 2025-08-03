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
