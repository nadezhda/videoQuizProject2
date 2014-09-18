from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import CreateView, UpdateView, DeleteView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from django.contrib.auth.models import User

from equiz.models import *
from equiz.serializers import *
from equiz.permissions import IsOwnerOrReadOnly
from equiz.forms import UserForm, SectionForm, QuestionForm, QuestionFormSet
from rest_framework import viewsets


# TODO: Generate consistent home page
def homepage(request):
    return render(request, 'home.html', {'welcome_string': 'Welcome to main page of e-Quiz'})


class SectionList(APIView):
    """
    This view provides `list` of all sections
    """
    # queryset = Section.objects.all()
    # serializer_class = SectionSerializer
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

    def get(self, request):
        sections = Section.objects.all()
        categories = Category.objects.all()
        section_serializer = SectionSerializer(sections, many=True)
        return Response(
            {'sections': section_serializer.data, 'categories': categories},
            template_name='sections/sectionlist.html')


class SectionDetail(generics.ListCreateAPIView):
    """
    This view provides `retrieve` info about the section
    """
    queryset = Section.objects.all()
    # serializer_class = SectionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )

    def pre_save(self, obj):
        obj.owner = self.request.user

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'section': self.object}, template_name='sections/section.html')


# class OwnerSectionList(viewsets.ModelViewSet):
#     queryset = Section.objects.all()
#     serializer_class = SectionSerializer
#     renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
#
#     def list(self, request, *args, **kwargs):
#         response = super(OwnerSectionList, self).list(request, *args, **kwargs)
#         if request.accepted_renderer.format == 'html':
#             return Response({'sections': response.data}, template_name='owner_section_list.html')
#         return response

# Own sections
# -------------------------------------------------
class OwnerSectionList(generics.ListCreateAPIView):
    """
    This view provides `list` and `create` actions.
    """
    # queryset = Section.objects.all()
    serializer_class = SectionSerializer
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer, )
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def pre_save(self, obj):
        obj.owner = self.request.user

    # def get_queryset(self):
    #     """
    #     This view should return a list of all the sections
    #     for the currently authenticated user.
    #     """
    #     user = self.request.user
    #     return Section.objects.filter(owner=user)

    def list(self, request, *args, **kwargs):
        """
        This view should return a list of all the sections
        for the currently authenticated user.
        """
        user = self.request.user
        sections = Section.objects.filter(owner=user)

        section_serializer = SectionSerializer(sections, many=True)
        return Response(
            {'sections': section_serializer.data},
            template_name='own_sections/owner_section_list.html')


