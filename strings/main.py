# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
ruud_gullit = 'Ruud Gullit'
marco_van_basten = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = f"{ruud_gullit} {goal_0}, {marco_van_basten} {goal_1}"
report = f"{ruud_gullit} scored in the {goal_0}nd minute\n{marco_van_basten} scored in the {goal_1}th minute"
player = 'Ruud Gullit'
first_name = player[:player.find(' ')]
last_name_len = len(player[player.find(' ')+1:])
last_name = player[player.find(' ')+1:]
name_short = f"{first_name[0]}. {last_name}"
chant = f"{first_name}! " * len(first_name)
chant = chant.strip()
good_chant = chant[-1] != ' '
print(2 !=3)
print(2 !=2)

