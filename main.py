import requests
import csv
import os
from datetime import datetime

def buscar_cnpj(cnpj):
    """Busca informações de um CNPJ na API"""
    try:
        url = "https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
        resposta = requests.get(url.format(cnpj=cnpj), timeout=10)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            return {
                'cnpj': cnpj,
                'razao_social': dados.get("razao_social", "N/A"),
                'cnae_fiscal': dados.get("cnae_fiscal", "N/A"),
                'status': 'sucesso'
            }
        else:
            return {
                'cnpj': cnpj,
                'razao_social': "N/A",
                'cnae_fiscal': "N/A",
                'status': f'erro: {resposta.status_code}'
            }
    except Exception as e:
        return {
            'cnpj': cnpj,
            'razao_social': "N/A",
            'cnae_fiscal': "N/A",
            'status': f'erro: {str(e)}'
        }

def processar_lista_cnpjs():
    """Processa lista de CNPJs e salva em CSV"""
    print("\n=== BUSCA EM LOTE DE CNPJS ===\n")
    print("Escolha a forma de entrada:")
    print("1. Arquivo de texto (um CNPJ por linha)")
    print("2. Digitar os CNPJs diretamente (separe por vírgula ou quebra de linha)")
    
    opcao = input("\nOpção (1 ou 2): ").strip()
    
    cnpjs = []
    
    if opcao == "1":
        arquivo = input("Nome do arquivo: ").strip()
        if os.path.exists(arquivo):
            with open(arquivo, 'r', encoding='utf-8') as f:
                cnpjs = [linha.strip() for linha in f if linha.strip()]
        else:
            print(f"Arquivo '{arquivo}' não encontrado!")
            return
    else:
        entrada = input("Digite os CNPJs (separados por vírgula ou linha a linha, termine com linha vazia):\n")
        if ',' in entrada:
            cnpjs = [c.strip() for c in entrada.split(',') if c.strip()]
        else:
            linhas = []
            while True:
                linha = input().strip()
                if not linha:
                    break
                linhas.append(linha)
            cnpjs = linhas
    
    if not cnpjs:
        print("Nenhum CNPJ fornecido!")
        return
    
    print(f"\nProcessando {len(cnpjs)} CNPJ(s)...\n")
    
    resultados = []
    for i, cnpj in enumerate(cnpjs, 1):
        print(f"[{i}/{len(cnpjs)}] Buscando CNPJ: {cnpj}")
        resultado = buscar_cnpj(cnpj)
        resultados.append(resultado)
        print(f"  └─ {resultado['razao_social']} | CNAE Fiscal: {resultado['cnae_fiscal']}\n")
    
    # Salvar em CSV
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"resultado_cnpjs_{timestamp}.csv"
    
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['cnpj', 'razao_social', 'cnae_fiscal', 'status'])
        writer.writeheader()
        writer.writerows(resultados)
    
    print(f"\n✓ Resultados salvos em: {nome_arquivo}")
    
    # Exibir resumo
    sucesso = sum(1 for r in resultados if r['status'] == 'sucesso')
    erro = len(resultados) - sucesso
    print(f"\nResumo: {sucesso} sucesso(s), {erro} erro(s)")

# Executar
if __name__ == "__main__":
    processar_lista_cnpjs()