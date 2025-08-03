import azure.functions as func
import json
from shared.models import Task
from shared.table_service import get_task_entity

def main(req: func.HttpRequest) -> func.HttpResponse:
    task_id = req.route_params.get("id")
    try:
        entity = get_task_entity(task_id)
        task = Task.from_entity(entity)
        return func.HttpResponse(
            json.dumps(task.dict(), default=str),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        return func.HttpResponse(f"Task not found: {e}", status_code=404)
