const passport = require('passport');

const isAuthenticated = (req, res, next) => {
  if (req.isAuthenticated()) {
    return next();
  }
  res.status(401).json({ message: 'Unauthorized' });
};

const googleAuth = passport.authenticate('google', {
  scope: ['https://www.googleapis.com/auth/plus.login'],
});

const googleAuthCallback = passport.authenticate('google', { failureRedirect: '/' });

const logout = (req, res) => {
  req.logout();
  res.redirect('/');
};

const checkAuth = (req, res) => {
  res.json({ user: req.isAuthenticated() ? req.user : null });
};

module.exports = { isAuthenticated, googleAuth, googleAuthCallback, logout, checkAuth };
