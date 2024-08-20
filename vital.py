import flet as ft
from data import question_data

def main(page: ft.Page):

    # Armazenando respostas do usuário
    respostas = {}

    # Índice da pergunta atual
    current_question_index = 0

    # Função que é chamada quando o botão é clicado
    def button_clicked(e):
        nonlocal current_question_index
        
        # Armazena a resposta atual
        selected_value = radio_opc.value
        if selected_value:
            current_question = list(question_data.keys())[current_question_index]
            respostas[current_question] = selected_value
        
        # Passa para a próxima pergunta
        current_question_index += 1
        
        if current_question_index < len(question_data):
            # Atualiza a pergunta e alternativas
            next_question = list(question_data.keys())[current_question_index]
            questions.value = next_question
            radio_opc.content.controls = [ft.Radio(value=alt, label=alt) for alt in question_data[next_question]]
            radio_opc.value = None  # Reseta a seleção
        else:
            # Exibe todas as respostas ao final
            t.value = "Você completou o questionário!"
            respostas_str = "\n".join([f"{q}: {a}" for q, a in respostas.items()])
            respostas_text.value = f"Respostas:\n{respostas_str}"
            page.remove(button)  # Remove o botão após a finalização
        
        page.update()
    
    # Inicializando elementos da interface
    t = ft.Text()
    respostas_text = ft.Text()
    questions = ft.Text(value=list(question_data.keys())[current_question_index])

    # Criando opções de resposta baseadas na primeira pergunta
    radio_opc = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value=alt, label=alt) for alt in question_data[questions.value]
        ])
    )

    button = ft.ElevatedButton(text='Próxima', on_click=button_clicked)
    
    # Adicionando os elementos à página
    page.add(ft.Text("Perguntas:"), questions, radio_opc, button, t, respostas_text)

ft.app(target=main)
