const fs = require('fs');
const path = require('path');

async function generatePpt(pdfPath) {
  const pptPath = pdfPath.replace('.pdf', '.pptx');
  fs.copyFileSync(pdfPath, pptPath);
  return pptPath;
}

module.exports = generatePpt;
