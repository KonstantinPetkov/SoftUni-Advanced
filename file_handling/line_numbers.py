from string import punctuation

with open("files/text.txt", "r") as text_file:
    text = text_file.readlines()

with open("files/output.txt", "w") as output_file:

    for index in range(len(text)):
        row = text[index]

        letters, marks = 0, 0

        for symbol in row:
            if symbol.isalpha():
                letters += 1
            elif symbol in punctuation:
                marks += 1

        output_file.write(f"Line {index+1}: {''.join(row[:-1])} ({letters})({marks})\n")