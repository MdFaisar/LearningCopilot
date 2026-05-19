# Vercel Deployment Quick Start

## 5-Minute Setup

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for Vercel deployment"
   git push
   ```

2. **Import on Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project" → Import from GitHub
   - Select your repository

3. **Add Environment Variables** (in Vercel dashboard)
   ```
   FIREBASE_CREDENTIALS_JSON=<paste entire Firebase service account JSON>
   GROQ_API_KEY=<your groq api key>
   SECRET_KEY=<generate a random secret>
   DEBUG=False
   VITE_API_URL=https://YOUR_VERCEL_DOMAIN.vercel.app/api
   VITE_FIREBASE_API_KEY=<your firebase api key>
   VITE_FIREBASE_AUTH_DOMAIN=<your project>.firebaseapp.com
   VITE_FIREBASE_PROJECT_ID=<your project id>
   VITE_FIREBASE_STORAGE_BUCKET=<your bucket>.appspot.com
   VITE_FIREBASE_MESSAGING_SENDER_ID=<your sender id>
   VITE_FIREBASE_APP_ID=<your app id>
   ```

4. **Deploy**
   - Click "Deploy"
   - Wait ~2-3 minutes for build and deployment
   - Your app will be live at `https://YOUR_VERCEL_DOMAIN.vercel.app`

5. **Update Firebase Auth**
   - Go to Firebase Console → Authentication → Authorized Domains
   - Add your Vercel domain

## What Changed

✓ **app.py** - Now serves frontend build files  
✓ **vercel.json** - Deployment configuration  
✓ **package.json** - Root build scripts  
✓ **Frontend** - Builds to `dist/` folder  
✓ **Environment** - All credentials now in `.env`  

## Verify Deployment

- **Frontend**: https://your-domain.vercel.app
- **API Health**: https://your-domain.vercel.app/api/health
- **Frontend Build**: Check Vercel dashboard → Deployments
- **Backend Status**: Check Vercel dashboard → Logs

## If Build Fails

1. Check Vercel build logs (dashboard → Deployments)
2. Verify all environment variables are set
3. Ensure `package-lock.json` and `requirements.txt` are committed
4. Test build locally: `npm run build && npm run build:backend`
5. Check that `frontend/dist` is NOT in `.gitignore`

## Key Files

| File | Purpose |
|------|---------|
| `vercel.json` | Tells Vercel how to build and deploy |
| `backend/app.py` | Serves API + frontend files |
| `frontend/vite.config.js` | Frontend build config |
| `package.json` | Root scripts for Vercel |
| `.gitignore` | Prevents secrets from being committed |
| `.env.example` | Template for environment variables |

## Monitoring

- **Vercel Dashboard**: Real-time deployment status
- **Vercel Logs**: Runtime application logs
- **Build Logs**: Available after each deployment
- **Analytics**: Performance metrics (if enabled)

## Next Steps

1. ✓ Test login with Google Auth
2. ✓ Create a course and upload materials
3. ✓ Generate study plans and quizzes
4. ✓ Monitor logs for any errors
5. Set up email alerts in Vercel if needed

## Support

See full [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed troubleshooting and advanced setup.
