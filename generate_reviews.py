import re

text = """### 1. Vinith Banoth
**★★★★★**

“I had severe pain in my front teeth and got a Root Canal Treatment at Roots Dental Care. Dr. Nikhil Gudla gave me honest advice and focused on the treatment I actually needed. I really appreciated his professional approach.”

### 2. Shruti Enjapuri
**★★★★★**

“I had an excellent experience at Roots Dental Care. Dr. Nikil Kumar was professional, knowledgeable and very gentle. He explained the procedure clearly and made sure I was comfortable throughout the treatment.”

### 3. Chaitali Tailor
**★★★★★**

“I had a Root Canal Treatment followed by zirconia crown placement. The treatment was smooth with minimal discomfort, and the crown looks and feels completely natural. The clinic is hygienic and uses advanced technology.”

### 4. Sangita Sonari
**★★★★★**

“I was very nervous about my treatment, but Dr. Ankit and the entire team were extremely gentle and understanding. Everything was explained clearly and I felt comfortable throughout. Thank you for the painless treatment.”

### 5. Vikas Morem
**★★★★★**

“Dr. Nikil Kumar is highly professional, caring and patient-friendly. The clinic is clean, hygienic and equipped with modern facilities. A great place for anyone looking for quality dental treatment.”

### 6. Vishal Gudla
**★★★★★**

“I had my front tooth implant done at Roots Dental Care. The entire process was smooth and the doctor did an excellent job. The result looks natural and has improved my smile significantly.”

### 7. Rai Gautam Shriram
**★★★★★**

“I had an excellent experience with my Root Canal Treatment. Dr. Nikhil explained everything clearly, the staff was professional and friendly, and the clinic was well maintained with modern equipment. Highly recommended.”

### 8. Moneesha Modi
**★★★★★**

“I had a Root Canal Treatment with a crown at Roots Dental Care and was extremely impressed with the professionalism of Dr. Ruta and her team. My dental anxiety was handled very well and the treatment was gentle and comfortable.”

### 9. Vaishali Bhawsar
**★★★★★**

“I had both an implant and Root Canal Treatment at Roots Dental Care. Dr. Ruta explained everything patiently and made me comfortable throughout the procedure. Dr. Ankit made my Root Canal Treatment a very comfortable experience. The staff was also extremely supportive.”

### 10. Sudip Vasoya
**★★★★★**

“My wife had a tooth extraction at Roots Dental Care and the treatment was painless. Dr. Ruta was friendly, knowledgeable and professional. The clinic maintains excellent hygiene and sterilization standards, and the staff is very helpful.”

### 11. Nitesh Saidane
**★★★★★**

“After having a poor experience at other clinics, I chose Roots Dental Care for my Root Canal and Implant treatment. Dr. Ankit and Dr. Ruta took their time, explained every step and focused on quality. I was completely satisfied with the treatment.”

### 12. Zainab Dadani
**★★★★★**

“Dr. Ruta takes the time to understand each patient and provides thorough explanations before treatment. Both Dr. Ruta and Dr. Ankit are knowledgeable and caring, and the staff is very friendly. Highly recommended.”

### 13. Tanu Upadhyay
**★★★★★**

“I have never been a fan of visiting the dentist, but I always felt comfortable at Roots Dental Care. Appointments were on time and I was involved in every decision regarding my treatment. I would happily recommend the clinic.”

### 14. Saumil Modi
**★★★★★**

“I had an implant treatment at Roots Dental Care and was extremely satisfied with the result. Dr. Ruta and Dr. Ankit were excellent, and the staff was very humble and supportive. I also appreciated their follow-up after the treatment.”

### 15. Harshith Bhasme
**★★★★★**

“The doctors are warm, friendly and explain everything in detail using pictures and videos. My Root Canal Treatment was done using a microscope, which was an impressive and advanced approach. Excellent treatment and hospitality.”"""

blocks = text.split("###")
reviews = []
for b in blocks:
    if not b.strip(): continue
    lines = [l.strip() for l in b.strip().split('\n') if l.strip()]
    
    # Extract name (remove number prefix)
    name_match = re.search(r'\d+\.\s*(.+)', lines[0])
    name = name_match.group(1) if name_match else lines[0]
    
    # Extract text
    body = lines[-1].strip('“"”')
    
    html = f'<div class="rev"><div class="stars" aria-label="5 out of 5">★★★★★</div><p>"{body}"</p><div class="who"><b>{name}</b></div></div>'
    reviews.append(html)

all_reviews = "".join(reviews)
# Double it for marquee
marquee_html = f'<div class="rev-marquee-wrap reveal"><div class="rev-marquee">{all_reviews}{all_reviews}</div></div>'

# Read index.html and replace rev-grid
with open('index.html', 'r', encoding='utf-8') as f:
    page = f.read()

page = re.sub(r'<div class="rev-grid reveal">.*?</div>\n  </div>', marquee_html + '\n  </div>', page, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(page)

print("Updated index.html with marquee.")
