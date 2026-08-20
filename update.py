import os
import glob
import re

dir_path = r'c:\Users\MADHUMITHA\Downloads\medical\medical'
html_files = glob.glob(os.path.join(dir_path, '*.html'))

body_orig = r'''        body {
            font-family: 'Inter', sans-serif;
            background-color: #f8fafc;
            color: #1a2a3a;
            transition: background-color 0.4s ease, color 0.4s ease;
            overflow-x: hidden;
            padding-top: 72px;
        }'''

body_new = r'''        body {
            font-family: 'Inter', sans-serif;
            background-color: #f8fafc;
            color: #1a2a3a;
            transition: background-color 0.4s ease, color 0.4s ease;
            overflow-x: hidden;
            padding-top: 60px;
        }'''

typo_orig = r'''        /* ===== TYPOGRAPHY ===== */
        h1,
        h2,
        h3,
        h4,
        h5,
        h6,
        .brand-logo {
            font-family: 'Poppins', sans-serif;
            font-weight: 700 !important;
            letter-spacing: -0.01em;
        }'''

typo_new = r'''        /* ===== TYPOGRAPHY ===== */
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
        }'''

nav_orig = r'''        /* ===== NAVBAR ===== */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
            background: var(--nav-bg);
            padding: 0 32px;
            height: 72px;
            display: flex;
            align-items: center;
            transition: all 0.35s cubic-bezier(0.22, 1, 0.36, 1);
            border-bottom: 1px solid transparent;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
        }
        .navbar.scrolled {
            height: 64px;'''

nav_new = r'''        /* ===== NAVBAR ===== */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
            background: var(--nav-bg);
            padding: 0 32px;
            height: 60px;
            display: flex;
            align-items: center;
            transition: all 0.35s cubic-bezier(0.22, 1, 0.36, 1);
            border-bottom: 1px solid transparent;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
        }
        .navbar.scrolled {
            height: 52px;'''

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace(body_orig, body_new)
    new_content = new_content.replace(typo_orig, typo_new)
    new_content = new_content.replace(nav_orig, nav_new)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f'Updated {file_path}')

