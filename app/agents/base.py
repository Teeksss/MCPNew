"""Base class for integrating agents with the MCP server."""

from abc import ABC, abstractmethod
from pydantic import BaseModel


class AgentResponse(BaseModel):
    message: str


class Agent(ABC):
    """Abstract agent interface."""

    name: str

    @abstractmethod
    def run(self, query: str) -> AgentResponse:
        """Run the agent with the provided query."""
        pass
