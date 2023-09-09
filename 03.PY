class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_em_nivel_recursivo(valor, self.raiz)
    
    def _inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no.esquerda)            
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no.direita)    

    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_pre_ordem_recursivo(self.raiz)

    def mostrar_pre_ordem_recursivo(self, no):
        print(no.valor, end=' ')
        if no.esquerda is not None:
            self.mostrar_pre_ordem_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_pre_ordem_recursivo(no.direita)

    def procurar(self, v):
        if self.raiz is None: #caso a raiz esteja vazia
            return False
        else:
            return self._procurar(self.raiz, v) #caso nao esteja vazia, procura com a raiz e o valor v que quer
    
    def _procurar(self, no, v):
        if no is None: #se o no atual ja for vazio, retorna falso
            return False
        if no.valor == v: #se o no atual é = ao v (valor que ta sendo buscado) retorna verdadeiro
            return True
        if self._procurar(no.esquerda, v): #recursividade verificando se o valor foi encontrado na subarvore E.
            return True
        if self._procurar(no.direita, v): #recursividade verificando se o valor foi encontrado na subarvore D
            return True


def inserir(arv):
    for i in range(7):
        n = int(input(f'Informe o {i+1}º número: '))
        arv.inserir_em_nivel(n)
    print('Números inseridos na árvore: ')
    arv.mostrar_pre_ordem()

def verificar(arv):
    v = int(input('Informe o número para verificar presença na árvore: '))
    if arv.procurar(v):
        print('Número presente na árvore')
    else:
        print('Número não está presente na árvore!')

arvore = ArvoreBinaria()
inserir(arvore)
print()
verificar(arvore)
