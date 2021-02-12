from random import randint

class WordFinder:

    """Word Finder: finds random words from a dictionary.
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
    

    def __init__(self, file):
        self.file = file
        self.words = list()
        self.compile_words_list()
        print(f"{len(self.words)} words read")


    def compile_words_list(self):
        
        my_file = open(self.file)

        for line in my_file:
            self.words.append(line.strip())
        
        my_file.close()
    
    def random(self):
        rnd_idx = randint(0, len(self.words)-1)
        return self.words[rnd_idx]

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """


    def __init__(self, file):
        super().__init__(file)

    def compile_words_list(self):
        
        my_file = open(self.file)

        for line in my_file:
            if line[0] is not "#" and line.strip():
                self.words.append(line.strip())
        
        my_file.close()




   
    


   