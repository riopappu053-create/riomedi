const fs = require('fs');
const path = require('path');

const dirPath = 'c:/Users/MADHUMITHA/Downloads/medical/medical';
const files = fs.readdirSync(dirPath).filter(file => file.endsWith('.html'));

files.forEach(file => {
    const filePath = path.join(dirPath, file);
    let content = fs.readFileSync(filePath, 'utf8');

    // 1. Update body padding-top
    content = content.replace(/(body\s*\{[^}]*?padding-top:\s*)72px(;[\s\S]*?\})/, '$160px$2');

    // 2. Update typography for h1-h6
    const typographyRegex = /\/\*\s*=====\s*TYPOGRAPHY\s*=====\s*\*\/[\s\S]*?font-weight:\s*700\s*!important;[\s\S]*?letter-spacing:\s*-0\.01em;\s*\}/;
    
    const newTypography = `/* ===== TYPOGRAPHY ===== */
        h1,
        h2,
        .brand-logo {
            font-family: 'Poppins', sans-serif;
            font-weight: 600 !important;
            letter-spacing: -0.01em;
        }
        h3,
        h4,
        h5,
        h6 {
            font-family: 'Poppins', sans-serif;
            font-weight: 500 !important;
            letter-spacing: -0.01em;
        }`;
    
    content = content.replace(typographyRegex, newTypography);

    // 3. Update navbar height
    content = content.replace(/(\.navbar\s*\{[^}]*?height:\s*)72px(;[\s\S]*?\})/, '$160px$2');

    // 4. Update navbar.scrolled height
    content = content.replace(/(\.navbar\.scrolled\s*\{[^}]*?height:\s*)64px(;[\s\S]*?\})/, '$152px$2');
    
    fs.writeFileSync(filePath, content, 'utf8');
    console.log('Updated ' + file);
});
