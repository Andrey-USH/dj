import django_filters
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from office.models import Staff, Department


class General(ListView):
    model = Staff
    template_name = 'office/get_list.html'
    context_object_name = 'staffs'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class GetDep(ListView):
    model = Staff
    template_name = 'office/get_list.html'
    context_object_name = 'staffs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Department.objects.get(pk=self.kwargs['department_id'])
        return context

    def get_queryset(self):
        return Staff.objects.filter(department_id=self.kwargs['department_id'])


class Detail(DetailView):
    model = Staff


class StartFilter(django_filters.FilterSet, DetailView):
    class Meta:
        model = Staff
        fields = ['lastname']


def filter_symbol(request):
    letter_filter = Q()
    if 'a' in request.GET:
        for letter in 'АБВГ':
            letter_filter |= Q(lastname__startswith=letter)
        f = StartFilter(request.GET, queryset=Staff.objects.filter(letter_filter))
        return render(request, 'office/staff_list.html', {'filter': f})

    if 'b' in request.GET:
        for letter in 'ДЕЁЖ':
            letter_filter |= Q(lastname__startswith=letter)
        f = StartFilter(request.GET, queryset=Staff.objects.filter(letter_filter))
        return render(request, 'office/staff_list.html', {'filter': f})

    if 'c' in request.GET:
        for letter in 'ЛМНОП':
            letter_filter |= Q(lastname__startswith=letter)
        f = StartFilter(request.GET, queryset=Staff.objects.filter(letter_filter))
        return render(request, 'office/staff_list.html', {'filter': f})

    if 'd' in request.GET:
        for letter in 'ЛМНОП':
            letter_filter |= Q(lastname__startswith=letter)
        f = StartFilter(request.GET, queryset=Staff.objects.filter(letter_filter))
        return render(request, 'office/staff_list.html', {'filter': f})

    if 'e' in request.GET:
        for letter in 'РСТУ':
            letter_filter |= Q(lastname__startswith=letter)
        f = StartFilter(request.GET, queryset=Staff.objects.filter(letter_filter))
        return render(request, 'office/staff_list.html', {'filter': f})

    if 'f' in request.GET:
        for letter in 'ФХЦЧШЩЭЮЯ':
            letter_filter |= Q(lastname__startswith=letter)
        f = StartFilter(request.GET, queryset=Staff.objects.filter(letter_filter))
        return render(request, 'office/staff_list.html', {'filter': f})
    else:
        all_items = Staff.objects.all()
        return render(request, 'office/staff_list.html', {'all_items': all_items})
