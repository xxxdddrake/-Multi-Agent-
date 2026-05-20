from pydantic import BaseModel

class WorkflowRequest(BaseModel):
    product: str
    market: str