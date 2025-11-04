# O que é o AI Foundry? 

Azure AI Foundry é uma plataforma da Microsoft para desenvolvimento, implantação e gerenciamento de soluções de inteligência artificial. Ela oferece ferramentas para criar modelos de IA, integrar serviços cognitivos e gerenciar pipelines de machine learning.

## Onde usar

- Criação de aplicações com IA generativa.
- Desenvolvimento de modelos customizados para visão computacional, NLP e análise preditiva.
- Integração com serviços do Azure, como Azure OpenAI, Cognitive Services e Azure Machine Learning.

## Onde não usar

- Projetos que exigem execução totalmente offline sem dependência de nuvem.
- Ambientes com restrições severas de compliance que não permitem uso de serviços em nuvem pública.
- Casos onde não há necessidade de escalabilidade ou recursos avançados de IA.

## Como usar

1.  Acesse o portal do Azure e habilite o Azure AI Foundry.
2.  Crie um workspace para gerenciar seus projetos.
3.  Escolha os serviços de IA necessários (ex.: modelos pré-treinados ou customizados).
4.  Configure pipelines de treinamento e implantação.
5.  Monitore e ajuste os modelos com ferramentas de governança e segurança.

---  

## Como o Foundry Funciona

O Foundry organiza os recursos em camadas para facilitar governança e colaboração. Cada instância possui um recurso `Azure AI Foundry` (antes chamado de AI Services) hospedado em um grupo de recursos do Azure. Dentro dele você cria *hubs* e *projects*, que funcionam como workspaces lógicos para equipes. Os projetos compartilham ativos comuns do hub (connections, compute, rede) e guardam seus próprios componentes como datasets, fluxos, agentes e deployments ([documentação](https://learn.microsoft.com/azure/ai-foundry/how-to/hub-create-projects)).

Fluxo típico de operação:

1. Provisionar o recurso Foundry e um hub/projeto para o time.
2. Conectar o projeto a serviços essenciais (Azure AI Services/OpenAI, Azure Storage, Application Insights etc.) via `Management center` > `Connections` ([guia de conexões](https://learn.microsoft.com/azure/ai-foundry/how-to/connections-add)).
3. Implantar modelos base ou serverless no catálogo (`Models + endpoints`) e habilitar o uso em playgrounds ou APIs.
4. Construir agentes, fluxos de Prompt com workflows ou integrações customizadas consumindo as conexões e deployments aprovados.
5. Monitorar telemetria (Application Insights), políticas e segurança diretamente pelo portal ou infraestrutura como código (Bicep/Terraform).

Essa arquitetura separa claramente gestão (hub) e consumo (project), permitindo que múltiplas equipes usem o mesmo backbone com isolamento de dados e políticas.

---  

## Extensibilidade do AI Foundry

O Foundry foi pensado para ser extensível via conexões reutilizáveis e APIs abertas. Alguns pontos-chave:

- **Connections reutilizáveis**: você pode integrar Azure AI Search, Cosmos DB, Storage, APIs externas ou endpoints personalizados. As conexões podem usar Managed Identity, service principal, chaves ou SAS, funcionando como *identity broker* para os recursos conectados ([conexões em hubs](https://learn.microsoft.com/azure/ai-foundry/how-to/hub-connections-add)).
- **SDKs e CLIs**: o serviço expõe SDKs (Python, REST) e suporte a Bicep/Terraform para automação de deployments, recriação de projetos e pipelines de CI/CD.
- **Agentes e ferramentas**: via Agent Service é possível anexar ferramentas próprias, fontes de dados e ações externas, mantendo o controle de credenciais através das mesmas conexões.
- **Infraestrutura compartilhável**: hubs diferentes podem consumir o mesmo recurso Foundry ou outras contas Azure AI, permitindo topologias multi-projeto ou multi-região conforme necessidade.
- **Observabilidade plugável**: Application Insights, Log Analytics e Azure Monitor se conectam como serviços auxiliares para métricas e logs centralizados.

Com essas extensões, times conseguem adicionar novos modelos, integrar dados proprietários e orquestrar agentes sem reimplantar a base, mantendo conformidade e governança centralizadas.

---  

## Exemplos de uso

Alguns casos de sucesso reais de clientes da Microsoft:  

### 1. Audi AG

- **Objetivo**: Assistente de autoatendimento para funcionários (RH).
- **Resultados**:
    - Deploy em apenas 2 semanas usando Azure AI Foundry, Cosmos DB, App Service e Functions.
    - Expandido para 8 agentes internos. [\[microsoft.com\]](https://www.microsoft.com/en/customers/story/24786-audi-ag-azure-ai-foundry)
- **Citação**:
    > “O Azure accelerator nos ajudou a pular meses de trabalho fundamental.” – Hendrik Drath, AI & Big Data. [\[microsoft.com\]](https://www.microsoft.com/en/customers/story/24786-audi-ag-azure-ai-foundry)

---  

### 2. LayerX (Mitsui & Co.)

- **Objetivo**: Automação de extração de dados de documentos financeiros jurídicos.
- **Resultados**:
    - Redução de 570 horas/ano de processamento manual.
    - Baseado em Foundry com Azure OpenAI, Cosmos DB, AI Search, Container Apps. [\[microsoft.com\]](https://www.microsoft.com/en/customers/story/24530-layerx-azure-ai-foundry)
- **Citação**:
    > “Escolhemos Azure desde o primeiro dia pelo encaixe perfeito com modelos OpenAI via Azure AI Foundry.” – Ryuya Nakamura. [\[microsoft.com\]](https://www.microsoft.com/en/customers/story/24530-layerx-azure-ai-foundry)

---  

### 3. Air India

- **Objetivo**: Atendimento automatizado ao cliente.
- **Resultados**:
    - 4 milhões de interações automatizadas.
    - 97% das sessões cobertas sem agente humano. [\[microsoft.com\]](https://www.microsoft.com/en/ai/ai-customer-stories)
- **Citação**:
    > “Estamos nos tornando uma empresa infundida por IA via parceria com Microsoft.”. [\[microsoft.com\]](https://www.microsoft.com/en/ai/ai-customer-stories)

---  

### 4. Ontada (Saúde)

- **Objetivo**: Análise de dados clínicos.
- **Resultados**:
    - Redução de 75% no tempo de processamento.
    - 70% dos dados não estruturados agora acessíveis. [\[microsoft.com\]](https://www.microsoft.com/en/ai/ai-customer-stories)

---  

### 5. Global Travel Collection

- **Objetivo**: Assistência para agentes de viagem.
- **Resultados**:
    - 1.5 milhões de horas de trabalho recuperadas com Foundry + Copilot Studio + Cosmos DB. [\[microsoft.com\]](https://www.microsoft.com/en-us/customers)

---  

### 6. Indiana Pacers

- **Objetivo**: Legendas em tempo real em arena esportiva.
- **Resultados**:
    - Local closed captions acionadas via Azure AI Foundry + SignalR + Functions. [\[microsoft.com\]](https://www.microsoft.com/en-us/customers)

---  

### 7. Microsoft (interno) – Feedback de clientes

- **Objetivo**: Análise automática de feedback multicanal (suporte, surveys, comunidade).
- **Resultados**:
    - Agente “multi-subagents” que agrupa, classifica e prioriza sinais.
    - Roteamento ativo e formulação de respostas asseveradas. [\[techcommun...rosoft.com\]](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/the-future-of-ai-from-noise-to-insight---an-ai-agent-for-customer-feedback/4464991)


---  
## HANDS ON

Bora colocar em prática esse conteúdo?  
Para isso vamos seguir o material prático: [AI Foundry na Prática](./Azure_AI_Foundry_na_Pratica.md)


---  

## Referências

- [Documentação oficial do Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)
- [O que é Azure AI Foundry?](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry)
- [Guia “Getting started” – Azure AI Foundry](https://ai.azure.com/explore/gettingstarted)
- [Quickstart – Criar agente no Agent Service](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/quickstart)
- [Quickstart SDK – primeiras etapas com código](https://learn.microsoft.com/en-us/azure/ai-foundry/quickstarts/get-started-code)
- [Treinamento e módulos – Azure AI Foundry](https://learn.microsoft.com/en-us/training/azure/ai-foundry)
- [Blog “Azure AI Foundry: Your AI App and agent factory”](https://azure.microsoft.com/en-us/blog/azure-ai-foundry-your-ai-app-and-agent-factory/)
- [DevBlog “What’s new in Azure AI Foundry”](https://devblogs.microsoft.com/foundry/whats-new-in-azure-ai-foundry-september-2025/)
- [DevBlog “Unleash your creativity at scale”](https://azure.microsoft.com/en-us/blog/unleash-your-creativity-at-scale-azure-ai-foundrys-multimodal-revolution/)
- [DevBlog “Welcome to the Azure AI Foundry Blog!”](https://devblogs.microsoft.com/foundry/welcome-to-azure-ai-foundry-blog/)
- [Blog GSDC “Building Intelligent Agents with Azure AI Foundry”](https://www.gsdcouncil.org/blogs/building-intelligent-agents-with-azure-ai-foundry)
- [Fórum “Copilot Studio Roadmap… Azure Foundry”](https://windowsforum.com/threads/copilot-studio-roadmap-enterprise-ai-agents-across-m365-power-platform-azure-foundry.385953/)

