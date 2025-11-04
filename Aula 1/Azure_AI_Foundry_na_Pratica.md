# AI Foundry na Prática

Agora que já sabe sobre o que se trata o AI Foundry é hora de colocar em prática as habilidades que foram adquiridas.  

## Agenda  

1. Criar um grupo de recursos
2. Criar um recurso do AI Foundry
3. Fazer o deploy de um modelo
4. Usar o Chat Playground para testar como o modelo se comporta

---  

## Criando um grupo de recursos

Crie um grupo de recursos para isolar os serviços usados no desafio. O portal oferece um fluxo guiado conforme a [documentação oficial](https://learn.microsoft.com/azure/azure-resource-manager/management/manage-resource-groups-portal#create-resource-groups).

1. Entre no [portal do Azure](https://portal.azure.com) com a assinatura habilitada para o Foundry.
2. No menu lateral, selecione `Resource groups` e clique em `Create`.
3. Escolha a assinatura correta, informe um nome exclusivo (ex.: `rg-foundry-lab`) e defina a região desejada.
4. Revise as informações em `Review + Create` e confirme com `Create`. Use a notificação `Go to resource group` para validar a criação.

> Dica: aplique tags (por exemplo, `projeto=frontier-girls`) para facilitar auditoria e limpeza após o laboratório.

---  

## Criando um recurso do AI Foundry

Com o grupo pronto, provisionamos o recurso do Azure AI Foundry e um hub/projeto para centralizar os experimentos. Utilize o assistente descrito na [quickstart oficial](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/quickstart-create-resources).

1. Acesse o [Azure AI Foundry portal](https://ai.azure.com) e selecione `Create project`.
2. Informe o nome do projeto (ex.: `foundry-lab-projeto`) e escolha `Create new hub` para gerar o hub automaticamente.
3. Defina o nome do hub, confirme a assinatura, o grupo de recursos e a região (mantenha o grupo criado anteriormente).
4. Revise o resumo em `Azure resources to be created` e confirme se hub, conta AI Foundry e conexões estão corretos.
5. Clique em `Create` e aguarde a implantação. Ao finalizar, o portal exibirá o projeto com links para deployments e playgrounds.

---  

## Fazendo o Deploy de um modelo de LLM

Após o recurso, faça o deploy de um modelo base (por exemplo, `gpt-4o-mini`) para habilitar testes e consumo via API. Siga o fluxo descrito em [How to deploy Azure OpenAI models](https://learn.microsoft.com/azure/ai-foundry/how-to/deploy-models-openai#deploy-an-azure-openai-model-from-your-project).

1. No projeto do Foundry, abra `Model catalog` ou `Models + endpoints`.
2. Filtre por `Azure OpenAI`, selecione o modelo desejado e clique em `Use this model`.
3. Escolha a conta AI Foundry criada anteriormente, defina o nome do deployment (ex.: `gpt4o-lab`) e valide SKU e quota.
4. Confirme com `Deploy` e aguarde a conclusão da implantação.
5. Ao final, use `Open in playground` para validar ou `View code` para copiar exemplos de consumo.

> Importante: monitore o consumo de Tokens-per-Minute (TPM) da assinatura para evitar bloqueios de quota.

---  

## Testando o Chat Playground

Com o deployment ativo, use o Chat Playground para validar respostas e ajustar configurações, conforme a [quickstart do playground](https://learn.microsoft.com/azure/ai-foundry/quickstarts/get-started-playground).

1. No projeto, abra `Playgrounds > Chat playground` e selecione o deployment criado (ex.: `gpt4o-lab`).
2. Personalize a `System message` com o contexto do desafio (ex.: orientar o assistente para o cenário Frontier Girls).
3. Opcionalmente, adicione `Safety system messages` para reforçar tom, limites e políticas.
4. Envie perguntas de teste, avalie latência, consistência e aderência às instruções.
5. Utilize `View code` para gerar snippets em Python, JavaScript ou REST com os parâmetros atuais.

> Boa prática: registre prompts e parâmetros eficazes (temperatura, top_p) para replicar comportamentos em produção.

---  

## BONUS: CAIRA - Composable AI Reference Architecture

CAIRA (Composable AI Reference Architecture) é um baseline de infraestrutura como código que acelera a criação de ambientes de IA no Azure com foco em segurança e observabilidade. O repositório oferece configurações base para soluções com Azure AI Foundry, permitindo que equipes iniciem agentes e cenários avançados com implantação consistente e escalável. Para começar, basta clonar `https://github.com/microsoft/CAIRA.git`, abrir o devcontainer fornecido (ou configurar o ambiente conforme a documentação de Environment Setup) e navegar até a pasta `reference_architectures/` para escolher e personalizar a configuração que melhor atende ao cenário. O modo de chat “🤖 CAIRA Assistant” orienta o processo ponta a ponta, valida pré-requisitos e ajuda a confirmar recursos após o deploy. O projeto aceita contribuições sob o Microsoft CLA, segue o Código de Conduta de Código Aberto e recomenda revisar o padrão de Responsible AI e as orientações de postura de segurança antes de levar a arquitetura para produção. Telemetrias opcionais (incluindo AVM) ajudam a evoluir o projeto, e podem ser desativadas conforme instruções do repositório.


## BONUS: Responsible AI  

Incorpore princípios de IA responsável antes de liberar o copiloto para uso amplo. Use as diretrizes da Microsoft como base para um checklist CAIRA (Checklist de Avaliação e Integridade de Responsabilidade em AI), conforme [Responsible AI na Azure](https://learn.microsoft.com/azure/well-architected/ai/responsible-ai) e [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai).

1. **Contexto e propósito**: documente objetivo do copiloto, públicos, dados suportados e limites conhecidos.
2. **Governança e segurança**: confirme RBAC, logs e estratégia Zero Trust para prevenir uso indevido e garantir rastreabilidade.
3. **Equidade e inclusão**: planeje revisões humanas e métricas para identificar respostas enviesadas ou excludentes.
4. **Transparência**: mantenha material explicando configurações do modelo, origem das instruções e orientações de validação humana.
5. **Ciclo contínuo**: estabeleça cadência para reavaliar o checklist sempre que houver atualização de modelo, dados ou políticas.

---  

## Referências

- https://learn.microsoft.com/azure/azure-resource-manager/management/manage-resource-groups-portal#create-resource-groups
- https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/quickstart-create-resources
- https://learn.microsoft.com/azure/ai-foundry/how-to/deploy-models-openai#deploy-an-azure-openai-model-from-your-project
- https://learn.microsoft.com/azure/ai-foundry/quickstarts/get-started-playground
- https://learn.microsoft.com/azure/well-architected/ai/responsible-ai
- https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai

