#This file contains all the classes which are include in the game:Sherlock Holmes
from time import sleep
from random import randint
from sys import exit
from textwrap import dedent


# Defination of a base class.

class scene(object):

	def __init__(self):
		self.description = ""
		self.mystery = "No mystery is in this scene."

	def action(self):
		pass

	def prline(self):
		print("\n","-"*50)   #function to print a line of hyphens

class introduction(scene):
#Introduction of this game
#Making a sub class of the base class 'scene'

	def __init__(self):
		self.description = ""
		super(introduction,self).__init__()


	def rules(self):	#To display rules of this game.

		self.prline()
		print(dedent("""
			............................................DISCLAMIMER................................................
			This Game is only meant for Sherlock lovers and those who are interested to solve riddles as it involves
			world's toughest riddle's which you can easily find on internet
			"""))
		sleep(3)
		print("\n\t\t\t\t\tAbOuT ThE GaMe\n")
		# dedent helps me print more lines in one print function. It removes whitespace before each line.

		print("****************************** Welcome to Sherlock Holmes: The Game ***********************************")

		print(dedent("""
			 Sherlock Holmes i.e you are lost in a place full of mysteries.
			 You have to solve each mystery to get closer to your freedom.
			 There will a riddle for you at each stage and you have to provide the right answer to get closer to victory.
			 These riddles are put up by none other than JAMES MORIARTY (he loves playing games).
			 He will set traps in form of riddles in every stage and if you answer all of correctly....he will set you free...maybe
			 Each riddle has answer that is of one or two words.
			 Mystery can be of any type like murder,escape,who is the theif,etc.
			 Spelling Mistakes will not be tolerated!!
			 There will be hints in some tough riddles just so that you dont cry.
			"""))
		print("\n\n")
		input("\n\tPress Enter to continue and CTRL-C to quit")

		self.prline() #calling the function that print line made of 50 hyphens

	def action(self):

		while True:      #to create an infinite loop
			print(dedent("""
				In front of you there's a mystery door. It is locked and can only be opened by guessing the correct lucky number of sherlock holmes.
				If you have watched sherlock holmes, you would know this code.
				It's the only requirement to play this game
				hint - Your house number.
				"""))
			code = "212"
			guess = input("> ") #taking input from user

			if guess == code:
				print("The door clicks open and the lock breaks, letting you in.")
				return "iced_tea"  #returning keyword of next scenes

			else:
				print("BZZZZZZZEDDD! You have no luck today sherlock!")
				return "death"



class iced_tea(scene):
#the 2nd scene of the GaMe
	def __init__(self):
		pass

	def action(self):
		sleep(2)  #Done to make more realistic as it will give a break for loading
		self.prline()

		print(dedent("""
			You find a sheet of paper with a riddle written on it.
			The riddle is: Two girls ate dinner together. They both ordered Iced tea.
			One girl drank them very fast and had finished five in the time it took the other to drink just one.
			The girl who drank one died while the other survived.
			All the drinks were poisoned.
			"""))
		sleep(2)
		print(dedent("""
			How did the girl who drank the most survive?
			Answer in one word - ***Where was the poison??***(NO CAPS PLEASE)
			"""))
		print("Hint - Answer is a three letter word which is a solid and is used in all cold drinks")
		decision = input("> ")
		Answer = "ice"

		if decision in Answer:
			print(dedent("""
				Wuhuuuuu!!You have cracked your first case Sherlockkk. I am impressed. Lets see what you do in the upcoming puzzles.
				Seee yaaa
				"""))
			return "murder_at_school"

		else:
			print(dedent("""
				Shame one you shelock. How can you be the best detective when you can't solve riddles made by a madman.
				You deserve to die!
				"""))
			return "death"

class murder_at_school(scene):

	def __init__(self):
		pass

	def action(self):
		sleep(2)
		self.prline()

		print(dedent("""
		You now go to the other room and find another mystery.
		This time it is a murder mystery (your space of interest)
		Mystery: On the first day of the school year, a geography teacher was murdered.
		The police had 4 suspects : the gardener, the math teacher, the coach and the school principal.
		They all had alibis:
		 1. The gardener was cutting bushes.
		 2. The math teacher was holding a mid-year test
		 3. The coach was playing basketball.
		 4. The principal was in his office.
		"""))
		sleep(5)
		print(" Who can be the killer?")
		Answer = input("> ")
		killer = "math teacher"
		sleep(2)

		if Answer in killer:
			print(dedent("""
				Well Done Sherlock!!
				Now you are playing like a real detective.
				Next puzzle won't be that easy my man.
				It's gonna be too much fun.
				Hehehahahahahahahahahahahahh
				"""))
			return "chemical_mystery"

		else:
			print(dedent("""
				You ain't that smart Sherlock. Moriarty is the best in making riddles!!
				Sad, but now i have to kill you.
				Say Goodbye to this world Sherlock.
				"""))
			return "death"



