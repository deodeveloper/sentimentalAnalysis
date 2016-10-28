from nltk import pos_tag
from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
#cd into the current directory and then use,  python -m nltk.downloader
nltk.data.path.append('./nltk_data/')
stemmer = PorterStemmer()
lemmatiser = WordNetLemmatizer()

def lemmatize( text ):
   return lemmatiser.lemmatize(text, pos="v");
