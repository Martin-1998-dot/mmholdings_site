button_html = '''
<!-- Email Button -->
<div style="position: fixed; bottom: 90px; right: 20px; z-index: 1000;">
  <a href="mailto:mmholdingsrealstate@gmail.com" target="_blank"
     style="background-color: #EA4335; color: white; border-radius: 50%; width: 60px; height: 60px;
            text-align: center; font-size: 24px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
            display: flex; align-items: center; justify-content: center; text-decoration: none;">
    ✉️
  </a>
</div>
'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

if button_html.strip() not in content:
    content = content.replace('</body>', button_html + '\n</body>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Email button added successfully.")
else:
    print("Email button already present.")
