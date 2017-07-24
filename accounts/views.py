from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import SignupForm, ProfileForm
from .models import Profile


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })


@login_required
def profile(request):
    # request.user
    return render(request, 'accounts/profile.html')


@login_required
def profile_edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)  # commit=False, form.save() 시에 model_instance.save() 를 호출하지 않도록 한다.
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_form.html', {
        'form': form,
    })
