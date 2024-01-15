import json
import pathlib
import pprint

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from . import aws_utils

def stack(request):
    dummy_stack_overview = """<UL><LI><a href="#">Resource 1</a></LI>
    <LI><a href="#">Resource 1</a></LI>
    <LI><a href="#">Resource 1</a></LI>
     """
    return render(request, "cfstack/cfstack.html",
                  dict(stack_overview=dummy_stack_overview,
                       page_title="This Title Seems Good Enough"),
                  )
def list_stacks_view(request):
    pagedata = dict(page_title="whatever",
                    stacks=aws_utils.get_stack_names())
    return render(request,
                  template_name="cfstack/stacklist.html",
                  context=pagedata)


def stack_contents_view(request, stack_file_name):
    base_dir = settings.BASE_DIR
    stacks_path = pathlib.Path(base_dir, "aws_mock_stacks")
    resources_file = stacks_path / stack_file_name
    with open(resources_file) as jsonstuff:
        return HttpResponse(pprint.pformat(json.load(jsonstuff)))





def htmx_stack_snyopsis_view(request, stack_file_name):
    return render(request, "cfstack/htmlpart_stack_synopsis.html",
                  context=dict(stack_name=stack_file_name))