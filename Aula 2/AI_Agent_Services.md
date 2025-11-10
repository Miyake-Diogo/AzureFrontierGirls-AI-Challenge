# AI Foundry - AI Agent Services

## Introdução

Imagine um mundo onde você não precisa lidar com tarefas repetitivas como processar faturas, resumir documentos ou gerenciar tickets de suporte. É isso que o **Azure AI Foundry** quer entregar: **automação inteligente** para liberar tempo e recursos, permitindo que você foque no que realmente importa.

Com os **Modelos de Linguagem (LLMs)**, abrimos a porta para sistemas que entendem dados não estruturados, tomam decisões e geram conteúdo. Mas transformar isso em produção não é tão simples: modelos podem errar, perder contexto e carecer de governança. É aí que entra o **Foundry Agent Service**.

![Imagem AI Foundry](../Attachments/Images/agent-service-the-glue.png)

---  

## O que é um **Agente de IA**?

- **Agentes ≠ Assistentes**  
    Enquanto assistentes ajudam pessoas, agentes **executam objetivos de forma autônoma**.
- Cada agente é **modular**, com:
    - **Modelo (LLM)**: inteligência e raciocínio.
    - **Instruções**: definem metas e comportamento.
    - **Ferramentas**: permitem buscar informações ou agir.

![AI Agent](../Attachments/Images/what-is-an-agent.png)  

Eles recebem entradas (prompts, alertas, mensagens) e geram saídas (resultados ou mensagens), podendo chamar ferramentas para buscar dados ou executar ações.

---  

## Como funciona a “Fábrica de Agentes” do Foundry?

![AI Agent](../Attachments/Images/agent-factory.png)

Pense no **Azure AI Foundry** como uma linha de montagem para agentes inteligentes:

1.  **Modelos**  
    Escolha entre GPT-4o, GPT-4, GPT-3.5, Llama e outros.
2.  **Customização**  
    Ajuste o modelo para seu caso: fine-tuning, prompts específicos, dados históricos.
3.  **Ferramentas**  
    Conecte o agente a recursos como Bing, SharePoint, Azure AI Search, Logic Apps, Azure Functions.
4.  **Orquestração**  
    Coordene tudo: chamadas de ferramentas, estados, logs e retries.
5.  **Observabilidade**  
    Monitore cada passo com logs, traces e integração com Application Insights.
6.  **Confiança e Segurança**  
    RBAC, Entra ID, filtros de conteúdo, criptografia e isolamento de rede.

Resultado: **agentes prontos para produção**, seguros e escaláveis.

---  

## Por que usar o Foundry Agent Service?

- **Visibilidade total**: acesso a threads estruturadas.
- **Coordenação multiagente**: suporte nativo para comunicação entre agentes.
- **Orquestração automática**: execução e logging sem esforço manual.
- **Segurança integrada**: filtros contra injeção de prompt e políticas corporativas.
- **Integração corporativa**: traga seu próprio storage, rede e índice.
- **Observabilidade**: rastreabilidade completa com Application Insights.
- **Controle de identidade**: RBAC, auditoria e acesso condicional via Entra.

---  

## HANDS ON

Bora colocar em prática esse conteúdo?  
Para isso vamos seguir o material prático: [AI Foundry na Prática](./Azure_AI_Foundry_na_Pratica_aula_2.md)

---


### Recursos adicionais

- [Documentação oficial](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview)
- Treinamentos e Certificações: 
    - [Azure AI Fundamentals](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/?source=recommendations)
    - [Develop AI Agent at Azure](https://learn.microsoft.com/en-us/training/modules/develop-ai-agent-azure/?source=recommendations)

