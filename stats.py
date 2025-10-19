def get_num_words(contents):
    splited_contents = contents.split()
    return len(splited_contents)

def get_num_characters(contents):
   characters_frequency = dict()
   for char in contents:
      lowered_char = char.lower()
      characters_frequency[lowered_char] = characters_frequency.get(lowered_char, 0) + 1
   return characters_frequency

def sort_characters_by_count(char_dict):
    sorted_list = []
    
    # Helper function for sorting
    def sort_on(dict):
        return dict["num"]
    
    # Create list of dictionaries for alphabetical characters only
    for char in char_dict:
        if char.isalpha():
            sorted_list.append({"char": char, "num": char_dict[char]})
    
    # Sort from greatest to least by count
    sorted_list.sort(reverse=True, key=sort_on)
    
    return sorted_list

