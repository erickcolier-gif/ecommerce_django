from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            # Esto imprimirá los errores en tu terminal de VS Code si el registro falla
            print("Errores en el formulario:", form.errors)
    else:
        form = RegistroForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def profile(request):
    # Esta vista es protegida, solo entran usuarios logueados
    return render(request, 'core/profile.html')