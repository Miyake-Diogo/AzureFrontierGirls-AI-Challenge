import asyncio
from agent_framework import ChatAgent
from agent_framework.azure import AzureOpenAIChatClient

chat_client = AzureOpenAIChatClient(
    api_key='',
    endpoint='https://<AIFOUNDRY-PROJECT>.cognitiveservices.azure.com/',
    deployment_name='gpt-4.1-mini',
    api_version='2025-01-01-preview',
)

async def main():
    agent = ChatAgent(
        chat_client=chat_client,
        instructions="""
        Você um assistente que ajuda o usuario.
        """
    )

    result = await agent.run("Explique como se fosse para uma criança de 10 anos o principio da incerteza de heizenberg.")
    print(result)

asyncio.run(main())

# Output: 
# Claro! Vou explicar o princípio da incerteza de Heisenberg de um jeito bem simples.
# Imagina que você está tentando pegar uma bolinha de pingue-pongue que está quicando na água. Se você olhar para ela, você pode ver onde ela está, certo? Mas, se você tentar pegar a bolinha para saber exatamente onde ela está, às vezes ela pula para um lugar diferente. 
# No mundo muito, muito pequeno, como o das partículas que formam tudo (átomos, elétrons), acontece algo parecido. O Princípio da Incerteza de Heisenberg diz que
# É como se, no mundo das coisas muito pequenas, ao tentar olhar bem de pertinho, as coisas ficassem meio “boradas” ou “confusas”. Isso acontece porque as partículas são muito diferentes das coisas grandes que a gente vê no dia a dia.
# Então, o princípio nos ensina que tem um limite no quanto a gente pode saber sobre essas partículas ao mesmo tempo, e isso é uma regra da natureza!
# Gostou da explicação? Quer que eu fale mais sobre isso?
  