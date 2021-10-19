"""
Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. 

Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]


"""


new_m=[]

def new(m):

  for i in m:

    if type(i) == list:
      new(i)
    else:
      new_m.append(i)
  return new_m


m = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(new(m))