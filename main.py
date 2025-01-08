import flet as ft

def main(page: ft.Page):
    # Define o estado inicial do número
    number = ft.Ref[ft.Text]()
    
    # Função para adicionar 1 ao número
    def add_number(e):
        current_value = int(number.current.value)
        number.current.value = str(current_value + 1)
        page.update()

    # Configuração inicial do número
    number_label = ft.Text("0", ref=number, size=20, color="blue")

    # Botão para adicionar o número
    add_button = ft.ElevatedButton("Adicionar 1", on_click=add_number)

    # Adicionando componentes à página
    page.add(
        ft.Column(
            [
                ft.Text("Clique para adicionar ao número:", size=18),
                number_label,
                add_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Executar a aplicação
if __name__ == "__main__":
    ft.app(target=main)
