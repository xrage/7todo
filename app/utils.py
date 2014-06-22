'''
 :author: "Dharmendra Verma"
 :copyright: "Copyright 2013, Shopsense.Co" 
 :created: 22/06/14
 :email: "dharmendraverma@shopsense.co"   
 :github: @xrage 

'''
import random
import string

class TokenGenerator:
    """
        To generate a random string of length passed.
    """
    @staticmethod
    def __get_random_token_lower__(token_length):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) \
                    for x in range(token_length))
