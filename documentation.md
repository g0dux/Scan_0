
```markdown
# Sherlock GUI

Este é um aplicativo de interface gráfica simples que utiliza a API oficial do Sherlock para buscar usuários em redes sociais.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas instaladas no seu ambiente Python:

- `tkinter`
- `requests`
- `colorama`

Você pode instalar as dependências usando:

```bash
pip install tkinter requests colorama
```

## Como usar

1. Execute o script `sherlock_gui.py`.
2. Insira o nome de usuário na caixa de entrada.
3. Clique no botão "Pesquisar" para iniciar a busca.
4. Os resultados serão exibidos na interface gráfica.

## Estrutura do Projeto

- `sherlock_gui.py`: O script principal que cria a interface gráfica e interage com a API do Sherlock.
- `README.md`: Este arquivo que fornece informações sobre o projeto.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar solicitações de pull.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
```

## Configurações Adicionais

- O aplicativo utiliza a API oficial do Sherlock para realizar buscas. Certifique-se de ter uma conexão de internet ativa durante o uso.

## Estrutura do Código

- `search(username, result_label, logger)`: Função principal que realiza a busca utilizando a API do Sherlock e atualiza a interface com os resultados.

- `on_search_button_click(entry, result_label, logger)`: Função chamada ao clicar no botão de pesquisa. Obtém o nome de usuário da entrada e inicia a busca.

- `create_gui()`: Função principal que cria a interface gráfica usando tkinter.

## Contato

Para dúvidas ou sugestões, sinta-se à vontade para entrar em contato via [email@example.com](mailto:email@example.com).
