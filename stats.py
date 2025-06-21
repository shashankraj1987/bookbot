import os

def get_book_text(file_loc: str) -> str:
    words_lower = []
    if os.path.exists(file_loc):
        pass
    else:
        raise FileNotFoundError

    with open(file_loc) as f:
        file_contents = f.read()
    
    for line in file_contents.split("\n"):
        for word in line.split(" "):
            if len(word.strip()) > 0:
                words_lower.append(word.lower())
    return words_lower


def get_num_words(file_contents: list[str]) -> str:
    return len(file_contents)


def word_occurance_count(text_list: list[str]) -> dict[str: int]:
    val_dict = {}
    for word in text_list:
        for letter in word:
            if letter in val_dict.keys():
                val_dict[letter] += 1
            else:
                val_dict[letter] = 1
    
    return val_dict


def sorted_dict(word_count_dict: dict[str, int]) -> dict[str, int]:
    return dict(sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True))