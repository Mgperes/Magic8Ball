import random
import time

# Lista de respostas possíveis
respostas = [
    "Sim, definitivamente.",
    "É decididamente assim.",
    "Sem dúvida.",
    "Sim, com certeza.",
    "Você pode contar com isso.",
    "Como eu vejo, sim.",
    "Muito provavelmente.",
    "Parece bom.",
    "Sim.",
    "Os sinais apontam que sim.",
    "Resposta nebulosa, tente novamente.",
    "Pergunte mais tarde.",
    "Melhor não te dizer agora.",
    "Não é possível prever agora.",
    "Concentre-se e pergunte novamente.",
    "Não conte com isso.",
    "Minha resposta é não.",
    "Minhas fontes dizem não.",
    "Não parece bom.",
    "Muito duvidoso."
]

# Função principal do jogo Magic 8 Ball
def magic8ball():
    print("🎱 Magic 8 Ball 🎱")
    print("Pense em uma pergunta de Sim ou Não e pressione Enter para continuar...")
    input()  # Espera o usuário pressionar Enter
    
    print("\nA bola mágica está pensando...")
    time.sleep(2)  # Pausa dramática
    
    # Seleciona uma resposta aleatória
    resposta = random.choice(respostas)
    print(f"\n🎱 Resposta: {resposta}\n")

# Executa o programa
if __name__ == "__main__":
    while True:
        magic8ball()
        
        # Pergunta se quer jogar novamente
        jogar_novamente = input("Quer fazer outra pergunta? (s/n): ").lower()
        if jogar_novamente != 's':
            print("\nAté mais! Que a sorte esteja com você! ✨")
            break
        #FIM