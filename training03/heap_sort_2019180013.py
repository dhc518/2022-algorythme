words = [
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
  'mom', 'hi', 'fine', 'ni', 'ongoing', 'ho', 'noh', 'jog', 'lion', 'loin',
  'fill', 'm', 'nee', 'join', 'noggin', 'neon', 'none', 'hm', 'gi', 'hook',
  'ion', 'in', 'gen', 'mono', 'feign', 'look', 'hinge', 'moonie', 'nil', 'ginkgo',
  'kilo', 'fief', 'ikon', 'moon', 'long', 'hf', 'lifeline', 'lingo', 'mink', 'nigh',
  'k', 'killing', 'hoi', 'mongol', 'nikkei', 'ime', 'hoof', 'me', 'floe', 'omen',
  'jiff', 'mike', 'foe', 'ingoing', 'leg', 'kiln', 'fin', 'noel', 'niff', 'minion',
  'gnome', 'ill', 'ogle', 'info', 'igloo', 'fife', 'milk', 'loo', 'en', 'high',
  'f', 'kook', 'miff', 'hele', 'hmi', 'longing', 'kink', 'n', 'fee', 'mm',
  'hole', 'hellene', 'mien', 'moo', 'homing', 'jiggle', 'inkling', 'll', 'off', 'goof',
  'lilo', 'ohm', 'melee', 'imf', 'hh', 'milfoil', 'kl', 'megohm', 'molehill', 'gel',
  'kennel', 'ml', 'noon', 'mf', 'inn', 'felon', 'ghee', 'helm', 'keel', 'memo',
  'nne', 'jinnee', 'on', 'hemline', 'nine', 'joie', 'glen', 'of', 'niggle', 'oil',
  'nom', 'mill', 'nominee', 'fling', 'hell', 'lego', 'gemini', 'finn', 'eh', 'fie',
  'onion', 'lemon', 'li', 'life', 'flog', 'jink', 'joggle', 'ofghijklmno', 'ofghijklmni', 'ofghijklmok'
]



def heapify(root, size):
  lc = root * 2 + 1
  if lc >= size: return
  child = lc
  rc = root * 2 + 2
  if rc < size:
    if array[rc] > array[lc]:
      child = rc

  if array[root] < array[child]:
    array[root], array[child] = array[child], array[root]
    heapify(child, size)



def main():
  count = len(array)

  last_parent_index = count // 2 - 1
  for n in range(last_parent_index, -1, -1):
      heapify(n, count)

  last_sort_index = count - 1
  while last_sort_index > 0:
    array[0], array[last_sort_index] = array[last_sort_index], array[0]
    heapify(0, last_sort_index)
    last_sort_index -= 1
  print(array)

array = words
main()





