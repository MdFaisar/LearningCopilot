# Personalized Learning Copilot

An AI-powered learning assistant that helps students plan, track, and master core courses through personalized study roadmaps, intelligent Q&A with RAG, adaptive quizzes, and knowledge tracking.

## Features

- 🎯 **Personalized Study Plans**: AI-generated week-by-week roadmaps tailored to your schedule and goals
- 💬 **Intelligent Q&A**: Ask questions and get answers from your course materials using RAG (Retrieval-Augmented Generation)
- 📊 **Progress Tracking**: Monitor your mastery levels and identify areas for improvement
- ✅ **Adaptive Quizzes**: Practice with questions that match your skill level
- 📚 **Course Management**: Upload and organize course materials (PDFs, slides)
- 🔐 **Google Authentication**: Secure login with Google OAuth

## Tech Stack

### Frontend
- **React** (Vite) - Modern UI framework
- **React Router** - Client-side routing
- **Firebase** - Authentication and Firestore database
- **Axios** - HTTP client
- **Recharts** - Data visualization
- **Lucide React** - Icons

### Backend
- **Flask** - Python web framework
- **Firebase Admin SDK** - Server-side Firebase integration
- **Sentence Transformers** - Text embeddings for RAG
- **FAISS** - Vector similarity search
- **Google Gemini AI** - Text generation for study plans and quizzes
- **PyPDF2/pdfplumber** - PDF processing

### Deployment
- **Render** - Backend hosting
- **Firebase Hosting** or **Vercel** - Frontend hosting

## Project Structure

```
Anti_2/
├── backend/
│   ├── app.py                 # Flask application entry point
│   ├── config.py              # Configuration management
│   ├── requirements.txt       # Python dependencies
│   ├── Procfile              # Render deployment config
│   ├── services/
│   │   ├── rag_service.py    # RAG pipeline
│   │   ├── study_plan_service.py  # Study plan generation
│   │   ├── quiz_service.py   # Quiz generation
│   │   └── knowledge_tracker.py   # Progress tracking
│   └── routes/
│       ├── auth.py           # Authentication endpoints
│       ├── courses.py        # Course management
│       ├── study_plans.py    # Study plan endpoints
│       ├── quiz.py           # Quiz endpoints
│       ├── qa.py             # Q&A endpoints
│       └── progress.py       # Progress tracking
│
└── frontend/
    ├── src/
    │   ├── components/       # Reusable components
    │   ├── contexts/         # React contexts
    │   ├── pages/            # Page components
    │   ├── services/         # API client
    │   ├── config/           # Firebase config
    │   ├── App.jsx           # Main app component
    │   └── main.jsx          # Entry point
    ├── package.json
    └── vite.config.js
```

## Setup Instructions

### Prerequisites
- **Node.js** (v18+)
- **Python** (v3.9+)
- **Firebase Project** (for authentication and database)
- **Google AI API Key** (for Gemini)

### 1. Firebase Setup

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create a new project
3. Enable **Google Authentication**:
   - Go to Authentication → Sign-in method
   - Enable Google provider
4. Create a **Firestore Database**:
   - Go to Firestore Database → Create database
   - Start in production mode
5. Enable **Storage**:
   - Go to Storage → Get started
6. Get your Firebase config:
   - Go to Project Settings → General
   - Scroll to "Your apps" → Web app
   - Copy the configuration
7. Generate a service account key:
   - Go to Project Settings → Service accounts
   - Click "Generate new private key"
   - Save as `firebase-credentials.json` in the `backend/` directory

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env

# Edit .env and add your credentials:
# - FIREBASE_CREDENTIALS_JSON (paste entire Firebase service account JSON)
# - GROQ_API_KEY (from console.groq.com)
```

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create .env file
copy .env.example .env

# Edit .env and add your Firebase config:
# VITE_FIREBASE_API_KEY=your-api-key
# VITE_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
# VITE_FIREBASE_PROJECT_ID=your-project-id
# VITE_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
# VITE_FIREBASE_MESSAGING_SENDER_ID=your-sender-id
# VITE_FIREBASE_APP_ID=your-app-id
# VITE_API_URL=http://localhost:5000/api
```

### 4. Running Locally

**Terminal 1 - Backend:**
```bash
cd backend
venv\Scripts\activate  # or source venv/bin/activate on Mac/Linux
python app.py
```

