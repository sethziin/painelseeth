import json
import os

KEYS_FILE = 'keys.json'

# Função para carregar as chaves válidas
def load_keys():
    if os.path.exists(KEYS_FILE):
        with open(KEYS_FILE, 'r') as file:
            return json.load(file)
    return []

# Função para salvar as chaves válidas
def save_keys(keys):
    with open(KEYS_FILE, 'w') as file:
        json.dump(keys, file, indent=4)

# Função para adicionar uma nova chave
def add_key():
    print("=== Adicionar Chave ===")
    key = input("Insira a nova chave: ").strip()
    if not key:
        print("Chave não pode estar vazia.")
        return

    keys = load_keys()
    if key in keys:
        print("Chave já existe.")
    else:
        keys.append(key)
        save_keys(keys)
        print("Chave adicionada com sucesso!")

# Função para listar as chaves válidas
def list_keys():
    keys = load_keys()
    if keys:
        print("Chaves válidas:")
        for key in keys:
            print(key)
    else:
        print("Nenhuma chave encontrada.")

# Função principal
def main():
    while True:
        print("=== MENU ADMINISTRATIVO ===")
        print("1. Adicionar Nova Chave")
        print("2. Listar Chaves Válidas")
        print("3. Sair")
        print()  # Linha em branco para separar as opções do prompt

        choice = input("Escolha uma opção: ").strip()

        if choice == '1':
            add_key()
        elif choice == '2':
            list_keys()
        elif choice == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
