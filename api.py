import justpy as jp
import definition
import json


class Api:
    path = '/api'
    """
    Handles requests at /api?w=word
    """

    @classmethod
    def get_response(cls, word, indent=None):
        defined = definition.Definition(word).get()
        print(f'?w         | {word}')
        print(f'definition | {defined}')

        response = {                                            # create dict for response
            "word": word,
            "definition": defined
        }

        return json.dumps(response, indent=indent)                             # converto to string and assing

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()                                       # create justpy webpage
        word = req.query_params.get('w')                        # get query-string ?w={word}

        """
        this way of returning word has the downside of returning
        all of html and javascript along with {word}
        """
        # print(word)
        # jp.Div(a=wp, text=word.title())                       # print word into div

        """
        this other way assigns only the {word} string to wp.html
        """
        wp.html = cls.get_response(word)                        # converto to string and assing
        print(f'wp.html    | {wp.html}')

        return wp
