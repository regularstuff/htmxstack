import json
import pathlib
import pprint

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from . import aws_utils

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


def htmx_stack_synopsis_view(request, stack_file_name):
    stack_def = aws_utils.get_stack_as_dict(stack_file_name)
    resource_count = len(stack_def["StackResourceSummaries"])
    resource_names = [resource["LogicalResourceId"] for resource in stack_def["StackResourceSummaries"]]
    return render(request, "cfstack/htmlpart_stack_synopsis.html",
                  context=dict(stack_name=stack_file_name,
                               resource_count=resource_count,
                               resource_names=resource_names))

def emptydiv(request, div_id):
    return HttpResponse(f"<div id='#{div_id}'>")
