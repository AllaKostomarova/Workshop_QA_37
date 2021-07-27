per_cent={'ТКБ':5.5, 'СКБ':5.9, 'ВТБ':4.28, 'СБЕР':4.0}
money=float(input('Введите сумму вклада: '))
deposit=[round(money*per_cent['ТКБ']/100,2),
         round(money*per_cent['СКБ']/100, 2),
         round(money*per_cent['ВТБ']/100, 2),
         round(money*per_cent['СБЕР']/100, 2)]
print('Максимальная сумма, которую вы можете заработать - ', max(deposit))