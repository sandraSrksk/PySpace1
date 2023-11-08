#def capitalizing_this():
#    return string.upper()

#string = input("Give a string")
#print(capitalizing_this())

def capitalizing_this(input_string):
    words = input_string.split()
    result = []
    
    for word in words:
        if "'" in word:
            # Handle words with apostrophes (e.g., "it's")
            parts = word.split("'")
            capitalized_parts = [part.capitalize() for part in parts]
            result.append("'".join(capitalized_parts))
        else:
            result.append(word.capitalize())
    
    return ' '.join(result)

# Example usage:
input_string1 = input("Give an input: ")


output1 = capitalizing_this(input_string1)


print(output1)  

