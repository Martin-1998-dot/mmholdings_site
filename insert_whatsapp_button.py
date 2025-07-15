button_html = '''
<!-- WhatsApp Chat Button -->
<div style="position: fixed; bottom: 20px; right: 20px; z-index: 1000;">
  <a href="https://wa.me/27614486260" target="_blank"
     style="background-color: #25D366; color: white; border-radius: 50%; width: 60px; height: 60px;
            text-align: center; font-size: 30px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
            display: flex; align-items: center; justify-content: center; text-decoration: none;">
    💬
  </a>
</div>
'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

if button_html.strip() not in content:
    content = content.replace('</body>', button_html + '\n</body>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("WhatsApp button added successfully.")
else:
    print("WhatsApp button already present.")
