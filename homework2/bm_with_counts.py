#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def boyer_moore_with_counts(p, p_bm,t):
    i = 0
    occurences=[]
    num_alignments=0
    num_character_comparisons=0
    while i < len(t)-len(p) + 1:
        shift = 1
        mismatched = False
        num_alignments+=1
        for j in range(len(p)-1,-1,-1):
            num_character_comparisons+=1
            if not p[j]==t[i+j]:
                skip_bc = p_bm.bad_character_rule(j, t[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        if not mismatched:
            occurences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i+=shift
    return occurences,num_alignments,num_character_comparisons

