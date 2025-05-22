# Projeto Livre Rodrigo
# Casos de Uso - Jogo da Cobrinha

Este projeto permite ao usuário jogar o clássico Jogo da Cobrinha via terminal, com diferentes funcionalidades acessadas por meio de comandos numéricos.

---

## 🎮 Caso de Uso – Iniciar Jogo

**Objetivo:** Permitir que o usuário inicie o jogo da cobrinha por meio de comandos no terminal.  
**Ator:** Usuário  
**Pré-condições:** Nenhuma  
**Condição de Entrada:** Pressionar a tecla `1`

### Fluxo Principal:
1. Usuário seleciona a opção `1`: Iniciar (B)
2. Usuário recebe a opção de definir a dificuldade: Fácil, Médio e Difícil (A)(B)
3. Usuário seleciona a dificuldade e insere seu nome (A)
4. Jogo começa com a cobrinha no meio da tela
5. Usuário coleta comidas, cresce e eventualmente perde
6. Usuário recebe a opção de tentar novamente ou voltar para o menu (B)(C)
7. Usuário volta para o menu
8. Usuário sai do jogo

### Fluxos Alternativos:
- **A. Usuário escolhe voltar uma tela**
  1. Volta para a tela anterior
- **B. Usuário seleciona uma opção inválida**
  1. Exibe mensagem de opção inválida
  2. Exibe o menu novamente
- **C. Usuário tenta novamente**
  1. Retorna à seleção de dificuldade e continua

---

## 🏆 Caso de Uso – Ver Placar

**Objetivo:** Exibir o placar dos jogadores do melhor para o pior  
**Pré-condições:** Nenhuma  
**Condição de Entrada:** Pressionar a tecla `2`

### Fluxo Principal:
1. Usuário seleciona a opção `2` (A)
2. O placar é exibido na tela
3. Usuário volta para o menu

### Fluxo Alternativo:
- **A. Usuário seleciona uma opção inválida**
  1. Exibe mensagem de erro
  2. Retorna ao menu

---

## 📖 Caso de Uso – Instruções

**Objetivo:** Exibir instruções e regras do jogo  
**Pré-condições:** Nenhuma  
**Condição de Entrada:** Pressionar a tecla `3`

### Fluxo Principal:
1. Usuário seleciona a opção `3` (A)
2. As instruções do jogo são exibidas
3. Usuário retorna ao menu

### Fluxo Alternativo:
- **A. Usuário seleciona uma opção inválida**
  1. Exibe mensagem de erro
  2. Retorna ao menu

---

## ❌ Caso de Uso – Sair

**Objetivo:** Encerrar o jogo  
**Pré-condições:** Nenhuma  
**Condição de Entrada:** Pressionar a tecla `4`

### Fluxo Principal:
1. Usuário seleciona a opção `4` (A)
2. O jogo é encerrado

### Fluxo Alternativo:
- **A. Usuário seleciona uma opção inválida**
  1. Exibe mensagem de erro
  2. Retorna ao menu
