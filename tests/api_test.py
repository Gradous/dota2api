#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests relating to the API calls. Code coverage can be deceiving"""

import unittest
import os

from dota2api import wrapper
from dota2api.src.exceptions import APIAuthenticationError


class ApiMatchTests(unittest.TestCase):
    """Tests relating to the Dota 2 API wrapper"""
    def setUp(self):
        """Set up test fixtures"""
        self.api_test = wrapper.Initialise(os.environ['D2_API_KEY'])

    def get_match_history_test(self):
        """Test get_match_history"""
        # Is the response a dictionary
        self.assertEqual(type(self.api_test.get_match_history().dict), type(dict()))
        # Do we default at 100 responses
        self.assertEquals(
            len(self.api_test.get_match_history().dict['matches']), 100)
        # Can we filter that to 1 response
        self.assertEquals(len(self.api_test.get_match_history(
            matches_requested=1).dict['matches']), 1)
        # Can we use the parameter to get only 1 players matches
        for matches in self.api_test \
            .get_match_history(account_id=88585077,
                               matches_requested=10).dict['matches']:
            if 19672354 in matches['players']:
                self.assertTrue(True)

    def get_match_details_test(self):
        """Test get_match_details"""
        # Is the response a dictionary
        self.assertEqual(type(self.api_test.get_match_details(
                              match_id=988604774).dict), type(dict()))
        # Do we get an error with no match ID
        self.assertEquals(self.api_test.get_match_details().dict['error'],
                          "No Match ID specified")


class ApiOtherTests(unittest.TestCase):
    """Tests relating to the other tests."""
    def setUp(self):
        """Set up test fixtures"""
        self.api_test = wrapper.Initialise(os.environ['D2_API_KEY'])

    def get_league_listing_test(self):
        """Test get_league_listing"""
        # Is the response a dictionary
        self.assertEqual(type(self.api_test.get_league_listing().dict),
                         type(dict()))

    def get_live_league_games_test(self):
        """Test get_live_league_games"""
        # Is the response a dictionary
        self.assertEqual(type(self.api_test.get_live_league_games().dict),
                         type(dict()))

    def get_team_info_by_team_id_test(self):
        """Test get_team_info_by_team_id"""
        # Is the response a dictionary
        self.assertEqual(type(self.api_test.get_team_info_by_team_id().dict),
                         type(dict()))

    def get_player_summaries_test(self):
        """Test get_player_summaries"""
        # Is the response a dictionary
        self.assertEqual(type(self.api_test.get_player_summaries().dict),
                         type(dict()))

    def get_heroes_test(self):
        """Test get_heroes"""
        # Is the response a dictionary
        self.assertEqual(type(self.api_test.get_heroes().dict),
                         type(dict()))

    def get_game_items_test(self):
        """Test get_game_items"""
        # Is the response a dictionary
        self.assertEqual(type(self.api_test.get_game_items().dict),
                         type(dict()))

    def get_tournament_prize_pool_test(self):
        """Test get_tournament_prize_pool"""
        # Is the response a dictionary
        self.assertEqual(type(self.api_test.get_tournament_prize_pool().dict),
                         type(dict()))


def invalid_api_key_test():
    """Test invalid_api_key"""
    api_test = wrapper.Initialise("invalid")
    try:
        api_test.get_match_history()
    except APIAuthenticationError:
        assert True
