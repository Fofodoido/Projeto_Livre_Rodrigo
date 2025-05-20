# Projeto_Livre_Rodrigo
Rodrigo Henrique Donato de Souza - 241012374

Projeto livre de Orientação a Objeto que busca fazer o jogo da cobrinha.
O projeto em UML e em Casos de Uso está na pasta principal do arquivo.

INSTRUÇÕES
    -No linux, use ./run_game_linux.sh para rodar
    -No Windows, use o "run_windows.bat" para rodar.
    -Verifique se Python está instalado.

DEFINIÇÃO DO PROBLEMA
    - Criar um jogo da cobrinha orientado a objeto.
    - O maior desafio foi, sem sombra de dúvidas, usar o Pygame e o adaptar.

CASOS DE USO.
Caso de Uso – Iniciar Jogo
Objetivo: Este caso possibilita o usuário jogar o jogo da cobrinha por meio de comandos no terminal.
Ator: Usuário
Pré-condições: Sem pré-condição.
Condição de Entrada: Apertar tecla “1”
Fluxo Principal:
    1. Usuário seleciona a opção 1: Iniciar (B)
    2. Usuário recebe a opção de definir um dificuldade: Fácil, médio e difícil. (A) (B)
    3. Usuário seleciona a dificuldade e recebe um prompt para inserir seu nome (A)
    4. Usuário começa o jogo no meio da tela.
    5. Usuário Coleta comidas, cresce e, eventualmente, perde.
    6. Usuário recebe a opção de tentar novamente ou de voltar para o menu (B)(C)
    7. Usuário volta para o Menu
    8. Usuário sai do jogo
Fluxos Alternativos:
    A. Usuário escolhe voltar uma tela.
        1. Volta para a tela anterior
    B. Usuário seleciona uma opção inválida
        1. Exibe mensagem de opção invalida
        2. Exibe o menu novamente
    C. Usuário tenta novamente
        1. Volta para a seleção de dificuldade e continua.

Caso - Ver Placar
Objetivo: Este caso mostra para o usuário o placar dos jogadores do melhor para o pior.
Pré-condições: nenhuma
Condição de Entrada: Teclar 2
Fluxo principal:
    1. Usuário seleciona a opção 2 (A)
    2. Usuário recebe todo o placar na tela
    3. Usuário volta para o menu
Fluxos alternativos:
    A. Usuário seleciona opção inválida
        1. Usuário recebe mensagem de erro
        2. Retorna para o menu

Caso – Sair
Objetivo: Sair do Jogo
Pré-condições: nenhuma
Condição de Entrada: Teclar 3
Fluxo Principal: 
    1. Usuário seleciona a opção 3 (A)
    2. Usuário sai do jogo.
Fluxo alternativo:
    A. Usuário seleciona opção inválida
        1. Usuário recebe mensagem de erro
        2. Usuário volta para o menu.


