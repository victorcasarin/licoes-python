import tkinter as tk
from tkinter import messagebox, font
from tkinter import ttk
import pandas as pd


def calcular():
    try:
        aporte_mensal = float(entry_aporte.get())
        incremento_aporte = float(entry_incremento.get())
        meta = float(entry_meta.get())
        taxa_selic_anual = float(entry_taxa_selic.get())

        if aporte_mensal <= 0 or incremento_aporte < 0 or meta <= 0 or taxa_selic_anual < 0:
            raise ValueError("Os valores devem ser positivos e maiores que zero.")

        taxa_juros_mensal = taxa_selic_anual / 100 / 12
        saldo = 0
        meses = 0
        resultados = []

        while saldo < meta:
            saldo = saldo * (1 + taxa_juros_mensal) + aporte_mensal
            resultados.append((meses + 1, aporte_mensal, saldo))
            aporte_mensal += incremento_aporte
            meses += 1

        mostrar_resultados(resultados, meses, taxa_juros_mensal)

    except ValueError as e:
        messagebox.showerror("Erro", str(e))


def mostrar_resultados(dados, total_meses, taxa_juros_mensal):
    resultado_window = tk.Toplevel(root)
    resultado_window.title("Resultados")
    resultado_window.configure(bg="#1E1E1E")

    tree = ttk.Treeview(resultado_window, columns=("Mês", "Aporte", "Saldo"), show="headings")
    tree.heading("Mês", text="Mês")
    tree.heading("Aporte", text="Aporte (R$)")
    tree.heading("Saldo", text="Saldo Total (R$)")
    tree.column("Mês", width=100)
    tree.column("Aporte", width=120)
    tree.column("Saldo", width=120)

    for index, linha in enumerate(dados):
        if index % 2 == 0:
            tree.insert("", tk.END, values=(linha[0], f"R$ {linha[1]:.2f}", f"R$ {linha[2]:.2f}"), tags=("evenrow",))
        else:
            tree.insert("", tk.END, values=(linha[0], f"R$ {linha[1]:.2f}", f"R$ {linha[2]:.2f}"), tags=("oddrow",))

    tree.tag_configure("evenrow", background="#2E2E2E", foreground="white")
    tree.tag_configure("oddrow", background="#3E3E3E", foreground="white")

    tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    scroll = ttk.Scrollbar(resultado_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scroll.set)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    total_label = tk.Label(resultado_window, text=f"Total de meses até atingir a meta: {total_meses}",
                           font=("Arial", 12, "bold"), bg="#1E1E1E", fg="white")
    total_label.pack(pady=10)

    taxa_label = tk.Label(resultado_window, text=f"Taxa de Rendimento Mensal: {taxa_juros_mensal * 100:.2f}%",
                          font=("Arial", 12, "bold"), bg="#1E1E1E", fg="white")
    taxa_label.pack(pady=10)

    download_button = tk.Button(resultado_window, text="Baixar Resultados em Excel",
                                command=lambda: salvar_excel(dados), bg="#4CAF50", fg="white")
    download_button.pack(pady=10)

    resultado_window.geometry("400x400")


def salvar_excel(dados):
    df = pd.DataFrame(dados, columns=["Mês", "Aporte (R$)", "Saldo Total (R$)"])
    try:
        df.to_excel("resultados_investimento.xlsx", index=False)
        messagebox.showinfo("Sucesso", "Resultados salvos em resultados_investimento.xlsx")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {str(e)}")


def limpar():
    entry_aporte.delete(0, tk.END)
    entry_incremento.delete(0, tk.END)
    entry_meta.delete(0, tk.END)
    entry_taxa_selic.delete(0, tk.END)
    entry_taxa_selic.insert(0, "9.25")  # Valor padrão


def on_enter(event):
    event.widget.tk_focusNext().focus()
    return "break"


# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de investimentos")
root.geometry("400x300")
root.configure(bg="#1E1E1E")

title_font = font.Font(family="Arial", size=14, weight="bold")

# Título centralizado
tk.Label(root, text="Calculadora de investimento", font=title_font, bg="#1E1E1E", fg="white").grid(row=0, column=0,
                                                                                                   columnspan=2,
                                                                                                   pady=10,
                                                                                                   sticky="nsew")

# Configurar as colunas para expandir
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

tk.Label(root, text="Aporte Mensal (R$):", bg="#1E1E1E", fg="white").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_aporte = tk.Entry(root)
entry_aporte.grid(row=1, column=1, padx=5, pady=5)
entry_aporte.bind("<Return>", on_enter)

tk.Label(root, text="Incremento (R$):", bg="#1E1E1E", fg="white").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_incremento = tk.Entry(root)
entry_incremento.grid(row=2, column=1, padx=5, pady=5)
entry_incremento.bind("<Return>", on_enter)

tk.Label(root, text="Meta (R$):", bg="#1E1E1E", fg="white").grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_meta = tk.Entry(root)
entry_meta.grid(row=3, column=1, padx=5, pady=5)
entry_meta.bind("<Return>", on_enter)

tk.Label(root, text="Taxa Selic Anual (%):", bg="#1E1E1E", fg="white").grid(row=4, column=0, sticky="e", padx=5, pady=5)
entry_taxa_selic = tk.Entry(root)
entry_taxa_selic.grid(row=4, column=1, padx=5, pady=5)
entry_taxa_selic.insert(0, "9.25")
entry_taxa_selic.bind("<Return>", on_enter)

tk.Button(root, text="Calcular", command=calcular, bg="#4CAF50", fg="white").grid(row=5, column=0, pady=20)
tk.Button(root, text="Limpar", command=limpar, bg="#f44336", fg="white").grid(row=5, column=1, pady=20)

root.bind("<Return>", lambda event: calcular())

root.mainloop()





