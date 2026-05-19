# Full Stack Deployment Guide - Learning Copilot

This document provides detailed instructions for deploying the entire Learning Copilot application (frontend + backend) to Vercel.

## Architecture

The application is now structured as a monorepo:
```
Anti_3/
├── frontend/          # React app (builds to dist/)
├── backend/           # Flask API server
├── vercel.json        # Vercel deployment config
├── package.json       # Root scripts
└── .gitignore         # Git configuration
```

**How it works on Vercel:**
1. Frontend (React/Vite) builds to `frontend/dist/`
2. Backend (Flask) serves the frontend build files as static assets
3. Backend API routes (`/api/*`) serve JSON responses
4. Single domain serves both frontend and API
5. SPA routing automatically redirects non-API routes to index.html

## Prerequisites

- GitHub account with repository
- Vercel account (free at vercel.com)
- Firebase project configured
- Groq API key

## Step-by-Step Deployment

### Step 1: Prepare Your Repository

```bash
# Navigate to project root
cd Anti_3

# Initialize Git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - full stack setup"

# Add your GitHub remote
git remote add origin https://github.com/YOUR_USERNAME/learning-copilot.git

# Push to GitHub
git push -u origin main
```

### Step 2: Configure Environment Variables Locally

Create `.env` files for local testing:

**backend/.env:**
```env
SECRET_KEY=your-dev-secret-key
DEBUG=False

FIREBASE_CREDENTIALS_JSON={"type":"service_account","project_id":"learn-31e25",...}
GROQ_API_KEY=gsk_xxxxxxxxxxxx
UPLOAD_FOLDER=uploads
VECTOR_STORE_PATH=vector_stores
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:5000
```

**frontend/.env:**
```env
VITE_FIREBASE_API_KEY=AIzaSy...
VITE_FIREBASE_AUTH_DOMAIN=learn-31e25.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=learn-31e25
VITE_FIREBASE_STORAGE_BUCKET=learn-31e25.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=661588498776
VITE_FIREBASE_APP_ID=1:661588498776:web:...
VITE_API_URL=http://localhost:5000/api
```

### Step 3: Test Locally

**Terminal 1 - Backend:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows or source venv/bin/activate on Mac/Linux
pip install -r requirements.txt
python app.py
# Backend runs on http://localhost:5000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm run dev
# Frontend runs on http://localhost:5173
```

**Terminal 3 - Build test (optional):**
```bash
cd frontend
npm run build
# Creates dist/ folder with production build
```

Verify:
- Frontend accessible at http://localhost:5173
- Backend API at http://localhost:5000/api/health
- Login works with Google Auth
- No console errors

### Step 4: Deploy to Vercel

1. **Go to [Vercel Dashboard](https://vercel.com/dashboard)**

2. **Click "New Project"**

3. **Import Repository**
   - Select "GitHub" → "Continue"
   - Authorize Vercel to access your GitHub
   - Select your `learning-copilot` repository
   - Click "Import"

4. **Vercel will auto-detect the monorepo**
   - Root Directory: `.` (root)
   - Framework: `Other` (custom setup)
   - Build Command: `npm run build && npm run build:backend`
   - Install Command: `npm install && cd frontend && npm install && cd ../backend && pip install -r requirements.txt`

5. **Add Environment Variables**
   - Click "Environment Variables"
   - Add each variable from your `.env` files:

**Environment Variables to Add:**

| Name | Value | Type |
|------|-------|------|
| `FIREBASE_CREDENTIALS_JSON` | `{"type":"service_account",...}` | Production |
| `GROQ_API_KEY` | `gsk_xxxxxxxxxxxx` | Production |
| `SECRET_KEY` | `your-production-secret-key` | Production |
| `DEBUG` | `False` | Production |
| `UPLOAD_FOLDER` | `uploads` | Production |
| `VECTOR_STORE_PATH` | `vector_stores` | Production |
| `ALLOWED_ORIGINS` | `https://your-vercel-domain.vercel.app` | Production |
| `VITE_FIREBASE_API_KEY` | `AIzaSy...` | Production |
| `VITE_FIREBASE_AUTH_DOMAIN` | `learn-31e25.firebaseapp.com` | Production |
| `VITE_FIREBASE_PROJECT_ID` | `learn-31e25` | Production |
| `VITE_FIREBASE_STORAGE_BUCKET` | `learn-31e25.appspot.com` | Production |
| `VITE_FIREBASE_MESSAGING_SENDER_ID` | `661588498776` | Production |
| `VITE_FIREBASE_APP_ID` | `1:661588498776:web:...` | Production |
| `VITE_API_URL` | `https://your-vercel-domain.vercel.app/api` | Production |

