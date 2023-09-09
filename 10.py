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

    def maior_num(self):
        if self.raiz == None:
            return 0
        else:
            return self._maior_num(self.raiz)
        
    def _maior_num(self, no):
        if no is None:
            return None
        maior_num = no.valor
        if no.esquerda is not None:
            valor_E = self._maior_num(no.esquerda)
            if valor_E > maior_num:          
                maior_num = valor_E
        if no.direita is not None:
            valor_D = self._maior_num(no.direita)
            if valor_D > maior_num:
                maior_num = valor_D
        return maior_num

def inserir(arv):
    for i in range(7):
        n = int(input(f'Informe o {i+1}º número: '))
        arv.inserir_em_nivel(n)
    print('Números inseridos na árvore: ')
    arv.mostrar_pre_ordem()

arvore = ArvoreBinaria()
inserir(arvore)
print()
maior = arvore.maior_num()
print(f'O maior nó dessa árvore é: {maior}')
