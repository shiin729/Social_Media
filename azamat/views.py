from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            # Удаление аватарки, если выбран чекбокс
            if form.cleaned_data.get('clear_avatar'):
                request.user.profile.avatar.delete(save=False)
                request.user.profile.avatar = 'avatars/default.jpg'  # Установите аватарку по умолчанию
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})

@csrf_exempt
def delete_avatar(request):
    if request.method == 'POST':
        profile = request.user.profile
        profile.avatar.delete(save=False)
        profile.avatar = 'avatars/default.jpg'  # Установите аватарку по умолчанию
        profile.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)