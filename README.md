# Íslenskur taugaþáttari fyrir liðgerð / Icelandic Constituency Parser
Íslenskur taugaþáttari, sem er þjálfaður á sögulega íslenska trjábankanum (IcePaHC), tilheyrir máltæknipakkanum Stanza og unnið er að því að gera hann aðgengilegan í gegnum pípuna þeirra (https://github.com/stanfordnlp/stanza). Hér verða sýnd notkunardæmi fyrir þáttarann.

Til að keyra þáttarann þarf að hafa Python 3.6 eða nýrri. Einnig þarf að sækja nokkra pakka til viðbótar en þeir eru taldir upp í skránni run.sh.

Hægt er að nálgast íslenska líkanið [hér](https://drive.google.com/drive/folders/14PwqLbhF66vTnJcE8ZtSAjNbCFkH69mj?usp=sharing). 

Ef líkanið er vistað í möppunni /stanza_is er hægt að keyra ./run.sh til að þátta texta. Keyrið eftirfarandi skipun:

```
./run.sh inputfile.txt txtOutputfile.txt psdOutputfile.psd
```
- inputfile.txt er inntakstextinn sem á að þátta.
- txtOutputfile.txt er úttakið úr þáttuninni þar sem hver lína inniheldur eina þáttaða setningu.
- psdOutputfile.psd er úttakið úr þáttuninni þar sem trén eru á svipuðu sniði og í IcePaHC-trjábankanum.



Einnig er hægt að nota líkanið á eftirfarandi hátt með Stanza pípunni:

```ruby
import stanza

nlp = stanza.Pipeline(lang='is', processors='tokenize, pos, constituency', constituency_model_path='/stanza_is/is_icepahc_transformer_finetuned_constituency.pt')
doc = nlp('Þetta er stutt setning.')
for sentence in doc.sentences:
    print(sentence.constituency)
```

Úttakið er þá:

```
(ROOT (IP*MAT (NP*SBJ (D-N Þetta)) (BEPI er) (NP*PRD (ADJ-N stutt) (N-N setning)) (. .)))
```
