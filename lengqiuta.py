# mathematical induction
import math
import rhinoscriptsyntax as rs

def lengqiuta():
	# (x/a)**2-(z - zz[3] / b)**2=1
	a = 46000
	b = 110269
	
	# no.4 is the neck, that is [3]
	
	# z space
	z = [26212, 21259, 17815, 15649, 13900, 12725, 11911, 11386, 11103, 11040, 11192, 11572]
	
	# segment
	n = 32
	
	# get z coordinate
	zz = []
	for i in range(len(z)):
		zz.append(sum(z[i:len(z)]))
	zz.append(0)
	
	# get x coordinate
	x = []
	for i in range(len(zz)):
		x1 = a * math.sqrt(1 + ((zz[i] - zz[3]) / b) **2)
		x.append(x1)
	
	rs.CurrentView("top")
	
	# add guide circle and points
	rs.AddLayer("guide")
	rs.CurrentLayer("guide")
	
	epts = []
	opts = []
	ptss = []
	for i in range(len(zz)):
		if (i % 2) == 1:
			# even number circle: 0 2 4 6 8 10 12
			cir = rs.AddCircle([0, 0, zz[i]], x[i])
			epts = rs.DivideCurve(cir, 2 * n)
			for j in range(len(epts)):
				if (j % 2) == 0:
					ptss.append(list(epts[j]))
		elif (i % 2) == 0:
			# odd number circle: 1 3 5 7 9 11
			cir = rs.AddCircle([0, 0, zz[i]], x[i])
			opts = rs.DivideCurve(cir, 2 * n)
			for j in range(len(opts)):
				if (j % 2) == 1:
					ptss.append(list(opts[j]))
	
	# vertical members
	rs.AddLayer("hbar", (0, 255 ,0))
	rs.CurrentLayer("hbar")
	
	i = 0
	while (i < (len(zz) * n)):
		if i in range((n - 1), len(zz) * n, n):
			rs.AddLine(ptss[i], ptss[i - n + 1])
		else:
			rs.AddLine(ptss[i], ptss[i + 1])
		i = i + 1
	
	# vertical members
	rs.AddLayer("vbar", (0, 0, 255))
	rs.CurrentLayer("vbar")
	
	for i in range(n):
		for j in range(0, (len(zz) - 1), 2):	#0, 2, 4, 6, 8, 10, 12
			t = n * j + i
			rs.AddLine(ptss[t], ptss [t + n])
			if t == (n * (j + 1) - 1):
				rs.AddLine(ptss[t], ptss[t + 1])
			else:
				rs.AddLine(ptss[t], ptss[t + n + 1])
	
	for i in range(n):
		for j in range(1, (len(zz)), 2):	#1, 3, 5, 7, 9, 11
			t = n * j + i
			rs.AddLine(ptss[t], ptss[t + n])
			if t == n * j:
				rs.AddLine(ptss[t], ptss[t + 2 * n - 1])
			else:
				rs.AddLine(ptss[t], ptss[t + n - 1])
	
	# add plane
	rs.AddLayer("plane", (255, 0, 0))
	rs.CurrentLayer("plane")
		
	for j in range(0, len(zz) - 1, 2):
		for i in range(j * n, j * n + n - 1, 1):
			rs.AddSrfPt([(ptss[i + 1]), (ptss[i]), (ptss[n + i + 1])])
		rs.AddSrfPt([(ptss[j * n]), (ptss[j * n + n - 1]), (ptss[j * n + n])])
		
	for j in range(0, len(zz) - 1, 2):
		for i in range(j * n + n, j * n + 2 * n - 1, 1):
			rs.AddSrfPt([(ptss[i]), (ptss[i + 1]), (ptss[i - n])])
		rs.AddSrfPt([(ptss[j * n + 2 * n - 1]), (ptss[j * n + n]), (ptss[j * n + n - 1])])
		
	for j in range(0, len(zz) - 1, 2):
		for i in range(j * n + 2 * n, j * n + 3 * n -1, 1):
			rs.AddSrfPt([(ptss[i]), (ptss[i + 1]), (ptss[i - n + 1])])
		rs.AddSrfPt([(ptss[j * n + 3 * n -1]), (ptss[j * n + 2 * n]), (ptss[j * n + n])])
	
	for j in range(0, len(zz) - 1, 2):
		for i in range(j * n + n, j * n + 2 * n - 1, 1):
			rs.AddSrfPt([(ptss[i + 1]), (ptss[i]), (ptss[i + n])])
		rs.AddSrfPt([(ptss[j * n + n]), (ptss[j * n + 2 * n -1]), (ptss[j * n + 3 * n - 1])])
	
	# delete guide layer
	rs.PurgeLayer("guide")
	
if __name__ == "__main__":
	lengqiuta()
