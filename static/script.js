document.addEventListener('DOMContentLoaded', () => {
    
    // Login Role Selection Logic
    const btnStudent = document.getElementById('btn-student');
    const btnAdmin = document.getElementById('btn-admin');
    const formStudent = document.getElementById('form-student');
    const adminModal = document.getElementById('admin-modal');
    const btnCancelAdmin = document.getElementById('btn-cancel-admin');
    const roleSelector = document.querySelector('.role-selector');

    if (btnStudent && btnAdmin) {
        btnStudent.addEventListener('click', () => {
            // Add a little click animation before submitting
            btnStudent.style.transform = 'scale(0.95)';
            setTimeout(() => {
                formStudent.submit();
            }, 150);
        });

        btnAdmin.addEventListener('click', () => {
            roleSelector.style.display = 'none';
            adminModal.style.display = 'block';
            document.getElementById('password').focus();
        });

        btnCancelAdmin.addEventListener('click', () => {
            adminModal.style.display = 'none';
            roleSelector.style.display = 'flex';
        });
    }

    // Toast Notification Logic
    const toasts = document.querySelectorAll('.toast');
    
    toasts.forEach(toast => {
        const closeBtn = toast.querySelector('.toast-close');
        
        // Auto dismiss after 5 seconds
        const timeoutId = setTimeout(() => {
            dismissToast(toast);
        }, 5000);

        // Manual dismiss
        closeBtn.addEventListener('click', () => {
            clearTimeout(timeoutId);
            dismissToast(toast);
        });
    });

    function dismissToast(toast) {
        toast.style.animation = 'fadeOutRight 0.4s forwards';
        setTimeout(() => {
            toast.remove();
        }, 400);
    }
});
