# -*- coding: utf-8 -*-
from nlp_rake import Rake


rake = Rake( max_words=2, min_chars=3, min_freq=1)
text = "were forest fires in california started last summer by left-wing activists? no, but the rumor had a big impact on social media. now researchers will take a closer look at how conspiracy theories about forest fires are spread, and what can be done to stop false information."
text2 = "Cod fishing in the Baltic Sea is stopped in a new EU decision"
text3="contributions from centre researchers the ocean panel has worked with an advisory network comprised of more than 135 private sector, ngo and intergovernmental organizations across 35 countries to advance action through their own institutions and networks. centre researchers have been deeply involved in a series of commissioned blue papers exploring pressing challenges at the nexus of the ocean and the economy: robert blasiak was the lead author on a blue paper offering guidelines for sustainable and equitable use of the ocean genome beatrice crona co-authored a blue paper on how the next generation of financing mechanisms can help support the ocean transition."
keywords = rake.apply(text2)
for tup in keywords:
    if tup[1] > 1:
        print(tup)