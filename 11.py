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
                
    def av_valida(self):
        if self.raiz is not None:
            if self.raiz.esquerda is None and self.raiz.direita is None:
                return True
            else: 
                menor_valor = float('-inf') # definindo o menor valor possivel
                maior_valor = float('inf') # definindo o maior valor possivel
                return self.buscar_valida_recursiva(self.raiz, menor_valor, maior_valor)
                
        return False # arvore é vazia
    
    def buscar_valida_recursiva(self, no, menor_valor, maior_valor):
        if no is None:
            return True
        if menor_valor < no.valor < maior_valor:
            return (self.buscar_valida_recursiva(no.esquerda, menor_valor, no.valor) 
                    and self.buscar_valida_recursiva(no.direita, no.valor, maior_valor))
        else:
            return False
          

def criar_arvore():
    arvore = ArvoreBinaria()
    
    qnt = int(input('Quantos valores deseja inserir? '))
    for i in range(qnt):
        num = int(input(f'Digite o {i+1}º valor: '))
        arvore.inserir_em_nivel(num)
    print('Valores inseridos com sucesso.')
    print('Em nivel: ')
    arvore.mostrar_em_nivel()
    print()
    print('inOrdem: ')
    arvore.mostrar_in_ordem()
    print()
    
    return arvore

def main():
    arvore = criar_arvore()
    
    if arvore.av_valida():
        print("A árvore é uma árvore de busca válida.")
    else:
        print("A árvore não é uma árvore de busca válida.")

main()
