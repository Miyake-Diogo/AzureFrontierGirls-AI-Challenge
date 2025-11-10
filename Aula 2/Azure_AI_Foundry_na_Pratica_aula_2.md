# AI Foundry na Prática - Aula 2

Agora que já sabe sobre o que se trata o AI Foundry e como os Agentes de AI funcionam, é hora de colocar em prática as habilidades que foram adquiridas.  

## Agenda  

1. Criar um grupo de recursos
2. Criar um recurso do AI Foundry
3. Fazer o deploy de um modelo
4. Criar um Agente
5. Criar um Workflow
6. Usar o Agent Chat Playground para testar como o modelo se comporta

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

## Criando um Agente no Azure AI Foundry

Após a criação do Recurso do Foundry, criação do projeto e implementação do Modelo, é hora de criar um Agente. No exemplo da aula de hoje criaremos um Agente capaz de enviar e-mails desejando Feliz Aniversário para o destinatário.

1. No projeto do Foundry, abra `Build and Customize` e clique em `Agents`. Na tela "Create and debug your agents", clique em `+ New agent`.

2. No menu à esquerda em "Setup" defina os campos 
- `Agent name:` Digite o nome desejado para o Agente (ex.: `AgentHappyBirthday`)
- `Deployment:` Escolha qual modelo deverá ser utilizado (ex.: `gpt4o-mini`)
- `Instructions:`Descreva as instruções que esse agente deverá realizar. (ex.: `Você é um Agente de envio de e-mails de feliz aniversário. Você envia e-mails em meu nome para desejar feliz aniversário para outras pessoas. Você não responde perguntas sobre qualquer outro assunto. Você envia e-mail somente sobre aniversários.`)
- `Agent Description:` Descreva seu agente para fins de documentação. Essa descrição não interfere nas instruções do agente. (ex.: `Agente que envia e-mails desejando Feliz Aniversário`)

3. Clique em `Try in playground` para testar o agente. Digite alguma mensagem desejando feliz aniversário para alguém (ex.: `Envie um e-mail para o "Nome e Email" desejando feliz aniversário com uma mensagem bem alegre e divertida.`)

    O Agente não será capaz de concluir a tarefa porque ele não tem conhecimento de quem é a pessoa e ele não tem instruções descritivas para envio do e-mail, e não tem nenhuma ferramenta (Tool) determinada em seu fluxo de tarefas.

4. Vamos configurar a ferramenta de envios de e-mails para ser utilizada pelo agente. Na mesma tela de configuração do Agente, vá até `Actions` e clique em `+Add`. 
- Selecione `Azure Logic Apps` e em seguida selecione `Workflow - SendEmailFromOutlook`.
- Em `Add Logic App action` - Resource, defina:
- `Tool name:` Descreva o Nome da Ferramenta (ex.: `AgentHappyBirthdaySendMail`)
- `Describe how to invoke tool:` Defina em quais circusntâncias a ferramenta deverá ser acionada pelo agente (ex.: `Use essa ferramenta quando um e-mail de aniversário precisa ser enviado`)
- Em `Add Logic App action` - Authentication, faça login com uma conta Outlook valida. Essa conta será responsável para o envio do email. Clique em create para finalizar a configuração da ferramenta.

5. Clique em `Try in playground` para testar o agente. Digite alguma mensagem desejando feliz aniversário para alguém (ex.: `Envie um e-mail para o "Nome e Email" desejando feliz aniversário com uma mensagem bem alegre e divertida como se você fosse o mestre Yoda de Star Wars.`)

    Agora o Agente será capaz de concluir a tarefa porque ele já sabe quem é a pessoa (você informou o nome e o e-mail no prompt) e ele já tem instruções descritivas para envio do e-mail (a ferramenta foi configurada para esse proposito).

6. Vamos configurar um catalogo de aniversariantes para que não seja necessário informar o endereço de e-mail no prompt. Faça o download do arquivo lista-de-aniversariantes.txt. Abra o arquivo e inclua um aniversariante novo com um endereço de e-mail válido.
- Na mesma tela de configuração do Agente, vá até `Knowledge` e clique em `+Add`. 
- Em `Add a data source` clique em `Files`. Em `Add files` selecione `Upload local`e clique em `Select local files`. Selecione o arquivo [lista-de-aniversariantes.txt](.\lista-de-aniversariantes.txt) que você baixou e editou no passo anterior. Clique em `Upload and save`

7. Clique em `Try in playground` para testar o agente. Digite alguma mensagem desejando feliz aniversário para alguém 
    (ex.: `Envie um e-mail para o "Nome que você adicionou na lista do arquivo [lista-de-aniversariantes.txt](.\lista-de-aniversariantes.txt)" desejando feliz aniversário com uma mensagem bem alegre e divertida usando o seu gosto por videogames como temática.`)

    Agora o Agente será capaz de concluir a tarefa porque ele já sabe quem é a pessoa (você informou o nome prompt e ele sabe qual o e-mail pois ele tem o conhecimento na base que você incluiu) e ele já tem instruções descritivas para envio do e-mail (a ferramenta foi configurada para esse proposito).  

8. Teste outras formas de interação com o agente.
    
> Importante: monitore o consumo de Tokens-per-Minute (TPM) da assinatura para evitar bloqueios de quota.

---

## Referências

- https://github.com/microsoft/ai-agents-for-beginners


