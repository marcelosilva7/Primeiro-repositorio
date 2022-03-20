print('Programinha para saber quanto vale as medidas em Metro')
metro = float(input('Digite o metro desejado! '))
km = metro*1000
hm = metro*100
dam = metro*10
dm = metro/10
cm = metro/100
mm = metro/1000
print(f'{metro:.2f} metros conventido em dm é {dm:.2f}M, em cm é {cm:.2f}M e em mm é {mm:.2f}M\n'
      f'em dam é {dam:.2f}M, em hm é {hm:.2f} e em km é {km:.2f}M')
