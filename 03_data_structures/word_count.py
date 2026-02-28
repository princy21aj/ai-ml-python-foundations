#counts how many times each word appears

def wcount(value):
    value = value.split()
    count={}
    for num in value:
        if num not in count:
            count[num] = 1
        else:
            count[num]=count[num]+1
    return count
            
        
  

sentence = input("Write the sentence : ")
word = wcount(sentence)

print(f"{word}")