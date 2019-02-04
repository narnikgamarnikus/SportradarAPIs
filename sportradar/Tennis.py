# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

from sportradar.api import API


class Tennis(API):

    def __init__(self, api_key, format_="json", language="en", timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, timeout, sleep_time)
        self.language = language
        self.prefix = f"tennis-t2/{language}/"

    def get_daily_results(self, year, month, day):
        """Provides match information and scoring, for all matches played on a given day"""
        path = "schedules/{year:4d}-{month:02d}-{day:02d}/results".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(self.prefix + path)

    def get_daily_schedule(self, year, month, day):
        """Provides the schedule for a given day"""
        path = "schedules/{year:4d}-{month:02d}-{day:02d}/schedule".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(self.prefix + path)

    def get_deleted_matches(self):
        """Provides deleted matches"""
        path = "schedules/deleted_matches"
        print(path)
        return self._make_request(self.prefix + path)

    def get_match_probabilities(self, match_id):
        """Provides match probabilities"""
        path = f"matches/{match_id}/probabilities"
        print(path)
        return self._make_request(self.prefix + path)

    def get_match_summary(self, match_id):
        """Provides match summary, including scores and statistics"""
        path = f"matches/{match_id}/summary"
        print(path)
        return self._make_request(self.prefix + path)

    def get_match_timeline(self, match_id):
        """Provides match information and scoring"""
        path = f"matches/{match_id}/timeline"
        print(path)
        return self._make_request(self.prefix + path)

    def get_player_profile(self, player_id):
        """Provides player information"""
        path = f"players/{player_id}/profile"
        print(path)
        return self._make_request(self.prefix + path)

    def get_player_versus_player(self, player_id_1, player_id_2):
        """Provides information on team versus team results"""
        path = f"players/{player_id_1}/versus/{player_id_2}/matches"
        print(path)
        return self._make_request(self.prefix + path)

    def get_player_results(self, player_id):
        """Provides the results for a given player"""
        path = f"players/{player_id}/results"
        print(path)
        return self._make_request(self.prefix + path)

    def get_player_schedule(self, player_id):
        """Provides the schedule for a player"""
        path = f"players/{player_id}/schedule"
        print(path)
        return self._make_request(self.prefix + path)

    def get_player_rankings(self):
        """Provides player rankings for a given tournaments"""
        path = "players/rankings"
        print(path)
        return self._make_request(self.prefix + path)

    def get_player_race_rankings(self):
        """Provides player rankings for a given tournaments"""
        path = "players/race_rankings"
        print(path)
        return self._make_request(self.prefix + path)

    def get_double_team_profile(self, team_id):
        """Team information, including player roster information"""
        path = f"double_teams/{team_id}/profile"
        print(path)
        return self._make_request(self.prefix + path)

    def get_double_team_results(self, team_id):
        """Provides a Team"s Results"""
        path = f"double_teams/{team_id}/results"
        print(path)
        return self._make_request(self.prefix + path)

    def get_double_team_schedule(self, team_id):
        """Provides a Team"s Schedule"""
        path = f"double_teams/{team_id}/schedule"
        print(path)
        return self._make_request(self.prefix + path)

    def get_double_team_versus_team(self, team_id_1, team_id_2):
        """Provides information on team versus team results"""
        path = f"double_teams/{team_id_1}/versus/{team_id_2}/matches"
        print(path)
        return self._make_request(self.prefix + path)

    def get_doubles_rankings(self):
        """Provides rankings for a Doubles"""
        path = "double_teams/rankings"
        print(path)
        return self._make_request(self.prefix + path)

    def get_doubles_race_rankings(self):
        """Provides double rankings for a Doubles"""
        path = "double_teams/race_rankings"
        print(path)
        return self._make_request(self.prefix + path)

    def get_tournament_info(self, tournament_id):
        """Provide information for a given Tournament found in the Tournament List
            endpoint
        """
        path = f"tournaments/{tournament_id}/info"
        print(path)
        return self._make_request(self.prefix + path)

    def get_tournament_list(self):
        """Provides a list of all covered Tournaments"""
        path = "tournaments"
        print(path)
        return self._make_request(self.prefix + path)

    def get_tournament_ongoing(self):
        """Provides updated information for a given Tournament found in the Tournament
            List endpoint
        """
        path = "tournaments/ongoing"
        print(path)
        return self._make_request(self.prefix + path)

    def get_tournament_results(self, tournament_id):
        """Provides results for a given Tournament found in the Tournament List en
            dpoint
        """
        path = f"tournaments/{tournament_id}/results"
        print(path)
        return self._make_request(self.prefix + path)

    def get_tournament_schedule(self, tournament_id):
        """Provides the schedule for a given Tournament found in the Tournament List
            endpoint
        """
        path = f"tournaments/{tournament_id}/schedule"
        print(path)
        return self._make_request(self.prefix + path)
