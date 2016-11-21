import os

# Directory for tweet content.
content_dir = 'content'

# File containing simple tweet content.
source_filename = 'simple.txt'

# File for already-tweeted content.
used_content_filename = 'used.txt'


def new_tweet():
    """ Returns a new tweet from the simple content source. """
    file = content_file()
    lines = file.readlines()
    tweet_content = lines[-1].rstrip('\n')
    file.close()
    print lines
    return tweet_content
    
def content_file():
    """ Returns the file containing plain text content for tweets. Callers must
        close the file when they are finished.    
    """
    content_source_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    content_filepath = os.path.join(content_source_dir, content_dir, source_filename)
    content_file = open(content_filepath, 'r+')
    return content_file

def delete_content(content):
    """ Deletes the given content (e.g. a tweet) from the simple content source.
    """
    file = content_file()
    d = file.readlines()
    file.seek(0)
    for line in d:
        if line != content:
            file.write(line)
    file.truncate()
    file.close()