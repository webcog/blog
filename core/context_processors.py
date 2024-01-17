from core.models import Profile

def profile_img(request):
    profile = Profile.objects.all()
    return{'profile': profile}
