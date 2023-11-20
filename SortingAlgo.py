#merge Sort algorithm
def merge(a,start,mid,end):
  i=start
  j=mid+1
  k=start
  merged = [0]*(end+1)

  while(i<=mid and j<=end):
    if(a[i]<a[j]):
      merged[k] = a[i]
      i+=1
    else:
      merged[k] = a[j]
      j+=1
    k+=1 
  
  while(i<=mid):
    merged[k] =  a[i]
    i+=1
    k+=1

  while(j<=end):
    merged[k] = a[j]
    k+=1
    j+=1

  for i in range(start, end+1):
    a[i] = merged[i]



#insertion sort algorithm
def insertion(a):
  n = len(a)
  for i in range(n):
    j=i-1
    while(a[j] < a[j-1] and j>0):
      (a[j], a[j-1]) = (a[j-1],a[j])
      j-=1



#selection sort algorithm
def selection(a):
  for i in range(len(a)):
    small = i
    for j in range(i, len(a)-1):
      if(a[j]<a[small]):
        small = j
    (a[small] , a[i]) = (a[i], a[small])
