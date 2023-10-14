from django.shortcuts import redirect


def gameParticipation(view_func):
    def wrapped_view(request, *args, **kwargs):
        if request.user.participation_math:
            # L'utilisateur est actif, exécutez la vue demandée
            return view_func(request, *args, **kwargs)
        else:
            # L'utilisateur n'est pas actif, redirigez-le vers la vue nommée "timeout"
            return redirect('timeout_math')
    
    return wrapped_view