from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .config import settings
from .rag.retrieval import Retriever
from .rag.generation import generate_answer

app = FastAPI(title=settings.app_name, debug=settings.debug)

retriever = Retriever()
registered_agents = {}


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    answer: str


class AgentRegistration(BaseModel):
    name: str
    endpoint: str


@app.get("/")
def read_root():
    return {"message": "Welcome to the MCP server"}


@app.post("/rag/query", response_model=QueryResponse)
def rag_query(request: QueryRequest):
    contexts = retriever.query(request.query)
    answer = generate_answer(contexts, request.query)
    return QueryResponse(answer=answer)


@app.post("/agents/register")
def register_agent(agent: AgentRegistration):
    if agent.name in registered_agents:
        raise HTTPException(status_code=400, detail="Agent already registered")
    registered_agents[agent.name] = agent.endpoint
    return {"status": "registered", "agent": agent.name}
