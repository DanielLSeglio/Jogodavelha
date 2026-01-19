# Jogo da Velha com IA (Minimax)

Este projeto é uma implementação do clássico **Jogo da Velha** em Python, com suporte a dois modos de jogo:
- Pessoa vs Pessoa  
- Pessoa vs Computador (IA)

O objetivo principal do projeto foi estudar **lógica de jogo, tomada de decisão e algoritmos de IA**, com foco no algoritmo **Minimax**.

---

## 🧠 Sobre a IA

Inicialmente, a IA foi implementada com **regras fixas**, como:
- Bloquear jogadas do oponente
- Priorizar o centro
- Ocupar cantos estrategicamente

Apesar de funcional, esse modelo era limitado, pois seguia apenas regras pré-definidas.

Posteriormente, a IA foi reescrita utilizando o algoritmo **Minimax**, que avalia todas as jogadas possíveis e escolhe a melhor decisão assumindo que o adversário jogue perfeitamente.

Com isso, a IA passa a:
- Não depender de regras fixas
- Avaliar estados futuros do jogo
- Garantir o melhor resultado possível no pior cenário

---

## ⚙️ Como funciona o Minimax (resumo)

O Minimax simula todas as jogadas futuras do jogo, alternando entre:
- **Maximizar** a pontuação da IA
- **Minimizar** a pontuação do adversário

Cada estado terminal (vitória, derrota ou empate) recebe uma pontuação, e a jogada escolhida é aquela que garante o melhor resultado possível mesmo diante de um adversário perfeito.

Esse algoritmo é especialmente eficiente para jogos de **pequeno espaço de estados**, como o jogo da velha.

---

## 🧩 Estrutura do Código

O código foi organizado em funções com responsabilidades bem definidas:
- Exibição do tabuleiro
- Validação de jogadas
- Verificação de vitória ou empate
- Controle do fluxo do jogo
- Lógica da IA com recursão e backtracking

O tabuleiro é representado como uma lista linear de 9 posições, facilitando a manipulação e a avaliação dos estados.

---

## ▶️ Como executar

### Requisitos
- Python 3.x

### Execução
Execute no terminal.
