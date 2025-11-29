import re, math, pickle
from collections import Counter

with open ("Quinhentismo.txt", "r", encoding="utf-8") as quin:
    Quinhentismo = [l.strip() for l in quin.readlines() if l.strip() ]

with open ("Barroco.txt", "r", encoding="utf-8") as barr:
    Barroco = [l.strip() for l in barr.readlines() if l.strip() ]

with open ("Arcadismo.txt", "r", encoding="utf-8") as arca:
    Arcadismo = [l.strip() for l in arca.readlines() if l.strip() ]

with open ("Romantismo.txt", "r", encoding="utf-8") as roma:
    Romantismo = [l.strip() for l in roma.readlines() if l.strip() ]

with open ("Realismo.txt", "r", encoding="utf-8") as real:
    Realismo = [l.strip() for l in real.readlines() if l.strip() ]

dados = []
for frase in Quinhentismo:
    dados.append((frase, "Quinhentismo"))
for frase in Barroco:
    dados.append((frase, "Barroco"))
for frase in Arcadismo:
    dados.append((frase, "Arcadismo"))
for frase in Romantismo:
    dados.append((frase, "Romantismo"))
for frase in Realismo:
    dados.append((frase, "Realismo"))

print("Banco de dados lido com sucesso!")

PALAVRAEXCLUIDAS = {
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

    palavras = [p for p in palavras if p not in PALAVRAEXCLUIDAS]

    return " ".join(palavras)

dados = [(tirar_formatacao(t), r) for (t, r) in dados]

print("Textos sem Formatacao")

def entropia(rotulos):
    total = len(rotulos)
    if total == 0:
        return 0.0
    cont = Counter (rotulos)
    ent = 0.0
    for k in cont:
        p = cont[k] / total
        ent -= p * math.log2(p)
    return ent


def ganho_informacao(dataset, palavra):
    N = len(dataset)
    if N == 0:
        return 0.0
    sim = [r for (t,r) in dataset if palavra in t.split()]
    nao = [r for (t,r) in dataset if palavra not in t.split()]
    h_d = entropia([r for _, r in dataset])
    h_sim = entropia(sim)
    h_nao = entropia(nao)
    return h_d - (len(sim)/N)*h_sim - (len(nao)/N)*h_nao


def contruir_arvore(dataset, vocab, depth=0, max_depth=12, min_samples=5):
    rotulos = [r for _, r in dataset]

    if len(set(rotulos)) == 1:
        return {"type": "leaf", "class": rotulos[0]}
    
    if depth >= max_depth or len(dataset) < min_samples:
        major = Counter(rotulos).most_common(1)[0][0]
        return {"type": "leaf", "class": major}
    
    melhor_ig = 0.0
    melhor_palavra = None
    
    for w in vocab:
        ig = ganho_informacao(dataset,w)
        if ig < 0.00005:
            continue
        if ig > melhor_ig:
            melhor_ig = ig
            melhor_palavra = w

    if melhor_palavra is None:
        major = Counter(rotulos).most_common(1)[0][0]
        return {"type": "leaf", "class": major}
    
    dataset_sim = [(t,r) for (t,r) in dataset if melhor_palavra in t.split()]
    dataset_nao = [(t,r) for (t,r) in dataset if melhor_palavra not in t.split()]

    if len (dataset_sim) == 0 or len (dataset_nao) == 0:
        major = Counter(rotulos).most_common(1)[0][0]
        return {"type": "leaf", "class": major}
    
    return { 
        "type": "node",
        "palavra": melhor_palavra,
        "sim": contruir_arvore(dataset_sim, vocab, depth+1, max_depth, min_samples),
        "nao": contruir_arvore(dataset_nao, vocab, depth+1, max_depth, min_samples)
    }

contador = Counter()
for texto,_ in dados:
    palavras = texto.split()
    palavras = [p for p in palavras if p not in PALAVRAEXCLUIDAS]
    contador.update(set(palavras))

vocab = [ w for w, c in contador.most_common(1000)]    

print("Treinando árvore...")
arvore = contruir_arvore(dados, vocab, max_depth=8, min_samples=4)
print("Treinamento concluído!")

with open("arvore_treinada.pkl", "wb") as arquivo:
    pickle.dump(arvore, arquivo)

print("Árvore treinada e salva em 'arvore_treinada.pkl'")

print(arvore)