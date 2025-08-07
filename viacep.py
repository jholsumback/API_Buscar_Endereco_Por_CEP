import requests

def pegar_endereco(cep: str) -> dict:
    """Busca endereço através do CEP"""
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code != 200:
        return {}
    return response.json()

def mostrar(valor):
    return valor if valor else "Não informado"

cep = input("Digite seu CEP: ")
endereco = pegar_endereco(cep)

# Verifica se a API retornou "erro": true (CEP inválido)
if endereco.get("erro") is True:
    print("❌ CEP não encontrado")
else:
    print("✅ Endereço encontrado:")
    print(f"Logradouro: {mostrar(endereco.get('logradouro'))}")
    print(f"Bairro: {mostrar(endereco.get('bairro'))}")
    print(f"Cidade: {mostrar(endereco.get('localidade'))}")
    print(f"Estado: {mostrar(endereco.get('estado') or endereco.get('uf'))}")
    print(f"DDD: {mostrar(endereco.get('ddd'))}")
