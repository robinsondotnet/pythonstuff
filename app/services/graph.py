import os

from facepy import GraphAPI

class GraphService(object):
    '''
        fb graphql service
    '''

    def __init__(self):
        access_token = os.environ.get("ACCESS_TOKEN")
        self.__graph = GraphAPI(access_token)

    def get_me(self):
        return self.__graph.get('me')
