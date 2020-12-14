
f = open("current_day.txt")
current_day = int(f.read())
f.close()

python_name = f"day-{current_day}.py"
input_name = f"input-{current_day}.txt"

open(python_name, "x")
open(input_name, "x")

f = open("current_day.txt", "w")
f.write(str(current_day + 1))
f.close()
