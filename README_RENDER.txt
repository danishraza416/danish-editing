DANISH EDITING - RENDER DEPLOYMENT

Files:
- app.py
- requirements.txt
- render.yaml

IMPORTANT:
Before publishing, open app.py and replace:
https://formsubmit.co/YOUR_EMAIL@example.com
with your own email address.

GITHUB:
1. Create a new GitHub repository.
2. Upload app.py, requirements.txt and render.yaml.
3. If you have photos/static files, upload them too.

RENDER:
1. Open Render.
2. New -> Web Service.
3. Connect the GitHub repository.
4. Build Command:
   pip install -r requirements.txt
5. Start Command:
   gunicorn app:app
6. Deploy.

After deployment Render gives you a public .onrender.com address.

NOTE:
The current editing app does not include the previously uploaded gallery photos.
Add your static/ folder to the GitHub repository if you want those photos online.
