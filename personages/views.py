from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from personages.models import Personage

from personages.forms import PersonageCreateForm


@login_required
def all_personages(request):
    all_personages = Personage.objects.filter(
        user_id=request.user)

    context = {
        'all_personages': all_personages,
    }

    return render(request, 'personages/all_personages.html', context=context)


# вариант FBV - Function Detailed View
def personage_details2(request, pk):
    get_personage_details = get_object_or_404(Personage, pk=pk)

    context = {
        'page_title': 'Detail title',
        'personage': get_personage_details,  # контекст следует называть четко по имени класса
    }

    return render(request, 'personages/personage_update.html', context=context)

def personage_create2(request):
    personage = Personage()

    context = {
        'page_title': 'Detail title',
        'personage': personage,  # контекст следует называть четко по имени класса
    }

    return render(request, 'personages/personage_create.html', context=context)

class PageTitleMixin:
    page_title = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


# вариант CBV - Class Detail View
class PersonageDetailView(PageTitleMixin, DetailView):
    # template_name = 'personages/personage_detail.html'  # автоматически вычисляется из имя класса + _detail
    model = Personage
    page_title = 'Personage detail'
    # pk_url_kwarg = 'pk' # нужно, если как primary key используется не 'pk' или 'slug'
    # context_object_name = 'personage_details' # можно переопределять, если нужен кастом,
    # но если не определено, за контекст берется имя класса
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            user_id=self.request.user
        )

class PersonageCreateView(LoginRequiredMixin, CreateView):
    model = Personage
    success_url = reverse_lazy('all_personages')
    form_class = PersonageCreateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


# class PersonageUpdateView(UserPassesTestMixin, UpdateView):
#     model = Personage
#     success_url = reverse_lazy('all_personages')
#     fields = '__all__'
#
#     def test_func(self):
#         print(self.request.user)
#         print(self.model.id)
#         print(self.model.user_id)
#         if self.request.user == self.model.user_id:
#             print("It's not your personage")


class PersonageUpdateView(LoginRequiredMixin, UpdateView):
    model = Personage
    success_url = reverse_lazy('all_personages')
    form_class = PersonageCreateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs