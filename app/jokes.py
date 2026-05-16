import random

# Word pools
subjects = ["programmers", "developers", "Python devs", "Java devs", "frontend engineers", "backend engineers"]
verbs = ["write", "debug", "refactor", "optimize", "deploy"]
objects = ["code", "functions", "algorithms", "APIs", "databases"]
punchlines = [
    "because they don't test enough.",
    "and hope it works.",
    "without reading the docs.",
    "and blame the computer.",
    "because they love coffee."
]

def get_random_joke():
    # Randomly choose a pattern
    pattern = random.choice([0, 1, 2])
    
    if pattern == 0:
        # Classic "Why" joke
        subject = random.choice(subjects)
        verb = random.choice(verbs)
        obj = random.choice(objects)
        punchline = random.choice(punchlines)
        return f"Why do {subject} {verb} {obj}? {punchline}"
    
    elif pattern == 1:
        # "How many" joke
        subject = random.choice(subjects)
        return f"How many {subject} does it take to change a light bulb? None, that's a hardware problem."
    
    else:
        # "Knock knock" style programming joke
        obj = random.choice(objects)
        return f"A {obj} walks into a bar and everyone says: 'Not again!'"
