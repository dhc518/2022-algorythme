edges = [ # 708=China, 725=Reran
  (0, 1, 686), (0, 2, 429), (0, 5, 232), (0, 9, 319), (0, 13, 193), 
  (1, 8, 180), (1, 10, 345), (1, 11, 100), (1, 13, 302), (1, 17, 374), 
  (2, 10, 83), (2, 11, 298), (2, 12, 730), (2, 17, 96), (3, 12, 332), 
  (3, 13, 494), (3, 17, 342), (4, 7, 378), (4, 8, 374), (4, 14, 235), 
  (4, 15, 214), (5, 12, 320), (5, 17, 302), (6, 15, 208), (6, 16, 190), 
  (7, 15, 240), (8, 11, 194), (8, 13, 709), (9, 12, 62), (10, 11, 254), 
  (10, 13, 249), (10, 17, 97), (11, 14, 323), (12, 13, 140), (12, 14, 572), 
  (12, 17, 494), (13, 14, 383), (13, 17, 479), (14, 16, 694), (15, 16, 392)
]
n_vertices = 18#max(max(e[0], e[1]) for e in edges) + 1

total_weight = 0
mst = []

edges.sort(key = lambda e: e[2])
#print(f'{edges}')

# root = []
# for i in range(n_vertice): roots[i] = i
roots = [i for i in range(n_vertices)]

def union(u, v):
  ur = get_root(u)
  vr = get_root(v)
  roots[vr] = ur


def get_root(v):
  root =  roots[v]
  if v != root:
    roots[v] = get_root(root) # 경로압축
  return  roots[v]

for u, v, w in edges:
  if get_root(u) == get_root(v): continue
  mst.append((u,v,w))
  union(u, v)
  total_weight += w
  if len(mst) >= n_vertices -1:
    break

print(f'n_vertices={n_vertices}  mst={mst} total_weight={total_weight}')