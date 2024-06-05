require('dotenv').config();
const express = require('express');
const session = require('express-session');
const mongoose = require('mongoose');
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const GoogleStrategy = require('passport-google-oauth20').Strategy; // Add Google OAuth Strategy
const User = require('./models/User');
const MongoStore = require('connect-mongo');
const pdfUploadMiddleware = require('./middlewares/pdfUpload');
const generatePptMiddleware = require('./middlewares/pptGeneration');
const fs = require('fs');
const path = require('path');
const { isAuthenticated, logout, checkAuth } = require('./middlewares/auth');
const connectDB = require('./db');
const crypto = require('crypto')

const app = express();

// MongoDB connection
connectDB();

// Session configuration
app.use(
  session({
    secret: process.env.SESSION_SECRET || 'your-secret-key-here',
    resave: false,
    saveUninitialized: true,
    store: MongoStore.create({
      mongoUrl: process.env.MONGODB_URI,
      mongoOptions: { useNewUrlParser: true, useUnifiedTopology: true },
      mongooseConnection: mongoose.connection,
    }),
    cookie: {
      maxAge: 24 * 60 * 60 * 1000, // 1 day
    },
  })
);

// Passport configuration
app.use(passport.initialize());
app.use(passport.session());

passport.serializeUser((user, done) => {
  done(null, user.id);
});

passport.deserializeUser(async (id, done) => {
  try {
    const user = await User.findById(id);
    done(null, user);
  } catch (error) {
    done(error);
  }
});


// Local Strategy
passport.use(
  new LocalStrategy(async (username, password, done) => {
    try {
      const user = await User.findOne({ username });
      if (!user) {
        return done(null, false, { message: 'Incorrect username.' });
      }
      if (!(await user.validPassword(password))) {
        return done(null, false, { message: 'Incorrect password.' });
      }
      return done(null, user);
    } catch (error) {
      return done(error);
    }
  })
);

// Google OAuth Strategy
passport.use(
  new GoogleStrategy(
    {
      clientID: process.env.GOOGLE_CLIENT_ID,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET,
      callbackURL: process.env.CALLBACK_URL,
    },
    async (accessToken, refreshToken, profile, done) => {
      try {
        let user = await User.findOne({ googleId: profile.id });

        if (!user) {
          // Create a new user if not found
          user = await User.create({
            googleId: profile.id,
            displayName: profile.displayName,
            // Add additional fields if needed
          });
        }

        return done(null, user);
      } catch (error) {
        return done(error);
      }
    }
  )
);

// Upload PDF file
app.post('/upload', isAuthenticated, pdfUploadMiddleware, async (req, res) => {
  // Upload logic
});

// Download generated PPT
app.get('/download/:fileName', isAuthenticated, (req, res) => {
  // Download logic
});

// Authentication routes
app.post('/auth/login', passport.authenticate('local', { successRedirect: '/', failureRedirect: '/login', failureFlash: true }));
app.get('/auth/google', passport.authenticate('google', { scope: ['profile'] }));
app.get('/auth/google/callback', passport.authenticate('google', { successRedirect: '/', failureRedirect: '/login' }));
app.post('/auth/logout', logout);
app.get('/auth/check-auth', checkAuth);

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});

// Handle 404 errors
app.use((req, res, next) => {
  res.status(404).send('Not Found');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
