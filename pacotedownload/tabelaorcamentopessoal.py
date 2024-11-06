import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog, font
from tkinter import ttk

def calcular_orcamento(event=None):
    try:
        salario = float(entry_salario.get() or 0)
        freelance = float(entry_freelance.get() or 0)
        investimentos = float(entry_investimentos.get() or 0)

        aluguel = float(entry_aluguel.get() or 0)
        supermercado = float(entry_supermercado.get() or 0)
        transporte = float(entry_transporte.get() or 0)
        contas = float(entry_contas.get() or 0)
        internet = float(entry_internet.get() or 0)
        lazer = float(entry_lazer.get() or 0)
        compras = float(entry_compras.get() or 0)
        outros = float(entry_outros.get() or 0)

        # Criando o DataFrame
        data = {
            "Categoria": ["Ganhos", "Salário", "Freelance", "", "Gastos Essenciais", "Aluguel",
                          "Supermercado", "Transporte", "Contas de Luz/Água", "Internet", "", "Gastos Não-Essenciais",
                          "Lazer", "Compras", "Outros", "", "Investimentos"],
            "Ganhos (R$)": [None, salario, freelance, None, None, None, None, None, None, None, None, None,
                            None, None, None, None, None],
            "Gastos (R$)": [None, None, None, None, None, aluguel, supermercado, transporte, contas, internet,
                            None, None, lazer, compras, outros, None, 0]  # Ajuste aqui
        }

        df = pd.DataFrame(data)

        # Calculando os totais
        total_ganhos = salario + freelance
        total_gastos = aluguel + supermercado + transporte + contas + internet + lazer + compras + outros

        # Adicionando os totais ao DataFrame
        df_totais = pd.DataFrame([{"Categoria": "Total", "Ganhos (R$)": total_ganhos, "Gastos (R$)": total_gastos}])
        df = pd.concat([df, df_totais], ignore_index=True)

        mostrar_resultados(df, total_ganhos, total_gastos)

    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def mostrar_resultados(df, total_ganhos, total_gastos):
    resultado_window = tk.Toplevel(root)
    resultado_window.title("Resultados do Orçamento")
    resultado_window.configure(bg="#1E1E1E")

    tree = ttk.Treeview(resultado_window, columns=("Categoria", "Ganhos (R$)", "Gastos (R$)"), show="headings")
    tree.heading("Categoria", text="Categoria")
    tree.heading("Ganhos (R$)", text="Ganhos (R$)")
    tree.heading("Gastos (R$)", text="Gastos (R$)")
    tree.column("Categoria", width=200)
    tree.column("Ganhos (R$)", width=100)
    tree.column("Gastos (R$)", width=100)

    for _, row in df.iterrows():
        tree.insert("", tk.END, values=(row["Categoria"], f"R$ {row['Ganhos (R$)']:.2f}" if row["Ganhos (R$)"] is not None else "",
                                          f"R$ {row['Gastos (R$)']:.2f}" if row["Gastos (R$)"] is not None else ""))

    tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    scroll = ttk.Scrollbar(resultado_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scroll.set)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    # Exibindo totais fora da tabela
    tk.Label(resultado_window, text=f"Total de Ganhos: R$ {total_ganhos:.2f}", bg="#1E1E1E", fg="white").pack(pady=(10, 0))
    tk.Label(resultado_window, text=f"Total de Gastos: R$ {total_gastos:.2f}", bg="#1E1E1E", fg="white").pack(pady=(0, 10))

    download_button = tk.Button(resultado_window, text="Baixar Resultados em Excel", command=lambda: salvar_excel(df), bg="#4CAF50", fg="white")
    download_button.pack(pady=10)

    resultado_window.geometry("400x400")

def salvar_excel(df):
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        df.to_excel(file_path, index=False)
        messagebox.showinfo("Sucesso", f"Orçamento salvo como {file_path}")

