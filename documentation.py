import justpy as jp
import api


class Doc:
    """
    About is a concrete class of page.Page
    """
    path = '/'
    example_text = api.Api.get_response('moon', indent=4)
    example_url = f'http://{jp.jpconfig.HOST}:{jp.jpconfig.HOST}/api?w=moon'

    @classmethod
    def serve(cls, request):
        wp = jp.WebPage()
        print(jp.jpconfig.HOST)

        div = jp.Div(a=wp, classes='bg-gray-200 h-screen')

        jp.Div(a=div, text='Instant Dictionary API', classes='text-4xl m-2')
        jp.Div(a=div, text='Get definition of words', classes='text-lg')
        jp.Hr(a=div)
        # jp.Div(a=div, text=f'http://{jp.HOST}:{jp.PORT}/api?w=moon')
        jp.A(a=div, text=cls.example_url, href=cls.example_url)
        jp.Hr(a=div)
        jp.Pre(a=div, text=cls.example_text, title=cls.example_text)

        return wp


# jp.Route(About.path, About.serve)
# jp.justpy(port=8001)

