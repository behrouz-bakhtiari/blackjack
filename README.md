# blackjack
Solution to Kaggle's blackjack challenge.
The game uses Monte Carlo simulation to figure out the win rate for the player. This is a slightly modified version of Blackjack. 
- The player is dealt two face-up cards. The dealer is dealt one face-up card.
- The player may ask to be dealt another card ('hit') as many times as they wish. If the sum of their cards exceeds 21, they lose the round immediately.
- The dealer then deals additional cards to himself until either:
    - The sum of the dealer's cards exceeds 21, in which case the player wins the round, or
    - The sum of the dealer's cards is greater than or equal to 17. If the player's total is greater than the dealer's, the player wins. Otherwise, the dealer wins (even in case of a tie).
    
When calculating the sum of cards, Jack, Queen, and King count for 10. Aces can count as 1 or 11. (When referring to a player's "total" above, we mean the largest total that can be made without exceeding 21. So A+8 = 19, A+8+8 = 17.)
