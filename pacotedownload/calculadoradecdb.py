import tkinter as tk
from tkinter import messagebox


def calcular_cdb(valor_investido, taxa_juros, anos):
    """Calcula o montante final de um CDB."""
    montante_final = valor_investido * (1 + taxa_juros / 100) ** anos
    return montante_final


def calcular_imposto(valor_investido, montante_final, anos):
    """Calcula o imposto de renda sobre os rendimentos (montante - valor investido)."""
    rendimento = montante_final - valor_investido  # Calcula o rendimento (lucro)
    dias = anos * 365  # Convertendo anos em dias

    if dias <= 180:
        aliquota_ir = 22.5 / 100  # 22,5% para até 180 dias
    elif dias <= 360:
        aliquota_ir = 20 / 100  # 20% para de 181 até 360 dias
    elif dias <= 720:
        aliquota_ir = 17.5 / 100  # 17,5% para de 361 até 720 dias
    else:
        aliquota_ir = 15 / 100  # 15% para mais de 720 dias

    # O imposto é apenas sobre o rendimento
    imposto = rendimento * aliquota_ir
    return imposto, aliquota_ir, rendimento


def formatar_valor(valor):
    """Formata o valor para exibição com vírgulas e pontos."""
    return f"{valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')


def calcular():
    """Lida com a entrada do usuário e exibe os resultados."""
    try:
        valor_investido = float(entry_investimento.get())
        taxa_juros = float(entry_juros.get())
        anos = int(entry_anos.get())

        # Calcula o montante final
        montante_final = calcular_cdb(valor_investido, taxa_juros, anos)

        # Calcula o imposto a ser pago, a alíquota e o rendimento
        imposto, aliquota_ir, rendimento = calcular_imposto(valor_investido, montante_final, anos)

        # Calcula o valor líquido após o imposto
        valor_liquido = montante_final - imposto

        # Mostra os resultados em uma mensagem
        resultado = (f"Montante final antes do imposto: R$ {formatar_valor(montante_final)}\n"
                     f"Rendimento: R$ {formatar_valor(rendimento)}\n"
                     f"Imposto de renda sobre o rendimento: R$ {formatar_valor(imposto)}\n"
                     f"Porcentagem do imposto de renda: {aliquota_ir * 100:.2f}%\n"
                     f"Valor líquido após o imposto: R$ {formatar_valor(valor_liquido)}")

        messagebox.showinfo("Resultado", resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")


# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de CDB")
root.geometry("400x300")  # Tamanho da janela
root.resizable(False, False)  # Impede redimensionar a janela

# Labels e entradas
label_investimento = tk.Label(root, text="Valor do Investimento (R$):")
label_investimento.pack(pady=5)

entry_investimento = tk.Entry(root)
entry_investimento.pack(pady=5)

label_juros = tk.Label(root, text="Taxa de Juros do CDB (%):")
label_juros.pack(pady=5)

entry_juros = tk.Entry(root)
entry_juros.pack(pady=5)

label_anos = tk.Label(root, text="Número de Anos:")
label_anos.pack(pady=5)

entry_anos = tk.Entry(root)
entry_anos.pack(pady=5)

# Botão de cálculo
botao_calcular = tk.Button(root, text="Calcular", command=calcular)
botao_calcular.pack(pady=20)

# Executando o loop da interface
root.mainloop()