class chemical_mystery(scene):

	def __init__(self):
		pass


	def action(self):
		sleep(2)
		self.prline()

		print(dedent("""
		Now let's see how strong is your chemistry Sherlock.
		A famous chemist was found murdered.
		It is known that two people were involved in the murder.
		A note was found that written by the chemist which read - '26-3-58/28-27-57-16'.
		"""))
		print("Answer by seperating their names by and....eg: ram and shyam")
		sleep(5)
		print("What are the names of the murderers?")
		print("This requires basic inorganic chemistry knowledge. You may search the internet for something needed to solve this case")
		answer = input("> ")
		Murderers = "felice and nicolas"

		if answer in Murderers:
			print(dedent("""
				ooooooo shit! How did you get that right!!I thought that was a tough question.
				You were good in chemistry sherlock, didn't you?
				Anyways.....Lets go to next question...This time i will defeat you boy.
				"""))
			return "the_ship_mystery"

		else:
			print(dedent("""
				ooooooo yeahh! I knew you would do this wrong.
				The heaven calls you Sherlock....Its time for you to die.
				"""))
			return "death"

class the_ship_mystery(scene):

	def __init__(self):
		pass

	def action(self):
		sleep(2)
		self.prline()

		print(dedent("""
		Sherlock you may be good at solving murder cases,
		but let's see do you have knowledge about flags.
		Ohh Shit! did i just gave you a hint. I should control my tongue.
		A Japanese ship was en route to the open sea. The Captain went for shower removing his ring and keeping it on table.
		When he returned, he found it had gone missing. The captain immediately called the three suspected crew members
		and asked each one where they were and what were they doing in the last fifteen minutes.
		The cook said, \"I was in fridge room getting meat for cooking.\"
		The Engineer said, \"I was working on generator engine.\"
		The seamen said, \"I was on the mast correcting the flag which was upside down by mistake.\"
		The radio officer said, \"I was messaging to a company about the arrivel.\"
		The navigation officer said, 'I was sleeping in my cabin.'
		"""))
		sleep(5)

		print(" Sherlock, can you tell me who was the theif?\n ")
		answer = input("> ")
		Theif = "seamen"

		if answer == Theif:
			print(" Well done Sherlock! you have again surpassed my intelligence. I shouldn't have given you the hint.")
			return "two_pills"

		else:
			print("Say ggodbye to this world Sherlock!")
			return "death"


class two_pills(scene):

	def __init__(self):
		pass

	def action(self):
		sleep(2)
		self.prline()

		print(dedent("""
		Now you are reaaly very close to your freedom
		Only two more riddles to go....
		Here you go:
		A serial killer kidnapped people and made them take 1 or 2 pills.
		One was harmless, and the other was poisonous.
		Whichever pill a victim took, the serial killer took the other one.
		The victim took their pill with water and died.
		The killer survived.
		"""))
		sleep(5)

		print("Can you tell how did the killer mangaged to survive everytime?")
		print("You may write the answer in sentence but it must contain a specific keyword\n")

		print("Hint - Poison may not be in the pill.")


		answer = input("> ")
		Reason = "Both the pill were harmless. The poison was in the glass of water the victim drank."
		Solution = "Poison was in the water."

		if answer in Solution:
			print("You have cracked it!! Now you're in the final round.")
			print(Reason)
			return "end_game"

		else:
			print("You were too close Sherlock but you failed")
			print("Say goodbye to this world......")
			return "death"

class end_game(scene):

	def __init__(self):
		pass

	def action(self):
		sleep(2)
		self.prline()
		print(dedent("""
		Welcome to the final round Sherlock
		So far you have played so well
		It's time for a twist.
		In this round, if you answer correctly you live and I die,
		else You die and i get to live!
		Hahahahahah it's gonna be so much fun
		Here's your final problem:\n
		A man is found murdered on a Sunday morning.
		His wife calls the police, who question the wife and the staff
		The wife says she was sleeping,
		The butler was cleaning the closet,
		The gardener was picking vegetables,
		The maid was getting the mail, and
		The cook was preparing breakfast.
		"""))
		sleep(5)

		print("Who was the murderer Sherlock?")
		answer = input("> ")
		murderer = "maid"

		if answer in murderer:
			print("Gunshot!!")
			sleep(3)
			print("Moriarty Dies")
			self.prline()
			print("CONGRATULATIONS! Sherlock.....You have solved all the mysteries and came out of this alive.")
			print("Moriarty is dead now."+ "You can go home and sleep.")
			exit(1) #To exit the game

		else:
			print("Gunshot!")
			sleep(5)
			print("You are dead")
			print("You have answered incorrectly and you died")
			print("Moriarty Won his game!")
			return "death"

class death(scene):
#death scene
	def action(self):
		sleep(2)
		self.prline()
		print(dedent("""                GAME OVER
			                     YOU ARE DEAD..!!!
		      """))

		self.prline()
		exit(1)


class play(object):
#class to different scenes in game
	def __init__(self):

		self.current_scene = introduction()
#self.cuurent_scene is the instance of the class depicting current scene
		self.next_scene = ''  #instance of the class depicting next scene
		self.scene_plot = {
			"iced_tea" : iced_tea(),
			"murder_at_school" : murder_at_school(),
			"chemical_mystery" : chemical_mystery(),
			"the_ship_mystery" : the_ship_mystery(),
			"two_pills" : two_pills(),
			"end_game" : end_game(),
			"death" : death() }  #dictionary containing classes using their names.

	def lets_play(self):

		self.current_scene.rules() # calling method of class introduction to display rules of the game.
		while self.current_scene != 0:

			self.next_scene = self.scene_plot[self.current_scene.action()]  #assigning an instance for the upcoming class/scene
			self.current_scene = self.next_scene


player = play() #making player an object of the class 'play'

player.lets_play() #calling lets_paly() function to start the GaMe
