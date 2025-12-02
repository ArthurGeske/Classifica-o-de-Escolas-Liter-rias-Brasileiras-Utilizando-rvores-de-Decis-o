# Classificação de Escolas Literárias Brasileiras Utilizando Árvores de Decisão
Algoritmo desenvolvido para Classificar as Escolas Literárias Brasileiras.

IMPORTANTE: para que o usuário possa ter uma melhor experiência ao executar o programa, sem ter de esperar a Árvore de Decisão ser treinada, é possível baixar os arquivos "classificador_textos.py" e  "arvore_treinada.pkl" e, após isso, executar o código dentro do terminal do Visual Studio Code (VSCode) ou no compilador online Google Colab (também pode ser executado em compiladores online de sua preferencia ou em outros softwares que estejam instalados em seu computador, porém, hoje estaremos explicando como executá-lo no VS Code e no Google Colab) seguindo as instruções abaixo. Porém, caso opte por treinar a Árvore, você deve baixar os arquivos "Arcadismo.txt", "Barroco.txt", "Quinhentismo.txt", "Realismo.txt", "Romantismo.txt", "arvore_treino.py" e "classificador_textos.py". Neste caso, não é necessário baixar o arquivo "arvore_treinada.pkl", pois neste caso você estará treinando a árvore, então o arquivo com a árvore treinada não se faz necessário. Porém, certifique-se de que todos os arquivos estejam dentro da mesma pasta, em ambos os casos.

VS Code:

Caso você deseje treinar a árvore, e, em seguida , executar o algoritmo, deve abrir no VS Code os arquivos "arvore_treino.py" e "classificador_textos.py". Entretanto, caso você deseje apenas executar o código sem realizar o treinamento, abra no VS Code o arquivo "arvore_treinada.pkl".

O código conta com os 5 períodos literários iniciais da disciplina de literatura, sendo eles: Quinhentismo, Barroco, Arcadismo, Romantismo e Realismo.

Para abrir o terminal do VS Code, você pode utilizar o atalho "Ctr" + "Shift" + " ' ". Para executar o código após abrir o terminal, você deve digitar os nomes das pastas acima da primeira linha de código (após "C:>"), utilizando o comando "cd" antes de digitar o nome de cada pasta. Lembre-se, você deve digitar o comando "cd" seguido do nome de uma pasta por vez. Após digitar o nome de todas as pastas que estão acima da primeira linha de código, caso você deseje treinar a árvore, deves digitar  "python arvore_treino.py". Após isso, dê enter e espere o tempo necessário para treinar a árvore, em seguida, deves digitar no terminal "python classificador_textos.py",  dê enter e, em seguida, coloque seu texto para que ele possa ser classificado em alguma das cinco escolas literárias contempladas no algoritmo. NÃO SE ESQUEÇA QUE O TEXTO DEVE PERTENCER A ALGUMA DAS ESCOLAS LITERÁRIAS QUE FORAM CONTEMPLADAS NO ALGORITMO, CITADAS ANTERIORMENTE.

Caso você deseje executar o código sem treinar a árvore, deves abrir o terminal, digitar, do mesmo modo, os nomes das pastas acima da primeira linha de código (após "C:>"), utilizando o comando "cd" antes de digitar o nome de cada pasta. Lembre-se, você deve digitar o comando "cd" seguido do nome de uma pasta por vez. Após digitar o nome de todas as pastas que estão acima da primeira linha de código, para realizar a execução do mesmo sem treinar o algoritmo, digite "python classificador_textos.py", em seguida, dê enter e insira o seu texto para que o programa possa classificá-lo. NÃO SE ESQUEÇA QUE O TEXTO DEVE PERTENCER A ALGUMA DAS ESCOLAS LITERÁRIAS QUE FORAM CONTEMPLADAS NO ALGORITMO, CITADAS ANTERIORMENTE.

Google Colab:

Para rodar o código no Google Colab você pode colar este link em seu navegador de internet: https://colab.research.google.com/drive/1t3Aasnj9PH7DxeAGN2fsOXxN53ovKu5z?authuser=0#scrollTo=ZffZcazI7EkU.

Quando já estiver dentro Google Colab, na barra lateral, vá na parte de arquivos e faça o upload dos arquivos "Arcadismo.txt", "Barroco.txt", "Quinhentismo.txt", "Realismo.txt", "Romantismo.txt" e "arvore_treino.py" (faça os uploads um por vez) e os coloque na pasta "contente", então você poderá executar os códigos apertando no botão de play no canto superior esquerdo do código ( o botão em formato de flecha), os códigos seguem a mesma logica explicada anterior mente. NÃO SE ESQUEÇA QUE O TEXTO DEVE PERTENCER A ALGUMA DAS ESCOLAS LITERÁRIAS QUE FORAM CONTEMPLADAS NO ALGORITMO, CITADAS ANTERIORMENTE.

Lembre-se que somente obras que são consideradas "literárias" podem ser executadas (sem presença de quebra de linha na entrada do programa ao digitá-lo, caso não atendido, será recebido com erro).

Como saída, o programa retorna a respectiva classificação do texto inserido anteriormente.

Exemplo de trecho de obra que você pode utilizar para testar o programa (caso deseje):

"Imagem da vida e feitos memoráveis de vossa mercê, quis primeiro fazer este riscunho, pera depois, sendo-me concedido por vossa mercê, ir mui particularmente pintando os membros desta Imagem, se não me faltar a tinta do favor de vossa mercê, a quem peço, humildemente, receba minhas Rimas, por serem as primícias com que tento servi-lo. E porque entendo que as aceitará com aquela benevolência e brandura natural, que custuma, respeitando mais a pureza do ânimo que a vileza do presente, não me fica mais que desejar, se não ver a vida de vossa mercê augmentada e estado prosperado, como todos os seus súbditos desejamos."

Este é um trecho da obra "Prosopopeia" (1601), de Bento Teixeira.

Saída esperada caso a entrada anterior seja inserida: "Barroco".

LINK Vídeo de Explicação do Código: https://youtu.be/pZ_J-H8Gfg4?si=a7L4SZpz1pNC3MTn
