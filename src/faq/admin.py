from django.contrib import admin
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    def admin_question(self):
        return self.question

    def admin_answer(self):
        if len(self.answer) > 50:
            return self.answer[:50] + '...'
        return self.answer

    admin_question.short_description = 'Pergunta'
    admin_answer.short_description = 'Resposta'

    list_display = (
        admin_question,
        admin_answer,
    )

