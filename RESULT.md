# Resultado - Desáfio CoorLab

## Ambiente
Para iniciar o desenvolvimento do projeto foi necessário realizar preparação do ambiente. Como primeiro passo, criei duas pastas dentro de "app": frontend e backend. Dentro delas verifiquei a instalação das dependências necessárias para cada desenvolvimento antes de iniciar a codificação propriamente dita.

# Backend
Pela experiência que já possuia com o python e a construção de APIs REST, optei por iniciar o desenvolviemento pelo backend em Flask. 

Após uma análise minuciosa da História de Usuário e do protótipo proposto, verifiquei a necessidade de duas rotas principais: 

- GET "/cities"
    Rota para verificar as cidades disponíveis para viagem, etapa pré-requisito para a solicitação de preços disponíveis.
- POST "/trips"
    Rota que recebe em seu body um JSON com o seguinte formato:
    {
        "cityNames": "",
        "date": ""
    }
    e recebe como resposta a opção mais de viagem mais confortável e rápida e a opção mais econômica.

    Obs: Visto que o banco de dados fornecido não oferecia informações adicionais sobre a data das viagens, ela foi inclusa na requisição, mas desnconsiderada na lógica de seleção das viagens.

Para melhor exibição, realizei um tratamento inicial do banco de dados no momento do carregamento, que incluem:
    - Formatação do tempo de duração e preços para aplicação da lógica de seleção.
    - Ajuste do nome de duas cidades para fins de correção e melhor exibição.

Considerando a quantidade de rotas e o escopo do projeto, optei por deixá-las em um arquivo único. Em caso de uma arquitetura com maior quantidade de Casos de Uso, a modularização da API é recomendada.

Para o teste das requisições do Backend, utilizei o software Insomnia ao longo do desenvolvimento.

# Frontend
Inciei o desenvolvimento com o criação da aplicação Vue.js. Como referência de UI e UX, me guiei pelo protótipo fornecido.

Além do demonstrado, adicionei uma tela inicial para aplicação que indica a funcionalidade de calculadora de viagens. Somente clicando sobre o botão na Sidebar, o usuário tem acesso à funcionalidade proposta.

A aplicação foi feita em uma View única HomeView.vue a qual é composta pelos componentes:
    - WelcomeComponent.vue (Texto de boas vindas)
    - SidebarButton.vue (Botão para acessar serviço da calculadora)
    - TripfinderComponent.vue (Janela da calculadora de viagens)
    - ResultGrid (Componente de exibição dos resultados)

Para conexão com o banco de dados, utilizei o Axios para as requisições cliente HTTP e na seleção da data, o vue2-datepicker especialmente para Vue 2.

Toda a lógica de sequências de ações foram baseadas no vídeo de protótipo, desde as selecões relativas a viagem até a limpeza dos dados pesquisados.




