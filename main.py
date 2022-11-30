from nodeList import NodeList

lista_simples = NodeList()

for c in range(30):
    lista_simples.append(c)

print("Tamanho da lista: ", lista_simples.length())
print("Lista completa:")
print(lista_simples)

print("Segundo elemento da lista: ", lista_simples.get(1))

print("Inserindo o elemento 100 na posição 5")
lista_simples.insert(4, 100)
print(lista_simples)

print("Adicionando 100 ao final da lista")
lista_simples.append(100)
print(lista_simples)
