const multer = require('multer');
const path = require('path');

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, './uploads');
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + path.extname(file.originalname));
  },
});

const upload = multer({ storage: storage });

function pdfUpload(req, res, next) {
  upload.single('pdf')(req, res, function (err) {
    if (err instanceof multer.MulterError) {
      return res.status(400).json({ message: 'File upload error.' });
    } else if (err) {
      return res.status(500).json({ message: 'Server error.' });
    }
    next();
  });
}

module.exports = pdfUpload;
