from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class Task(BaseModel):
    PartitionKey: str = Field(default="Task")
    RowKey: str = Field(default_factory=lambda: str(uuid.uuid4()))
    description: str
    status: str = Field(default="created")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def to_entity(self):
        # pydantic's .dict() will serialize datetime to ISO string by default
        return self.dict()

    @classmethod
    def from_entity(cls, entity: dict):
        data = {
            "description": entity.get("description"),
            "status": entity.get("status"),
            "created_at": entity.get("created_at"),
            "updated_at": entity.get("updated_at")
        }
        obj = cls(**data)
        obj.PartitionKey = entity["PartitionKey"]
        obj.RowKey = entity["RowKey"]
        return obj
