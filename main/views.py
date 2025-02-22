from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    subjects = Subject.objects.all()
    return render(request, 'index.html', {'subjects':subjects})


def test_view(request, pk):
    subject = Subject.objects.get(id=pk)
    questions = Questions.objects.filter(subject_id=subject)

    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_answer = request.POST.get(str(question.id))
            if selected_answer:
                answer = Answers.objects.get(id=selected_answer)
                if answer.is_correct:
                    score += 1

        return render(request, 'result.html', {'score': score, 'total': questions.count()})

    return render(request, 'test.html', {'subject': subject, 'questions': questions})  