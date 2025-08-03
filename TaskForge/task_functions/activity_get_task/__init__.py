from shared.table_service import get_task_entity
from shared.models import Task

def main(task_id: str) -> dict:
    entity = get_task_entity(task_id)
    task = Task.from_entity(entity)
    return task.dict()
