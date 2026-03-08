## Q1: Conceptual - Under the Hood of Python Dictionaries

### Time Complexity

In Python, dictionaries are implemented as hash tables.

* **Lookup, Insert, Delete:** Average case is $O(1)$.
* **Worst-case:** $O(n)$, where $n$ is the number of elements in the dictionary.

### Why is the average $O(1)$?

When you insert or look up a key, Python uses a hash function to convert that key into an integer memory index. Because this mathematical operation and the subsequent memory access take a constant amount of time regardless of how large the dictionary gets, the operation is $O(1)$.

### What causes worst-case $O(n)$?

The worst-case scenario is caused by **hash collisions**. If many different keys evaluate to the exact same hash value (or map to the same underlying array index), Python has to resolve this by checking subsequent slots (a technique called open addressing or probing). If every key collides, finding an item means scanning through a linear chain of elements, taking $O(n)$ time.

### Python's Hash Function: Strings vs. Integers

* **Integers:** Python tries to hash integers to themselves (e.g., `hash(42)` is usually `42`). This makes hashing numbers incredibly fast, though it does mean sequential numbers will hash to sequential slots.
* **Strings:** Strings use a randomized hashing algorithm (specifically, SipHash). Every time you start a new Python process, a random seed is generated. This means `hash("apple")` will output a completely different number in different Python sessions. This prevents "Hash Denial of Service" (DoS) attacks, where a malicious user could intentionally feed an application strings that they know will collide, thereby bringing the system to a halt.

### When to Choose a Dict over a List

* **Use a Dict when:** You need fast $O(1)$ lookups based on a specific, non-sequential identifier (like a string, an ID number, or a tuple). It is ideal for relationships, mappings, and counting frequencies.
* **Use a List when:** Your data is strictly ordered, you frequently need to sort or iterate through items sequentially, or your access patterns rely on continuous integer indices.

---

## Q2: Coding - Grouping Anagrams

Here is an efficient, clean implementation utilizing Python's `collections.defaultdict`. By sorting the characters of a word, we generate a normalized "signature" that will be identical for all anagrams of that word.

from collections import defaultdict

def group_anagrams(words: list[str]) -> dict[str, list[str]]:
    # defaultdict automatically creates an empty list if a key doesn't exist
    anagrams = defaultdict(list)
    
    for word in words:
        # Sort the characters to create the anagram signature (e.g., 'eat' -> 'aet')
        signature = "".join(sorted(word))
        # Append the original word to the corresponding list
        anagrams[signature].append(word)
        
    return dict(anagrams)

# Example usage:
# print(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
# Returns: {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}

```

---

## Q3: Debug/Analyze - Fixing Character Frequencies

def char_freq(text):
    freq = {}
    
    for char in text:
        # Fix 1: Use .get() to provide a default value of 0 if the key doesn't exist yet.
        freq[char] = freq.get(char, 0) + 1      
        
    # Fix 2: Iterate over .items() to get both keys and values, 
    # and sort by the value (item[1]) in descending order.
    sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    
    return sorted_freq

# Example usage:
# print(char_freq("banana"))
# Returns: [('a', 3), ('n', 2), ('b', 1)]

