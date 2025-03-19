class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.completa = False
    
    def marcar_completa(self):
        self.completa = True
        
    def __str__(self):
        if self.completa == False:
            return f"[ ] {self.descricao}"
        else:
            return f"[X] {self.descricao}"

class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []
    
    def adicionar_tarefa(self, descricao):
        nova_tarefa = Tarefa(descricao)
        
        self.tarefas.append(nova_tarefa)
        pass
    
    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas.pop(indice)
        else:
            print("Indice invalido")
            
    def listar_tarefas(self):
        for i,tarefa in enumerate(self.tarefas):
            print(f"{i}. {tarefa}")
            
    def marcar_tarefa_completa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].marcar_completa()
        else:
            print("Indice invalido")
            
def main():
    lista = ListaDeTarefas()
    print("1. Adicionar tarefa\n2. Remover tarefa\n3. Listar tarefas\n4. Marcar tarefa como completa\n5. Sair\n")
   
    while True:
        
        escolha = int(input("Escolha uma opção: "))
        
        if escolha == 1:
            lista.adicionar_tarefa(input("Digite a decricao da tarefa: "))
            print("Tarefa adicionada com sucesso!")
        elif escolha == 2:
            lista.listar_tarefas()
            lista.remover_tarefa(int(input("Digite o indice da tarefa que deseja remover: ")))
            print("Tarefa removida com sucesso!")
        elif escolha == 3:
            lista.listar_tarefas()
        elif escolha == 4:
            lista.marcar_tarefa_completa(int(input("Digite o indice da tarefa a marcar como completa: ")))
        elif escolha == 5:
            break
        else:
            print(escolha)
            print("Opção inválida, tente novamente.")
        
            
    
if __name__ == "__main__":
    main()