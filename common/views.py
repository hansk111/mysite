from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import RegisterForm
from django.views.generic import View

# Create your views here.
def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.user_image = request.FILES['user_image']
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'common/signup.html', {'form': form})

def page_not_found(request, exception):

    return render(request, 'common/404.html', {})

# class KakaoSignInView(View):
#     def get(self, request):
#         app_key = 'dd99876cc36043c5db37fcb1310f3ca7'
#         redirect_url = 'http://localhost:8000/users/signin/kakao/callback'
#         kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?response_type=code'
#         return redirect(f'{kakao_auth_api}&client_id={app_key}&redirect_url={redirect_url}')
def kakao_login(request):
    app_rest_api_key = os.environ.get("KAKAO_REST_API_KEY")
    redirect_uri = main_domain + "accounts/kakao/login/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={'dd99876cc36043c5db37fcb1310f3ca7'}&redirect_uri={'http://localhost:8000/accounts/kakao/login/callback'}&response_type=code"
    )
