class NimGame(object):
    def __init__(self, piles):
        self.piles = piles

    def is_game_over(self):
        return all(pile == 0 for pile in self.piles)

    def make_move(self, pile_index, stones):
        if pile_index < 0 or pile_index >= len(self.piles):
            raise ValueError("Invalid pile index.")
        if stones <= 0 or stones > self.piles[pile_index]:
            raise ValueError("Invalid number of stones to remove.")
        self.piles[pile_index] -= stones

    def get_piles(self):
        return self.piles
    def can_win(self):
        """
        Determines if the current player can win the Nim game given the current state of piles.
        :rtype: bool
        """
        xor_sum = 0
        for pile in self.piles:
            xor_sum ^= pile
        return xor_sum != 0
    def optimal_move(self):
        """
        Determines the optimal move for the current player to maximize their chances of winning.
        :rtype: tuple
        """
        xor_sum = 0
        for pile in self.piles:
            xor_sum ^= pile

        if xor_sum == 0:
            return None  # No winning move available

        for i, pile in enumerate(self.piles):
            target_pile = pile ^ xor_sum
            if target_pile < pile:
                stones_to_remove = pile - target_pile
                return (i, stones_to_remove)

        return None  # Should not reach here if can_win() is True
    def play_game(self):
        """
        Simulates a game of Nim between two players, where the current player uses the optimal strategy.
        :rtype: str
        """
        current_player = 1
        while not self.is_game_over():
            if self.can_win():
                move = self.optimal_move()
                if move:
                    pile_index, stones = move
                    self.make_move(pile_index, stones)
                    print(f"Player {current_player} removes {stones} stones from pile {pile_index}.")
            else:
                # If the current player cannot win, they can make any valid move (for simplicity, remove 1 stone from the first non-empty pile)
                for i, pile in enumerate(self.piles):
                    if pile > 0:
                        self.make_move(i, 1)
                        print(f"Player {current_player} removes 1 stone from pile {i}.")
                        break

            current_player = 2 if current_player == 1 else 1

        winner = 2 if current_player == 1 else 1
        print(f"Player {winner} wins!")
        return f"Player {winner} wins!"
    def reset_game(self, new_piles):
        """
        Resets the game with a new configuration of piles.
        :type new_piles: List[int]
        """
        self.piles = new_piles
    
    def get_current_state(self):
        """
        Returns the current state of the game, including the piles and whose turn it is.
        :rtype: dict
        """
        return {
            "piles": self.piles,
            "current_player": 1 if self.can_win() else 2
        }
    def get_winner(self):
        """
        Determines the winner of the game based on the current state of piles.
        :rtype: int
        """
        if self.is_game_over():
            return 2 if self.can_win() else 1
        return None  # Game is not over yet
    def get_possible_moves(self):
        """
        Returns a list of all possible moves for the current player.
        :rtype: List[tuple]
        """
        possible_moves = []
        for i, pile in enumerate(self.piles):
            for stones in range(1, pile + 1):
                possible_moves.append((i, stones))
        return possible_moves
    def get_game_summary(self):
        """
        Returns a summary of the game, including the current state and possible moves.
        :rtype: dict
        """
        return {
            "current_state": self.get_current_state(),
            "possible_moves": self.get_possible_moves()
        }
    def get_nim_sum(self):
        """
        Calculates the Nim-sum of the current piles.
        :rtype: int
        """
        nim_sum = 0
        for pile in self.piles:
            nim_sum ^= pile
        return nim_sum
    def is_winning_position(self):
        """
        Determines if the current position is a winning position for the current player.
        :rtype: bool
        """
        return self.get_nim_sum() != 0
    def get_losing_moves(self):
        """
        Returns a list of moves that would lead to a losing position for the current player.
        :rtype: List[tuple]
        """
        losing_moves = []
        for i, pile in enumerate(self.piles):
            for stones in range(1, pile + 1):
                # Simulate the move
                self.make_move(i, stones)
                if not self.is_winning_position():
                    losing_moves.append((i, stones))
                # Undo the move
                self.piles[i] += stones
        return losing_moves
    def get_winning_moves(self):
        """
        Returns a list of moves that would lead to a winning position for the current player.
        :rtype: List[tuple]
        """
        winning_moves = []
        for i, pile in enumerate(self.piles):
            for stones in range(1, pile + 1):
                # Simulate the move
                self.make_move(i, stones)
                if self.is_winning_position():
                    winning_moves.append((i, stones))
                # Undo the move
                self.piles[i] += stones
        return winning_moves
    def get_optimal_strategy(self):
        """
        Returns the optimal strategy for the current player, which includes the best move and the resulting state.
        :rtype: dict
        """
        optimal_move = self.optimal_move()
        if optimal_move:
            pile_index, stones = optimal_move
            # Simulate the move
            self.make_move(pile_index, stones)
            resulting_state = self.get_current_state()
            # Undo the move
            self.piles[pile_index] += stones
            return {
                "optimal_move": optimal_move,
                "resulting_state": resulting_state
            }
        return None  # No optimal move available
    def get_game_history(self):
        """
        Returns the history of moves made in the game.
        :rtype: List[tuple]
        """
        # This method would require tracking moves made during the game, which is not implemented in the current class.
        # For now, we can return an empty list or raise a NotImplementedError.
        raise NotImplementedError("Game history tracking is not implemented.")
    def reset_game_history(self):
        """
        Resets the history of moves made in the game.
        """
        # This method would require tracking moves made during the game, which is not implemented in the current class.
        # For now, we can raise a NotImplementedError.
        raise NotImplementedError("Game history tracking is not implemented.")
    def get_game_statistics(self):
        """
        Returns statistics about the game, such as the number of moves made and the number of winning/losing positions encountered.
        :rtype: dict
        """
        # This method would require tracking moves and positions during the game, which is not implemented in the current class.
        # For now, we can return an empty dictionary or raise a NotImplementedError.
        raise NotImplementedError("Game statistics tracking is not implemented.")
    def get_game_state_representation(self):
        """
        Returns a string representation of the current game state, including the piles and whose turn it is.
        :rtype: str
        """
        state = self.get_current_state()
        return f"Piles: {state['piles']}, Current Player: {state['current_player']}"    
    def get_game_state_visualization(self):
        """
        Returns a visual representation of the current game state, which can be useful for debugging or displaying the game.
        :rtype: str
        """
        visualization = ""
        for i, pile in enumerate(self.piles):
            visualization += f"Pile {i}: {'|' * pile} ({pile} stones)\n"
        return visualization.strip()
    def get_game_state_summary(self):
        """
            Returns a summary of the current game state, including the piles, whose turn it is, and possible moves.
            :rtype: dict
        """
        return {
                "current_state": self.get_current_state(),
                "possible_moves": self.get_possible_moves(),
                "nim_sum": self.get_nim_sum(),
                "is_winning_position": self.is_winning_position()
            }    
    def get_game_state_details(self):
        """
        Returns detailed information about the current game state, including the piles, whose turn it is, possible moves, and optimal strategy.
        :rtype: dict
        """
        return {
            "current_state": self.get_current_state(),
            "possible_moves": self.get_possible_moves(),
            "nim_sum": self.get_nim_sum(),
            "is_winning_position": self.is_winning_position(),
            "optimal_strategy": self.get_optimal_strategy()
        }
    def get_game_state_analysis(self):
        """
        Returns an analysis of the current game state, including the piles, whose turn it is, possible moves, optimal strategy, and winning/losing moves.
        :rtype: dict
        """
        return {
            "current_state": self.get_current_state(),
            "possible_moves": self.get_possible_moves(),
            "nim_sum": self.get_nim_sum(),
            "is_winning_position": self.is_winning_position(),
            "optimal_strategy": self.get_optimal_strategy(),
            "winning_moves": self.get_winning_moves(),
            "losing_moves": self.get_losing_moves()
        }
    def get_game_state_summary_with_analysis(self):
        """
        Returns a comprehensive summary of the current game state, including the piles, whose turn it is, possible moves, optimal strategy, winning/losing moves, and game statistics.
        :rtype: dict
        """
        return {
            "current_state": self.get_current_state(),
            "possible_moves": self.get_possible_moves(),
            "nim_sum": self.get_nim_sum(),
            "is_winning_position": self.is_winning_position(),
            "optimal_strategy": self.get_optimal_strategy(),
            "winning_moves": self.get_winning_moves(),
            "losing_moves": self.get_losing_moves(),
            "game_statistics": self.get_game_statistics()  # This will raise NotImplementedError
        }
    def get_game_state_summary_with_visualization(self):
        """
        Returns a comprehensive summary of the current game state, including the piles, whose turn it is, possible moves, optimal strategy, winning/losing moves, game statistics, and a visual representation of the game state.
        :rtype: dict
        """
        return {
            "current_state": self.get_current_state(),
            "possible_moves": self.get_possible_moves(),
            "nim_sum": self.get_nim_sum(),
            "is_winning_position": self.is_winning_position(),
            "optimal_strategy": self.get_optimal_strategy(),
            "winning_moves": self.get_winning_moves(),
            "losing_moves": self.get_losing_moves(),
            "game_statistics": self.get_game_statistics(),  # This will raise NotImplementedError
            "game_visualization": self.get_game_state_visualization()
        }
                