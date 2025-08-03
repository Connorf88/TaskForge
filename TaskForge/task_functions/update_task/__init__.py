import azure.functions as func
import json
from shared.table_service import update_task_entity

def main(req: func.HttpRequest) -> func.HttpResponse:
    task_id = req.route_params.get("id")
    try:
        updates = req.get_json()
        entity = update_task_entity(task_id, updates)
        return func.HttpResponse(
            json.dumps(entity, default=str),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        return func.HttpResponse(f"Error updating task: {e}", status_code=500)
