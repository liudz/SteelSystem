# ver: 1.0.0
# finished: 2018/03/31
# made by: liudongze
# dan ceng qiu mian wang qiao (lei huan xing) (JGJ 7 -2010)
import math
import rhinoscriptsyntax as rs

def wangqiao():
	l = 8000
	f = 2000
	m = 5
	n = 12
	
	# circle center and radius
	xn = l /(2 * m)
	r = (f**2 + (l/2)**2)/(2*f)
	ctrs = []
	rads = []
	#  from top circle to devide circle
	for i in range(m):
		x = xn* (i + 1)
		z = math.sqrt(r**2 - x**2) - (r - f)
		ctrs.append([0, 0, z])
		rads.append(x)
	
	# create guide circle
	
	pts = []
	ptss = []
	rs.CurrentView("top")
	
	rs.AddLayer("guide")
	rs.CurrentLayer("guide")
	
	for i in range(m):
		cir = rs.AddCircle(ctrs[i], rads[i])
		pts = rs.DivideCurve(cir, n)
		ptss.append(pts)
	
	# vertical direction
	
	rs.AddLayer("hdir", (0, 255, 0))
	rs.CurrentLayer("hdir")
	
	toppt = [0, 0, f]
	for i in range(n):
		rs.AddLine(toppt,ptss[0][i])
	
	for i in range(m - 1):
		for j in range(n):
			rs.AddLine(ptss[i][j],ptss[i+1][j])
	
	# horizonal direction
	
	rs.AddLayer("vdir", (0, 0, 255))
	rs.CurrentLayer("vdir")
	
	for i in range(m):
		for j in range(n - 1):
			rs.AddLine(ptss[i][j], ptss[i][j+1])
			rs.AddLine(ptss[i][n - 1], ptss[i][0])
	
	# add shell
	rs.AddLayer("plane", (255, 0, 0))
	rs.CurrentLayer("plane")
	
	for i in range(n - 1):
		rs.AddSrfPt([(ptss[0][i]), (ptss[0][i + 1]), (0, 0, f)])
	rs.AddSrfPt([(ptss[0][n - 1]), (ptss[0][0]),(0, 0, f)])
	
	for i in range(m - 1):
		for j in range(n - 1):
			rs.AddSrfPt([(ptss[i][j]), (ptss[i + 1][j]), (ptss[i + 1][j + 1]), (ptss[i][j + 1])])
		rs.AddSrfPt([(ptss[i][n - 1]), (ptss[i + 1][n - 1]), (ptss[i + 1][0]), (ptss[i][0])])
	
	# delete guide layer
	rs.PurgeLayer("guide")

if __name__ == "__main__":
	wangqiao()
