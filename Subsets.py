class Subsets(object):     
 def subsets(self, S):
    
  S.sort()
  res = []

  def dfs(depth, start, valuelist):
    res.append(valuelist)
    if depth == len(S): 
      return
    for i in range(start, len(S)):
      dfs(depth+1, i+1, valuelist+[S[i]])

  dfs(0, 0, [])
  return res