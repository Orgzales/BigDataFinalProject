# BigDataFinalProject

Objective:
Analyze transcripts from over 128+ episodes of the Dungeons & Dragons 5e series, Critical Role, alongside data generated from 1000+ random characters. The aim is to determine:

	- Optimal classes, races, and magic spells for the campaign.
	- Success rates for specific classes.
	- Challenge rates based on a dataset of monsters.
	- Develop a session system to track character outcomes.
	- Implement a level-up system based on transript dataset.
	- Develop possible magic usage from magic spell dataset.
	- Create new lis
	- Predict the success of various character quantities in the campaign based on gathered statistics.

Background: Critical Role is a D&D 5e campaign with a rich storyline spanning over a year. The character dataset includes outliers, such as level 200 characters with an expected high success rate, and level 1 characters whose survival may vary. Factors such as class, race, abilities, weapons, magic spells, and additional skills will influence their survivability. With seven years of experience as a Dungeon Master and player, I can discern which statistics hold greater significance than others.

##TODO/STEP 0:
CREATE OUTPUT FILES FOR PROCESSING STATS
	- Charaters output file contains:
		- Name: Used to just ID the Charaters 
		- Class: To compare what spells or abilities are brought up into each session 
		- Skills: TO compare which skills are brought up into each session 
		- Processed Spells: Magic that the charater specializes in 
		- Level: Each session will automatically has a success rate for each level of the charater such as level 2 = 2% for each session. Also to compare the Challenge rating for the monster names brought up into the campaign in total.
		- These will be used to compare the amount of times in the transcripts a previous player uses a Class ability or class spell, or when the DM has asked for a certain skill check
		- EX: In the transcript in session 1, if stealth count = 9 , a charater with the stealth skill would have possibly a +9% success rate in that session 
		- EX: If a charater that doesn't have the correct abilities in the session, then it's possible they may come out with a 0% success rate in that session. Once all 128 sessions have been totaled with the average of all percentages, it will be determine how likely that charater will be able to win the campaign
		
	- SpellList:
		- Name: To ID which spells are in the transcripts
		- Class: WHich class are able to use the magic
		- EX: Each time a spell/feature of a class is brought up, if the charater has a class for the spell access such as Wizard with Acid = 3, they would get +3% success
		- EX: If the CHarater has the spell in it's process spells, the percentage is doubled. If frost = 4, the success rate = 8%
	
	- Monsters: 
		- Name: To ID which monsters are in the transcripts 
		- Challenge rating: To ID what level requirment is recommended 
		- EX: If in a session there is a Challenge Rating 3 Monster, and if a player is level 1, their success rate will go down by 3%

##TODO/STEP 1:
	- Tokenize the transcripts of each file using Glob
	- For each file, use a dictionary/lists to find the amount of times a spell, word, or etc has been said:
		- SPELLS: Find out how many times spells have been used + Classes can use them 
		- Monsters: Find out each monster and match challenge rating 
		- Seperate each file into a session for each match 
	- Make sure to make it not case sensitive
	
##TODO/STEP 2
	- W/ total amount of spells in total + Session amount of spells using pandas 
		- Get the classes that the spell could use or access by
		- Check if the charater has the class that is within the requiements 
			- if the charater does give out a precent success to that name in that session 
			- Any nans replace it with "Charater knows no spells"
			- Make a method to get for each class if the charater has multiple 
		- for each session keep the success rate from each charter 
		- also get the total average of success rate for all sessions for each charaters		
		- Do the same for abilities and skills 
			- May have to make a sepererate list of abilities for classes 
		- 
		
##TODO/STEP 3
	- Make each session name based on file name 
	- Add a permanent success rate addition when a level up is found in the session 
	- tokenize all words to get a cluster of certain words for 3d models
	
###Success Rates 
	- Player level: +Lv%
	- If player has spell: +1% Each occurance
	- If player can learn spell: +0.5% Each occurance
	- If Player has skill: +0.5% Each occurance
	- If Session has level up: +1 to level rate 
	- Monster CR lowers success: Challeneg rating = 3 -> -3% 
		Challenege rating 0.4 -> -0.4%
	
	
#Charts to Create
	- a line chart of the avg success rate for each session among all charaters 
	- a graph of most common spells, classses, monsters, and charters 
		- possibly for each session 
	- A cluster graph of the most successful classes with the spells 
	- cluster/3d graph of the common words, spells, and charaters 


###Data Sources
https://www.kaggle.com/datasets/matheusdalbuquerque/critical-role-campain-2-transcripts
https://www.kaggle.com/datasets/patrickgomes/dungeons-and-dragons-5e-monsters
https://www.kaggle.com/datasets/joebeachcapital/dungeons-and-dragons-characters
https://www.kaggle.com/datasets/mrpantherson/dndspells
 
