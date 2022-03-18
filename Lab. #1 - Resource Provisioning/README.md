# Lab. #1 - Resource Provisioning  

**Objetivo desse lab:**

Provisionar recursos dentro do OCI utilizando infraestrutura como código.

**Os recursos provisionados serão:**

1. OKE

2. DEVOPS

3. APM

4. API GATEWAY

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

- Selecione um compartment como primeira opção e o restante não será necessário alterar.

- Clique em NEXT.

  

![](./images/printstackcomp.PNG)


- Nessa nova tela irá pedir para conferir as informações e clique em CREATE

  

![](./images/printstackcreate.PNG)


- Criado nossa STACK vamos agora clicar em PLAN

  

![](./images/printplan.PNG)

  

![](./images/printplan2.PNG)


- Após concluído nosso PLAN, vamos agora voltar para nossa STACK e clicar em APPLY para de fato iniciar os provisionamentos e isso irá durar em torno de uns 20 minutos.

  

![](./images/printapply.PNG)

  

![](./images/printapply2.PNG)

  

## Ambientes Provisionados com Sucesso !

 - Após finalizar o APPLY com sucesso, podemos conferir nossos
   provisionamentos que foram efetuados.

**Recursos provisionados:**

1. OKE

2. OCI DevOps

3. APM

4. API Gateway

**Juntamente com recursos de Rede e Gerenciamento como:**

1. VCN

2. Subnets

3. Dynamic Groups

4. Compartments