from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views import generic

from polls.models import Poll, Choice

# def index(request):
#     latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#     context = {'latest_poll_list': latest_poll_list}
#     return render(request, 'polls/index.html', context)

# def detail(request, poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/detail.html', {'poll': poll})
#     # try:
#     #     poll = Poll.objects.get(pk=poll_id)
#     # except Poll.DoesNotExist:
#     #     raise Http404
#     # return render(request, 'polls/detail.html', {'poll': poll})

# def results(request, poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/results.html', {'poll': poll})

# def vote(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'poll': p,
#             'error_message': "You didn't select a choice.",
#             })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'
    def get_queryset(self):
        return Poll.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Poll
    template_name = "polls/results.html"


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def func_test():
    a = "msg132"
    if a:
        print a
    else:
        print "Hello Python"

class AboutView(generic.TemplateView):
    template_name = "polls/about.html"

