import pandas as pd
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from django.core.files.storage import FileSystemStorage
import os

def upload_file(request):
    summary = {}
    
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            uploaded_file = form.save()  # Save the uploaded file
            
            # Load the file using pandas
            file_path = uploaded_file.file.path
            
            # Determine file type and read data
            if uploaded_file.file.name.endswith('.csv'):
                data = pd.read_csv(file_path)
            elif uploaded_file.file.name.endswith('.xls') or uploaded_file.file.name.endswith('.xlsx'):
                data = pd.read_excel(file_path)
            else:
                # Handle unsupported file types
                return render(request, 'upload.html', {'form': form, 'error': 'Unsupported file type'})
            
            # Create summary: count occurrences of each column name
            for column in data.columns:
                summary[column] = {'count': data[column].count()}  # Get count of non-null entries
                
            # Pass summary to the template
            return render(request, 'summary.html', {'summary': summary})
    
    else:
        form = FileUploadForm()
    
    return render(request, 'upload.html', {'form': form})

def generate_summary(file_path):
    # Example summary logic; adapt based on your requirements
    data = pd.read_excel(file_path)  # Load Excel file (or use pd.read_csv for CSV)
    summary = {
        'Total Rows': len(data),
        'Column Names': list(data.columns),
        # Add more summary metrics as needed
    }
    return summary

def success(request):
    return render(request, 'fileuploadapp/success.html')