Backend will run on `http://localhost:5000`

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Frontend will run on `http://localhost:5173`

## Deployment

### Full Stack Deployment on Vercel

Deploy both frontend and backend together on Vercel with a single monorepo setup.

#### Prerequisites
- GitHub account with your project repository
- Vercel account (vercel.com)

#### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/learning-copilot.git
git push -u origin main
```

#### Step 2: Deploy to Vercel

1. Go to [Vercel](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Vercel will auto-detect the monorepo setup
5. Configure environment variables (see Step 3)
6. Click "Deploy"

#### Step 3: Set Environment Variables on Vercel

After importing your project, add these environment variables in Vercel dashboard:
- Go to **Settings → Environment Variables**

**Backend Environment Variables:**
```
FIREBASE_CREDENTIALS_JSON=<your-entire-firebase-service-account-json>
GROQ_API_KEY=<your-groq-api-key>
SECRET_KEY=<your-secret-key>
DEBUG=False
UPLOAD_FOLDER=uploads
VECTOR_STORE_PATH=vector_stores
ALLOWED_ORIGINS=https://your-vercel-domain.vercel.app
```

**Frontend Environment Variables:**
```
VITE_FIREBASE_API_KEY=<your-firebase-api-key>
VITE_FIREBASE_AUTH_DOMAIN=<your-firebase-auth-domain>
VITE_FIREBASE_PROJECT_ID=<your-firebase-project-id>
VITE_FIREBASE_STORAGE_BUCKET=<your-firebase-storage-bucket>
VITE_FIREBASE_MESSAGING_SENDER_ID=<your-sender-id>
VITE_FIREBASE_APP_ID=<your-app-id>
VITE_API_URL=https://your-vercel-domain.vercel.app/api
```

#### How It Works

1. **vercel.json** - Configuration file that tells Vercel:
   - Build commands: Build frontend, prepare backend
   - Install commands: Install frontend & backend dependencies
   - Framework: Custom (Flask)

2. **app.py** - Updated to serve frontend build files:
   - Serves React app on `/`
   - Handles SPA routing (non-API routes serve index.html)
   - Serves API routes on `/api/*`

3. **Automatic Builds:**
   - Frontend: Built with Vite during deployment
   - Backend: Flask app ready to serve (no build needed)
   - Both run on same domain for seamless integration

#### Update Frontend API URL After Deployment

After deployment, update your frontend environment:

1. Vercel provides your deployment URL (e.g., `https://learning-copilot-abc.vercel.app`)
2. Update `VITE_API_URL` to include `/api` prefix
3. Re-deploy to apply changes

```
VITE_API_URL=https://learning-copilot-abc.vercel.app/api
```

#### Troubleshooting Vercel Deployment

**Build fails with "Python not found"**
- Ensure `vercel.json` has `"env": { "PYTHON_VERSION": "3.9" }`
- Check that `backend/requirements.txt` exists

**Frontend shows 404**
- Ensure `frontend/dist` is not in `.gitignore`
- Check that vite build completes successfully
- Verify `app.py` static_folder path is correct

**API calls return 404**
- Check CORS settings in `app.py`
- Verify `VITE_API_URL` points to correct domain with `/api` prefix
- Check backend environment variables are set

**Firebase errors**
- Verify `FIREBASE_CREDENTIALS_JSON` is properly formatted (valid JSON)
- Check Firebase project ID matches frontend config
- Ensure Auth domain is accessible from Vercel

### Local Development

To run both frontend and backend locally:

**Terminal 1 - Backend:**
```bash
cd backend
venv\Scripts\activate  # or source venv/bin/activate on Mac/Linux
python app.py
```
Backend runs on `http://localhost:5000`

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```
Frontend runs on `http://localhost:5173`

**Or run both simultaneously:**
```bash
npm run dev  # From root directory (requires concurrently package)
```

## Usage Guide

### 1. Create a Course
1. Login with Google
2. Click "Add Course" on the dashboard
3. Enter course title, description, and syllabus
4. Click "Create Course"

### 2. Upload Materials
1. Go to course detail page
2. Click "Upload PDF" to add course materials
3. Click "Process Materials for Q&A" to enable RAG

### 3. Generate Study Plan
1. On the course detail page, click "Generate Study Plan"
2. The AI will create a personalized week-by-week roadmap
3. View and track your progress in the Study Plan page

### 4. Take Quizzes
1. Go to the Quiz page
2. Select a course
3. Click "Generate Quiz"
4. Answer questions and submit
5. View results and explanations

### 5. Ask Questions
1. Go to the Q&A page or course detail page
2. Type your question
3. Get AI-powered answers with citations from course materials

### 6. Track Progress
1. Go to the Progress page
2. View your overall mastery, quiz scores, and study hours
3. Identify weak topics that need more attention

## Color Palette

The application uses a professional color scheme:
- **White** (#FFFFFF) - Primary background
- **Gray** (#F3F4F6 - #111827) - Text and neutral elements
- **Orange** (#F97316) - Primary actions and highlights
- **Black** (#000000) - High contrast text
- **Green** (#22C55E) - Success states and mastery indicators

## API Documentation

### Authentication
- `POST /api/auth/verify` - Verify Firebase token

### Courses
- `GET /api/courses` - List user's courses
- `POST /api/courses` - Create new course
- `GET /api/courses/:id` - Get course details
- `PUT /api/courses/:id` - Update course
- `DELETE /api/courses/:id` - Delete course
- `POST /api/courses/:id/materials` - Upload course material
- `POST /api/courses/:id/process` - Process and index materials

### Study Plans
- `POST /api/study-plans/generate` - Generate personalized study plan
- `GET /api/study-plans/:courseId` - Get study plan for course
- `PUT /api/study-plans/:id` - Update study plan
- `POST /api/study-plans/:id/adjust` - Auto-adjust based on progress

### Quiz
- `POST /api/quiz/generate` - Generate adaptive quiz
- `POST /api/quiz/submit` - Submit quiz answers
- `GET /api/quiz/history/:courseId` - Get quiz history

### Q&A (RAG)
- `POST /api/qa/query` - Ask question with RAG retrieval
- `GET /api/qa/history/:courseId` - Get Q&A history

### Progress
- `GET /api/progress/:courseId` - Get progress for course
- `POST /api/progress/session` - Log study session
- `PUT /api/progress/mastery` - Update topic mastery

## Troubleshooting

### Backend Issues

**Error: Firebase Admin initialization failed**
- Ensure `FIREBASE_CREDENTIALS_JSON` is set in `.env`
- Verify it's valid JSON (no extra quotes or formatting)
- Check the service account email is correct

**Error: Google AI API key invalid**
- Get a new API key from [Groq Console](https://console.groq.com)
- Update `GROQ_API_KEY` in `.env`

**Error: Module not found**
- Activate virtual environment
- Run `pip install -r requirements.txt`

**Error: Port already in use**
- Change PORT in `.env` or kill the process using port 5000
- On Windows: `netstat -ano | findstr :5000` then `taskkill /PID <pid> /F`
- On Mac/Linux: `lsof -i :5000` then `kill -9 <pid>`

### Frontend Issues

**Error: Firebase configuration invalid**
- Check all `VITE_FIREBASE_*` environment variables in `.env`
- Ensure no trailing spaces or quotes
- Verify values match Firebase Console exactly

**Error: Network request failed**
- Check that backend is running
- Verify `VITE_API_URL` points to correct backend URL with `/api` prefix
- Check CORS configuration in backend

**Error: Blank page or 404 on Vercel**
- Ensure frontend build completed successfully
- Check `vercel.json` configuration
- Verify `app.py` static_folder path: `static_folder='../frontend/dist'`
- Check backend logs on Vercel dashboard

### Vercel Deployment Issues

**Build fails with module errors**
- Run `npm install && pip install -r requirements.txt` locally first
- Commit `package-lock.json` and `requirements.txt` to Git
- Check vercel.json has correct build commands

**Frontend shows 404 or "Cannot find module"**
- Ensure `frontend/dist` folder exists after build
- Check Vercel build logs for Vite errors
- Verify Node.js version is 18.x or higher

**API requests timeout or fail**
- Check Vercel function timeout settings (default 10s)
- Verify backend environment variables are set in Vercel dashboard
- Check Firebase credentials are correctly formatted in env var
- Monitor Vercel logs for detailed error messages

**CORS errors on Vercel**
- Update `ALLOWED_ORIGINS` to include your Vercel domain
- Ensure backend CORS settings allow the frontend domain
- Check that requests include correct `Authorization` header

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions, please create an issue on GitHub.
