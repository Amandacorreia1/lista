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
    
    def altura_da_arvore(self):
        if self.raiz is None:
            return 0
        else:
            return self.altura_arvore(self.raiz) - 1

    def altura_arvore(self, no):
        if no is None:
            return 0
        else:
            return max(self.altura_arvore(no.esquerda), self.altura_arvore(no.direita)) + 1
                
    def mostrar_nos_no_nivel(self, nivel):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            altura = self.altura_da_arvore()
            if nivel > altura:
                print()
                print('O nível informado não existe na árvore.')
            else:
                self.mostrar_nos_no_nivel_recursivo(self.raiz, nivel, 0)
    
    def mostrar_nos_no_nivel_recursivo(self, no, nivel, nivel_atual):
        if nivel == 0:
            print(no.valor)
        elif no is not None:
            if nivel == nivel_atual:
                print(no.valor, end=' ')
            else:
                self.mostrar_nos_no_nivel_recursivo(no.esquerda, nivel, nivel_atual + 1)
                self.mostrar_nos_no_nivel_recursivo(no.direita, nivel, nivel_atual + 1)
                
def nos_nivel_arvore():
    a = ArvoreBinaria()
    
    qnt = int(input('Quantos valores deseja inserir? '))
    for i in range(qnt):
        num = int(input(f'Digite o {i+1}º valor: '))
        a.inserir_em_nivel(num)
    print('Valores inseridos com sucesso.')
    
    print()
    nivel = int(input('Informe o nível para mostrar os nós: '))
    print(f'Nós no nível {nivel}:' ,end=' ')
    a.mostrar_nos_no_nivel(nivel)
    print()

# Chamando a função principal
nos_nivel_arvore()
