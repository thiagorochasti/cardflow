import sankhya_generator
import os

def main():
    input_file = 'input.csv'
    output_file = 'retorno_cartao.txt'
    sequencial = 1 # Pode ser parametrizado ou lido de um arquivo de controle
    
    if not os.path.exists(input_file):
        print(f"Erro: Arquivo {input_file} não encontrado.")
        return

    print(f"Lendo {input_file}...")
    try:
        transactions = sankhya_generator.read_csv(input_file)
        print(f"Encontradas {len(transactions)} transações.")
        
        print(f"Gerando {output_file}...")
        sankhya_generator.generate_file(output_file, sequencial, transactions)
        
        print("Concluído com sucesso!")
        print(f"Arquivo gerado em: {os.path.abspath(output_file)}")
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
