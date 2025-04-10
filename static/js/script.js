const avatarInput = document.getElementById('avatarInput');
        const avatarPreview = document.getElementById('avatarPreview');

        avatarInput.addEventListener('change', (event) => {
            const file = event.target.files[0];
            if (file) {
                avatarPreview.src = URL.createObjectURL(file);
            }
        });

        const deleteAvatarButton = document.getElementById('deleteAvatarButton');
        deleteAvatarButton.addEventListener('click', () => {
            if (confirm('Вы уверены, что хотите удалить аватарку?')) {
                fetch("{% url 'delete_avatar' %}", { method: 'POST', headers: { 'X-CSRFToken': '{{ csrf_token }}' } })
                    .then(response => {
                        if (response.ok) {
                            avatarPreview.src = '/media/avatars/default.jpg'; // Укажите путь к аватарке по умолчанию
                        } else {
                            alert('Не удалось удалить аватарку.');
                        }
                    });
            }
        });