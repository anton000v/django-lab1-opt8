from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length = 150, verbose_name="Вопрос")
    question_answer = models.CharField(max_length=50, verbose_name='Ответ')
    right_answers_counter = models.PositiveSmallIntegerField(default=0, verbose_name='Правильных ответов')
    wrong_answers_counter = models.PositiveSmallIntegerField(default=0, verbose_name='Неправильных ответов')

    def __str__(self):
        return self.question_text


    def is_answer_right(self, answer):
        if answer == self.question_answer:
            return True
        return False
    
    def incr_right_counter(self):
        self.right_answers_counter += 1

    def incr_wrond_counter(self):
        self.wrong_answers_counter += 1

