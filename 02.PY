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
    
    def mostrar_pos_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_pos_ordem_recursivo(self.raiz)

    def mostrar_pos_ordem_recursivo(self, no):
        if no.esquerda is not None:
            self.mostrar_pos_ordem_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_pos_ordem_recursivo(no.direita)
        print(no.valor, end=' ')

    def mostrar_in_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_in_ordem_recursivo(self.raiz)

    def mostrar_in_ordem_recursivo(self, no):
        if no.esquerda is not None:
            self.mostrar_in_ordem_recursivo(no.esquerda)
        print(no.valor, end=' ')
        if no.direita is not None:
            self.mostrar_in_ordem_recursivo(no.direita)
      
    def mostrar_em_nivel(self):
        if self.raiz is None:
            return
        else:
            print(self.raiz.valor, end=' ')
            self.mostrar_em_nivel_recursivo(self.raiz)

    def mostrar_em_nivel_recursivo(self, no):
        if no.esquerda is not None:
            print(no.esquerda.valor, end=' ')
        if no.direita is not None:
            print(no.direita.valor, end=' ')

        if no.esquerda is not None:
            self.mostrar_em_nivel_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_em_nivel_recursivo(no.direita)
        
arvore = ArvoreBinaria()
print('Travessia em niveis: ')
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)
arvore.mostrar_em_nivel()