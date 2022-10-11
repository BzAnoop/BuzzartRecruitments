from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

def take_quiz(request,id):
    if request.method == 'POST':
        quiz = get_object_or_404(models.LanguageQuiz, pk=id)
        sitting = get_object_or_404(models.Sitting, quiz=quiz, user=request.user)
        for k,v in request.POST.iteritems():
            if 'choice-for' in k:
                q = Question.objects.get(pk=k.split('-')[-1])
                choice = Choice.objects.get(pk=v)
                sitting_question = get_object_or_404(SittingQuestion,sitting=sitting,question=q)
                sitting_question.answer = choice
                sitting_question.save()
        correct_answers = len([x for x in sitting.sitting_questions.all() if x.answer.correct])
        result = float(correct_answers)/sitting.sitting_questions.all().count() * 100

        return render(request,'quiz/result.html',context={'result':result,
                                                          'level':level,
                                                          'quiz':quiz})

    if request.method == 'GET':

        with transaction.atomic():
            quiz = get_object_or_404(models.LanguageQuiz, pk=id)

            if models.Sitting.objects.filter(quiz=quiz, user=request.user).exists():
                sitting = get_object_or_404(models.Sitting, quiz=quiz, user=request.user)
                check_expired_sitting(sitting)
                sitting.delete()

            sitting = models.Sitting.objects.create(quiz=quiz, user=request.user)
            sitting.load_questions()

        questions = [x.question for x in sitting.sitting_questions.all()]
        paginator = Paginator(questions,2)
        page_num = request.GET.get('page',1)
        page = paginator.page(page_num)

        context = {'page':page,
                   'quiz':quiz}

        return render(request,'quiz/quiz.html',context=context)