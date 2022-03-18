# Lab. 1 - Resource Provisioning  

Nesta etapa, você irá provisionar recursos dentro da OCI utilizando infraestrutura como código (IaC) com o Resource Manager!

- 🌀 [Página oficial do Resource Manager](https://www.oracle.com/br/devops/resource-manager/)
- 🧾 [Documentação do Resource Manager](https://docs.oracle.com/pt-br/iaas/Content/ResourceManager/home.htm)

**Os recursos provisionados serão:**

- OKE
- OCI DevOps
- APM
- API Gateway
- Streaming
- Object Storage

**Juntamente com recursos de REDE e GERENCIAMENTO como:**

1. VCN

2. SUBNETS

3. DYNAMIC GROUPS

4. COMPARTMENTS

  

## 1. Download repositório

  

 - Como primeiro passo devemos fazer o download do arquivo no repositório do github.

 - Para isso, acesse o [repositório](https://github.com/CeInnovationTeam/terraform-dev-linuxtips) e clique em **Download ZIP**.
  

![](./images/IMG01.PNG)
  

## Upload do terraform no Oracle Resource Manager

  

- Primeiro de tudo devemos estar **logados no OCI**

- Vá até o menu sanduiche na esquerda

  

![](./images/printsand.PNG)


- Clique em "**Developer Services**"

  

![](./images/printdevserv.PNG)


- Nas opcões que aparecer selecione "**Resource Manager**".

  

![](./images/printorm.PNG)


- Selecione e crie uma nova **STACK**

  

![](./images/printstack.PNG)

- Selecione como source **a pasta do seu computador contendo os arquivos .tf baixados**, fazendo assim com que o Resource Manager já preencha todos os campos.

  

![](./images/printcstack.PNG)

- Clique em NEXT e podemos conferir as infos sobre os recursos que serão provisionados.

- Lembre-se de selecionar o compartment criado, como abaixo.

![](./images/IMG02.PNG)

- Ao final da página, altere o display name padrão do container registry de "container_repository" para "java-img".

- Lembre-se também de alterar o bucket_namespace para o namespace da sua tenancy, como abaixo.

![](./images/IMG03.PNG)



- Criado nossa STACK vamos agora clicar em PLAN

  

![](./images/printplan.PNG)

  

![](./images/printplan2.PNG)


- Após concluído nosso PLAN, vamos agora voltar para nossa STACK e clicar em APPLY para de fato iniciar os provisionamentos e isso irá durar em torno de uns 20 minutos.

  

![](./images/printapply.PNG)

  

![](./images/printapply2.PNG)

  

## Ambientes Provisionados com Sucesso !

 - Após finalizar o APPLY com sucesso, podemos conferir nossos
   provisionamentos que foram efetuados!

### 😎 Booooaaa !!! Você foi capaz de provisionar recursos usando Terraform na OCI! 🚀

