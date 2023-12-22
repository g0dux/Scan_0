import tkinter as tk
from tkinter import ttk
import requests
import colorama
import logging
from colorama import Fore, Style

def search(username, result_label, logger):
    """Pesquisa pelo usuário nas redes sociais usando a ferramenta sherlock-py."""
    try:
        response = requests.get(f"https://sherlock-project.herokuapp.com/api/{username}")
        response.raise_for_status()
        results = response.json()
        if results:
            logger.info(f"Encontramos {len(results)} resultados:")
            result_label.config(text=f"Encontramos {len(results)} resultados:")
            for site, data in results.items():
                logger.info(f"- {site}: {data['url_user']}")
                result_label.config(text=result_label.cget("text") + f"\n- {site}: {data['url_user']}")
                if data['exists'] == "yes":
                    logger.info(Fore.GREEN + "Usuário encontrado!" + Style.RESET_ALL)
                    result_label.config(text=result_label.cget("text") + "\nUsuário encontrado!")
                else:
                    logger.info(Fore.RED + "Usuário não encontrado!" + Style.RESET_ALL)
                    result_label.config(text=result_label.cget("text") + "\nUsuário não encontrado!")
        else:
            logger.info("Nenhum resultado encontrado.")
            result_label.config(text="Nenhum resultado encontrado.")

    except requests.exceptions.RequestException as e:
        logger.exception(f"Ocorreu um erro na requisição: {e}")
        result_label.config(text="Ocorreu um erro na requisição.")

    except ValueError as e:
        logger.exception(f"Ocorreu um erro na decodificação JSON: {e}")
        result_label.config(text="Ocorreu um erro na decodificação JSON.")

def on_search_button_click(entry, result_label, logger):
    username = entry.get()
    if username:
        search(username, result_label, logger)

def create_gui():
    root = tk.Tk()
    root.title("Sherlock GUI")

    # Inicializa o módulo colorama
    colorama.init()

    # Cria um logger com o nome 'sherlock'
    logger = logging.getLogger('sherlock')

    # Define o nível de logging para INFO
    logger.setLevel(logging.INFO)

    # Cria um frame
    frame = ttk.Frame(root, padding="10")
    frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Cria uma entry para inserir o nome de usuário
    entry = ttk.Entry(frame, width=20)
    entry.grid(column=0, row=0, padx=5, pady=5)

    # Cria um botão de pesquisa
    search_button = ttk.Button(frame, text="Pesquisar", command=lambda: on_search_button_click(entry, result_label, logger))
    search_button.grid(column=1, row=0, padx=5, pady=5)

    # Cria um rótulo para exibir os resultados
    result_label = ttk.Label(frame, text="")
    result_label.grid(column=0, row=1, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()