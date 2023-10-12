metros=float(input("Qual o tamanho da área a ser pintada em metros quadrados?: "))

litros=metros/3
latas = litros/18

print("Serão usadas",f"{latas:.2f}","latas de tinta")
print("O preco total é de: ",f"R${latas*80:.2f}")
