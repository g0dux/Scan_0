Documentação da ferramenta de hacking

Introdução

Esta ferramenta é um aplicativo de interface gráfica do usuário (GUI) que pode ser usado para realizar pesquisas sobre dispositivos e domínios. A ferramenta usa as APIs IPinfo.io e Whois Lookup para obter informações sobre dispositivos e domínios.

Requisitos

Para usar esta ferramenta, você precisará dos seguintes requisitos:

Python 3.10 ou superior
As bibliotecas Python requests, json e tkinter
Para instalar as bibliotecas Python necessárias, você pode usar o seguinte comando:

pip install -r requirements.txt
Instalação

Para instalar a ferramenta, você precisará descompactar o arquivo zip fornecido. Em seguida, você poderá executar a ferramenta executando o seguinte comando:

python3 hacking_tool.py
Uso

A ferramenta tem uma interface simples e fácil de usar. Para realizar uma pesquisa, você precisará seguir estas etapas:

Selecione o tipo de pesquisa.
Insira o valor de pesquisa.
Clique no botão "Pesquisar".
A ferramenta retornará as informações da pesquisa na área de texto "Resultados".

Tipos de pesquisa

A ferramenta suporta dois tipos de pesquisa:

IP: Pesquisa informações sobre um dispositivo com o endereço IP especificado.
Domínio: Pesquisa informações sobre um domínio.
Valores de pesquisa

O valor de pesquisa depende do tipo de pesquisa selecionado. Para uma pesquisa de IP, o valor de pesquisa deve ser um endereço IP. Para uma pesquisa de domínio, o valor de pesquisa deve ser um domínio.

Resultados

As informações da pesquisa são retornadas como um objeto JSON. O objeto JSON pode conter as seguintes informações:

IP: O endereço IP do dispositivo ou domínio.
Hostname: O hostname do dispositivo ou domínio.
Sistema operacional: O sistema operacional do dispositivo.
Portas abertas: As portas abertas no dispositivo.
Exemplo

Aqui está um exemplo de como usar a ferramenta:

# Selecione o tipo de pesquisa
variable_type.set("ip")

# Insira o valor de pesquisa
entry_input.insert(0, "192.168.1.1")

# Clique no botão "Pesquisar"
button_search.invoke()
A ferramenta retornará as seguintes informações:

{
    "ip": "192.168.1.1",
    "hostname": "meu-computador",
    "operating_system": "Linux",
    "open_ports": ["22", "80", "443"]
}
Créditos

Esta ferramenta foi desenvolvida por [andha0].
