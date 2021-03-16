# BOJ 최소 스패닝 트리 1197 - 크루스칼 알고리즘
import sys

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

input = sys.stdin.readline


n, m = map(int, input().split())
parent = [0] * (n+1)
edges = []
result = 0

for i in range(1, n+1):
  parent[i] = i

for _ in range(m):
  a, b, c = map(int, input().split())
  edges.append((c, a, b))

edges.sort()

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)
