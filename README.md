# Deploy automático de uma função AWS Lambda em Python

Refazer manualmente o deploy de uma função lamda sempre que uma alteração for feita pode ser moroso e tomar um tempo desnecessário. E ainda estar sujeito a esquecimentos e erros do usuário. Por isso, fazer o deploy automático sempre que uma alteração for feita é importante para manter as funções sempre na última versão.

O objetivo do projeto é criar um roteiro para automatizar o deploy de uma função AWS Lambda em Python sempre que um __git push__ for realizado na branch main. Para isso são utilziadas os seguintes serviços: __GitHub__, __Code Build__, __IAM__ e __Lambda__. 

Para reproduzir o projeto é necessário seguir as instruções dadas na sessão [passo a passo](#passo-a-passo-para-executar-o-projeto). Note que alguns arquivos precisam ser modificados antes de começar a fazer as aterações.

## Estrutura do projeto
    .
    ├── buildspec.yml
    ├── iam-policy.json
    ├── lambda_function.py
    ├── README.md
    └── requirements.txt

## Passo a passo para executar o projeto

<p align="center">
  <img src = https://github.com/LeonardoDonatoNunes/deploy_automatico_aws_lambda/blob/main/automatizacaoDeployLambda.png width=50%>
</p>

1) Criar uma função lambda no console da AWS;
2) Criar um repositório no GitHub;
3) Criar um projeto no Code Build e criar a conexão com o repositório criado anteriormente;
4) Alterar a política IAM adicionando com o conteúdo do arquivo `iam-policy.json`. Neste ponto é preciso alterar o valor da chave `Resource` para o arn da função lambda criada;
5) Alterar o conteúdo do arquivo `buildspec.yml` que contém as instruções para o deploy. Neste arquivo é importante verificar e alterar a versão do Python na `linha 5` e o `nome_da_funcao_lamda` na `linha 19` para o nome da função criada anteriormente;
6) Alterar o conteúdo do arquivo `requirements.txt` com as dependencias da função criada.

Pronto! Agora basta modificar a função lambda, que está no arquivo `lamda_function.py`, commitar e fazer um push que a função lambda na AWS será atualizada pelo __CodeBuild__.

## Referências

Conteúdo adaptado do canal [Felix Yu](https://www.youtube.com/@FelixYu) do YouTube. Vídeo: [CI/CD from GitHub to AWS Lambda (i.e., automatically update lambda function code) with CodeBuild](https://www.youtube.com/watch?v=AmHZxULclLQ&ab_channel=FelixYu). Acessado em: 2024-02-08.
