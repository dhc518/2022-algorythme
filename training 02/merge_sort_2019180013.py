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

def merge(start, mid, end): # mid is in left, end=inclusive in right
    # 공간복잡도 = O(n)
    merged = []
    l, r = start, mid+1
    while l <= mid and r <= end: # 선수가 있을 때 까지
        if words[l] <= words[r]:
            merged += [ words[l] ] # merged.append(words[i])
            l += 1
        else:
            merged += [words[r]]
            r += 1
    if l <= mid: # 왼쪽팀에 선수가 남아있다면
        merged += words[l:mid+1]# 어디에 +1을 해야할지
    elif r <= end: # 오른쪽팀에 선수가 남아있다면
        merged += words[r:end+1]
    # merged 가 완성되었음 => words 에 채워넣어야 한다.
    words[start:end+1] = merged # ??? 의 어디에는 -1 이나 +1??


def mergeSort(start=0, end=None): # end = Inclusive
    if end == None: end = len(words) - 1
    if end == start: return #재귀호출의 종료 조건

    mid = (start + end) // 2 # mid is included in left part
    mergeSort(start, mid) #왼쪽
    mergeSort(mid+1, end) #오른쪽
    merge(start, mid, end)


print(words)
mergeSort()
print(words)
