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

    def mostrar_em_ordem(self):
        if self.raiz is None:
            print("A raiz está vazia")
        else:
            self.mostrar_em_ordem_recursivo(self.raiz)
        
    def mostrar_em_ordem_recursivo(self, no):
        if no.esquerda is not None:
            self.mostrar_em_ordem_recursivo(no.esquerda)
        print(no.valor, end=' ')
        if no.direita is not None:
            self.mostrar_em_ordem_recursivo(no.direita)
        
    def altura(self):
        if self.raiz is None:
            return 0
        else:
            return self._altura(self.raiz) 
    
    def _altura(self, no):
        if no is None:
            return 0
        altura_e = 0
        altura_d = 0

        if no.esquerda is not None:
            altura_e = 1 + self._altura(no.esquerda)
        if no.direita is not None:
            altura_d = 1 + self._altura(no.direita)
        if altura_e > altura_d:
            return altura_e
        else:
            return altura_d

def inserir(arv):
    for i in range(7):
        n = int(input(f'Informe o {i+1}º número: '))
        arv.inserir_em_nivel(n)
    print('Números inseridos na árvore: ')
    arv.mostrar_em_ordem()

arvore = ArvoreBinaria()
inserir(arvore)
print()
altura = arvore.altura()
print('Altura da árvore: ', altura)