6. **Click "Deploy"**

Vercel will now:
- Clone your repository
- Install dependencies
- Build the frontend
- Prepare the backend
- Deploy everything

### Step 5: Verify Deployment

1. **Wait for build to complete**
   - Vercel will show build logs
   - Look for ✓ marks for success

2. **Test your app**
   - Go to `https://your-vercel-domain.vercel.app`
   - You should see the Learning Copilot app
   - Test login with Google
   - Check console for any errors

3. **Test API endpoints**
   - Visit `https://your-vercel-domain.vercel.app/api/health`
   - Should return `{"status":"healthy"...}`

4. **Monitor Logs**
   - Go to Vercel Dashboard → Select your project
   - Click "Logs" tab to see real-time logs
   - Check for any errors or warnings

## Post-Deployment

### Update Firebase Auth Redirect URI

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project
3. Go to **Authentication → Settings → Authorized domains**
4. Add your Vercel domain: `your-vercel-domain.vercel.app`

### Update Google OAuth Credentials

If you're using Google Auth:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select your project
3. Go to **APIs & Services → Credentials**
4. Find your OAuth 2.0 Client ID
5. Click to edit
6. Add to **Authorized JavaScript origins:**
   - `https://your-vercel-domain.vercel.app`
7. Add to **Authorized redirect URIs:**
   - `https://your-vercel-domain.vercel.app`
   - `https://your-vercel-domain.vercel.app/`
8. Save

### Monitor Application

- **Vercel Analytics**: Track performance metrics
- **Vercel Logs**: Monitor real-time application logs
- **Firebase Console**: Check usage and errors
- **Error Tracking**: Set up Sentry or similar for error monitoring

## Troubleshooting

### Build Fails

**Error: "Module not found"**
- Ensure `package.json` and `requirements.txt` are committed to Git
- Check `vercel.json` has correct paths
- Run build locally to test: `npm run build`

**Error: "Python version not compatible"**
- Ensure `vercel.json` specifies Python 3.9:
```json
{
  "env": {
    "PYTHON_VERSION": "3.9"
  }
}
```

### Frontend Issues

**Blank white page or 404**
- Check browser console for errors
- Verify `frontend/dist` exists
- Check backend logs for serving errors
- Ensure `VITE_API_URL` is correct

**Firebase errors on login**
- Verify Firebase credentials in env vars
- Check authorized domains in Firebase Console
- Ensure Google OAuth URIs are updated
- Check browser console for specific error

### API Issues

**502 Bad Gateway**
- Check backend logs in Vercel dashboard
- Verify all environment variables are set
- Test API locally before deploying
- Check Firebase initialization logs

**CORS errors**
- Verify `ALLOWED_ORIGINS` includes your Vercel domain
- Check backend CORS configuration in `app.py`
- Ensure requests have correct `Authorization` header

**Timeout errors**
- Long-running operations may timeout (Vercel limit: 60s for builds)
- Optimize database queries
- Cache expensive operations
- Monitor performance in Vercel dashboard

## Continuous Deployment

Your app will automatically redeploy when you:

1. Push to `main` branch on GitHub
2. Changes are pushed to your repository
3. Vercel webhook triggers automatic build
4. If build succeeds, deployment happens automatically

To pause auto-deployment:
- Go to Vercel Dashboard → Project Settings → Deployments
- Disable "Automatic Deployments"

## Scaling Considerations

As your app grows:

1. **Database**: Migrate from Firestore to production-scale solution if needed
2. **File Storage**: Consider cloud storage (Firebase Storage, AWS S3)
3. **API Rate Limiting**: Implement rate limiting for public APIs
4. **Caching**: Add caching layer (Redis) for frequently accessed data
5. **CDN**: Enable Vercel's built-in CDN for static assets
6. **Monitoring**: Set up comprehensive error tracking and performance monitoring

## Cost Estimates

**Vercel (Free Tier includes):**
- Unlimited deployments
- Automatic HTTPS
- Global edge network
- 100 GB/month bandwidth
- Full serverless function support

**Firebase Spark Plan:**
- Real-time database: 1 GB storage
- Cloud Storage: 5 GB/month
- Authentication: Unlimited

**Groq API:**
- Free tier available with rate limits
- Pay-as-you-go after free tier

## Support & Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Firebase Documentation](https://firebase.google.com/docs)
- [Groq API Docs](https://console.groq.com/docs)
- [React Documentation](https://react.dev)
- [Flask Documentation](https://flask.palletsprojects.com)
