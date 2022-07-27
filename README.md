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

Passo 1 - Com o Docker e o Git devidamente instalados, faça o download do arquivo [api_pagarme.bundle](https://github.com/FBarros98/API/blob/master/api_pagarme.bundle) presente neste repositório e salve em um diretório a sua escolha.

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
- api_pagarme.yml

Para acessar a API devemos seguir o seguinte fluxo: 

Passo 1 - Abra o Windows Powershell e navegue até o diretório "api_pagarme" que foi criado. 

Passo 2 - Execute o comando abaixo no terminal do Powershell:

    docker-compose up -d

OBS: Antes de executar o comando garanta que o Docker Desktop está com o status 'running'.

Esse comando irá criar um container em seu docker com todos os requisitos necessários para executar a API Pagar.me.

Passo 3 - Abra um navegador web de sua escolha e acesse a página : [localhost:8000](http://localhost:8000/).

# Confiabilidade

A observabilidade fornece insights sobre o comportamento dos aplicativos executados em seus ambientes. Ela deve ser vista como um atributo de qualquer sistema que você constrói e deseja monitorar. Ser capaz de detectar e corrigir eventos de causa raiz rapidamente é algo indispensável para a infraestrutura de um sistema.

Para monitorar a API Pagar.me, podemos utilizar um produto da empresa Elastic, chamado [Elastic Observability](https://www.elastic.co/guide/en/observability/current/observability-introduction.html). O Observability possui um recurso chamado Uptime, que nos permite criar processos de monitoramento de diversos tipos, dentre eles temos o monitoramento sintético, que nos permite simular as interações de um usuário em nossas aplicações. 
Para executarmos esse monitoramento sintético, será necessário realizar a configuração do serviço [Heartbeat Synthetics](https://www.elastic.co/guide/en/observability/current/uptime-set-up.html#uptime-set-up-choose-heartbeat) em um servidor/container de sua escolha.

# Como realizar o monitoramento

O monitoramento sintético é realizado através de steps. Cada step irá simular uma determinada interação do usuário. 
Esse roteiro deve ser criado em um arquivo TypeScript, utilizando a biblioteca [Playwright](https://playwright.dev/docs/intro).
O processo de criação do roteiro pode ser acompanhado seguindo as informações de [Write a synthetic test](https://www.elastic.co/guide/en/observability/current/synthetics-create-test.html).
Esse arquivo Typescript permitirá que o monitoramento seja realizado de maneira local, para validar que os testes estão ocorrendo da maneira esperada. 

Para realizar o monitoramento da nossa API através do Uptime, é necessário que um arquivo YAML seja criado com os mesmos steps utilizados no arquivo Typescript. 
Esse YAML deve ser colocado no servidor no qual o serviço do Heartbeat Synthetics está sendo executado.
No nosso caso, a API Pagar.me será monitorada utilizando o arquivo [api_pagarme.yml](https://github.com/FBarros98/API-Pagar.me/blob/86f0ed35a00aaa6262cdaf66c0b7edeb43672a68/api_pagarme.yml).

Dessa forma, será possível visualizar através do portal do Elastic informações como: status code da página; screenshot da tela para validação visual; validar se todos os steps foram executados com sucesso. 

Além disso, é possível criar um alerta caso seja encontrado algum problema durante o monitoramento da API. Esse alerta pode ser enviado para diversas plataformas, como podemos ver em [Monitor status alert](https://www.elastic.co/guide/en/observability/current/monitor-status-alert.html). 
 







