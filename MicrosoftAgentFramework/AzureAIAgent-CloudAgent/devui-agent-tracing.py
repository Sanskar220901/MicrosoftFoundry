import os
from pathlib import Path

from agent_framework import Agent
from agent_framework.devui import serve
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
from dotenv import load_dotenv


def create_docs_agent(project_endpoint: str, model: str) -> Agent:
    """Create a local Agent Framework agent backed by a Foundry model."""
    credential = AzureCliCredential()
    client = FoundryChatClient(
        project_endpoint=project_endpoint,
        model=model,
        credential=credential,
    )
    return Agent(
        client=client,
        name="docs-agent",
        instructions="You are a helpful assistant that can help with documentation questions.",
    )


def load_agent() -> Agent:
    # Load the .env stored beside this script, regardless of the shell's working directory.
    load_dotenv(Path(__file__).with_name(".env"))

    # Prefer the current Agent Framework names while accepting names used by older samples.
    project_endpoint = os.getenv("FOUNDRY_PROJECT_ENDPOINT") or os.getenv("AI_FOUNDRY_PROJECT_ENDPOINT")
    model = (
        os.getenv("FOUNDRY_MODEL")
        or os.getenv("MODEL_DEPLOYMENT_NAME")
        or os.getenv("AI_FOUNDRY_DEPLOYMENT_NAME")
    )

    if not project_endpoint:
        raise RuntimeError("FOUNDRY_PROJECT_ENDPOINT is not set.")
    if not model:
        raise RuntimeError("FOUNDRY_MODEL or MODEL_DEPLOYMENT_NAME is not set.")

    return create_docs_agent(project_endpoint=project_endpoint, model=model)


def main() -> None:
    agent = load_agent()
    serve(
        entities=[agent],
        host="127.0.0.1",
        port=8080,
        auto_open=True,
        instrumentation_enabled=True,
        auth_enabled=False,
    )


if __name__ == "__main__":
    main()
