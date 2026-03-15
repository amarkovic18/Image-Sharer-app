from django.views.generic import TemplateView, DetailView, FormView
from .models import Post
from .forms import AddForm
from django.contrib import messages



class HomePage(TemplateView):
    template_name="home.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['posts']=Post.objects.all()
        return context
class AddDetail(DetailView):
    template_name="detail.html"
    model=Post
class FormPage(FormView):
    template_name="post.html"
    form_class=AddForm
    success_url="/"
    
    def dispatch(self,request,*args,**kwargs):
        self.request=request
        return super().dispatch(request,*args,**kwargs)
    def form_valid(self,form):
        new_post=Post.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image']

        )
        messages.add_message(self.request, messages.SUCCESS,"Your upload was successful!")
        return super().form_valid(form)



        



