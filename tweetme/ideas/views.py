from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Idea
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.urls import reverse_lazy
from django.db.models import Q

class TweetDetailView(DetailView):
    template_name = "detail_view.html"
    queryset = Idea.objects.all()

    def get_object(self):
         # return Idea.objects.get(id=pk)
          print(self.kwargs)
          pk = self.kwargs.get("pk")
          obj = get_object_or_404(Idea, pk=pk)
          return obj

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Idea
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy("tweet:list")

class TweetListView(ListView):
    template_name = "list_view.html"
    # queryset = Idea.objects.all()
    # print(queryset)

    def get_queryset(self, *args, **kwargs):
        qs = Idea.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                    )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        #context["another_list"] = Tweet.objects.all()
        #print(context)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("tweet:create")
        return context



class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'create_view.html'
    success_url = "/tweet/create"
    login_url = '/admin/'
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(TweetCreateView, self).form_valid(form)



class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Idea.objects.all()
    form_class = TweetModelForm
    template_name = 'update_view.html'
    success_url = "/tweet/"






# # def tweet_detail_view(request, id=1):
#     obj = Idea.objects.get(id=id) # GET from database
#     print(obj)
#     # # # context = {
#        #  "object": obj
#    # #  }
#     return render(request, "detail_view.html", context)


# def tweet_list_view(request):
#     queryset = Idea.objects.all()
#     print(queryset)
#     for obj in queryset:
#         print(obj.content)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "list_view.html", context)