class OwnSectionCreate(CreateView):
    template_name = 'own_sections/section_create.html'
    # model = Section
    form_class = SectionForm
    success_url = reverse_lazy('owner-section-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnSectionCreate, self).form_valid(form)


class OwnSectionUpdate(UpdateView):

    template_name = 'own_sections/section_update.html'
    model = Section
    success_url = reverse_lazy('owner-section-list')


class OwnSectionDelete(DeleteView):
    template_name = 'own_sections/section_confirm_delete.html'
    model = Section
    success_url = reverse_lazy('owner-section-list')


class OwnerSectionDetail(generics.ListCreateAPIView):
    """
    This view provides `detail`, `create`,
   `update` and `destroy` actions.
    """
    queryset = Section.objects.all()
    # serializer_class = SectionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )

    def pre_save(self, obj):
        obj.owner = self.request.user

    def get(self, request, *args, **kwargs):
        """
        This view should return a list of all the sections
        for the currently authenticated user.
        """
        user = self.request.user
        self.object = self.get_object()
        # return Section.objects.filter(owner=user)
        return Response({'section': self.object}, template_name='own_sections/own_section.html')

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return Response({'section': self.object}, template_name='sections/section.html')

    # def list(self, request, *args, **kwargs):
    #     """
    #     This view should return a list of all the sections
    #     for the currently authenticated user.
    #     """
    #     user = self.request.user
    #     sections = Section.objects.filter(owner=user)
    #
    #     section_serializer = SectionSerializer(sections, many=True)
    #     return Response(
    #         {'sections': section_serializer.data},
    #         template_name='own_sections/owner_section_list.html')


# Questions
# -------------------------------------------------
class QuestionCreate(CreateView):
    template_name = 'own_sections/question_create.html'
    model = Question
    form_class = QuestionForm
    # success_url = reverse_lazy('owner-section-list')

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        question_form = QuestionFormSet()
        # section = Section.objects.filter(pk=kwargs['pk'])
        # section_serializer = SectionSerializer(section, many=True)
        # return self.render_to_response(self.get_context_data(form=form, question_form=question_form, section=section_serializer.data))
        return self.render_to_response(self.get_context_data(form=form, question_form=question_form))

    def dispatch(self, *args, **kwargs):
        self.section = get_object_or_404(Section, pk=kwargs['pk'])
        return super(QuestionCreate, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        question_form = QuestionFormSet(self.request.POST)

        # if "cancel" in request.POST:
        #     self.object = self.get_object()
        #     self.object.section = self.section
        #     self.object.save()
        #     return HttpResponseRedirect(self.get_success_url())

        if(form.is_valid() and question_form.is_valid()):
            return self.form_valid(form, question_form)
        else:
            return self.form_invalid(form, question_form)


    def form_valid(self, form, question_form):
        self.object = form.save(commit=False)
        self.object.section = self.section
        self.object.save()
        question_form.instance = self.object
        question_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, question_form):

        return self.render_to_response(
            self.get_context_data(form=form,
                                  question_form=question_form))

    def get_success_url(self):
        return reverse_lazy('owner-section-detail', kwargs={'pk': self.object.section.id})


class QuestionDelete(DeleteView):
    model = Question

    def get_success_url(self):
        return reverse_lazy('owner-section-detail', kwargs={'pk': self.object.section.id})



class UserList(generics.ListAPIView):
    """
    This view provides `list` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    This view provides `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class QuestionList(generics.ListAPIView):
#     """
#     This view provides `list` actions.
#     """
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#
#
# class QuestionDetail(generics.RetrieveAPIView):
#     """
#     This view provides `detail` actions.
#     """
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer


class CategoryList(APIView):
    """
    Returns a list of all categories.
    """
    # model = Category
    # serializer_class = CategorySerializer
    # queryset = Category.objects.all()
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request):
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return Response(
            {'categories': category_serializer.data},
            template_name='category_list.html')


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a single author.
    Also allows updating and deleting
    """
    # model = Category
    # serializer_class = CategorySerializer
    queryset = Category.objects.all()
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'category': self.object}, template_name='category_detail.html')

#
# class APIRoot(APIView):
#
#     def get(self, request):
#         # Assuming we have views named 'user-list' and 'section-list'
#         # in our project's URLconf.
#         return Response({
#             'users': reverse('user-list', request=request),
#             'sections': reverse('section-list', request=request)
#         })
#


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'sections': reverse('section-list', request=request, format=format),
        'owner-sections': reverse('owner-section-list', request=request, format=format)
    })

# class SectionViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list`,
#     and `retrieve` actions.
#     """
#     queryset = Section.objects.all()
#     serializer_class = SectionSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     def pre_save(self, obj):
#         obj.owner = self.request.user
#
#
# class MySectionViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list`, `create`, `retrieve`,
#     `update` and `destroy` actions.
#     """
#     queryset = Section.objects.all()
#     serializer_class = SectionSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
#
#     def pre_save(self, obj):
#         obj.owner = self.request.user
#
#     def get_queryset(self):
#         """
#         This view should return a list of all the sections
#         for the currently authenticated user.
#         """
#         user = self.request.user
#         return Section.objects.filter(owner=user)
#
#
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

             # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print
            user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response('register.html', {'user_form': user_form, 'registered': registered}, context)


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')


def qtests(request):
    return render(request, 'sections/tests.html', {'': ''})