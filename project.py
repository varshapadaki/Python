class Team:
    def __init__(self, name):
        self.name = name

class Match:
    def __init__(self, match_id, team1, team2, team1_score=None, team2_score=None):
        self.match_id = match_id
        self.team1 = team1
        self.team2 = team2
        self.team1_score = team1_score
        self.team2_score = team2_score
        self.winner = None

class Match_Result_Tracker:
    def __init__(self):
        self.matches = {}
        self.next_match_id = 1

    def create_match(self, team1, team2):
        match_id = self.next_match_id
        match = Match(match_id, team1, team2)
        self.matches[match_id] = match
        self.next_match_id += 1
        print(f"Match {match_id} created between {team1.name} and {team2.name}")

    def update_match_score(self, match_id, team1_score, team2_score):
        match = self.matches.get(match_id)
        if match:
            match.team1_score = team1_score
            match.team2_score = team2_score
            if team1_score > team2_score:
                match.winner = match.team1.name
            elif team2_score > team1_score:
                match.winner = match.team2.name
            else:
                match.winner = "Draw"
            print(f"Match {match_id} score updated")
        else:
            print(f"Match {match_id} not found")

    def delete_match(self, match_id):
        if match_id in self.matches:
            del self.matches[match_id]
            print(f"Match {match_id} deleted successfully")
        else:
            print(f"Match {match_id} not found")

    def display_match_details(self, match_id, filename):
        match = self.matches.get(match_id)
        if match:
            with open("match_results_display.txt", 'a') as file:
                file.write(f"Match ID: {match.match_id}\n")
                file.write(f"Team 1: {match.team1.name} (Score: {match.team1_score})\n")
                file.write(f"Team 2: {match.team2.name} (Score: {match.team2_score})\n")
                file.write(f"Winner: {match.winner}\n\n")
        else:
            print(f"Match {match_id} not found")

    def team_statistics(self, team_name):
        total_matches = 0
        total_wins = 0
        total_losses = 0
        total_draws = 0

        for match in self.matches.values():
            if match.team1.name == team_name:
                total_matches += 1
                if match.winner == team_name:
                    total_wins += 1
                elif match.winner == "Draw":
                    total_draws += 1
                else:
                    total_losses += 1
            elif match.team2.name == team_name:
                total_matches += 1
                if match.winner == team_name:
                    total_wins += 1
                elif match.winner == "Draw":
                    total_draws += 1
                else:
                    total_losses += 1

        return {
            "Total Matches Played": total_matches,
            "Total Wins": total_wins,
            "Total Losses": total_losses,
            "Total Draws": total_draws
        }

    def save_results(self, filename):
        with open("match_results.txt", 'w') as file:
            for match in self.matches.values():
                file.write(f"{match.match_id},{match.team1.name},{match.team2.name},{match.team1_score},{match.team2_score},{match.winner}\n")

    def load_results(self, filename):
        self.matches = {}
        with open("match_results.txt", 'r') as file:
            for line in file:
                match_data = line.strip().split(',')
                match_id, team1_name, team2_name, team1_score, team2_score, winner = match_data
                team1 = Team(team1_name)
                team2 = Team(team2_name)
                match = Match(int(match_id), team1, team2, int(team1_score), int(team2_score))
                match.winner = winner
                self.matches[int(match_id)] = match

# Example usage
if __name__ == "__main__":
    # Create Match_Result_Tracker instance
    tracker = Match_Result_Tracker()

    # Create teams
    team1 = Team("Mumbai Indians")
    team2 = Team("Chennai Super Kings")
    team3 = Team("Royal Challengers Bangalore")
    team4 = Team("Kolkata Knight Riders")
    team5 = Team("Delhi Capitals")
    team6 = Team("Gujarat Titans")

    # Schedule matches
    tracker.create_match(team1, team2)
    tracker.create_match(team3, team6)
    tracker.create_match(team1, team4)
    tracker.create_match(team5, team6)
    tracker.create_match(team1, team6)
    tracker.create_match(team2, team3)
    tracker.create_match(team4, team5)
    tracker.create_match(team3, team4)
    tracker.create_match(team2, team5)
    
    tracker.delete_match(3)
    
    # Update match scores
    tracker.update_match_score(1, 180, 170)
    tracker.update_match_score(2, 150, 150)
#     tracker.update_match_score(3, 206, 217)
    tracker.update_match_score(4, 166, 186)
    tracker.update_match_score(5, 127, 168)
    tracker.update_match_score(6, 175, 172)
    tracker.update_match_score(7, 257, 201)
    tracker.update_match_score(8, 188, 134)
    tracker.update_match_score(9, 238, 212)

    # Save match results to a file
    tracker.save_results("match_results.txt")

    # Display match details in a file
    for match_id in range(1, 10):
        tracker.display_match_details(match_id, "match_results_display.txt")
