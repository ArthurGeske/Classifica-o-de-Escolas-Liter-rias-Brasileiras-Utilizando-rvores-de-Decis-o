import pickle, re

PALAVRASEXCLUIDAS = {
    "a","o","as","os","de","do","da","das","dos","e","que","em","para","por","um","uma",
    "no","na","nos","nas","se","com","ao","era","mas","ou","porem","entre","sobre","sem",
}

def tirar_formatacao(texto):
    texto = texto.lower()
    texto = texto.replace("ç", "c") \
                 .replace("á", "a").replace("à", "a").replace("â", "a").replace("ã", "a") \
                 .replace("é", "e").replace("ê", "e") \
                 .replace("í", "i") \
                 .replace("ó", "o").replace("ô", "o").replace("õ", "o") \
                 .replace("ú", "u")

    texto = re.sub(r'[^a-z\s]', ' ', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()

    palavras = texto.split()

    palavras = [p for p in palavras if p not in PALAVRASEXCLUIDAS]

    return " ".join(palavras)

def prever_arvore(arvore, texto):
    if arvore["type"] == "leaf":
        return arvore["class"]
    if arvore["palavra"] in texto.split():
        return prever_arvore(arvore["sim"], texto)
    else:
        return prever_arvore(arvore["nao"], texto)
    
with open("arvore_treinada.pkl", "rb") as arquivo:
    arvore = pickle.load(arquivo)

texto = input("\nDigite o texto que deseja indentificar:\n")

texto_limpo = tirar_formatacao(texto)
classe = prever_arvore(arvore, texto_limpo)

print("\nMovimento literário previsto:", classe)