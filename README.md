# Overview
Este documento tem por objetivo guiar o usuário a como acessar a API Pagar.me no Windows, utilizando Docker-Compose. 

# Ferramentas necessárias

- Docker
- Git

# Docker

O Docker é uma plataforma aberta para desenvolvimento, envio e execução de aplicações. Ele permite que você separe suas aplicações em sua infraestrutura, tornando possível uma entrega mais rápida. Com o Docker, você pode gerenciar sua infraestrutura da mesma forma que gerencia suas aplicações. Ao aproveitar as metodologias do Docker para enviar, testar e implantar a aplicação, você pode reduzir significativamente o atraso entre a escrita do código e a execução em produção.

- [Get Docker](https://docs.docker.com/desktop/install/windows-install/).
- Em caso de problemas durante a instalação do o uso do Docker, visite [Troubleshoot Topics](https://docs.docker.com/desktop/troubleshoot/topics/).

# Git 

O recurso do Git que realmente o diferencia de quase todos os outros SCM é seu modelo de ramificação. O Git permite e incentiva você a ter várias ramificações locais que podem ser totalmente independentes umas das outras. A criação, mesclagem e exclusão dessas linhas de desenvolvimento leva segundos.

- [Download Git](https://git-scm.com/downloads)

# Clonando o repositório

Passo 1 - Com o Docker e o Git devidamente instalados, faça o download do arquivo [api.bundle](https://github.com/FBarros98/API/blob/master/api.bundle) presente neste repositório e salve em um diretório a sua escolha.

Passo 2 - Abra o terminal do Git Bash, navegue até o diretório no qual se encontra o arquivo [api_pagarme.bundle](https://github.com/FBarros98/API/blob/master/api_pagarme.bundle) e execute o seguinte comando: 

    git clone api_pagarme.bundle

Nesse diretório será criada uma pasta que contém todo o conteúdo desse repositório. 

# Acessando API

A pasta criada pelo arquivo [api_pagarme.bundle](https://github.com/FBarros98/API/blob/master/api_pagarme.bundle) deve conter os seguintes arquivos:

- app.py
- docker-compose.yml
- dockerfile
- requirements.txt
- README.md
- .gitignore

Para acessar a API devemos seguir o seguinte fluxo: 

Passo 1 - Abra o Windows Powershell e navegue até o diretório "api" criado pelo arquivo [api_pagarme.bundle](https://github.com/FBarros98/API/blob/master/api_pagarme.bundle). 

Passo 2 - Execute o comando abaixo no terminal do Powershell:

    docker-compose up -d

Esse comando irá criar um container em seu docker com todos os requisitos necessários para executar a API Pagar.me.

Passo 3 - Abra um navegador web de sua escolha e acesse a página : [localhost:8000](http://localhost:8000/).

# Confiabilidade

A observabilidade fornece insights sobre o comportamento dos aplicativos executados em seus ambientes. Ela deve ser vista como um atributo de qualquer sistema que você constrói e deseja monitorar. Ser capaz de detectar e corrigir eventos de causa raiz rapidamente é algo indispensável para a infraestrutura de um sistema.

Para monitorar a API Pagar.me podemos utilizar uma ferramenta da empresa Elastic, chamada [Elastic Observability](https://www.elastic.co/guide/en/observability/current/observability-introduction.html). O Observability possui um recurso chamado Heartbeat Synthetics, que nos permite simular as interações de um usuário em nossas aplicações. Desta forma, será possível monitorar o status code da API e as informações que são exibidas por ela.
Todo processo de configuração do servidor para enviar os dados para o Elasticsearch pode ser observado visitando [Send data to Elasticsearch](https://www.elastic.co/guide/en/observability/current/add-observability-data.html).

# Como realizar o monitoramento

O monitoramento realizado pelo Heartbeat Synthetics é feito através de steps. Cada step irá simular uma determinada interação do usuário. 
Esses roteiro deve ser criado em um arquivo YAML, na linguagem TypeScript, utilizando a biblioteca [Playwright](https://playwright.dev/docs/intro).
O processo de criação do YAML pode ser acompanhado seguindo as informações de [Write a synthetic test](https://www.elastic.co/guide/en/observability/current/synthetics-create-test.html).

Para o monitoramento da nossa API, foi utilizado o arquivo [api_pagarme.yml](https://github.com/FBarros98/API-Pagar.me/blob/86f0ed35a00aaa6262cdaf66c0b7edeb43672a68/api_pagarme.yml).

Com ele, será possível validar o status code da página, tirar um screenshot da tela para validação visual e verificar se os dados presentes na API estão sendo exibidos corretamente. 






