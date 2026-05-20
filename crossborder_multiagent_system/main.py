from fastapi import FastAPI
from orchestrator.workflow import run_full_workflow
from schemas.request import WorkflowRequest

app = FastAPI(title="CrossBorder Multi-Agent System")

@app.get("/")
async def root():
    return {"status": "running"}

@app.post("/run-workflow")
async def run_workflow(data: WorkflowRequest):
    result = await run_full_workflow(
        product=data.product,
        market=data.market
    )
    return result