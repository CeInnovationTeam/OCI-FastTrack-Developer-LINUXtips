Olá, neste laboratório você aprenderá como registrar, monitorar e analisar os logs da infraestrutura Compute de OCI que você provisionou nos laboratórios anteriotes utilizando a **Oracle Cloud Observability and Management Platform**!

- 🌀 [Página oficial do OCI Observability and Management Platform](https://www.oracle.com/br/manageability/)
- 🧾 [Documentação do OCI Logging](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/loggingoverview.htm)
- 🧾 [Documentação do OCI Logging Analitics](https://docs.oracle.com/en-us/iaas/logging-analytics/index.html)
- 🧾 [Documentação do OCI Monitoring](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm)

**A seguir você aprenderá o passo-a-passo desta configuração:**

 - [Pre Reqs: Criar Canal no Slack e logar na sua conta OCI](#PreReqs)
 - [Passo 1: Ativar o serviço de Logging](#Passo1)
 - [Passo 2: Ativar o serviço de Logging Analytics](#Passo2)

- - -

## <a name="PreReqs"></a> Pre Reqs: Executar terraform de preparação de ambiente, e coletar informações relevantes ao processo

 1. Crie um [Workapace](https://slack.com/intl/pt-br/help/articles/201402297-Criar-um-canal) ou [Logue](https://slack.com/intl/pt-br/help/articles/212681477-Entrar-no-Slack) em um workspace existente;
 2. Crie um [Canal](https://slack.com/intl/pt-br/help/articles/201402297-Criar-um-canal) no Slack chamado *#linuxtips-lab5*;
 3. Faça o [login](https://www.oracle.com/cloud/sign-in.html) em sua conta na OCI;
 4. Execute o [Lab. #1](../Lab.%20%231%20-%20Resource%20Provisioning), caso não o tenha executado anteriormente;

---

## <a name="Passo1"></a> Passo 1: Ativar o serviço de Logging e Logging Analytics

1. No 🍔 menu de hambúrguer, acesse: **Observability and Management Platform** → **Logging**:
![](https://github.com/ladan19/images-lp/blob/main/photo-2.png?raw=true)
2. No menu à esquerda **Logging** clique em **Logs** e em seguida no botão à direita **Enable service log**:
![](https://github.com/ladan19/images-lp/blob/main/photo-3.png?raw=true)
3. Escolha em **Service** o item *Virtual Cloud Network* e em **Resource** selecione a subnet pública criada anteriormete. Em **Log Category** selecione a opção de *Flow Logs* e em **Log Name** digite o nome *Flowlogs-VCN*. Depois em Log Location cria um novo group:
![](https://github.com/ladan19/images-lp/blob/main/photo-4.png?raw=true)
4. Na mesma tela em **Log Location**, clique em **Create New Group** para criar um grupo e em **Name** digite o nome do grupo *LogGroupFlow*:
![](https://github.com/ladan19/images-lp/blob/main/photo-5.png?raw=true)
5. Agora clique no botão **Enable Log** para habilitar a configuração:
![](https://github.com/ladan19/images-lp/blob/main/photo-6.png?raw=true)
6. Após a ativação (2-3 minutos), inicia-se a coleta de logs. Para visualizar no menu à esquerda **Logging** clique em **Logs** e depois clique no Log Name que acabamos de criar **Flowlogs-VCN**:
![](https://github.com/ladan19/images-lp/blob/main/photo-7.png?raw=true)
7. Você vizualizará o dashboard de coleta de logs da VCN escolhida. Clique em **Explore with Log Search** à direita para:
![](https://github.com/ladan19/images-lp/blob/main/photo-8.png?raw=true)
8. Pronto! A pardir de agora você pode modificar as buscar para filtrar o log desejado. Dica: Mude a vialização para **Visualize** e divirta-se!


---

## <a name="Passo2"></a> Passo 2: Ativar o serviço de Logging Analytics

1. sdsds
2. 

---

### 👏🏻 Parabéns!!! Você foi capaz de configurar com sucesso um pipeline completo de **DevOps** na OCI! 🚀
