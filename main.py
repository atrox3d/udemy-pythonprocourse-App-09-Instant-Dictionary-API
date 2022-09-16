import justpy as jp
import api
import documentation

jp.Route(documentation.Doc.path, documentation.Doc.serve)
jp.Route(api.Api.path, api.Api.serve)
jp.justpy(
    # host='0.0.0.0'
)
