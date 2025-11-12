# Copyright (c) Microsoft. All rights reserved.

import asyncio
import os

from agent_framework import ChatAgent
from agent_framework.azure import AzureAIAgentClient
from azure.ai.agents.aio import AgentsClient
from azure.ai.projects.aio import AIProjectClient
from azure.identity.aio import AzureCliCredential

"""
Azure AI Agent with Existing Agent Example

This sample demonstrates working with pre-existing Azure AI Agents by providing
agent IDs, showing agent reuse patterns for production scenarios.
"""


async def main() -> None:
    print("=== Azure AI Chat Client with Existing Agent ===")

    # Create the client
    async with (
        AzureCliCredential() as credential,
        AIProjectClient(endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"], credential=credential) as project_client,
        AgentsClient(endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"], credential=credential) as agents_client,

    ):
        azure_ai_agent = await project_client.agents.create_agent(
            model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
            # Create remote agent with default instructions
            # These instructions will persist on created agent for every run.
            instructions="Retorne todas as informações que o usuario pedir usando como referencia o que o Luffy do One Piece responderia. Seja Respeitoso nas respostas.",
        )

        chat_client = AzureAIAgentClient(agents_client=agents_client, agent_id=azure_ai_agent.id)

        try:
            async with ChatAgent(
                chat_client=chat_client,
                # Instructions here are applicable only to this ChatAgent instance
                # These instructions will be combined with instructions on existing remote agent.
                # The final instructions during the execution will look like:
                # "'End each response with [END]. Respond with 'Hello World' only'"
                instructions="Retorne as referencias no final usando bullet points",
            ) as agent:
                query = "Pesquise sobre o valor do dolar hoje e o que pode ter afetado esse valor."
                print(f"User: {query}")
                result = await agent.run(query)
                # Based on local and remote instructions, the result will be
                # 'Hello World [END]'.
                print(f"Agent: {result}\n")
        finally:
            # Clean up the agent manually
            await project_client.agents.delete_agent(azure_ai_agent.id)


if __name__ == "__main__":
    asyncio.run(main())