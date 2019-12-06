import sys
import os
import utils

def convert(file):
  print(file)
  filename, _ = os.path.splitext(file)

  f = open(file, 'rb')
  d = open(filename + '.txt', 'w', encoding='utf-8')

  meta = []

  count = utils.readInt(f)
  for _ in range(count):
    meta.append([utils.readInt(f), utils.readInt(f)])

  for i in range(count):
    d.write(utils.read(f, meta[i][0], meta[i][1]).decode('utf-8').replace('\n', '\\n'))
    d.write('\n')
  
  d.close()
  f.close()


for i in range(1, len(sys.argv)):
  convert(sys.argv[i])