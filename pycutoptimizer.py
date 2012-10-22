#!/usr/bin/pythoni
from Rect import Rect
from Vector import Vector
from copy import copy

#Tudo em mm

# Formica 3,08m x 1,25m
sheet = Rect(-1, -1, 3080, 1250)

lst_cortes=[]
lst_cortes.append(Rect(-1, -1, 1220, 300))
lst_cortes.append(Rect(-1, -1, 1220, 300))
lst_cortes.append(Rect(-1, -1, 1220, 370))
lst_cortes.append(Rect(-1, -1, 1220, 370))
lst_cortes.append(Rect(-1, -1, 350, 300))
lst_cortes.append(Rect(-1, -1, 350, 300))
lst_cortes.append(Rect(-1, -1, 1220, 70))
lst_cortes.append(Rect(-1, -1, 1220, 70))
lst_cortes.append(Rect(-1, -1, 350, 70))
lst_cortes.append(Rect(-1, -1, 350, 70))

# INICIO NAO MECHER
def AreaComparator(a, b):
	area1 = a.width * a.height
	area2 = b.width * b.height

	return (area1 > area2) or (area1 == area2)

def PositionComparator(a, b):
	return (a.y < b.y) or ((a.y == b.y) and ((a.x < b.x) or ((a.x == b.x) and ((a.height > b.height) or ((a.height == b.height) and (a.width > b.width))))))

vctCuts = Vector(lst_cortes, AreaComparator)

sheet_area = sheet.width * sheet.height

total_cut_area = 0
for cut in vctCuts:
	total_cut_area += (cut.width * cut.height)

print "Area chapa: " + str(sheet_area) + " mm2"
print "Area dos cortes: " + str(total_cut_area) + " mm2"

gaps = Vector([Rect(0, 0, sheet.width, sheet.height)], PositionComparator)
for cut in vctCuts:
	#g = Vector([Rect(-1, -1, 0, 0)], PositionComparator)
	#g = copy(gaps)

	last = False
	for g in gaps:
		if ((g.width >= cut.width) and (g.height >= cut.height)):
			break
		last = True

	if not last:
		cut.x = g.x
		cut.y = g.y
		
		count = 0
		while (count < len(gaps)):
			g = gaps[count]
			if (not((cut.right() < g.x) or (cut.bottom() < g.y) or (cut.x > g.right()) or (cut.y > g.bottom()))):
				print "AQUI"
				# Add a gap to the left of the new rectangle if possible
				print g
				print cut
				if (g.x < cut.x):
					print "AQUI1"
					gaps.__add__(Rect(g.x, g.y, cut.x - g.x, g.height))

				# Add a gap on top of the new rectangle if possible
				if (g.y < cut.y):
					print "AQUI2"
					gaps.__add__(Rect(g.x, g.y, g.width, cut.y - g.y))

				# Add a gap to the right of the new rectangle if possible
				if (g.right() > cut.right()):
					print "AQUI3"
					gaps.__add__(Rect(cut.right() + 1, g.y, g.right() - cut.right(), g.height))

				# Add a gap below the new rectangle if possible
				if (g.bottom() > cut.bottom()):
					print "AQUI4"
					gaps.__add__(Rect(g.x, cut.bottom() + 1, g.width, g.bottom() - cut.bottom()))

				gaps.erase(count)
				count += 1
			else:
				count += 1
for cut in vctCuts:
	print cut
