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

#FILE SPELLLIST.PY and CHARATERS.PY
	- Spells: 
		- Grabbing and ETL only the columns needed for the Data Success Rate 
			- Spell Name: To check how many occurances in each file 
			- Spell Classes: To see which class can have access to the spell 
			- Spell Level: TO see what level class you need to be to learn the spell 
		- Export to new CSV
	- Charaters: 
		- Grabbing and ETL only information relevant to characters and filling nans 
			- Name: To identify charaters 
			- Class: + LV: TO give deafult success rate for character and find what spells they can learn 
			- Spells KNown: To give success based on spells they already know 
			- Skills: TO find how many occurances a skill they know is used in the session 
		- Export to new CSV
			
#FILE MAIN.PY
	- Read CSV Files: Reads data from CSV files of Charaters, Spells, and Monsters
	- Read and tokenize each session txt file in transcripts
		- Count each word, spell, and monster in each session sepererate
		- Count each time a level up appears for permanent success addition later 
		- Count total of all words, spells, and monsters of all sessions 
	- Clean all charater data
		- seperate levels and class in case of multiple classess in a charater 
	- Go through each session (transcritp file count) for each charater for the following to get the success rate %:
		- Add the levels x 2.5 of charater (based on max level charater 20 has 50% of winning) 
		- For each spell check:
			- IF the charater knows the spell
			- IF the charater can learn the spell based on class + level requirements 
			- Add the spell know rate (count of spell found in session)/10  (Small percentage due to a spell being used in most common usages and if it succeeds or not) 
			- Add the spell can learn rate (count of spell found in session)/10
		- For each skill check:
			- If the character has skill 
			- add skill (count of skill found in session)/10) (skills can also fail or succeed) 
	- Once all charaters from each session is stored in dictionary/lists for each session, export it to new CSV for graphing for later 


#FILE CHART.PY
	- Getting the following Graphs from the CSV of session data:
		- For the first 5 sessions of 1000 charaters 
			- Each legend has name and class lv of charater 
			- Getting Average of all charaters for each session for comparison 
			- Success Rate of the first 10 charaters #1-#10 in all sessions 
			- Seperate chart for each session of the top 10 highest success rate characters 
			- Seperate chart for each session of the bottom 10 lowest success rate characters 
		- FOr 100 sessions of 1000 charaters 
			- Average of all characters for each session for comparison
			- Success Rate of the first 10 charaters #1-#10 in all sessions 
			- For the first 500 charaters, make a sepererate graph of their success rates for all session comparied to the avereage 




###Data Sources
https://www.kaggle.com/datasets/matheusdalbuquerque/critical-role-campain-2-transcripts
https://www.kaggle.com/datasets/patrickgomes/dungeons-and-dragons-5e-monsters
https://www.kaggle.com/datasets/joebeachcapital/dungeons-and-dragons-characters
https://www.kaggle.com/datasets/mrpantherson/dndspells
 
