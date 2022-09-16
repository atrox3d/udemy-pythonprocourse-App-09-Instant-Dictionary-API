import justpy as jp
import api


class Doc:
    """
    About is a concrete class of page.Page
    """
    path = '/'
    example = api.Api.get_response('moon', indent=4)

    @classmethod
    def serve(cls, request):
        wp = jp.WebPage()
        print(jp.HOST)

        div = jp.Div(a=wp, classes='bg-gray-200 h-screen')

        jp.Div(a=div, text='Instant Dictionary API', classes='text-4xl m-2')
        jp.Div(a=div, text='Get definition of words', classes='text-lg')
        jp.Hr(a=div)
        jp.Div(a=div, text=f'http://{jp.HOST}:{jp.PORT}/api?w=moon')
        jp.Hr(a=div)
        jp.Pre(a=div, text=cls.example)

        return wp


# jp.Route(About.path, About.serve)
# jp.justpy(port=8001)

