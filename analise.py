import pandas as pd
import glob
import os

# Define o caminho da pasta onde estão os arquivos CSV
pasta = '/arquivos/'

# Lista todos os arquivos CSV dentro da pasta especificada
arquivos = glob.glob(os.path.join(pasta, '*.csv'))

# Lê cada arquivo CSV encontrado e armazena em uma lista de DataFrames
# Obs: encoding="utf_16" indica que os arquivos estão codificados em UTF-16
lista_df = [pd.read_csv(arq, encoding="utf_16", sep=',') for arq in arquivos]

# Concatena todos os DataFrames em um único DataFrame
df_unico = pd.concat(lista_df, ignore_index=True)

# Configuração global para exibir números sem notação científica
pd.set_option("display.float_format", "{:,.2f}".format)

# Ajusta a coluna 'Valor Consolidado':
# - Remove pontos (usados como separadores de milhar)
# - Substitui vírgulas por pontos (para formato numérico padrão)
df_unico['Valor Consolidado'] = df_unico['Valor Consolidado'].str.replace('.', '').str.replace(',', '.')
df_unico['Valor Consolidado'] = df_unico['Valor Consolidado'].astype(float)

# Define formato de exibição dos números com vírgula como separador decimal
pd.options.display.float_format = lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Agrupa os dados pela coluna 'Situação da Negociação' e calcula métricas:
consolidado = df_unico.groupby('Situação da Negociação').agg(
    quantidade_devedores=('CPF/CNPJ do Optante', 'nunique'),  # número de devedores distintos
    quantidade_transacoes_devedores=('CPF/CNPJ do Optante', 'count'),  # total de transações
    trasacoes_com_atraso=('Qtde de Parcelas em Atraso', lambda x: (x > 0).sum()),  # transações com atraso
    total_valor_consolidado=('Valor Consolidado', 'sum')  # soma dos valores consolidados
).reset_index()

# Calcula os totais de todas as colunas numéricas
totais = consolidado.sum(numeric_only=True)

# Cria uma linha adicional com os totais
linha_total = pd.DataFrame([totais], index=['Total'])

# Junta os resultados consolidados com a linha de totais
df_final = pd.concat([consolidado, linha_total], ignore_index=True)

# Exibe o DataFrame final
df_final
