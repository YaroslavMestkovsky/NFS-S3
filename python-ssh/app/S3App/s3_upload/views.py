from django.shortcuts import render, redirect, get_object_or_404
from .models import Document
from .forms import DocumentForm

def document_list(request):
    documents = Document.objects.all()
    return render(request, './documents/documents_list.html', {'documents': documents})

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, './documents/upload_document.html', {'form': form})

def delete_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    document.delete()
    return redirect('document_list')

def welcome(request):
    return render(request, './welcome.html')
