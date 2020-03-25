#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def naive_2mm(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        mismach = 0
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                mismach += 1
        if mismach<3:
            occurrences.append(i)  # all chars matched; record
    return occurrences

