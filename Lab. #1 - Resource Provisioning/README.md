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

![](./images/IMG04_01.PNG)

3. Nesta nova janela, certifique que está no compartment "root" e clique em **Create Stack**.

![](./images/IMG05.PNG)

4. Selecione a opção "Zip file", clique em "browse" e arraste o arquivo (.zip), que contém os arquivos .tf. O Resource Manager irá preencher todos os campos.

![](./images/IMG06.PNG)

5. Clique em **Next**, para podermos configurar alguns parâmetros sobre os recursos a serem provisionados.

6. Nesta nova tela, lembre-se de selecionar o compartment criado, como abaixo.

![](./images/IMG02.PNG)

7. Duplique a aba do seu navegador, clique no menu do lado direto no ícone do usuário e no nome da sua tenancy.

![](./images/IMG08.PNG)

8. Agora copie o **Object Storage Namespace**.

![](./images/IMG09.PNG)

9. De volta à aba do Resource Manager, altere o **bucket_namespace** para o namespace copiado.

10. Altere também o **display name** padrão do container registry de "container_repository" para "java-img".

![](./images/IMG03.PNG)


11. Criada nossa stack, clique em **Apply** e confirme a ação.


![](./images/IMG07.PNG)


12. O provisionamento dos recursos deverá durar em torno de 25 minutos.

13. Após finalizar o Apply com sucesso, podemos conferir o provisionamento dos nossos recursos!

### ✅ Ambientes provisionados com sucesso!!! Você foi capaz de provisionar recursos usando Terraform na OCI! 🚀

