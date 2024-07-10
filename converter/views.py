from django.shortcuts import render
from .forms import AmountForm
from .utils import number_to_words

def convert_amount(request):
    if request.method == 'POST':
        form = AmountForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            words_en = number_to_words(amount, 'en')
            words_hi = number_to_words(amount, 'hi')
            return render(request, 'converter/result.html', {
                'amount': amount,
                'words_en': words_en,
                'words_hi': words_hi
            })
    else:
        form = AmountForm()
    return render(request, 'converter/index.html', {'form': form})
