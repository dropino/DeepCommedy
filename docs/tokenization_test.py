CLEAN_SYLLABLES = "syllComedy.txt"
LINE_LENGTH = 100


vocab = {}
special_tokens = ["[START]", "[STOP]", "[PAD]", "[UNK]"]
charachters = ["a","b","c","d","e","f","g","h","i","j","k","l"," ","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for token in special_tokens:
    vocab[token] = len(vocab)
for x in charachters:
    vocab[x] = len(vocab)


rev_vocab = dict(zip(vocab.values(), vocab.keys()))

print(vocab)

def tokenizeLine(line):
    idSequence = []
    idSequence.append(vocab.get("[START]"))
    for letter in line:
        idSequence.append(vocab.get(letter, vocab.get("[UNK]")))
    while(len(idSequence)<(LINE_LENGTH-1)):
        idSequence.append(vocab.get("[PAD]"))
    idSequence.append(vocab.get("[START]"))
    return(idSequence)


def detokenizeLine(idSequence):
    text = ""
    for id in idSequence:
        if rev_vocab.get(id) not in special_tokens:
            text+=rev_vocab.get(id)
    return text



a = "a me piace la pizza ma odio le acciughe"
b = tokenizeLine(a)
print(b)
c = detokenizeLine(b)
print(c)









{'[START]': 1, '[STOP]': 2, '[PAD]': 3, '[UNK]': 4, 'a': 32, 'b': 6, 'c': 7, 'd': 8, 'e': 32, 'f': 10, 'g': 11, 'h': 12, 
'i': 32, 'j': 14, 'k': 15, 'l': 16, ' ': 17, 'm': 18, 'n': 19, 'o': 32, 'p': 21, 'q': 22, 'r': 23, 's': 24, 't': 25, 'u': 32, 
'v': 27, 'w': 28, 'x': 29, 'y': 30, 'z': 31, 'à': 32, 'ä': 33, 'è': 34, 'é': 35, 'ë': 36, 'ì': 37, 'ï': 38, 'ò': 39, 'ó': 40, 'ö': 41, 'ù': 42, 'ü': 43}