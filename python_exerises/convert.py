import random
WORDS = ['account', 'pig', 'snow', 'summer', 'coat']

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))] # => [ACCOUNT, APPLE, CAT]
    other_names = random.sample(WORDS, snippet.count("***")) # => [dog, picture, pig]
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))    # ["cat, dog, apple"]

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

print(convert("class %%%(object):\n\tdef __init__(self, ***)", "class %%% has-a __init__ that takes self and *** parameters."))
