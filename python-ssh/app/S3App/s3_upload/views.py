import boto3
from django.shortcuts import render, redirect, get_object_or_404
from .models import Document
from .forms import DocumentForm
#from minio import Minio #todo не сильно нужно

def document_list(request):
    documents = Document.objects.all()
    return render(request, './documents/documents_list.html', {'documents': documents})

def upload_document(request):
    if request.method == 'POST':
        # s3 = boto3.client(
        #    's3',
        #    endpoint_url='http://minio:9000',
        #    aws_access_key_id='minio_root_user',
        #    aws_secret_access_key='minio_root_user',
        #    region_name=''
        # )
        # s3.upload_file('/app/S3App/s3_upload/file.txt', 'test-bucket', 'file.txt')
        #minio_client = Minio(
        #    "minio:9000",  # Адрес контейнера MinIO
        #    access_key="minio_root_user",  # Ваш MINIO_ROOT_USER
        #    secret_key="minio_root_user",  # Ваш MINIO_ROOT_PASSWORD
        #    secure=False  # Если MiniO работает через HTTP, указываем False
        #)

        #try:
        #    s3.upload_file('/app/S3App/s3_upload/file.txt', 'test-bucket', 'file.txt')
        #    print("File uploaded successfully")
        #except Exception as e:
        #    print(f"Failed to upload: {e}")

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
