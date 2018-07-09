import weasyprint
from weasyprint import HTML, CSS, Document
from weasyprint.fonts import FontConfiguration

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# from django.contrib.staticfiles.finders import find as find_static_file
# from django.conf import settings


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, parser_classes, renderer_classes
from rest_framework.renderers import BaseRenderer
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
#
# def image_as_base64(image_file, format='png'):
#     """
#     :param `image_file` for the complete path of image.
#     :param `format` is format for image, eg: `png` or `jpg`.
#     """
#     if not os.path.isfile(image_file):
#         return None
#
#     encoded_string = ''
#     with open(image_file, 'rb') as img_f:
#         encoded_string = base64.b64encode(img_f.read())
#     return 'data:image/%s;base64,%s' % (format, encoded_string)
#
# def get_image(request):
#     return image_as_base64(settings.STATIC_URL + 'logo1.png')
#     # image_data = get_graph() # assuming this returns PNG data
#     # return HttpResponse(image_data, mimetype="image/png")

css_string = """
@page {
    size: 10cm 19cm ;
    font-family: 'Open Sans';
    font-size: 12pt;
    padding: 0;
     margin: 0;
    
    @top-center {
        height: 45px;
        white-space: pre;
        text-align: left;
        content: 'This is the header;
        background: url('{% static 'images/background.png' %}');
        background-size: 100%;
        width: 100%;
    }
    @bottom-left {
        margin-left: 50px;
        content: 'This is the footer;
        font-size: 10pt;
        color: #999;
    }
    @bottom-right {
        width: 22px;
        height: 22px;
        content: url('{% static 'images/footer-logo.png' %}');
    }
}
"""
class PDFRenderer(BaseRenderer):
    media_type = 'application/pdf'
    format = 'pdf'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        print (data, media_type,renderer_context)
        return data


class PDFResponse(HttpResponse):
    def __init__(self, pdf, file_name, *args, **kwargs):
        headers = {
            'Content-Disposition': 'filename="{}.pdf"'.format(file_name),
            'Content-Length': len(pdf),
        }
        super(PDFResponse, self).__init__(
            pdf,
            content_type='application/pdf',
            *args,
            **kwargs
        )

class SimpleExample(APIView):

    renderer_classes = (PDFRenderer, BrowsableAPIRenderer,)

    def post(self, request):
        return Response({})

    @staticmethod
    def get_html_doc(request,  *args, **kwargs):
        print ('build_absolute_uris=========%s'%request.build_absolute_uri())
        print ('get_host=========%s'%request.get_host())
        print ('get_full_path=========%s'%request.get_full_path())
        base_url = '{scheme}://{host}/'.format(
            scheme=request.scheme,
            host=request._get_raw_host()
        )
        print ('base_url=========%s'%base_url)
        html_template = loader.get_template('sample.html')
        stylesheet = CSS(string=css_string)

        # stylesheet = CSS(string='@page { size: Letter;  margin: 0in 0.44in 0.2in 0.44in; }')
        base_url = 'http://web:7001/'
        media_type = 'screen'
        html_page = HTML(
                string='</span>',
                base_url=base_url,
                media_type=media_type
            ).render()
        pdf_pages = []
        for item in range(1,(int(request.GET.get('limit','1')) or 1)+1):
            pdf_file = HTML(
                    string=html_template.render({'first_name':'DEMO%s'%(item)}, request),
                    base_url=base_url,
                    media_type=media_type
                ).render(stylesheets=[stylesheet])
            pdf_pages+=pdf_file.pages
        return html_page.copy(pdf_pages)

    def get(self, request,  *args, **kwargs):
        # html_template = loader.get_template('sample.html')
        # context = {'first_name':'DEMO', 'city': 'INDIA'}
        # return  HttpResponse(html_template.render(context, request))

        html_doc = self.get_html_doc(request,  *args, **kwargs)
        print ('===========================')

        print (html_doc)
        pdf_data = html_doc.write_pdf()
        response = PDFResponse(pdf_data,file_name='sample',status=status.HTTP_200_OK)
        response['Content-Disposition'] = 'filename="sample.pdf"'
        return response
