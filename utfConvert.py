"""
The purpose of this file is to take a .txt file as input, and change the encoding from uft-16 to uft-8.
This is useful, as the trainlist.txt, vallist.txt were originally defaulted to uft-16 le encoding.

"""
import sys
import os

if __name__ == "__main__":
    inputF = sys.argv[1]
    outputF = sys.argv[2]

    if not os.path.exists(outputF):
        with open(outputF, "w") as file:
            file.write('')

    print(f"File {outputF} initiated.")

    os.chmod(inputF, 666)
    os.chmod(outputF, 666)

    with open(inputF, "r", encoding='utf-16') as sourceText, \
    open(outputF, "w", encoding='utf-8') as destText:
            
            for line in sourceText:
                destText.write(line)
    
    print(f"Encoding complete. File {outputF} now contains UTF-8 version of file {inputF}.")


