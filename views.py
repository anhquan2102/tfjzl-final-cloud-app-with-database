from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

from .models import Choice, Question, Submission


@require_POST
def submit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice_id = request.POST.get("choice")
    selected_choice = get_object_or_404(Choice, pk=choice_id)
    Submission.objects.create(question=question, selected_choice=selected_choice)
    return render(request, "exam_result.html", {"question": question})


def show_exam_result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    submissions = Submission.objects.filter(question=question)
    correct_count = submissions.filter(selected_choice__is_correct=True).count()
    total_count = submissions.count()
    return render(
        request,
        "exam_result.html",
        {
            "question": question,
            "submissions": submissions,
            "correct_count": correct_count,
            "total_count": total_count,
        },
    )
