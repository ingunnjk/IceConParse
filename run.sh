# Parse plain text files using the Stanza neural parser and a model trained on IcePaHC
#
# Usage: ./run.sh inputfile.txt outputfile.txt outputfile.psd
#
# inputfile.txt:    plain text input
# outputfile.txt:   parsed .txt file (one tree/sentence in each line, no extra formatting)   
# outputfile.psd:   parsed .psd file formatted like IcePaHC
#
# Dependencies:
# python3
# stanza (pip3 install stanza)
# detectormorse (pip3 install detectormorse)
# tokenizer (pip3 install tokenizer)
# numpy (pip3 install numpy) 

input=$1
txtOutput=$2
psdOutput=$3
tempfile=${input%.txt}.temp
temptxt=${txtOutput%.txt}.temp
temppsd=${tempfile}.psd

# Use Greynir's tokenizer for punctuation splitting:
echo 'Splitting sentences based on punctuation.'
tokenize $1 > $tempfile

# Use a matrix clause splitter developed by Anton Karl Ingason based on Detector Morse
echo 'Splitting matrix clauses.'
python3 ./splitter/splitter.py ./splitter/iceconj.gz $tempfile > $tempfile.out

# The matrix clause splitter seems to output all sentences twice, lets remove the second (duplicate) half
linecount=$(wc -l < $tempfile.out)
half=$((linecount / 2))
head -n $half $tempfile.out > $tempfile
rm -f $tempfile.out

# Run Stanza neural parser and postprocess
echo 'Running the Stanza neural parser (this may take a while).'
python3 ./runStanza.py $tempfile $temptxt $temppsd
rm -f $tempfile

# Save the output files
echo 'Saving output files.'
mv -f $temptxt $txtOutput
mv -f $temppsd $psdOutput

echo 'Done!'

