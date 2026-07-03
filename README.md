# Projeto Calculadora de Estatísticas para RPGs de mesa
Uma calculadora desenvolvida em Python com script executável em Shell Script. Esse projeto foi criado para a atividade prática do curso de Analista de Dados da EBAC.

Se trata de uma calculadora que realiza operações matemáticas para criar as estatísticas de um personagem de um RPG de mesa (jogo de tabuleiro) em um determinado sistema de fantasia. Ela calcula estatísticas como pontos de vida, pontos de energia, magias e habilidades.

# Requisitos
- Acesso à um terminal Linux;
- (para edição do programa ou script) conhecimentos em Python 3 e Shell Script (Bash)

# Como executar a calculadora
1. Abra o terminal Linux.
2. Vá até a pasta onde o projeto está e conceda a permissão de execução para o arquivo: chmod 744 executarcalc.sh
3. Para executar o programa, digite o seguinte comando: ./executarcalc.sh

# Explicação do código
Primeiramente, o programa pede pelo valor dos pontos de vida do personagem, que normalmente variam entre 10 e 18. Após isso, ele pede pelo valor de vigor, que é um número somado aos pontos de vida toda vez que um personagem sobe de nível.

Finalmente, ele pede pelo nível do personagem, que vai de 1 a 20. Nessa operação matemática, o nível funciona como um multiplicador para o vigor. E então, a calculadora realiza a operação e te entrega o valor final dos pontos de vida do personagem.

O processo se repete para os seus pontos de energia, que substitui os pontos de vida, e para o fôlego, que substitui o vigor, com o mesmo cálculo.

As próximas informações disponíveis são as magias e habilidades do seu personagem. Os cálculos são baseados no seu nível, cujo valor foi pedido anteriormente na operação dos pontos de vida.

Ao final da geração das estatísticas, o código te dá a possibildade de calcular outro personagem. Se a resposta for sim, todo o processo recomeça e o programa continua sendo executado. Do contrário, o programa se encerra.
