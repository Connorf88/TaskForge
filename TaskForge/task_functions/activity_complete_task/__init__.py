from shared.table_service import update_task_entity

def main(task: dict) -> dict:
    task_id = task.get("RowKey")
    updated_entity = update_task_entity(task_id, {"status": "completed"})
    return updated_entity
