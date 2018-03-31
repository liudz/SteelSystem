# ver: 1.0.0
# finished: 2018/03/31
# made by: liudongze
# zheng fang si jiao zhui wang jia (JGJ 7 - 2010)
import rhinoscriptsyntax as rs

def wangjia():
	m = 10
	n = 8
	dx = 3000
	dy = 2000
	h = 2000
	
	rs.AddLayer("Top", (255,0,0))
	rs.CurrentLayer("Top")
	txchord(m, n, dx, dy, 0)
	tychord(m, n, dx, dy, 0)
	
	rs.AddLayer("Bottom", (0,255,0))
	rs.CurrentLayer("Bottom")
	bxchord(m, n, dx, dy, h)
	bychord(m, n, dx, dy, h)
	
	rs.AddLayer("Middle", (0,0,255))
	rs.CurrentLayer("Middle")
	brace(m, n, dx, dy, h)
	
	rs.AddLayer("Plane", (255,255,0))
	rs.CurrentLayer("Plane")
	addplane(m, n, dx, dy)

def txchord(m, n, dx, dy, h):
	j = 0
	while j <= n:
		for i in range(m):
			sp = [i*dx, j*dy, h]
			ep = [(i+1)*dx, j*dy, h]
			rs.AddLine(sp, ep)
		j = j + 1
		
def tychord(m, n, dx, dy, h):
	i = 0
	while i <= m:
		for j in range(n):
			sp = [i*dx, j*dy, h]
			ep = [i*dx, (j+1)*dy, h]
			rs.AddLine(sp, ep)
		i = i + 1
	
def bxchord(m, n, dx, dy, h):
	j = 0
	while j < n:
		for i in range(m - 1):
			sp = [(dx/2 + i*dx), (dy/2 + j*dy), -h]
			ep = [(dx/2 + (i+1)*dx), (dy/2 + j*dy), -h]
			rs.AddLine(sp, ep)
		j = j + 1

def bychord(m, n, dx, dy, h):
	i = 0
	while i < m:
		for j in range(n - 1):
			sp = [(dx/2 + i*dx), (dy/2 + j*dy), -h]
			ep = [(dx/2 + i*dx), (dy/2 + (j+1)*dy), -h]
			rs.AddLine(sp, ep)
		i = i + 1

def brace(m, n, dx, dy, h):
	for i in range(m):
		for j in range(n):
			sp = [(dx/2 + i*dx), (dy/2 + j*dy), -h]
			ep1 = [i*dx, j*dy, 0]
			ep2 = [(dx + i*dx), j*dy, 0]
			ep3 = [i*dx, (dy + j*dy), 0]
			ep4 = [(dx + i*dx), (dy + j*dy), 0]
			rs.AddLine(sp, ep1)
			rs.AddLine(sp, ep2)
			rs.AddLine(sp, ep3)
			rs.AddLine(sp, ep4)

def addplane(m, n, dx, dy):
	for i in range(m):
		for j in range(n):
			plane = rs.WorldXYPlane()
			origin = (i * dx, j * dy, 0)
			newplane = rs.MovePlane(plane, origin)
			rs.AddPlaneSurface(newplane, dx, dy)

if __name__ == "__main__":
	wangjia()
