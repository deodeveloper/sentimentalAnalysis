import math
import sys
import nltk
import settings
import dataset

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
    db = dataset.connect(settings.CONNECTION_STRING)
    result = db.query('SELECT id, text FROM tweet')
    table = db[settings.TABLE_NAME]
    for row in result:
        text = row['text']
        score = sentiment(text)
        table.update(dict(id=row['id'], afinnScore=score), ['id'])