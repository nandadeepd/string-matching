from util import FileManipulation


FILE_PATH = "./utils/bunch-of-urls.txt"
fm = FileManipulation(FILE_PATH)
print(fm.read_file())

TEXT = fm.read_file()
PATTERN = "jpg"