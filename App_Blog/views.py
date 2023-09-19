from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView,View,TemplateView

from App_Blog import models
from App_Blog.models import Blog,Comment,Likes
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from App_Blog.forms import CommentForm


# def blog_list(request):
#     return render(request,'blog_list.html',context={})



class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'create_blog.html'
    fields = ['blog_title', 'blog_content','blog_image']

    # def get_success_url(self):
    #     return reverse('App_Blog:blog_list')



    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug="aaaaa"
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('App_Blog:blog_list'))


class BlogList(ListView):
    context_object_name = 'blogs'
    model=Blog
    template_name = "blog_list.html"


@login_required
def blog_details(request,slug):
    blog=Blog.objects.get(slug=slug)
    comment_form= CommentForm()

    already_liked=Likes.objects.filter(blog=blog,user=request.user)
    if already_liked:
        liked= True
    else:
        liked=False

    if request.method=='POST':
        comment_form=CommentForm(request.POST)

        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.user=request.user
            comment.blog=blog
            comment.save()
            return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug':slug}))


    return render(request,'blog_details.html',context={'blog':blog,'comment_form':comment_form, 'liked':liked})




@login_required
def liked(reqest,pk):
    blog=Blog.objects.get(pk=pk)
    user=reqest.user
    already_like=Likes.objects.filter(blog=blog,user=user)
    if not already_like:
        liked_post=Likes(blog=blog,user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug': blog.slug}))



@login_required
def unliked(reqest,pk):
    blog=Blog.objects.get(pk=pk)
    user = reqest.user
    already_like = Likes.objects.filter(blog=blog, user=user)
    already_like.delete()
    return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug': blog.slug}))



class MyBloges(LoginRequiredMixin,TemplateView):
    template_name = "my_blogs.html"




class UpdateBlog(LoginRequiredMixin,UpdateView):
    model=Blog
    fields=['blog_title','blog_content','blog_image']
    template_name = 'edit_blog.html'

    def get_queryset(self):
        queryset = Blog.objects.order_by('-id')
        return queryset

    def get_success_url(self, **kwargs):
        return reverse_lazy('App_Blog:blog_details',kwargs={'slug':self.object.slug})

