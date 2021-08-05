from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.http import HttpResponse
from .models import Post, Comment, Category
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Count
from django.http import HttpResponse, JsonResponse
import json

# from django.utils.html import strip_spaces_between_tags, strip_tags
# Create your views here.

def screengolf(request):
    return render(request, 'board/screengolf.html')



def golfrule(request):
    return render(request, 'board/golfrule.html')

def show_category(request):
    return render(request, 'board/category.html', {'category': Category.objects.all()})

def board(request):
    categoryall = Category.objects.all()
    category = Category.objects.all()
    popular_post_list = Post.objects.annotate(num_comment=Count('comment')).order_by('-num_comment', '-create_date')
    popular_post_list = popular_post_list[:3]
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    so = request.GET.get('so', '')  # 정렬기준
    print("so=", so)
    print("page=", page)
    print("kw=", kw)
   
     # 정렬
    if so == 'recommend':        
        post_list = Post.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        post_list = Post.objects.annotate(num_comment=Count('comment')).order_by('-num_comment', '-create_date')
    else:  # recent
        post_list = Post.objects.order_by('-create_date')
  
    if kw:
        post_list = post_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(comment__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

      
    paginator = Paginator(post_list, 4)  # 페이지당 4개씩 보여주기
    page_obj = paginator.get_page(page)


    context = {'post_list': page_obj, 'page': page, 'kw': kw, 'so': so, 'category': category,'categoryall': categoryall, 'popular_post_list': popular_post_list}
    

    return render(request, 'board/post_list.html', context)

def board_category(request, category_id):
    categoryall = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    popular_post_list = Post.objects.annotate(num_comment=Count('comment')).order_by('-num_comment', '-create_date')
    popular_post_list = popular_post_list[:3]
    page = request.GET.get('page', '1')  # 페이지
    print("categorypage=", page)
    kw = request.GET.get('kw', '')  # 검색어

    so = request.GET.get('so', 'recent')  # 정렬기준

     # 정렬
    if so == 'recommend':        
        post_list = Post.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        post_list = Post.objects.annotate(num_comment=Count('comment')).order_by('-num_comment', '-create_date')
    else:  # recent
        post_list = Post.objects.order_by('-create_date')
  
    if kw:
        post_list = post_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(comment__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()
    
    # post_list = post_list.get_descendants(include_self=True)
    post_list = post_list.filter(category__in=Category.objects.get(pk=category_id).get_descendants(include_self=True))
    
    paginator = Paginator(post_list, 4)  # 페이지당 4개씩 보여주기
    page_obj = paginator.get_page(page)
    print("category pagenater")


    context = {'post_list': page_obj, 'page': page, 'kw': kw, 'so': so, 'category': category,'categoryall': categoryall,'popular_post_list': popular_post_list}
    

    return render(request, 'board/post_list.html', context)





def detail(request, post_id):

    categoryall = Category.objects.all()
    category = Category.objects.all()
    popular_post_list = Post.objects.annotate(num_comment=Count('comment')).order_by('-num_comment', '-create_date')
    popular_post_list = popular_post_list[:3]
    





    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post, 'popular_post_list': popular_post_list, 'category': category,'categoryall': categoryall, }
    return render(request, 'board/post_detail.html', context)

def comment_create(request, post_id):
    
    post = get_object_or_404(Post, pk=post_id)



    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now()
            comment.post = post
            comment.author = request.user
            comment.save()
            # return redirect('board:detail', post_id=post.id)
            return redirect('{}#comment_{}'.format(
                resolve_url('board:detail', post_id=post.id), comment.id))
    else:
        form = CommentForm()
    context = {'post': post, 'form': form}
    return render(request, 'board/post_detail.html', context)
    
def index(request):
   return render(request, 'common/login_success.html')

@login_required(login_url='common:login')
def post_create(request):

    # ca = request.POST.get('category', '') 
   
    # if ca == '골프':
    #     category = Category.objects.get(pk=1)
    # elif ca == '식물':
    #     category = Category.objects.get(pk=2)
    # elif ca == '여행':
    #     category = Category.objects.get(pk=3)
    # else:
    #     category = Category.objects.get(pk=4)
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.author = request.user
            

            # post.category = category
            post.save()

            for headimage in request.FILES.getlist('head_image'):
               post.head_image = headimage
               post.save()



           
            return redirect('board:board')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'board/post_form.html', context)

@login_required(login_url='common:login')
def post_modify(request, post_id):
    
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('board:detail', post_id=post.id)
    
    # ca = request.POST.get('category', '') 
    # if ca == '골프':
    #     category = Category.objects.get(pk=1)
    # elif ca == '식물':
    #     category = Category.objects.get(pk=2)
    # elif ca == '여행':
    #     category = Category.objects.get(pk=3)
    # else:
    #     category = Category.objects.get(pk=4)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.modify_date = timezone.now()  # 수정일시 저장
            # post.category = category
            post.save()
            for headimage in request.FILES.getlist('head_image'):
               post.head_image = headimage
               post.save()
            return redirect('board:detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'board/post_form.html', context)

@login_required(login_url='common:login')
def post_delete(request, post_id):
   
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('board:detail', post_id=post.id)
    post.delete()
    return redirect('board:board')

@login_required(login_url='common:login')
def comment_modify(request, comment_id):
 
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('board:detail', post_id=comment.post.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            # return redirect('board:detail', post_id=comment.post.id)
            return redirect('{}#comment_{}'.format(
                resolve_url('board:detail', post_id=comment.post.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'board/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete(request, comment_id):
   
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect('board:detail', post_id=comment.post.id)

@login_required(login_url='common:login')
def vote_post(request, post_id):
    
    post = get_object_or_404(Post, pk=post_id)
    if request.user == post.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        post.voter.add(request.user)
        # context = {'like_count': post.voter.count()}
    # return HttpResponse(json.dumps(context), content_type='application/json')
    return redirect('board:detail', post_id=post.id)


    




@login_required(login_url='common:login')
def vote_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        comment.voter.add(request.user)
    return redirect('board:detail', post_id=comment.post.id)
