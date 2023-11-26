# Importa as bibliotecas necessárias
import requests
import json
import tkinter as tk
from tkinter import ttk

# Define constantes para as URLs das APIs
IPINFO_URL = "https://api.ipinfo.io/v1/{}"
WHOIS_URL = "https://api.whois.com/whois/{}"

# Define a classe InfoTool
class InfoTool:
    """
    Uma classe que representa uma ferramenta de hacking simples.
    """

    def __init__(self, master):
        """
        Inicializa a ferramenta com a janela principal.

        Args:
            master: A janela principal da aplicação.
        """

        self.master = master
        self.master.title("InfoTool")
        self.master.geometry("600x400")
        self.master.resizable(False, False)

        # Cria os widgets da interface
        self.create_widgets()

    def create_widgets(self):
        """
        Cria os widgets da interface gráfica.
        """

        # Cria o frame para os widgets de entrada
        self.input_frame = ttk.Frame(self.master)
        self.input_frame.pack(padx=10, pady=10)

        # Cria o label para o tipo de pesquisa
        self.type_label = ttk.Label(self.input_frame, text="Tipo de pesquisa:")
        self.type_label.grid(row=0, column=0, sticky=tk.W)

        # Cria o combobox para o tipo de pesquisa
        self.type_combobox = ttk.Combobox(self.input_frame, values=["ip", "domain"], state="readonly")
        self.type_combobox.grid(row=0, column=1, sticky=tk.W)
        self.type_combobox.set("ip")

        # Cria o label para o valor de pesquisa
        self.value_label = ttk.Label(self.input_frame, text="Valor de pesquisa:")
        self.value_label.grid(row=1, column=0, sticky=tk.W)

        # Cria o entry para o valor de pesquisa
        self.value_entry = ttk.Entry(self.input_frame)
        self.value_entry.grid(row=1, column=1, sticky=tk.W)

        # Cria o botão para obter as informações
        self.get_info_button = ttk.Button(self.input_frame, text="Obter informações", command=self.get_info)
        self.get_info_button.grid(row=2, column=0, columnspan=2, sticky=tk.EW)

        # Cria o frame para os widgets de saída
        self.output_frame = ttk.Frame(self.master)
        self.output_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Cria o text para exibir as informações
        self.info_text = tk.Text(self.output_frame, state="disabled")
        self.info_text.pack(fill=tk.BOTH, expand=True)

        # Cria a scrollbar para o text
        self.info_scrollbar = ttk.Scrollbar(self.output_frame, command=self.info_text.yview)
        self.info_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configura o text para usar a scrollbar
        self.info_text.config(yscrollcommand=self.info_scrollbar.set)

    def get_info(self):
        """
        Obtém informações sobre o valor de pesquisa de acordo com o tipo de pesquisa e exibe na interface.
        """

        # Obtém o tipo de pesquisa
        type = self.type_combobox.get()

        # Obtém o valor de pesquisa
        value = self.value_entry.get()

        # Verifica se o valor de pesquisa é válido
        if value:
            # Realiza a pesquisa
            if type == "ip":
                info = self.get_ip_info(value)
            elif type == "domain":
                info = self.get_domain_info(value)
            else:
                info = None

            # Exibe as informações
            self.show_info(info)
        else:
            # Exibe uma mensagem de erro
            self.show_error("Por favor, digite um valor de pesquisa válido.")

    def get_ip_info(self, ip):
        """
        Obtém informações sobre um dispositivo com o endereço IP especificado.

        Args:
            ip: O endereço IP do dispositivo.

        Returns:
            Um dicionário com informações sobre o dispositivo, ou None se ocorrer um erro.
        """

        response = requests.get(IPINFO_URL.format(ip))
        if response.ok:
            return response.json()
        else:
            return None

    def get_domain_info(self, domain):
        """
        Obtém informações sobre um domínio.

        Args:
            domain: O domínio.

        Returns:
            Um dicionário com informações sobre o domínio, ou None se ocorrer um erro.
        """

        response = requests.get(WHOIS_URL.format(domain))
        if response.ok:
            return response.json()
        else:
            return None

    def show_info(self, info):
        """
        Exibe as informações obtidas em formato JSON na interface.

        Args:
            info: Um dicionário com informações sobre o valor de pesquisa, ou None se ocorrer um erro.
        """

        # Limpa o text
        self.info_text.config(state="normal")
        self.info_text.delete(1.0, tk.END)

        # Verifica se as informações são válidas
        if info:
            # Formata as informações em JSON
            info_json = json.dumps(info, indent=2)

            # Insere as informações no text
            self.info_text.insert(tk.END, info_json)
        else:
            # Insere uma mensagem de erro no text
            self.info_text.insert(tk.END, "Não foi possível obter as informações. Tente novamente mais tarde.")

        # Desabilita o text
        self.info_text.config(state="disabled")

    def show_error(self, message):
        """
        Exibe uma mensagem de erro na interface.

        Args:
            message: A mensagem de erro.
        """

        # Limpa o text
        self.info_text.config(state="normal")
        self.info_text.delete(1.0, tk.END)

        # Insere a mensagem de erro no text
        self.info_text.insert(tk.END, message)

        # Desabilita o text
        self.info_text.config(state="disabled")

# Define a função principal
def main():
    """
    Ponta de entrada principal da aplicação.
    """

    # Cria a janela principal
    root = tk.Tk()

    # Cria o objeto InfoTool
    tool = InfoTool(root)

    # Inicia o loop principal da aplicação
    root.mainloop()

# Executa a função principal
if __name__ == "__main__":
    main()
