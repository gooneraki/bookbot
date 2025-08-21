def get_num_words(raw_contents):
    return len(raw_contents.split())

def get_char_counter(raw_contents):
    result = {}
    for char in raw_contents:
        lower_char = char.lower()

        if lower_char not in result:
            result[lower_char] = 0
        result[lower_char] += 1
    return result

def get_sorted_dictionaries(counter_obj):
    
    counter_list = [{'char':key, "num":counter_obj[key]} for key in counter_obj]
    
    
    def sort_on(items):
        return items["num"]

    counter_list.sort(reverse=True, key=sort_on)
    return counter_list