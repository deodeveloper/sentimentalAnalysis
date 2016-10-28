import math
import sys
import nltk
nltk.data.path.append('./nltk_data/')

reload(sys)
sys.setdefaultencoding('utf-8')

filenameAFINN = 'AFINN/AFINN-111.txt'
afinn = dict(map(lambda (w, s): (w, int(s)), [
    ws.strip().split('\t') for ws in open(filenameAFINN)]))

def sentiment(text):
    words = nltk.word_tokenize(text.lower())
    sentiments = map(lambda word: afinn.get(word, 0), words)
    if sentiments:
        sentiment = float(sum(sentiments)) / math.sqrt(len(sentiments))
    else:
        sentiment = 0
    return sentiment


if __name__ == '__main__':
    # Single sentence example:
    text = "Finn is stupid and idiotic"
    print("%6.2f %s" % (sentiment(text), text))

    # No negation and booster words handled in this approach
    text = "But he is awesome. He is pretty too. I love him"
    print("%6.2f %s" % (sentiment(text), text))