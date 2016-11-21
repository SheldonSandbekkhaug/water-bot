import os

# Directory for tweet content.
content_dir = 'content'

# File containing simple tweet content.
source_filename = 'simple.txt'

# File for already-tweeted content.
used_content_filename = 'used.txt'


def new_tweet():
    """ Returns a new tweet from the simple content source. """
    filename = get_filepath(source_filename)
    with open(filename, 'r+') as file:
        lines = file.readlines()
        tweet_content = lines[-1]
    
    copy_to_used_file(tweet_content)
    delete_content(tweet_content)
    return tweet_content.rstrip('\n')

def get_filepath(filename):
    """ Returns the filepath in the content directory with the given filename.
    """
    content_source_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    content_filepath = os.path.join(content_source_dir, content_dir, filename)
    return content_filepath

def delete_content(content):
    """ Deletes the given content (e.g. a tweet) from the simple content source.
    """
    filename = get_filepath(source_filename)
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if line != content:
                file.write(line)
        file.truncate()
    
def copy_to_used_file(content):
    """ Appends the given content to the used-tweets file. """
    filepath = get_filepath(used_content_filename)
    with open(filepath, 'a') as file:
        file.write(content)  