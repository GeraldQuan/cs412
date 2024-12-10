// Display an alert message when a form is submitted
document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', (event) => {
            if (!confirm('Are you sure you want to submit this form?')) {
                event.preventDefault(); // Prevent form submission
            }
        });
    });
});

// Toggle visibility of elements (e.g., for error/success messages)
function toggleVisibility(id) {
    const element = document.getElementById(id);
    if (element) {
        element.style.display = (element.style.display === 'none' || !element.style.display) ? 'block' : 'none';
    }
}

// Highlight table rows on hover
document.addEventListener('DOMContentLoaded', () => {
    const rows = document.querySelectorAll('table tr');

    rows.forEach(row => {
        row.addEventListener('mouseenter', () => {
            row.style.backgroundColor = '#f1f1f1';
        });

        row.addEventListener('mouseleave', () => {
            row.style.backgroundColor = '';
        });
    });
});

// Add client-side validation for forms
document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', (event) => {
            const inputs = form.querySelectorAll('input, textarea, select');
            let valid = true;

            inputs.forEach(input => {
                if (input.required && !input.value.trim()) {
                    input.style.borderColor = 'red';
                    valid = false;
                } else {
                    input.style.borderColor = '';
                }
            });

            if (!valid) {
                event.preventDefault(); // Prevent form submission if validation fails
                alert('Please fill in all required fields.');
            }
        });
    });
});

// Dismiss alert messages after 5 seconds
document.addEventListener('DOMContentLoaded', () => {
    const alerts = document.querySelectorAll('.alert');

    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.display = 'none';
        }, 5000);
    });
});
