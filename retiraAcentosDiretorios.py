from unicodedata import normalize
def remover_acentos(txt, codif='utf-8'):
    return normalize('NFKD', txt).encode('ASCII', 'ignore')

import os
rootdir = r'path'

for dirs in os.walk(rootdir): 
	str_dirs=str(dirs[0])
	try:
		os.rename(str_dirs, remover_acentos(str_dirs))
		print (remover_acentos(str_dirs))
	except WindowsError:
		continue

if __name__ == '__main__':
    from doctest import testmod
    testmod()
