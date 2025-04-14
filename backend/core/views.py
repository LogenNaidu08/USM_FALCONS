# backend/core/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from openai import OpenAI  # Requires openai package

class ChatbotView(APIView):
    def post(self, request):
        user_message = request.data.get('message', '')
        
        # Initialize OpenAI client
        client = OpenAI(api_key="your-api-key")
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant for the USMFalcons football team. Answer questions about the team, players, fixtures, and history."},
                    {"role": "user", "content": user_message}
                ]
            )
            
            reply = response.choices[0].message.content
            return Response({'reply': reply})
            
        except Exception as e:
            return Response({'error': str(e)}, status=500)