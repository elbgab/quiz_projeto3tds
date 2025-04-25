def executar_quiz(perguntas):
    pontuacao = 0
    
    for pergunta in perguntas:
        print("\n" + pergunta["pergunta"])
        for i, opcao in enumerate(pergunta["opcoes"], 1):
            print(f"{i}. {opcao}")
        
        # Leitura e validação da resposta
        resposta_usuario = input("Escolha uma opção (1-4): ")
        
        # Verifica se a resposta do usuário está correta
        if pergunta["opcoes"][int(resposta_usuario) - 1] == pergunta["resposta"]:
            print("Resposta correta!")
            pontuacao += 1
        else:
            print("Resposta errada.")
    
    print(f"\nSua pontuação final foi: {pontuacao}/{len(perguntas)}")