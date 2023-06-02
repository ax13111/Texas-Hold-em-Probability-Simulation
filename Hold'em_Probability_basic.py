#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:09:07 2023

@author: sunyenpeng
"""

import random
import itertools

def poker_deck():
    color=["♠", "♣", "♥", "♦"]
    number=[i+1 for i in range(13)]
    poker=[]
    for i in color:
        for j in number:
            poker.append((i,j))
    return poker

deck=poker_deck()


#Check combination:
def has_straight_flush(cards): #Note, the cards input should be in tuple!
    
    cards_by_suit = {}
    for card in cards:
        suit, rank = card
        if suit not in cards_by_suit:
            cards_by_suit[suit] = []
        cards_by_suit[suit].append(rank)

    for suit in cards_by_suit:
        ranks = sorted(cards_by_suit[suit])
        if ranks == [1, 10, 11, 12, 13]:
            return True
        for i in range(len(ranks) - 4):
            if ranks[i:i+5] == list(range(ranks[i], ranks[i]+5)):
                return True
    return False

def has_flush(cards):
    color=[]
    for c in cards:
        color.append(c[0])
    if color.count(color[0])==5:
        return True
    return False

def has_fourofakind(cards):
    number=[]
    check=[]
    for c in cards:
        number.append(c[-1])
    for n in number:
        check.append(number.count(n))
    if check.count(4)==4:
        return True
    return False

def has_fullhouse(cards):
    number=[]
    for c in cards:
        number.append(c[-1])
    if number.count(number[0])==2 and number.count(number[-1])==3:
        return True
    elif number.count(number[0])==3 and number.count(number[-1])==2:
        return True
    
    return False

def has_straight(cards):
    number=[]
    for n in cards:
        number.append(n[-1])
    number.sort()
    for i in range(len(number) - 4):
        if number[i]+1 in number and number[i]+2 in number and number[i]+3 in number and number[i]+4 in number:
            return True
        elif 1 in number and 10 in number and 11 in number and 12 in number and 13 in number:
            return True
        return False
    
def has_set(cards):
    number=[]
    for c in cards:
        number.append(c[-1])
    for n in number:
        if number.count(n)==3:
            return True
    return False

def has_twopair(cards):
    number=[]
    check=[]
    for c in cards:
        number.append(c[-1])
    for n in number:
        check.append(number.count(n)) #I count the frequency of numbers appear in the combination and create a list named _check_ to store the frequency 
        
    if check.count(1)==3 and check.count(2)==4: #Check the frequency. Logically, since we consider public cards and hands(5+2=7cards), so if we have two pairs then the frequency will be 1,1,1,2,2,2,2
        return True
    return False

def has_pair(cards):
    number=[]
    check=[]
    for c in cards:
        number.append(c[-1])
        
    for n in number:
        check.append(number.count(n))
    
    if check.count(2)==2:
        return True
    return False





sf=0 #Number of straight flush
fok=0 #Number of four of a kind
fh=0 #Number of fullhouse
flush=0 #Number of flush
straight=0 #Number of straight
st=0 #Number of set
tp=0 #Number of two pairs
p=0 #Number of one pair
h=0 #Number of high cards
        
if __name__=="__main__":
    print("Enter the numer of trials you want to do:")
    N=int(input("> "))
    for i in range(N):
        random.shuffle(deck)
        hands=deck[0:7]
        
        if has_straight_flush(hands):
            sf+=1
        elif has_fourofakind(hands):
            fok+=1
        elif has_fullhouse(hands):
            fh+=1
        elif has_flush(hands):
            flush+=1
        elif has_straight(hands):
            straight+=1
        elif has_set(hands):
            st+=1
        elif has_twopair(hands):
            tp+=1
        elif has_pair(hands):
            p+=1
        else:
            h+=1
    print("Out of",N,"of trials, You have:\n")
    print(sf,"times of straight flush, with a probability of:",sf/N,"\n")
    print(fok,"times of four of a kind, with a probability of:",fok/N,"\n")
    print(fh,"times of full house, with a probability of:",fh/N,"\n")
    print(flush,"times of flush, with a probability of:",flush/N,"\n")
    print(straight,"times of straight, with a probability of:",straight/N,"\n")
    print(st,"times of set, with a probability of:",st/N,"\n")
    print(tp,"times of two pairs, with a probability of:",tp/N,"\n")
    print(p,"times of a pair, with a probability of:",p/N,"\n")
    print(h,"times of high cards, with a probability of:",h/N,"\n")
        
    



























































