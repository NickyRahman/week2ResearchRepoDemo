program_list = ["PatternCircle.py", "PatternHexagon.py", "SpiralHue.py"]

for program in program_list:
    exec(open(program).read())
    print("\nFinished: " + program)