from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import fitz  # PyMuPDF

class PdfUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('pdf')
        if not file:
            return Response({'error': 'No file uploaded'}, status=400)
        
        # Save the file
        file_name = default_storage.save(file.name, ContentFile(file.read()))
        file_path = default_storage.path(file_name)
        
        try:
            # Process the PDF file
            document = fitz.open(file_path)
            pdf_data = {"pages": []}
            
            for page_num in range(len(document)):
                page = document.load_page(page_num)
                blocks = page.get_text("blocks")  # Extract text blocks with layout info
                page_data = {"page_number": page_num + 1, "blocks": []}

                for block in blocks:
                    block_data = {
                        "bbox": block[:4],  # The bounding box of the block
                        "text": block[4]    # The text within the block
                    }
                    page_data["blocks"].append(block_data)

                pdf_data["pages"].append(page_data)
            
            # Delete the file after processing
            default_storage.delete(file_name)

            return Response(pdf_data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
