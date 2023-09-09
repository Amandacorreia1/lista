
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
                
    def mostrar_filhos_do_no(self, valor):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            buscar_no = self.encontrar_no(self.raiz, valor)
            if buscar_no is not None:
                print(f'Filhos do nó {valor}:', end=' ')
                if buscar_no.esquerda:
                    print(buscar_no.esquerda.valor, end=' ')
                if buscar_no.direita:   
                    print(buscar_no.direita.valor, end=' ')
                print()
                if not buscar_no.esquerda and not buscar_no.direita:
                    print(f'O nó {valor} não possui filhos.')
            else:
                print(f'O nó {valor} não está presente na árvore.')

    def encontrar_no(self, no, valor):
        if no is None:
            return None
        if no.valor == valor:
            return no
        esquerda = self.encontrar_no(no.esquerda, valor)
        if esquerda:
            return esquerda
        direita = self.encontrar_no(no.direita, valor)
        return direita
     
def busca_por_no():
    
    a = ArvoreBinaria()
    
    qnt = int(input('Quantos valores deseja inserir na árvore? '))
    for i in range(qnt):
        num = int(input(f'Informe o {i+1}º valor: '))
        a.inserir_em_nivel(num)
    print('Valores inseridos na arvore.')
    
    print()
    no = int(input('Digite um nó para mostrar seus filhos: '))
    a.mostrar_filhos_do_no(no)
    print()
    
busca_por_no()
    
