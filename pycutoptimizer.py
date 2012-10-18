#!/usr/bin/python

#Tudo em mm

# Formica 3,08m x 1,25m
tamanho_da_chapa=[3080, 1250]

lst_cortes=[]
lst_cortes.append([1220, 300])
lst_cortes.append([1220, 300])
lst_cortes.append([1220, 370])
lst_cortes.append([1220, 370])
lst_cortes.append([350, 300])
lst_cortes.append([350, 300])
lst_cortes.append([1220, 70])
lst_cortes.append([1220, 70])
lst_cortes.append([350, 70])
lst_cortes.append([350, 70])

# INICIO NAO MECHER
import Rect

def AreaComparator(a, b):
	area1 = a.width * a.height
	area2 = b.width * b.height

	return (area1 > area2) or (area1 == area2)

def PositionComparator(a, b):
	return (a.y < b.y) or ((a.y == b.y) and ((a.x < b.x) or ((a.x == b.x) and ((a.height > b.height) or ((a.height == b.height) and (a.width > b.width))))))

area_chapa = tamanho_da_chapa[0] * tamanho_da_chapa[1]

area_total_cortes = 0
for corte in lst_cortes:
	corte.append(corte[0] * corte[1])
	corte.append(-1)
	corte.append(-1)
	area_total_cortes += corte[2]

lst_cortes = sorted(lst_cortes, key=lambda corte: corte[2], reverse=True)

print "Area chapa: " + str(area_chapa) + " mm2"
print "Area dos cortes: " + str(area_total_cortes) + " mm2"

posicionamento = [[tamanho_da_chapa[0], tamanho_da_chapa[1], 0, 0]]
for corte in lst_cortes:
	last = False
	for posicao in posicionamento:
		if ((posicao[0] >= corte[0]) and (posicao[1] >= corte[1])):
			break
		last = True

	if not last:
		corte[3] = posicao[2]
		corte[4] = posicao[3]
		
		pos = iter(posicionamento)
		posicao = pos.next()
		count = 0
		while True:
			print str(corte[3] + corte[0] - 1) + " < " + str(posicao[2])
			print str(corte[4] + corte[1] - 1) + " < " + str(posicao[3])
			print str(corte[3]) + " > " + str(posicao[2] + posicao[0] - 1)
			print str(corte[4]) + " > " + str(posicao[3] + posicao[1] - 1)
			
			if (not ((corte[3] + corte[0] - 1 < posicao[2]) or (corte[4] + corte[1] - 1 < posicao[3]) or (corte[3] > posicao[2] + posicao[0] - 1) or (corte[4] > posicao[3] + posicao[1] - 1))):
				if (posicao[2] < corte[3]):
					print "AQUI1"
					posicionamento.append([corte[3] - posicao[2], posicao[3], posicao[2], posicao[3]])
				if (posicao[3] < corte[4]):
					print "AQUI2"
					posicionamento.append([corte[3], corte[4] - posicao[3], posicao[2], posicao[3]])
				if (posicao[2] + posicao[0] - 1 > corte[3] + corte[0] - 1):
					print "AQUI3"
					posicionamento.append([(posicao[2] + posicao[0] - 1) - (corte[3] + corte[0] - 1), posicao[1], (corte[3] + corte[0] - 1) + 1, posicao[3]])

				if (posicao[3] + posicao[1] - 1 > corte[4] + corte[1] - 1):
					print "AQUI4"
					posicionamento.append([posicao[0], (posicao[3] + posicao[1] - 1) - (corte[4] + corte[1] - 1), posicao[3], (corte[4] + corte[1] - 1) + 1])
				posicionamento.pop(count)
				count += 1
			else:
				print "AQUI5"
				try:
					pos.next()
				except StopIteration:
					break

print posicionamento
print lst_cortes
