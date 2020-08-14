# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:33:31 2020

@author: behrouz
"""


def should_hit(player_total, dealer_card_val, player_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay. player_aces is the number of aces the player has.
    """
    if dealer_card_val in ["K", "Q", "J"]:
        dealer_card_val = 10
    if dealer_card_val == "A":
        dealer_card_val == 11
    
    # rows from 1 to 16, columns from 2 to A
    Hard = [[1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1], 
            [1,2,2,2,2,1,1,1,1,1],
            [2,2,2,2,2,2,2,2,1,1],
            [2,2,2,2,2,2,2,2,2,2],
            [1,1,0,0,0,1,1,1,1,1],
            [0,0,0,0,0,1,1,1,1,1],
            [0,0,0,0,0,0,0,1,1,1],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]
            
    # rows from 11 to 20, columns from 2 to A
    Soft = [[1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1],        
            [1,1,1,2,2,1,1,1,1,1],
            [1,1,1,2,2,1,1,1,1,1],
            [1,1,2,2,2,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,1,1,1,1,1],
            [0,0,0,0,0,0,0,0,1,1],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]
    if player_aces == 0:
        if player_total <= 16:
            if Hard[player_total - 1][dealer_card_val - 2] in [1,2]:
                return True
    else:
        if player_total <= 20:
            if Soft[player_total - 11][dealer_card_val - 2] in [1,2]:
                return True
    return False    
    
    