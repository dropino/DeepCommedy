CLEAN_SYLLABLES = "syllComedy.txt"
LINE_LENGTH = 100


vocab = {}
special_tokens = ["[START]", "[END]", "[PAD]", "[UNK]"]
charachters = ['|', ' ', 'e', 'a', 'i', 'o', 'n', 'r', 'l', 't', 's', 'c', 'd', , 'u', 'm', 'p', 'v', '’', 'g', 'h', 'f', 'q', 'b', 'z', 'ì', 'ù', 'ò', 'è', 'é', 'à', '?', '!', 'ó', '‘', 'x', 'j', 'y']

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
    idSequence.append(vocab.get("[END]"))
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