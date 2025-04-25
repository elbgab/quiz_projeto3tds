# main.py
import perguntas
import quiz

def executar_quiz():
    quiz.executar_quiz(perguntas.perguntas)

if __name__ == "__main__":
    print("Bem-vindo ao quiz de Python, JavaScript e SQL!")
    executar_quiz()