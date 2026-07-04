'''
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt . Store at least three 
names of cats in the first file and three names of dogs in the second file . Write 
a program that tries to read these files and print the contents of the file to the 
screen . Wrap your code in a try-except block to catch the FileNotFound error, 
and print a friendly message if a file is missing . Move one of the files to a dif
ferent location on your system, and make sure the code in the except block 
executes properly .
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail 
silently if either file is missing 
'''
def ReadFile(file_path):

    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
       # print(f"File not found: {file_path}")
        pass
        return None
    except Exception as e:
        #print(f"An error occurred while reading the file: {e}")
        pass
        return None