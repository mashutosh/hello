# -*- coding: utf-8 -*-
"""
You are the organiser of a conference and need to schedule presentations. You have received requests from N presenters stored in the csv file along with other details as

Presenter Name    No. of Hours for Presentation     Cost benefit for presenter
P1                     2                               100
P2                     2                               50
P3                     3                               150

The first column is the presenter name
Second column indicates number of hours presenter will take for the presentation (assume it to be an integer)
Last one indicates the associated cost (Fees that presenter will charge).

You are given that your conference will last for N hrs (N taken as an input) divided into 3 sessions (with no breaks and back to back presentation for example 8 hrs=3+3+2 hrs) and any of the session do not exceed N/2 hours. 

Write the code to provide the following solution.

Maximize the number of presenters  Select the case that fits in maximum number of presenters in the given time schedule. If multiple cases satisfy this scenario, select the ones with minimum cost.

A session need not be fully utilized. But it should not be left empty without a presentation or In case all the 3 sessions cant be filled then output should be “Not enough presenters”
"""
import csv

class Organizer(object):
    """ A class to """

    def __init__(self, n, ):
        """ Initialization """
        self.total_no_of_hours = n

    def parseCSVInput(self, csv_input):
        """
        this will parse the csv string input with # saperated records like  'p1,2,100 # p2,3,200 # p3,1,250 # p4,5,100'
	
	The first item of a comma saperated record is the presenter name
	Second item indicates number of hours presenter will take for the presentation (assume it to be an integer)
	Last one indicates the associated cost (Fees that presenter will charge).
        """
        if not csv_input:
            return
        presenter_list = []
        #this will return a list of tuple where each tuple is a presentors details like name hrs and cost
        res = csv_input.split('#')
        for item in res:
            presenter_list.append(tuple(item.split(',')))
        return presenter_list

    def organiseEvent(self, presenter_list):
        """
        schedule event for n hrs and allocate presentor for all combination for time <= n
        """
	max_hrs = self.total_no_of_hours
	final_time_list = []
	import itertools as it
	comb_list = list(it.combinations(presenter_list,3))
  	for comb in comb_list:
            #checker is initialised to 0 and will add up to total no of hrs 
            #for a combination and will be used to compare with max_hrs i.e total_no_of_hours
	    checker = 0
	    break_flag = False
	    for item in comb:
		p_hours = float(item[1])
                #any session do not exceed N/2 hours and sum of time of any combination should not exceed max_hrs
		if p_hours > max_hrs/2 or checker > max_hrs:
		    break_flag = True
		    break
		checker = checker + p_hours
	    # if any combination satisfies the criteria add it to the final_time_list
	    if checker <= max_hrs and not break_flag: 
		final_time_list.append(comb)
        if not final_time_list:
            return "Not enough presenters"
	return final_time_list
    
    def organiseEventOptimumCost(self, presenter_list):
        """
        reqirement : If multiple cases satisfy this scenario, select the ones with minimum cost.
        final_cost_list will look like [((('p1','2','50'),('p2','2','100'), ('p3','2','150')), 300), ((('p1','2','50'),('p2','2','100'),('p4','1','200')), 350)
        """
	from operator import itemgetter
	final_cost_list = []
	for presenter in presenter_list:
	    total_cost = 0
	    for item in presenter:
		p_cost = item[2]    
		total_cost = total_cost + int(p_cost)
            # sum the cost and add it to the cost list with the record like (('p1', '2', '50'),('p2', '2', '100'), ('p3', '2', '150')), 300)
	    final_cost_list.append((presenter, total_cost))
        
	print final_cost_list
        #sort the cost list and return first record with minimum cost 
	return sorted(final_cost_list,key=itemgetter(1))[0][0]
    

if __name__=='__main__':
    #csv_input is a string input with # saperated records
    csv_input = "p1,2,100#p2,2,200#p3,2,250#p4,5,100"
    event_total_time = 6.0
    organiser_obj = Organizer(event_total_time)
    #convert csv_input to a list of tuples like [(p1, 2, 100), (p2, 3, 200), (p3, 2, 200)]
    list_input = organiser_obj.parseCSVInput(csv_input)
    final_time_list = organiser_obj.organiseEvent(list_input)
    #If multiple cases satisfy this scenario, select the ones with minimum cost.
    if len(final_time_list) > 1:
        final_time_list = organiser_obj.organiseEventOptimumCost(final_time_list)

