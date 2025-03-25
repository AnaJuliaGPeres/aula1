📝 Resumo do Projeto
O projeto é uma aplicação em Python com Pygame, onde textos animados se movem pela tela de diferentes formas. Além disso, há um sistema de música de fundo e um efeito sonoro ao bater nas bordas da tela.

A estrutura do código está dividida em arquivos específicos para diferentes funcionalidades:

config.py → Contém configurações globais, como tamanho da tela, cores e velocidade dos textos.

dvd.py → Define a lógica de movimentação dos textos, com classes abstratas e concretas.

game.py → Gerencia o jogo, incluindo a música e eventos de teclado (trocar música e pausar).

main.py → Ponto de entrada do programa, inicializando o jogo.

Os textos podem se mover de três formas:

BouncingText → Se move em todas as direções e quica nas bordas.

VerticalText → Move-se apenas na vertical.

HorizontalText → Move-se apenas na horizontal.

Anteriormente no inicio o código estava estruturado da seguinte forma: 

![alt text](<DVD/UML Diagramainicio.png>)

Com a Nova estruturação e melhorias no projeto, o código esta estruturado da seguinte forma: 

![alt text](<DVD/UML Apos.png>)


📌 SOLID no projeto
1- Responsabilidade Única (SRP)
Cada classe tem uma única função bem definida.
MoveText cuida da lógica de exibição do texto.
Game gerencia o loop do jogo e a música.

2- Aberto/Fechado (OCP)
O código permite adicionar novas classes de movimento sem alterar o código base.
Se quisermos um DiagonalText, basta criar uma nova classe sem modificar MoveText.

3-L - Substituição de Liskov (LSP)
Podemos substituir MoveText por qualquer subclasse (BouncingText, VerticalText, HorizontalText) sem quebrar o código.
O jogo não precisa saber qual é o tipo específico do texto para chamá-lo.

4- Segregação de Interfaces (ISP)
MoveText tem apenas os métodos essenciais (update() e draw()), sem forçar subclasses a implementar métodos desnecessários.
Nenhuma subclasse tem código inútil.

5- Inversão de Dependência (DIP)
Game depende da classe abstrata MoveText, não das implementações específicas.
Isso permite adicionar novos tipos de movimento sem modificar Game.

📌 Clean Code no projeto
Código modular e bem organizado
Cada funcionalidade está separada em arquivos diferentes (config.py, dvd.py, game.py...), facilitando a manutenção.

Boas práticas de nomenclatura
Os nomes das classes, métodos e variáveis são claros e descritivos (update(), draw(), toggle_pause()...), tornando o código fácil de entender.

Uso correto de abstrações
A classe MoveText é abstrata e define o comportamento esperado, garantindo um código reutilizável e bem estruturado.

Evita código duplicado
O método _change_color() está em MoveText, evitando repetição nas subclasses.

Uso de constantes no config.py
As configurações do jogo são centralizadas, evitando valores mágicos espalhados pelo código.

