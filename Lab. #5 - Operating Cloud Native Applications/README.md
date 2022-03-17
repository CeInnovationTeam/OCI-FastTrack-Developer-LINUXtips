# Lab. #5 - Operating Cloud Native Applications

Olá, neste laboratório você aprenderá como registrar, monitorar e analisar os logs da infraestrutura Compute de OCI que você provisionou nos laboratórios anteriotes utilizando a **Oracle Cloud Observability and Management Platform**!

- 🌀 [Página oficial do OCI Observability and Management Platform](https://www.oracle.com/br/manageability/)
- 🧾 [Documentação do OCI Logging](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/loggingoverview.htm)
- 🧾 [Documentação do OCI Logging Analitics](https://docs.oracle.com/en-us/iaas/logging-analytics/index.html)
- 🧾 [Documentação do OCI Monitoring](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm)

**A seguir você aprenderá o passo-a-passo desta configuração:**

- [Pre Reqs: Criar Canal no Slack e logar na sua conta OCI](#PreReqs)
- [Passo 1: Ativar o serviço de Logging e habilitar a coleta dos Logs](#Passo1)
- [Passo 2: Ativar o serviço de Logging Analytics e criar um grupo para os Logs](#Passo2)
- [Passo 3: Criar o Service Connector para replicar os logs do Logging para o Logging Analytics](#Passo3)

- - -

## <a name="PreReqs"></a> Pre Reqs: Criar Canal no Slack e logar na sua conta OCI

 1. Crie um [Workapace](https://slack.com/intl/pt-br/help/articles/201402297-Criar-um-canal) ou [Logue](https://slack.com/intl/pt-br/help/articles/212681477-Entrar-no-Slack) em um workspace existente;
 2. Crie um [Canal](https://slack.com/intl/pt-br/help/articles/201402297-Criar-um-canal) no Slack chamado *#linuxtips-lab5*;
 3. Faça o [login](https://www.oracle.com/cloud/sign-in.html) em sua conta na OCI;
 4. Execute o [Lab. #1](../Lab.%20%231%20-%20Resource%20Provisioning), caso não o tenha executado anteriormente;

---

## <a name="Passo1"></a> Passo 1: Ativar o serviço de Logging e habilitar a coleta dos Logs

1. No 🍔 menu de hambúrguer, acesse: **Observability and Management Platform** → **Logging**:
![](https://github.com/ladan19/images-lp/blob/main/photo-2.png?raw=true)
2. No menu à esquerda **Logging** clique em **Logs** e em seguida no botão à direita **Enable service log**:
![](https://github.com/ladan19/images-lp/blob/main/photo-3.png?raw=true)
3. Escolha em **Service** o item *Virtual Cloud Network* e em **Resource** selecione a subnet pública criada anteriormete. Em **Log Category** selecione a opção de *Flow Logs* e em **Log Name** digite o nome *Flowlogs-VCN*. Depois em Log Location clique em **Show Advanced Options** e clique em **Create New Group** para criar um novo grupo:
![](https://github.com/ladan19/images-lp/blob/main/photo-4.png?raw=true)
4. Na tela de criação de grupo de log em **Name** digite o nome do grupo *LogGroupFlow* e clique no botão **Create**:
![](https://github.com/ladan19/images-lp/blob/main/photo-5.png?raw=true)
5. Deixe selecionado o *LogGroupFlow* como **Log Group** e clique no botão **Enable Log** para habilitar a configuração:
![](https://github.com/ladan19/images-lp/blob/main/photo-6.png?raw=true)
6. Após a ativação (2-3 min), inicia-se a coleta de logs (5-6 min). Para visualizar no menu à esquerda **Logging** clique em **Logs** e depois clique no Log Name que acabamos de criar **Flowlogs-VCN**:
![](https://github.com/ladan19/images-lp/blob/main/photo-7.png?raw=true)
7. Você vizualizará o dashboard de coleta de logs da VCN escolhida. Clique em **Explore with Log Search** à direita para:
![](https://github.com/ladan19/images-lp/blob/main/photo-8.png?raw=true)
8. Pronto! A pardir de agora você pode modificar as buscar para filtrar o log desejado.

> Dica: Mude a vialização para **Visualize** e divirta-se!


---

## <a name="Passo2"></a> Passo 2: Ativar o serviço de Logging Analytics e criar um grupo para os Logs

1. No 🍔 menu de hambúrguer, acesse: **Observability and Management Platform** → **Logging Analytics** :
![](https://github.com/ladan19/images-lp/blob/main/photo-10.png?raw=true)
2. Ative o clicando no botão **Start Using Logging Analytics**:
![](https://github.com/ladan19/images-lp/blob/main/photo-11.png?raw=true)
3. Após a inicialização, clique no botão **Take me to Log Explorer**:
![](https://github.com/ladan19/images-lp/blob/main/photo-12.png?raw=true)

> Dica: Repare que o serviço já cria algumas poíticas e um grupo de log *Default*

5. Na console de Log Explorer no menu superior à esquerda clique e selecione **Administration**:
![](https://github.com/CeInnovationTeam/OCI-FastTrack-Developer-LINUXtips/blob/main/Lab.%20%235%20-%20Operating%20Cloud%20Native%20Applications/images/Image02.png?raw=true)
6. Agora clique em **Log Groups** no menu **Resources** e em seguida no botão **Create Log Group**, para criarmos um novo grupo de log:
![](https://github.com/ladan19/images-lp/blob/main/photo-13.png?raw=true)
![](https://github.com/ladan19/images-lp/blob/main/photo-14.png?raw=true)
7. Na console de criação de grupo de Log em **Name** digite o nome do grupo *LogGroupVCN* e depois clique no botão **Create**:
![](https://github.com/ladan19/images-lp/blob/main/photo15.png?raw=true)

---

## <a name="Passo3"></a> Passo 3: Criar o Service Connector para replicar os logs do Logging para o Logging Analytics


1. No 🍔 menu de hambúrguer, acesse: **Observability and Management Platform** → **Service Connectors**:
![](https://github.com/ladan19/images-lp/blob/main/photo-16.png?raw=true)
3. Na console de *Service Connectors* clique no botão **Create Service Connector**:
![](https://github.com/CeInnovationTeam/OCI-FastTrack-Developer-LINUXtips/blob/main/Lab.%20%235%20-%20Operating%20Cloud%20Native%20Applications/images/Image03.png?raw=true)
1. Em **Connector Name** digite *LogVCNConnector*, em **Configure Source** selecione *Logging* e em **Target** selecione *Logging Analytcs*. Na parte de *Configure Source* selecione em **Log Group** o *LogGroupFlow* e em **Logs** selecione o *FlowLogs-VCN* criados anteriosmente:
![](https://github.com/ladan19/images-lp/blob/main/photo17.png?raw=true)
1. Em **Configuration Target** selecione o **Log Group** *LogGroupVCN* e (Muito Importante :warning:) clique no botão **Create** à direita _para criar as políticas para o conector tenha permissão de escrita_. Após isso clique no botão **Create** no canto inferior à esquerda para criar o conector:
![](https://github.com/ladan19/images-lp/blob/main/photo-18.png?raw=true)
1. asdas


---

### 👏🏻 Parabéns!!! Você foi capaz de configurar com sucesso um pipeline completo de **DevOps** na OCI! 🚀
