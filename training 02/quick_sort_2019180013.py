from random import randint

words = [
  'jingo', 'lf', 'log', 'non', 'lj', 'goo', 'hmg', 'joe', 'knell', 'minim',
  '2019180013', '두혁찬',
  'mog', 'jim', 'km', 'lining', 'mingle', 'ell', 'folk', 'melon', 'ln', 'link',
  'knife', 'fennel', 'loon', 'john', 'ff', 'felloe', 'liking', 'lino', 'om', 'keg',
  'joke', 'no', 'hog', 'jell', 'fino', 'elfin', 'gin', 'lone', 'oh', 'gong',
  'ogee', 'oi', 'jig', 'filling', 'g', 'ge', 'mn', 'femme', 'fen', 'kj',
  'gene', 'online', 'mg', 'goggle', 'emf', 'loll', 'meek', 'l', 'gem', 'filing',
  'infill', 'hello', 'ink', 'monk', 'kg', 'ghillie', 'elf', 'gm', 'leo', 'genie',
  'hoe', 'he', 'eke', 'moll', 'gnomon', 'fm', 'lei', 'million', 'going', 'feminine',
  'infilling', 'liege', 'mo', 'o', 'goon', 'hg', 'legging', 'holm', 'enjoin', 'e',
  'mini', 'logging', 'kin', 'hen', 'logo', 'flee', 'inf', 'fog', 'knee', 'limn',
  'jingo', 'lf', 'log', 'non', 'lj', 'goo', 'hmg', 'joe', 'knell', 'minim',
  'menfolk', 'feel', 'mlle', 'ken', 'home', 'if', 'linen', 'ne', 'lo', 'knoll',
  'mime', 'ooh', 'nomen', 'hill', 'kohl', 'efl', 'offline', 'lee', 'king', 'legion',
  'one', 'hike', 'genome', 'neigh', 'lifelong', 'him', 'gigolo', 'fo', 'fe', 'ego',
]
array = words

def partition(start, end): #end=inclusive
  ri = randint(start, end)
  array[start], array[ri] = array[ri], array[start]
  pv = array[start]

  p, q = start, end+1
  while True:
    #find p
    while True:
      p += 1

      if q < p: break

      if p> end or array[p] > pv: break
    # found p

    # find p
    while True:
      q -= 1

      if q < p: break

      if q < start or array[q] <= pv: break

    if p >= q: break #더이상 바꿀게 없다

    # swap @p and @q
    array[p], array[q] = array[q], array[p]

  # swap @start and #q
  if start != q:
      array[start], array[q] = array[q], array[start]
  return q

def insertionSort(start, end): #end=inclusive
  for i in range(start + 1, end+1):
    v = array[i] # i 위치의 v 값이 주인공
    j = i - 1 # v 와 비교를 시작할 위치
    while start <= j and array[j] > v:
      array[j+1] = array[j] # 오른쪽으로 밀어준다
      j -= 1

    array[j+1] = v


def quickSort(start, end): #end=inclusive
  if start >= end: return  # 재귀호출의 종료 조건
  if start - end <= 10: # size of this array <= 10
    return insertionSort(start, end)
  pi = partition(start, end)
  quickSort(start, pi-1)
  quickSort(pi+1, end)


quickSort(0, len(array)-1)
print(array)