def limpar():
    entry_salario.delete(0, tk.END)
    entry_freelance.delete(0, tk.END)
    entry_investimentos.delete(0, tk.END)
    entry_aluguel.delete(0, tk.END)
    entry_supermercado.delete(0, tk.END)
    entry_transporte.delete(0, tk.END)
    entry_contas.delete(0, tk.END)
    entry_internet.delete(0, tk.END)
    entry_lazer.delete(0, tk.END)
    entry_compras.delete(0, tk.END)
    entry_outros.delete(0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Orçamento Pessoal")
root.geometry("400x500")
root.configure(bg="#1E1E1E")

title_font = font.Font(family="Arial", size=14, weight="bold")

# Título centralizado
tk.Label(root, text="Calculadora de Orçamento Mensal", font=title_font, bg="#1E1E1E", fg="white").grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

# Labels e entradas para ganhos
tk.Label(root, text="Salário (R$):", bg="#1E1E1E", fg="white").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_salario = tk.Entry(root)
entry_salario.grid(row=1, column=1, padx=5, pady=5)
entry_salario.bind('<Return>', calcular_orcamento)

tk.Label(root, text="Freelance (R$):", bg="#1E1E1E", fg="white").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_freelance = tk.Entry(root)
entry_freelance.grid(row=2, column=1, padx=5, pady=5)
entry_freelance.bind('<Return>', calcular_orcamento)

tk.Label(root, text="Investimentos (R$):", bg="#1E1E1E", fg="white").grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_investimentos = tk.Entry(root)
entry_investimentos.grid(row=3, column=1, padx=5, pady=5)
entry_investimentos.bind('<Return>', calcular_orcamento)

# Labels e entradas para gastos essenciais
tk.Label(root, text="Aluguel (R$):", bg="#1E1E1E", fg="white").grid(row=4, column=0, sticky="e", padx=5, pady=5)
entry_aluguel = tk.Entry(root)
entry_aluguel.grid(row=4, column=1, padx=5, pady=5)
entry_aluguel.bind('<Return>', calcular_orcamento)

tk.Label(root, text="Supermercado (R$):", bg="#1E1E1E", fg="white").grid(row=5, column=0, sticky="e", padx=5, pady=5)
entry_supermercado = tk.Entry(root)
entry_supermercado.grid(row=5, column=1, padx=5, pady=5)
entry_supermercado.bind('<Return>', calcular_orcamento)

tk.Label(root, text="Transporte (R$):", bg="#1E1E1E", fg="white").grid(row=6, column=0, sticky="e", padx=5, pady=5)
entry_transporte = tk.Entry(root)
entry_transporte.grid(row=6, column=1, padx=5, pady=5)
entry_transporte.bind('<Return>', calcular_orcamento)

tk.Label(root, text="Contas de Luz/Água (R$):", bg="#1E1E1E", fg="white").grid(row=7, column=0, sticky="e", padx=5, pady=5)
entry_contas = tk.Entry(root)
entry_contas.grid(row=7, column=1, padx=5, pady=5)
entry_contas.bind('<Return>', calcular_orcamento)

tk.Label(root, text="Internet (R$):", bg="#1E1E1E", fg="white").grid(row=8, column=0, sticky="e", padx=5, pady=5)
entry_internet = tk.Entry(root)
entry_internet.grid(row=8, column=1, padx=5, pady=5)
entry_internet.bind('<Return>', calcular_orcamento)

# Labels e entradas para gastos não essenciais
tk.Label(root, text="Lazer (R$):", bg="#1E1E1E", fg="white").grid(row=9, column=0, sticky="e", padx=5, pady=5)
entry_lazer = tk.Entry(root)
entry_lazer.grid(row=9, column=1, padx=5, pady=5)
entry_lazer.bind('<Return>', calcular_orcamento)

tk.Label(root, text="Compras (R$):", bg="#1E1E1E", fg="white").grid(row=10, column=0, sticky="e", padx=5, pady=5)
entry_compras = tk.Entry(root)
entry_compras.grid(row=10, column=1, padx=5, pady=5)
entry_compras.bind('<Return>', calcular_orcamento)

tk.Label(root, text="Outros (R$):", bg="#1E1E1E", fg="white").grid(row=11, column=0, sticky="e", padx=5, pady=5)
entry_outros = tk.Entry(root)
entry_outros.grid(row=11, column=1, padx=5, pady=5)
entry_outros.bind('<Return>', calcular_orcamento)

# Botões
btn_calcular = tk.Button(root, text="Calcular", command=calcular_orcamento, bg="#4CAF50", fg="white")
btn_calcular.grid(row=12, column=0, columnspan=2, pady=10)

btn_limpar = tk.Button(root, text="Limpar", command=limpar, bg="#f44336", fg="white")
btn_limpar.grid(row=13, column=0, columnspan=2, pady=5)

root.mainloop()







