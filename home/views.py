from django.shortcuts import render
from django.http import JsonResponse
from dotenv import load_dotenv
import os
from groq import Groq  # Make sure `groq` is installed via pip

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def index(request):
    return render(request, 'index.html')

# Home page (renders index.html)
def assist(request):
    return render(request, 'assist.html')

# Handles the voice/chat prompt
def ask_groq(request):
    if request.method == 'POST':
        prompt = request.POST.get('message', '')  # match with `index.html` field

        try:
            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = response.choices[0].message.content
            return JsonResponse({'response': reply})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)
