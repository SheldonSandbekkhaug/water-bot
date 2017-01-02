import os

from markovbot import MarkovBot

# Directory for tweet content.
content_dir = 'content'

def markov_tweet():
    """ Generates a tweet using a Markov bot. """
    bot = MarkovBot()
    read_book(bot, 'alice.txt')
    read_book(bot, 'dao.txt')
    read_book(bot, 'pride.txt')
    read_book(bot, 'sherlock.txt')
    read_book(bot, 'oz.txt')
    
    seed_words = ['drink', 'health', 'water', 'river', 'stream']
    tweet_content = bot.generate_text(15, seedword=seed_words)
    print tweet_content
    
    # Check if the generated content has a seed word in it.
    for word in seed_words:
        if word in tweet_content:
            return tweet_content + ' #DrinkWater'
    return None
        
def read_book(bot, filename):
    """ Tells the Markov bot to read the book with the given file name. """
    filepath = get_filepath(filename)
    bot.read(filepath)    
    return
    
# TODO: Refactor I/O code into its own file.
def get_filepath(filename):
    """ Returns the filepath in the content directory with the given filename.
    """
    content_source_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    content_filepath = os.path.join(content_source_dir, content_dir, filename)
    return content_filepath    
