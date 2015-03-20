def me() :
	print """

	Amanat - Save a message that trusted to you

	-- Synopsis

	$: amanat.py [Options]

	-- Options
	[random | view | add | remove | merge | rename | help | version | about | exit]

	> random
	Default options. Display random message from random person.

	> view [all|name] [all|number of message]
	The first argument decide message from who will display. all is default. The second argument decide which message will display. all is default. Choose name or/and number of message to spesific display. Numbering was sorted ascending (oldest on top).

	> add [blank|name] ["message"]
	The first argument decide message from who will add. blank is default. If blank choosed, showing the list of person that already exist then asking for person. If you put person that not exist, will make a new person to list. Name of person just alphabetic without space. message must be in (double) quote.

	> remove [all|name] [all|number of message]
	The first argument decide message from who will remove. all is default. The second argument decide which message will remove. all is default. Choose name or/and number of message to spesific remove. Numbering was sorted ascending (oldest on top)

	> merge [all|name] [all|number of message] [all|name] [all|number of message] [merge name]
	You can merge 2 message from 2 person. Merge name is the merge message will be save. Old messege will be delete.

	>rename
	rename someone

	> help 
	Display this help.

	> version
	Display version of amanat program

	> about
	Display about this program

	> exit
	exit

		"""