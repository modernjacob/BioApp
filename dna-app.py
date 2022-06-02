# BioInformatics // DNA Nucleatide Sequence
# Streamlit Project 
# Terminal // cd Desktop/Code/Projects/BioApp // streamlit run dna-app.py

from operator import index
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

st.write("""
# DNA Nucleotide Count 

This App will count the Nucleotide composition of query DNA

***
""")

st.header('Enter DNA Sequence')

sequence_input = '>DNA Query\n'

#sequence 
#sequence = st.sidebar.text_area("Sequence Input", sequence_input, height = 250)
sequence = st.text_area("Sequence Input", sequence_input, height = 250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.subheader('Neucleotide Sequence:')

st.write("""
***
""")

#Prints the input
st.header('Input (DNA Query)')
sequence

# Neucleotide count
st.header('Output: (DNA Neucleotide Count)')

# Print Dictionary 
st.subheader('Dictionary')
def DNA_neucleotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
    ])
    return d

X = DNA_neucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

# Print Text
st.subheader('Count')
st.write(str(X['A']) + ': Adenine')
st.write(str(X['T']) + ': Thymine')
st.write(str(X['G']) + ': Guanine')
st.write(str(X['C']) + ': Cytosine')

# Dataframe
st.subheader('Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

# Bar Chart
st.subheader('Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(
    width=alt.Step(80)
)
st.write(p)
