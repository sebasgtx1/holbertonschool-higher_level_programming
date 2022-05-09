#!/usr/bin/python3
def multiple_returns(sentence):
    len_sentence = len(sentence)
    if (len_sentence == 0):
        return (0, None)
    else:
        return (len_sentence, sentence[0])
