from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_has_ownship(func):
    def decorated(request,*args,**kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        print(kwargs)
        if not profile.user == request.user:
            return HttpResponseForbidden()
        else:
            return func(request, *args, **kwargs)
    return decorated
