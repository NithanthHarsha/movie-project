class LoginRoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
       

    def __call__(self, request):
    
        if request.path.startswith('/manager/') or request.path.startswith('/admin/'):
            if request.user.is_authenticated:
                if hasattr(request.user, 'userprofile'):
                    if request.user.userprofile.role != 'manager'and not request.user.is_superuser:
                        from django.http import HttpResponseForbidden
                        return HttpResponseForbidden("You do not have permission to access this page.")
                else:
                    from django.http import HttpResponseForbidden
                    return HttpResponseForbidden("You do not have permission to access this page.")
            else:
                from django.shortcuts import redirect
                return redirect('login_user')
        response = self.get_response(request)



        return response