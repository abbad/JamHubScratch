'''
 unit tests for jamhub app.
'''

from django.test import TestCase

from utils.friendships import getUsersFromFriendRequests

from friendship.models import Friend, FriendshipRequest

# User app 
from django.contrib.auth.models import User

USER_ID = 1

def addUser(userName = 'test', passWord = '123'):
	''' function to create a user ''' 
	return User.objects.create(username = userName, password = passWord)

def addFriendShip(fromUser, toUser, message = ""):
	''' funciton to add a friendship '''
	return FriendshipRequest.objects.create(from_user = fromUser, to_user = toUser, message = message) 
	
class friendships_utils_functional_tests(TestCase):
	'''
		class for testing friendships utils 
	'''
	def setUp(self):
		self.users = []
		self.users.append(addUser())
		self.users.append(addUser("test1", "123"))
		self.users.append(addUser("test2", "123"))
		# create two friendShip requests.
		self.friendships = [] 
		self.friendships.append(addFriendShip(self.users[1], self.users[0]))
		self.friendships.append(addFriendShip(self.users[2], self.users[0]))
		
	def test_getUsersFromFriendRequests(self):
		''' test wether function can return list of users.'''
		# get the user. 
		User.objects.get(pk = USER_ID)
		# List all unread friendship requests
		friendRequests = getUsersFromFriendRequests(Friend.objects.unread_requests(self.users[0]))
		# check type outer type
		self.assertEquals(type(friendRequests), type([])) 
		# check object inside the list.
		self.assertEquals(type(friendRequests[0]), type(self.users[0])) 
		# to do check data integrity.
		
		
		
		