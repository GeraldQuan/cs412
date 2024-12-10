from django import forms
from .models import Book, Borrower, Reminder, Review


class BookForm(forms.ModelForm):
    """
    Form for creating or updating a Book instance.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'year_published', 'category', 'is_borrowed']
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'genre': 'Genre',
            'year_published': 'Year Published',
            'category': 'Category',
            'is_borrowed': 'Is Borrowed?',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter genre'}),
            'year_published': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter year'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'is_borrowed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class BorrowerForm(forms.ModelForm):
    """
    Form for adding or updating a Borrower instance.
    """
    class Meta:
        model = Borrower
        fields = ['book', 'borrower_name', 'borrow_date', 'return_date']
        labels = {
            'book': 'Book',
            'borrower_name': 'Borrower Name',
            'borrow_date': 'Borrow Date',
            'return_date': 'Return Date',
        }
        widgets = {
            'book': forms.Select(attrs={'class': 'form-control'}),
            'borrower_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter borrower name'}),
            'borrow_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Select borrow date'}
            ),
            'return_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Select return date'}
            ),
        }


class ReminderForm(forms.ModelForm):
    """
    Form for creating or updating a Reminder instance.
    """
    class Meta:
        model = Reminder
        fields = ['book', 'reminder_date', 'notes']
        labels = {
            'book': 'Book',
            'reminder_date': 'Reminder Date',
            'notes': 'Additional Notes',
        }
        widgets = {
            'book': forms.Select(attrs={'class': 'form-control'}),
            'reminder_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Select reminder date'}
            ),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Add any additional notes here...',
            }),
        }


class ReviewForm(forms.ModelForm):
    """
    Form for adding or updating a Review instance.
    """
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        labels = {
            'rating': 'Rating (1-5)',
            'comment': 'Your Review',
        }
        widgets = {
            'rating': forms.Select(
                choices=[(i, i) for i in range(1, 6)],
                attrs={'class': 'form-control'}
            ),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your review here...',
            }),
        }

    def clean_rating(self):
        """
        Validate that the rating is between 1 and 5.
        """
        rating = self.cleaned_data.get('rating')
        if not (1 <= rating <= 5):
            raise forms.ValidationError('Rating must be between 1 and 5.')
        return rating
