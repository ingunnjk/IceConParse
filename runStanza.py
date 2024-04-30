import sys
import stanza
from nltk.tree import *

input = sys.argv[1]
txt_output = sys.argv[2]
psd_output = sys.argv[3]

with open(input, encoding='utf-8') as infile:
    text = infile.read()

# Stanza Neural Parser, using the model trained on IcePaHC
nlp = stanza.Pipeline(lang='is', processors='tokenize, pos, constituency', constituency_model_path='./stanza_is/is_icepahc_transformer_finetuned_constituency.pt', tokenize_pretokenized=True)
doc = nlp(text)

# Replace * with - and remove ROOT
with open(psd_output, 'w', encoding='utf-8') as psdout:
    with open(txt_output, 'w', encoding='utf-8') as txtout:
        for sentence in doc.sentences:
            sentence = str(sentence.constituency).replace('*', '-')
            sentence = sentence.replace('ROOT ', '')
            # One tree in each line
            txtout.write(sentence)
            txtout.write('\n')
            # Format the sentences with NLTK
            tree = Tree.fromstring(sentence)
            psdout.write(str(tree))
            psdout.write('\n\n')