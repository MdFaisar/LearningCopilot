# Firebase Credentials Configuration

## Summary of Changes

All Firebase credentials are now stored in environment variables (`.env` files) and accessed through the code configuration. This improves security by keeping sensitive data out of the codebase.

## Backend Changes

### 1. `.env` File
**Old:**
```
FIREBASE_CREDENTIALS_PATH=firebase-credentials.json
```

**New:**
```
FIREBASE_CREDENTIALS_JSON={"type":"service_account","project_id":"...","private_key":"..."}
```

The entire Firebase Admin SDK credentials JSON is now stored as a single environment variable.

### 2. `config.py`
- Added JSON parsing to convert the `FIREBASE_CREDENTIALS_JSON` string into a dictionary
- New `FIREBASE_CREDENTIALS` attribute that contains the parsed credentials
- No longer reads from `FIREBASE_CREDENTIALS_PATH`

### 3. `app.py`
- Updated Firebase initialization to use `app.config['FIREBASE_CREDENTIALS']` instead of reading from file path
- Uses the parsed credentials dictionary to initialize Firebase Admin SDK

## Frontend Changes

### `.env` File
Already configured to read Firebase credentials:
```
VITE_FIREBASE_API_KEY=...
VITE_FIREBASE_AUTH_DOMAIN=...
VITE_FIREBASE_PROJECT_ID=...
VITE_FIREBASE_STORAGE_BUCKET=...
VITE_FIREBASE_MESSAGING_SENDER_ID=...
VITE_FIREBASE_APP_ID=...
```

### `src/config/firebase.js`
No changes needed - already reads from `import.meta.env` (Vite environment variables)

## How to Setup

### Backend
1. Go to Firebase Console > Project Settings > Service Accounts
2. Click "Generate New Private Key"
3. Copy the entire JSON content
4. Paste it as the value of `FIREBASE_CREDENTIALS_JSON` in `.env`

Example (minified):
```
FIREBASE_CREDENTIALS_JSON={"type":"service_account","project_id":"learn-31e25","private_key_id":"...","private_key":"...","client_email":"...","client_id":"...","auth_uri":"...","token_uri":"...","auth_provider_x509_cert_url":"...","client_x509_cert_url":"..."}
```

### Frontend
1. Go to Firebase Console > Project Settings > Your Apps > Web App
2. Copy the configuration
3. Add each field to `.env` with the `VITE_` prefix

Example:
```
VITE_FIREBASE_API_KEY=AIzaSyDly__aEtjczfCN-LwVC6AOydQ2DDD_tJA
VITE_FIREBASE_AUTH_DOMAIN=learn-31e25.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=learn-31e25
VITE_FIREBASE_STORAGE_BUCKET=learn-31e25.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=661588498776
VITE_FIREBASE_APP_ID=1:661588498776:web:10f0229ee669ddb73a2d2d
```

## Security Best Practices

1. **Never commit `.env` files** - They contain sensitive credentials
2. **Use `.env.example`** - Contains template with placeholder values
3. **In production** - Store credentials in secure environment management (e.g., GitHub Secrets, Render Dashboard, Vercel Dashboard)
4. **Rotate credentials** - Periodically generate new Firebase Admin SDK credentials

## Files Modified

- `backend/.env` - Updated to use `FIREBASE_CREDENTIALS_JSON`
- `backend/.env.example` - Updated documentation
- `backend/config.py` - Added JSON parsing for Firebase credentials
- `backend/app.py` - Updated Firebase initialization logic
- `frontend/.env` - Already configured (no changes)
- `frontend/.env.example` - Already configured (no changes)
