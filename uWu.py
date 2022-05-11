import random
def generateuwu(sentence):  # The sentence-converter starts here
    word_list = sentence.split()
    for number, word in enumerate(word_list):
        if word == "my":
            word_list[number] = "mwy"
        elif word == "to":
            word_list[number] = "tuwu"
        elif word == "had":
            word_list[number] = "hawd"
        elif word == "you":
            word_list[number] = "yuw"
        elif word == "go":
            word_list[number] = "gow"
        elif word == "and":
            word_list[number] = "awnd"
        elif word == "have":
            word_list[number] = "haw"
        elif word == "love":
            word_list[number] = "wuv"
        elif word == "bye":
            word_list[number] = "bai"
        elif word == "disease":
            word_list[number] = "pathOwOgen"
        elif word == "fuck":
            word_list[number] = "fluff"
        elif word == "hell":
            word_list[number] = "hecc"
        elif word == "hi":
            word_list[number] = "hai"
        elif word == "sorry":
            word_list[number] = "sowwy"
        elif word == "the":
            word_list[number] = "teh"

          
        else:
            word = word.replace("ll", "w").replace("r", "w").replace("l", "w").replace("th", "d").replace("fu", "fwu").replace("no", "nyo").replace("na", "nya")
            word_list[number] = word

        if random.randrange(0, 11) == 1:
            word_list[number] = word[0] + "-" + word


    final = " ".join(word_list)

    return final

