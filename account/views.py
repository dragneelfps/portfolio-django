from django.shortcuts import render, redirect
from django.views import View

class LoginView(View):

    def get(self, request):
        return render(request, 'account/login.html')

    def post(self, request):
        if request.POST['email'] == 'dragneelfps@gmail.com' and request.POST['password'] == 'pass1234':
            # success
            request.session['is_logged_in'] = 'true'
            return redirect('home')
        else:
            return render(request, 'account/login.html', {
                'error': {
                    'title': 'Login failed',
                    'message': 'Incorrect credentials'
                }
            })

class LogoutView(View):

    def get(self, request):
        del request.session['is_logged_in']
        return redirect('home')

