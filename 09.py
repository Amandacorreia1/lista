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

    def contador_nos(self):
        if self.raiz == None:
            return 0
        else:
            return self._contador_nos(self.raiz)
        
    def _contador_nos(self, no):
        if no is None:
            return 0
        if no is not None:
            count = 1
        if no.esquerda is not None:
            count += self._contador_nos(no.esquerda)
        if no.direita is not None:
            count += self._contador_nos(no.direita)
        return count

num = int(input('Deseja adicionar quantos nós a árvore?: '))   
def inserir(arv):
    for i in range(num):
        n = int(input(f'Informe o {i+1}º número: '))
        arv.inserir_em_nivel(n)
    print('Números inseridos na árvore: ')
    arv.mostrar_pre_ordem()


arvore = ArvoreBinaria()
inserir(arvore)
print()
qnt_nos = arvore.contador_nos()
print(f'A árvore possui: {qnt_nos} nós')