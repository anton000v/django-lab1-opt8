from django.shortcuts import render
from django.views import View
from .models import Question
from django.http import JsonResponse, Http404

class IndexPage(View):
    def get(self, request):
        all_questions = Question.objects.all()
        context = {
            'all_questions': all_questions,
        }
        return render(request,'Lab1/index.html', context=context)

class CheckAnswer(View):
    def get(self, request):
        pass
        if request.is_ajax():
            id = request.GET.get('id')
            answer = request.GET.get('answer')
            print(id+' ' + answer)
            if (q := Question.objects.get(id=id)).is_answer_right(answer):
                q.incr_right_counter()
                q.save()
                return JsonResponse({'message':'Правильно!'})
            else:
                q.incr_wrond_counter()
                q.save()
                return JsonResponse({'message':'Неправильно!'})
        else:
            raise Http404

class AdminPage(View):
    def get(self, request):
        if request.user.is_superuser:
            all_questions = Question.objects.all()
            context = {
                'all_questions': all_questions,
            }
            return render(request,'Lab1/admin.html', context=context)
        else:
            raise Http404