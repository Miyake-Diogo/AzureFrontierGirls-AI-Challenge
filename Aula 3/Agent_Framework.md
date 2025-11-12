# Microsoft Agent Framework

Abaixo vai um **resumo direto** do que é o *Microsoft Agent Framework*, suas **capacidades principais** e uma curadoria de **tutoriais + repositórios de código** para você começar rápido.

---  

## O que é o Microsoft **Agent Framework**?

O **Microsoft Agent Framework (MAF)** é um framework open source (C#/.NET e Python) para **construir, orquestrar e implantar agentes de IA** — de um chat simples até **workflows multi‑agentes** com telemetria, ferramentas, memória e integração com provedores diversos (Azure OpenAI, Foundry Models, etc.). Ele sucede e unifica aprendizados do **Semantic Kernel** e do **AutoGen**, oferecendo APIs mais simples e um runtime alinhado ao **Azure AI Foundry Agent Service** quando você quiser hospedagem gerenciada. [\[github.com\]](https://github.com/microsoft/agent-framework), [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel/), [\[devblogs.m...rosoft.com\]](https://devblogs.microsoft.com/semantic-kernel/semantic-kernel-and-microsoft-agent-framework/)

Em alto nível, o MAF fornece:

- **SDK multi‑linguagem** (Python e .NET) com **APIs unificadas** para criar agentes e **workflows em grafo** (com *checkpointing*, *streaming* e *human‑in‑the‑loop*). [\[github.com\]](https://github.com/microsoft/agent-framework)
- **Observabilidade** via **OpenTelemetry** e integrações de telemetria, além de **DevUI** para desenvolvimento/teste de agentes. [\[github.com\]](https://github.com/microsoft/agent-framework)
- **Interoperabilidade** com padrões/protocolos (p.ex., **MCP**, A2A) e múltiplos provedores de modelo (Azure OpenAI, Foundry, OpenAI). [\[github.com\]](https://github.com/microsoft/agent-framework), [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/agent-framework/user-guide/agents/agent-types/azure-ai-foundry-models-responses-agent)
- **Caminho de migração** de **Semantic Kernel** e **AutoGen** (o MAF é tratado como a “evolução”/“SK 2.0”). [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel/), [\[github.com\]](https://github.com/microsoft/agent-framework/discussions/1127)

> Para um panorama guiado e hands‑on, veja a documentação oficial do Agent Framework no Microsoft Learn. [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/agent-framework/)

---  

## Capacidades (em prática)

1.  **Agentes single/multi‑agente**  
    Crie desde um agente de chat até **sistemas multi‑agentes** (padrões como *sequential*, *concurrent*, *group chat*, *handoff*, *manager/“magnetic” orchestration*). [\[microsoft.github.io\]](https://microsoft.github.io/ai-agents-for-beginners/14-microsoft-agent-framework/)

2.  **Workflows em grafo e ferramentas (Tools)**  
    Conecte agentes a **ferramentas determinísticas** (funções, APIs, conectores) e componha **pipelines** com **estado** e **checkpoints** para tarefas longas. [\[github.com\]](https://github.com/microsoft/agent-framework)

3.  **Observabilidade integrada**  
    Tracing distribuído com **OpenTelemetry** para cada passo do agente (invocação de ferramenta, raciocínio, orquestração), com painéis no Azure AI Foundry/Insights. [\[github.com\]](https://github.com/microsoft/agent-framework)

4.  **Provedores de modelo e hospedagem**  
    Use o MAF **localmente** ou **hospedado** no **Azure AI Foundry Agent Service**, que oferece o ciclo de vida gerenciado (criar/testar/operar agentes, threads, ferramentas). [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/training/paths/develop-ai-agents-on-azure/), [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/4-azure-ai-agent-service)

5.  **Integração com Foundry Models (OpenAI Responses compatível)**  
    Você pode criar agentes que consomem **Foundry Models** usando **client libraries OpenAI** (API compatível *Responses*). [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/agent-framework/user-guide/agents/agent-types/azure-ai-foundry-models-responses-agent)

6.  **Migração simplificada (SK/AutoGen → MAF)**  
    Guias oficiais explicam equivalências de namespaces, criação de agentes, threads, etc., reduzindo *boilerplate* e padronizando padrões entre provedores. [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel/)

---  

## Como o MAF se relaciona com **Copilot Studio** e **Agents**?

- **Copilot Studio** é a plataforma low‑code para criar **agentes** com **orquestração generativa**, conhecimento, ferramentas e **multi‑agente (child/connected)** — ideal para equipes *fusion* e cenários M365/Teams/Web. [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/microsoft-copilot-studio/), [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-generative-actions), [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-add-other-agents)
- O **Agent Framework** é o **SDK code‑first** para times de engenharia que precisam **orquestração programática**, *tooling* avançado e integração a pipelines/telemetria… podendo também **conectar**‑se ao **Azure AI Foundry Agent Service** para um runtime gerenciado. [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/training/paths/develop-ai-agents-on-azure/), [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/4-azure-ai-agent-service)

Se você precisa de **multi‑agente low‑code** (ex.: “mestre” + “child agents”) dentro do Copilot Studio, há recursos nativos de **connected/child agents** e **generative orchestration**. [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-add-other-agents), [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-generative-actions)

---  

## Exemplos mínimos de código (Python)
> Observação o env do código mostrado em aula foi pego do repositório: https://github.com/microsoft/agent-framework/tree/main/python.  
> Note que não é necessário todas as variáveis de ambiente, somente as que envolvam o Azure Open AI para os exemplos mostrados.  



> Python – instalação e hello world (repo oficial) [\[github.com\]](https://github.com/microsoft/agent-framework)

```bash
pip install agent-framework 
```

```python
from agents import AIAgent
# Dica: veja os exemplos no diretório `python/` e `workflow-samples/` do repositório.
# Criação varia conforme provedor; o padrão é criar o client e então o AIAgent com instructions.
```

> Para passos completos do “**Quick Start**” (pré‑requisitos, pacotes e exemplos), use o guia do Microsoft Learn. [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/agent-framework/tutorials/quick-start)

---  

## Tutoriais recomendados (passo a passo)

- **Agent Framework – Quick Start (Learn)**: inicia em minutos com .NET ou Python, usando Azure OpenAI. [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/agent-framework/tutorials/quick-start)
- **Learning Path – Develop AI agents on Azure** (9 módulos): visão, Agent Service, VS Code extension, **ferramentas personalizadas** e **multi‑agente**. [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/training/paths/develop-ai-agents-on-azure/)
- **AI Agents for Beginners (curso)** + **lição: “Exploring Microsoft Agent Framework”** com padrões, cenários e código. [\[microsoft.github.io\]](https://microsoft.github.io/ai-agents-for-beginners/), [\[microsoft.github.io\]](https://microsoft.github.io/ai-agents-for-beginners/14-microsoft-agent-framework/)
- **Migração do Semantic Kernel para Agent Framework** (benefícios, mapeamentos de API). [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel/)
- **Blog/Docs – relação SK ↔ MAF** (posição oficial do time SK). [\[devblogs.m...rosoft.com\]](https://devblogs.microsoft.com/semantic-kernel/semantic-kernel-and-microsoft-agent-framework/)

### Copilot Studio (low‑code), se for do seu interesse

- **Orquestração generativa (quando, como e limitações)**. [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-generative-actions)
- **Child/Connected Agents (preview)** — montar **multi‑agente** via Studio. [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-add-other-agents)
- **Fundamentos e Academy** – blocos: Knowledge, Tools, Topics, Instructions. [\[microsoft.github.io\]](https://microsoft.github.io/agent-academy/recruit/02-copilot-studio-fundamentals/), [\[github.com\]](https://github.com/microsoft/agent-academy/blob/main/docs/recruit/02-copilot-studio-fundamentals/README.md)

---  

## Repositórios e exemplos de **código**

- **Repo oficial do Agent Framework (MAF)** – código‑fonte, pacotes Python/.NET, **workflow‑samples** e **DevUI**. [\[github.com\]](https://github.com/microsoft/agent-framework)
- **Agent Framework Samples (hands‑on)** – trilha com *for beginners*, ferramentas, RAG, multi‑agente, workflows. [\[github.com\]](https://github.com/microsoft/Agent-Framework-Samples)
- **Agentic AI Lab – Agent Framework** – *notebooks* e exemplos práticos (agentes, memória, observabilidade). [\[github.com\]](https://github.com/microsoft/agentic-ai-lab/blob/main/agent-framework/README.md)
- **Learning path + SDK do Azure AI Foundry Agent Service** – para **hospedar/gerir agentes** no Azure (visual e code‑first). [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/training/paths/develop-ai-agents-on-azure/), [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/4-azure-ai-agent-service)

---  

## Quando usar o MAF (padrões típicos)

- **Aplicações enterprise** que exigem **telemetria de ponta a ponta**, **recuperação** de tarefas longas e **observabilidade**. [\[github.com\]](https://github.com/microsoft/agent-framework)
- **Soluções multi‑agente** (planejador/execução, *handoffs*, colaboração) com **workflows declarativos em grafo**. [\[github.com\]](https://github.com/microsoft/agent-framework), [\[microsoft.github.io\]](https://microsoft.github.io/ai-agents-for-beginners/14-microsoft-agent-framework/)
- **Integrações customizadas** (MCP/A2A, ferramentas próprias, APIs internas, Foundry/OpenAI). [\[learn.microsoft.com\]](https://learn.microsoft.com/en-us/agent-framework/user-guide/agents/agent-types/azure-ai-foundry-models-responses-agent), [\[github.com\]](https://github.com/microsoft/agent-framework)

---  

