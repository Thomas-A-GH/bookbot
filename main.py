def main():
    path = 'books/frankenstein.txt'

    with open(path) as f:
        file_contents = f.read()
        
        produce_report(path,file_contents)
        

def string_to_int(text):
    lowered_string = text.lower()
    count_char = {}
    for char in lowered_string:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
    sorted_count = dict(sorted(count_char.items(), key=lambda x: int(x[1]), reverse=True))
    return sorted_count

def produce_report(path, file_contents):
    word_count = file_contents.split()
    char_count = string_to_int(file_contents)

    print(f"--- Begin report of {path} ---")
    print(f"{len(word_count)} words found in the document")

    for key in char_count:
        if key.isalpha() == True:
            print(f"The '{key}' character was found {char_count[key]} times")
        else:
            pass
    print("--- End report ---")

        
main()