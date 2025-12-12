import pandas as pd
import matplotlib.pyplot as plt
dados = pd.read_excel('analisedados.xlsx')
dados['Faturamento'] = dados['Qtd'] * dados['Preço Unit.']
faturamento_total =dados['Faturamento'].sum()
print(dados)
print(f'O faturamento total é R${faturamento_total:.2f}')
media_vendas= dados['Faturamento'].mean()
maior_venda= dados['Faturamento'].max()
print(f'A media de vendas foi {media_vendas:.2f} e a maior venda foi {maior_venda:.2f}\n')

tabela_ana = dados[dados['Vendedor'] == 'Ana']
total_ana = tabela_ana['Faturamento'].sum()
print(f'O total de vendas de ana foi R${total_ana:.2f}')


vendas_por_vendedor = dados.groupby('Vendedor')['Faturamento'].sum()
vendas_por_vendedor.plot(kind='bar')
plt.show()

print('Carregar/Calcular --> Agrupar --> Plotar --> Mostrar')

dados.to_excel("relatorio_final.xlsx", index=False)