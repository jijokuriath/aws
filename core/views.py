from django.shortcuts import render
from django.http import HttpResponse
from core.models import Message

# Create your views here.
def msg(request):
	from django.template import Template, Context

	tmplt = """<ul>
	
			{% for msg in messages %}
			<li>
			{{msg.message}}
			</li>
			{% endfor %}

			</ul>"""

	t = Template(tmplt)
	c = Context({'messages':Message.objects.all()})
	
	return HttpResponse(t.render(c))