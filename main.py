import os
import sqlite3
import customtkinter as ctk
import pandas as pd

# Configuração inicial do Tema da Interface Gráfica
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class AppTemplate(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Template Base Python - Corporativo")
        self.geometry("500x400")

        # Título na tela
        self.label = ctk.CTkLabel(
            self, text="Bem-vindo ao seu Template Base!",
            font=("Arial", 18, "bold")
        )
        self.label.pack(pady=20)

        # Botão de Teste do Banco de Dados
        self.btn_db = ctk.CTkButton(
            self, text="Testar Conexão SQLite", command=self.testar_sqlite
        )
        self.btn_db.pack(pady=10)

        # Botão de Teste de Excel na Rede
        self.btn_excel = ctk.CTkButton(
            self, text="Simular Leitura de Excel", command=self.testar_excel
        )
        self.btn_excel.pack(pady=10)

        # Caixa de texto para logs/resultados
        self.textbox = ctk.CTkTextbox(self, width=420, height=150)
        self.textbox.pack(pady=10)
        self.textbox.insert(
            "0.0", "Logs do sistema aparecerão aqui...\nPronto para uso!\n"
        )

    def testar_sqlite(self):
        try:
            db_path = "meu_banco.db"
            conexao = sqlite3.connect(db_path)
            cursor = conexao.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS logs(id INTEGER PRIMARY KEY AUTOINCREMENT,"
                " texto TEXT)"
            )
            cursor.execute(
                "INSERT INTO logs (texto) VALUES ('Teste executado com sucesso')"
            )
            conexao.commit()
            conexao.close()
            self.textbox.insert("end", "[SQLite] Banco criado e dado inserido!\n")
        except Exception as e:
            self.textbox.insert("end", f"[SQLite Erro] {e}\n")

    def testar_excel(self):
        # Exemplo simulando o caminho de rede (substitua pelo caminho real \\servidor\pasta\arquivo.xlsx)
        self.textbox.insert(
            "end",
            "[Excel] Para ler arquivos da rede, use: pd.read_excel(r'\\\\servidor\\pasta\\arquivo.xlsx')\n",
        )


if __name__ == "__main__":
    app = AppTemplate()
    app.mainloop()
