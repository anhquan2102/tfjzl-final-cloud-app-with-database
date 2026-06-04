from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

from .models import Choice, Question, Submission


@require_POST
def submit(request, course_id):
    question_id = request.POST.get("question_id")
    choice_id = request.POST.get("choice")
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = get_object_or_404(Choice, pk=choice_id)
    submission = Submission.objects.create(
        question=question,
        selected_choice=selected_choice,
    )
    return render(
        request,
        "exam_result.html",
        {"question": question, "submission": submission, "course_id": course_id},
    )


def show_exam_result(request, course_id, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    question = submission.question
    submissions = Submission.objects.filter(question=question)
    correct_count = submissions.filter(selected_choice__is_correct=True).count()
    total_count = submissions.count()
    return render(
        request,
        "exam_result.html",
        {
            "question": question,
            "submission": submission,
            "course_id": course_id,
            "submissions": submissions,
            "correct_count": correct_count,
            "total_count": total_count,
        },
    )
