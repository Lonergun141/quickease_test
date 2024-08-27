from django.shortcuts import render
from .forms import UploadFileForm
import pypdfium2 as pdfium
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserNotes
from .serializers import UserNotesSerializer
from rest_framework import generics


# Create your views here.

def UploadFile(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        pdf = pdfium.PdfDocument(file)
        n_pages = len(pdf)
        for page_number in range(n_pages):
            page = pdf.get_page(page_number)
            pil_image = page.render().to_pil()
            pil_image.save(f"test_folder/image_{page_number+1}.png")
        
    else:
        form = UploadFileForm()
    return render(request, '../templates/uploads.html', {'form': form})

def UploadImage(request):
    pass

#User Notes

class UserNotesListCreateView(generics.ListCreateAPIView):
    serializer_class = UserNotesSerializer
    
    def get_queryset(self):
        return UserNotes.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class UserNotesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserNotesSerializer
    def get_queryset(self):
        return UserNotes.objects.filter(user=self.request.user)
