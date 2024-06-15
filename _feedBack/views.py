from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import FeedBackSerializer
from utils.send_email import send_email

# Functions
@api_view(['POST'])
def postFeedBack(request) -> Response:
    serializer = FeedBackSerializer(data=request.data)

    if serializer.is_valid():
        # get full name and email
        full_name = request.data.get('full_name')
        email = request.data.get('email')

        # configure email data
        subject = "Feedback from slliks4 portfolio"
        admin_message = f"""Hey Skills :), you got a new feedback in your portfolio from {full_name}. Log in to your database to view the message. https://slliks4server.vercel.app/admin@slliks4-portfolio/_feedBack/feedback/"""
        user_message = f"""
Hi {full_name},

Thank you for reaching out and leaving your feedback. We have received your message and our team will review it shortly. Your input is valuable to us and helps us improve our services.

If you have any further questions or additional comments, feel free to reply to this email.

Best regards,
Skills Nwokolo Anthony
slliks4.vercel.app

Note: This is an automated response. Please do not reply to this email.
"""

        # Send email notification
        send_email(subject=subject, message=user_message, to_email=email)
        send_email(subject=subject, message=admin_message, to_email='skillsnwokolo372@gmail.com')

        # save request data
        serializer.save()
        
        return Response({'message': 'success'}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
