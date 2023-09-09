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
                
    def nos_no_nivel(self, nivel):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            altura = self.altura()
            if nivel > altura:
                print()
                print('Esse nível não existe na árvore.')
            else:
                self._nos_no_nivel(self.raiz, nivel, 0)
    
    def _nos_no_nivel(self, no, nivel, nivel_atual):
        if nivel == 0:
            print(self.raiz.valor)
        elif no is not None:
            if nivel == nivel_atual:
                print(no.valor, end=' ')
            else:
                self._nos_no_nivel(no.esquerda, nivel, nivel_atual + 1)
                self._nos_no_nivel(no.direita, nivel, nivel_atual + 1)

    def percorrer_raiz_ate_no(self, valor):
        caminho = self._percorrer_raiz_ate_no(self.raiz, valor)
        if caminho:
            print(f'Caminho até o nó {valor}:', end=' ')
            for valor in caminho:
                print(valor, end=' ')
            print()
        else:
            print(f'O nó {valor} não existe na árvore.')

    def _percorrer_raiz_ate_no(self, no, valor):
        if no is None:
            return None

        if no.valor == valor:
            return [no.valor]
        
        caminho_E = self._percorrer_raiz_ate_no(no.esquerda, valor)
        if caminho_E:
            return [no.valor] + caminho_E

        caminho_D = self._percorrer_raiz_ate_no(no.direita, valor)
        if caminho_D:
            return [no.valor] + caminho_D
        
        return None

qnt = int(input('Quantos números deseja inserir na árvore? '))    
def inserir(qnt):
    for i in range(7):
        n = int(input(f'Informe o {i+1}º número: '))
        qnt.inserir_em_nivel(n)
    print('Números inseridos na árvore: ')
    qnt.mostrar_pre_ordem()

arvore = ArvoreBinaria()  
inserir(arvore)
print()

valor = int(input('Digite o valor do nó para percorrer até ele: '))
arvore.percorrer_raiz_ate_no(valor)