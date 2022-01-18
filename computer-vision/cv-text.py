import easyocr


def text_recog(pathtofile, texttofile = "result.txt"):
    reader = easyocr.Reader(['ru','en']) # this needs to run only once to load the model into memory
    result = reader.readtext(pathtofile, detail = 0, paragraph=True)
    
    with open(texttofile, "w") as file:
        for line in result:
            file.write(f"{line}\n\n")

    return f"Result wrote in file {texttofile}"

def main():
    filepath = input("File path: ")
    print(text_recog(pathtofile=filepath))

if __name__ == "__main__":
    main()