"""
This module will tie together code from fetch_data.py and cc_markov.py.
"""

from markov_python.cc_markov import MarkovChain

import fetch_data

my_chain = MarkovChain()
my_chain.add_string(fetch_data.get_content('http://wiersze.juniora.pl/tuwim/tuwim_l01.html'))

# 3 years

my_text = my_chain.generate_text()

for word in my_text:
    print u"word: {}".format(word)
