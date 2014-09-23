# -*- coding: utf-8 -*-
import unittest
from organizor_problem import Organizer

class OrganizorTestCase(unittest.TestCase):
    """Tests for `organizor_problem.py`."""

    def test_parseCSVInput(self):
        """ """
        organiser_obj = Organizer(6.0)
        csv_input = "p1,2,100#p2,2,200#p3,2,250#p4,5,100"
        pattern = organiser_obj.parseCSVInput(csv_input)
        assert len(pattern) > 0
        csv_input = ""
        pattern = organiser_obj.parseCSVInput(csv_input)
        assert pattern ==  None

    def test_organiseEvent(self):
        """
        usecase1 : Maximize the number of presenters - Select the case that fits in maximum number of presenters in the given time schedule
        usecase2 : In case all the 3 sessions can’t be filled then output should be “Not enough presenters”.
        """
        organiser_obj = Organizer(6.0)
        comb_list_input = [('p1', '2', '100'), ('p2', '2', '200'), ('p3', '2', '250'), ('p4', '5', '100')]
        pattern = organiser_obj.organiseEvent(comb_list_input)
        assert len(pattern) > 0
        organiser_obj = Organizer(6.0)
        comb_list_input = [('p1', '4', '100'), ('p2', '2', '200'), ('p3', '2', '250'), ('p4', '5', '100')]
        pattern = organiser_obj.organiseEvent(comb_list_input)
        assert pattern == 'Not enough presenters'

    def test_organiseEventOptimumCost(self):
        """
        usecase1 :If multiple cases satisfy this scenario, select the ones with minimum cost.
        """
        organiser_obj = Organizer(6.0)
        comb_list_input = [('p1', '2', '50'), ('p2', '2', '100'), ('p3', '2', '150'), ('p4', '1', '200')]
        pattern = organiser_obj.organiseEvent(comb_list_input)
        assert len(pattern) > 1
        pattern = organiser_obj.organiseEventOptimumCost(pattern)
        cost = sum(int(item[2]) for item in pattern)
        assert cost == 300

if __name__ == '__main__':
    unittest.main()
