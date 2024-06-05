const passport = require('passport');
const User = require('../models/User');

exports.googleAuth = passport.authenticate('google', {
  scope: ['https://www.googleapis.com/auth/plus.login'],
});

exports.googleAuthCallback = passport.authenticate('google', { failureRedirect: '/' });

exports.logout = (req, res) => {
  req.logout();
  res.redirect('/');
};

exports.checkAuth = (req, res) => {
  res.json({ user: req.isAuthenticated() ? req.user : null });
};

exports.createUser = async (googleId, displayName, email) => {
  try {
    const user = await User.create({
      googleId,
      displayName,
      username: email,
      email,
    });
    return user;
  } catch (error) {
    console.error('Error creating user:', error);
    throw error;
  }
};
