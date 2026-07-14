import zipfile
import xml.etree.ElementTree as ET

def get_docx_text(path):
    namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    try:
        with zipfile.ZipFile(path) as z:
            xml_content = z.read('word/document.xml')
            root = ET.fromstring(xml_content)
            paragraphs = []
            for para in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                text = ''.join(node.text for node in para.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text)
                if text:
                    paragraphs.append(text)
            return paragraphs
    except Exception as e:
        print(f"Error: {e}")
        return []

paras = get_docx_text(r"D:\Gemini\Post_TOE_Physics\Temporal\books\Код кванта.docx")
for i in range(10, 36):
    if i < len(paras):
        print(f"[{i}]: {paras[i]}")
