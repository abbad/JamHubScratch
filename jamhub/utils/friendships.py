'''
	Helper function for friendship 
	main use is to reformat data that is driver from the app 
'''
from django.contrib.auth.models import User

import re


def getUsersFromFriendRequests(friendshipRequests):	
	''' function to get every request for a certain user 
		@ return a list
		it will parse the following and get requested user
		<FriendshipRequest: User #423 friendship requested #2> of course with handeling the objects.
	'''	
	users = []
	# iterate over the query.
	for friendshipRequest in friendshipRequests:
		# find from
		textFound = re.search('#[0-9]*', str(friendshipRequest))
		# get the user.
		users.append(User.objects.get(pk = textFound.group(0)[1:]))
		
	# return the users
	return users