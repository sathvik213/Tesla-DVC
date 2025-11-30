from pathlib import Path
print(type(Path('spam','bacon','eggs')))
print(str(Path('spam')/Path('ham','clam')))


print(Path.cwd())# shows current working directory 
# os.chdir('lkdj') # changes the current directory to passed string value 

# os.makedirs('./home') # makes new directory
# alternative approach
# Path('./home').mkdir()

# print(Path('./home').is_absolute())

# apt=Path(r"C:\Users\sathvik\Desktop\code\Tesla-DVC\requirements.txt")

# for i in range(len(apt.parents)):
#   print(apt.parents[i])

import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'ooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))

import shutil
# from pathlib import Path
p = Path.cwd()
shutil.copy(p / 'spam.txt', p / 'some_folder')