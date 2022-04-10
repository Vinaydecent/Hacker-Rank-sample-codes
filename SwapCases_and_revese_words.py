def reverse_words_order_and_swap_cases(sentence):
     Output = '';
    for char in s:
        if(char.isupper()==True):
            Output += (char.lower());
        elif(char.islower()==True):
            Output += (char.upper());
        else:
            Output += char;
    word_list = Output.split()
    reversed_list = word_list[:: -1]
    reversed_sentence = " ".join(reversed_list)
    return reversed_sentence
   


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = raw_input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
