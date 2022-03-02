#!/bin/sh

corenlp -annotators tokenize,ssplit,pos,lemma,ner,parse,depparse,coref,sentiment -file input.txt
less input.txt.out






