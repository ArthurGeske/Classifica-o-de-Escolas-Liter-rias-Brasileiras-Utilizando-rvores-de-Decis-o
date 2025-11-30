# Classificação de Escolas Literárias Brasileiras Utilizando Árvores de Decisão
Algoritmo desenvolvido para Classificar as Escolas Literárias Brasileiras.

IMPORTANTE: para que o usuário possa ter uma melhor experiência ao executar o programa, sem ter de esperar a Árvore de Decisão ser treinada, é possível baixar o arquivo "classificador_textos.py" e o arquivo "árvore_treinada.pkl" e, após isso, executar o código dentro do terminal do Visual Studio Code (VSCode) (este também pode ser executado em compiladores online e em outros softwares que estejam instalados em seu computador, porém, hoje estaremos explicando como executá-lo no VS Code) seguindo as instruções abaixo. Porém, caso opte por treinar a Árvore, você deve baixar os arquivos "Arcadismo.txt", "Barroco.txt", "Quinhentismo.txt", "Realismo.txt", "Romantismo.txt", "árvore_treino.py" e "classificador_textos.py". Neste caso, não é necessário baixar o arquivo "árvore_treinada.pkl", pois neste caso você estará treinando a árvore, então o arquivo com a árvore treinada não se faz necessário. Porém, certifique-se de que todos os arquivos estejam dentro da mesma pasta, em ambos os casos.

O código conta com os 5 períodos literários iniciais da disciplina de literatura, sendo eles: Quinhentismo, Barroco, Arcadismo, Romantismo e Realismo.

Para executar este código, é necessário que você instale o software VS Code, ou algum semelhante. Também sendo de grande alternativa compiladores online que executem em Python. Ao adentrar o terminal do VS Code, deves digitar, para executar o código após abrir o terminal, os comandos acima da primeira linha de código (após "C:>"), e então quando o seu terminal já estiver parecido com aquela linha usando o comando "cd", digite "python arvore_treino.py" se quiser executar o código de criar a árvore (o que não será preciso), ou digite direto "python classificador_textos.py" e coloque seu texto para que ele possa ser classificado em alguma das cinco escolas literárias contempladas no algoritmo. 

Para melhor entendimento e aprendizado sobre como interagir com o código, selecione algum texto que supõe estar situado entre os demais 5 períodos literários contemplados neste trabalho, valendo salientar que somente obras que são consideradas "literárias" podem ser executadas (sem presença de quebra de linha na entrada do programa ao digitá-lo, caso não atendido, será recebido com erro).

Exemplo de trecho de obra que você pode utilizar para testar o programa (caso deseje):

"Imagem da vida e feitos memoráveis de vossa mercê, quis primeiro fazer este riscunho, pera depois, sendo-me concedido por vossa mercê, ir mui particularmente pintando os membros desta Imagem, se não me faltar a tinta do favor de vossa mercê, a quem peço, humildemente, receba minhas Rimas, por serem as primícias com que tento servi-lo. E porque entendo que as aceitará com aquela benevolência e brandura natural, que custuma, respeitando mais a pureza do ânimo que a vileza do presente, não me fica mais que desejar, se não ver a vida de vossa mercê augmentada e estado prosperado, como todos os seus súbditos desejamos."

Este é um trecho da obra "Prosopopeia" (1601), de Bento Teixeira.

Saída esperada caso a entrada anterior seja inserida: "Barroco".

Link Video de Explicação do Código: https://youtu.be/pZ_J-H8Gfg4?si=a7L4SZpz1pNC3MTn
