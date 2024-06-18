import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x400")
        self.root.configure(bg="blue")

        self.title_label = tk.Label(root, text="Jans Engenharia", fg="green", bg="blue", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        self.company_label = tk.Label(root, text="Empresa a fazer vistoria:", fg="white", bg="blue")
        self.company_entry = tk.Entry(root)

        self.username_label = tk.Label(root, text="Nome de Usuário:", fg="white", bg="blue")
        self.password_label = tk.Label(root, text="Senha:", fg="white", bg="blue")

        self.company_label.pack()
        self.company_entry.pack()
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(root, text="Entrar", bg="green", fg="white", command=self.login)
        self.login_button.pack(pady=10)

        self.view_companies_button = tk.Button(root, text="Empresas vistoria salvas", bg="orange", fg="white", command=self.view_saved_companies)
        self.view_companies_button.pack(pady=10)

        self.saved_companies = {}  # Dicionário para armazenar as empresas e seus resumos

    def login(self):
        company_name = self.company_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "Juan" and password == "administrador":
            messagebox.showinfo("Login", "Logado com sucesso!")
            self.root.withdraw()  # Fecha a janela de login
            self.open_main_window(company_name)
        else:
            messagebox.showerror("Login", "Login incorreto.")
            self.password_entry.delete(0, tk.END)  # Limpa o campo de senha

    def open_main_window(self, company_name):
        self.main_window = tk.Toplevel(self.root)
        self.main_window.title("Itens a ser adicionado")
        self.main_window.attributes('-fullscreen', True)  # Define a janela principal como tela cheia
        self.main_window.configure(bg="black")

        self.company_name = company_name  # Guarda o nome da empresa

        header_label = tk.Label(self.main_window, text="Itens a ser adicionado", fg="orange", bg="black", font=("Arial", 10, "bold"))
        header_label.pack(pady=20)

        # Lista de itens
        items = ["Porta corta Fogo", "Rede de hidrante", "Extintores", "Sinalização e acessibilidade", "Tampão Story",
                 "Tampão C/corrente", "Chave Story", "Adaptador P/Hidrante", "Abrigo d/Hidrante", "Válvula P/Hidrante",
                 "Tampa de ferro Fundivel", "Detector de sirenes", "Central de alarme e incêndio 24 setores", "Sprinkler",
                 "Mangueira d/incêndio predial", "Mangueira de incêndio industrial", "Motor bomba", "Motor Diesel",
                 "Sinalizador áudio visual", "Detector óptico d/fumaça contato seco", "Central de alarme e incêndio 124 endereços",
                 "Cabo blindado para Alarme", "Acionador Manual"]

        self.entries = {}
        self.quantities = {}

        for item in items:
            frame = tk.Frame(self.main_window, bg="black")
            frame.pack(fill=tk.X, padx=20, pady=2)

            label = tk.Label(frame, text=item, fg="white", bg="black", font=("Arial", 5), width=30, anchor='w')  # Diminuindo o tamanho da fonte
            label.pack(side=tk.LEFT, padx=10)

            entry = tk.Entry(frame, font=("Arial", 5), width=5)
            entry.pack(side=tk.LEFT, padx=10)
            self.entries[item] = entry

            save_button = tk.Button(frame, text="Salvar", bg="green", fg="white", font=("Arial", 6), command=lambda i=item, e=entry: self.save_item(i, e))
            save_button.pack(side=tk.LEFT, padx=10)

        self.resumo_total_button = tk.Button(self.main_window, text="Resumo", bg="orange", fg="white", font=("Arial", 6), command=self.mostrar_resumo_total)
        self.resumo_total_button.pack(pady=20)

    def save_item(self, item, entry):
        quantidade = entry.get()
        if quantidade.isdigit():
            self.quantities[item] = quantidade
            messagebox.showinfo("Salvar", f"{item}: {quantidade} salvo com sucesso!")
        else:
            messagebox.showerror("Erro", "Quantidade deve ser um número.")
        entry.delete(0, tk.END)  # Limpa o campo de entrada

    def mostrar_resumo_total(self):
        resumo_text = self.get_resumo_detalhado()
        self.saved_companies[self.company_name] = resumo_text  # Salva o resumo para a empresa

        self.resumo_window = tk.Toplevel(self.main_window)
        self.resumo_window.title("Resumo Total")
        self.resumo_window.attributes('-fullscreen', True)  # Define a janela de resumo como tela cheia
        self.resumo_window.configure(bg="black")

        resumo_label = tk.Label(self.resumo_window, text="Resumo Total", fg="white", bg="black", font=("Arial", 10, "bold"))
        resumo_label.pack(pady=20)

        detalhes_label = tk.Label(self.resumo_window, text=resumo_text, fg="green", bg="black", justify=tk.LEFT, font=("Arial", 5))
        detalhes_label.pack(padx=50, pady=20, fill=tk.BOTH, expand=True)

    def get_resumo_detalhado(self):
        resumo = f"Empresa: {self.company_name}\n"
        for item, quantidade in self.quantities.items():
            resumo += f"{item}: {quantidade}\n"
        resumo += f"Data: {datetime.now().strftime('%d/%m/%Y')}\n"
        resumo += f"Hora: {datetime.now().strftime('%H:%M:%S')}\n"
        return resumo

    def view_saved_companies(self):
        self.saved_companies_window = tk.Toplevel(self.root)
        self.saved_companies_window.title("Empresas Vistoria Salvas")
        self.saved_companies_window.attributes('-fullscreen', True)
        self.saved_companies_window.configure(bg="black")

        header_label = tk.Label(self.saved_companies_window, text="Empresas Vistoria Salvas", fg="orange", bg="black", font=("Arial", 10, "bold"))
        header_label.pack(pady=20)

        for company, resumo in self.saved_companies.items():
            company_button = tk.Button(self.saved_companies_window, text=company, bg="green", fg="white", font=("Arial", 6),
                                       command=lambda c=company: self.show_company_summary(c))
            company_button.pack(pady=5)

    def show_company_summary(self, company):
        resumo_text = self.saved_companies[company]

        self.company_summary_window = tk.Toplevel(self.saved_companies_window)
        self.company_summary_window.title(f"Resumo de {company}")
        self.company_summary_window.attributes('-fullscreen', True)
        self.company_summary_window.configure(bg="black")

        resumo_label = tk.Label(self.company_summary_window, text=f"Resumo de {company}", fg="white", bg="black", font=("Arial", 10, "bold"))
        resumo_label.pack(pady=20)

        detalhes_label = tk.Label(self.company_summary_window, text=resumo_text, fg="green", bg="black", justify=tk.LEFT, font=("Arial", 5))
        detalhes_label.pack(padx=50, pady=20, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()
