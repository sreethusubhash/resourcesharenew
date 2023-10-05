from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count
from . models import Resources,Category
from apps.user.models import User
from .utils import generate_cat_count_list
from .form import PostResourceForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_page(request):
    cnt = Resources.objects.all().count()
    user_cnt = User.objects.filter(is_active=True).count()
    res_per_cat = Resources.objects.values("cat_id__cat").annotate(cnt=Count("cat_id"))
    context={'cnt':cnt,
             'user_cnt':user_cnt,
             'res_per_cat':res_per_cat}
    return render(request=request,
                  template_name='resources/home.html',
                  context=context)
def resource_detail_old(request):
    res = (Resources.objects.select_related
    ('user_id','cat_id')
    .prefetch_related('tags').get(pk=id))
    #review = res.tags.all()
   # avg_rate=
    context={'res':res}
             #,'review':review.count(),'avg_rate':avg_rate}
    return render(request=request,
                  template_name='resources/detail.html',
                  context=context)
    

def home_page_old(request):
    cnt = Resources.objects.all().count()
    user_cnt = User.objects.filter(is_active=True).count()
    res_per_cat = Resources.objects.values("cat_id__cat").annotate(cnt=Count("cat_id"))
    
    response=f"""
    <html>
        <h1>Welcome to ResourceShare</h1>
        
        <h3>Number of Active users</h3>
        <p> {cnt} resources and counting!</p>
        <p> {user_cnt} users and counting</p>
        
         <h3>Resources per Category</h3>
         <ol>
            {generate_cat_count_list(res_per_cat)}
         </ol>
    </html>
  """
    return HttpResponse(response)


@login_required   
def resource_detail(request, id):
    max_viewed_resources=5
    viewed_resources=request.session.get('viewed_resources',[])
    
    #res = Resources.objects.get(pk=id)
    #res = Resources.objects.select_related('user_id').get(pk=id)
    #res = Resources.objects.select_related('user_id','cat_id').get(pk=id)
    res = (Resources.objects.select_related
    ('user_id','cat_id').prefetch_related('tags').get(pk=id))
    
    #prepare data
    viewed_resource=[id,res.title]
    #check if that data exist already in session and remove it
    if viewed_resource in viewed_resources:
        viewed_resources.remove(viewed_resource)
    #Add it as first item in the list
    viewed_resources.insert(0,viewed_resource)
    #Get limit of viewed resources
    viewed_resources=viewed_resources[:max_viewed_resources]
    #add it back in the session
    request.session['viewed_resources']=viewed_resources
    
    
    response = f"""
        <html>
            <h1>{res.title}</h1>
            <p><b>User</b>: {res.user_id.username}</p>
            <p><b>Tags</b>: {res.all_tags()}</p>
            <p><b>Link</b>: {res.link}</p>
            <p><b>Category</b>: {res.cat_id.cat}</p>
            <p><b>Description</b>: {res.description}</p>
        </html>
    """
    return HttpResponse(response)
def resource_post_old(request):
    #breakpoint()
    return render(request,'resources/post.html')
 
@login_required   
def resource_post(request):
    #breakpoint()
    #return render(request,'resources/post.html')
    #Unbound#user made a GET request
    if request.method == 'GET':
        form=PostResourceForm()
        return render(request,
        'resources/resource_post.html',
            {'form':form}
            )
     #
    #Bound#user made a POST request
    else:
        #info={'title':'title','link':'link','description':'description',}
        form=PostResourceForm(request.POST)
        #form=PostResourceForm(info)
        #validation
        #.is_valid() method
        #.cleaned_data() method
        if form.is_valid():
            data=form.cleaned_data
            #manually add a user id
            #save it to db
            #redirect the user to the home page
        else:
            pass
  
    
class HomePage(TemplateView):
    template_name='home_page.html'
