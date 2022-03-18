# Lab. 1 - Resource Provisioning  

Nesta etapa, você irá provisionar recursos dentro da OCI utilizando Terraform com o serviço **Resource Manager**!

- 🌀 [Página oficial do Resource Manager](https://www.oracle.com/br/devops/resource-manager/)
- 🧾 [Documentação do Resource Manager](https://docs.oracle.com/pt-br/iaas/Content/ResourceManager/home.htm)

Os recursos provisionados serão:

- OKE
- Artifact Registry
- Container Registry
- OCI DevOps
- APM
- API Gateway
- Streaming
- Object Storage
- Functions

Juntamente com recursos de Rede e Gerenciamento como:

- VCN
- Subnets
- Dynamic Groups
- Policies
- Compartments

- - -

## Passo 1 - Download do repositório

Como primeiro passo, devemos fazer o download do arquivo (zip) no repositório do github.

 1. Para isso, acesse o [repositório](https://github.com/CeInnovationTeam/terraform-dev-linuxtips) e clique em **Download ZIP**.
  

![](./images/IMG01.PNG)
  

## Passo 2 - Upload do terraform no Resource Manager

1. Faça o [login](https://www.oracle.com/cloud/sign-in.html) em sua conta na OCI.

2. No 🍔 menu de hambúrguer, acesse: **Developer Services** → **Resource Manager** → **Stacks**.

![](./images/IMG04_1.PNG)


- Nesta nova janela, certifique que está no compartment "root" e clique em **Create Stack**.

![](./images/IMG05.PNG)

- Selecione a opção "Zip file", clique em "browse" e arraste o arquivo (.zip), que contém os arquivos .tf. O Resource Manager irá preencher todos os campos.

![](./images/IMG06.PNG)

- Clique em **NEXT**, para podermos configurar alguns parâmetros sobre os recursos a serem provisionados.

- Nesta nova tela, lembre-se de selecionar o compartment criado, como abaixo.

![](./images/IMG02.PNG)

- Ao final da página, altere o display name padrão do container registry de "container_repository" para "java-img".

- Lembre-se também de alterar o bucket_namespace para o namespace da sua tenancy, como abaixo.

![](./images/IMG03.PNG)


- Criada nossa Stack, vamos agora clicar em **Apply**.


![](./images/IMG07.PNG)

  

![](./images/printplan2.PNG)


- Após concluído nosso PLAN, vamos agora voltar para nossa STACK e clicar em APPLY para de fato iniciar os provisionamentos e isso irá durar em torno de uns 20 minutos.

  

![](./images/printapply.PNG)

  

![](./images/printapply2.PNG)

  

## Ambientes Provisionados com Sucesso !

 - Após finalizar o APPLY com sucesso, podemos conferir nossos
   provisionamentos que foram efetuados!

### 😎 Booooaaa !!! Você foi capaz de provisionar recursos usando Terraform na OCI! 🚀

