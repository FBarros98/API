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

Passo 2 - Abra o terminal do Git Bash, navegue até o diretório no qual se encontra o arquivo [api.bundle](https://github.com/FBarros98/API/blob/master/api.bundle) e execute o seguinte comando: 

    git clone api.bundle

Nesse diretório será criada uma pasta que contém todo o conteúdo desse repositório. 

# Acessando API

A pasta criada pelo arquivo [api.bundle](https://github.com/FBarros98/API/blob/master/api.bundle) deve conter os seguintes arquivos:

- app.py
- docker-compose.yml
- dockerfile
- requirements.txt
- README.md
- .gitignore

Para acessar a API devemos seguir o seguinte fluxo: 

Passo 1 - Abra o Windows Powershell e navegue até o diretório "api" criado pelo arquivo [api.bundle](https://github.com/FBarros98/API/blob/master/api.bundle). 

Passo 2 - Execute o comando abaixo no terminal do Powershell:

    docker-compose up -d

Esse comando irá criar um container em seu docker com todos os requisitos necessários para executar a API Pagar.me.

Passo 3 - Abra um navegador web de sua escolha e acesse a página : [localhost:8000](http://localhost:8000/).





