# =========================================
#   CYBER SECURITY NOTES - TRYHACKME 
#   Module: Web Fundamentals / Pre Security
# =========================================

# -----------------------------------------
#   TASK 1: PUTTING IT ALL TOGETHER
# -----------------------------------------

# 1. URL STRUCTURE
URL = "https://google.com/search?q=hack"
"""
https://     = Protocol - Secure connection
google.com   = Domain - Website ka naam
/search      = Path - Kis page pe jana hai
?q=hack      = Parameter - Extra data bhej rahe
"""

# 2. HTTP REQUEST METHODS
GET  = "Server se data MAANGNA"  # Example: Google search
POST = "Server ko data BHEJNA"   # Example: Login form submit

# 3. HTTP RESPONSE CODES - EXAM MEIN PAKKA AAYEGA
status_codes = {
    200: "OK - Sab theek, page mil gaya",
    301: "Moved - Page naye address pe chala gaya", 
    404: "Not Found - Page gum ho gaya",
    500: "Server Error - Server kharab ho gaya"
}

# 4. WEBSITE KE 3 HISSE
HTML = "Haddi - Structure banata hai"
CSS  = "Kapde - Rang-roop deta hai" 
JS   = "Dimaag - Click karne pe kaam karta hai"

# -----------------------------------------
#   TASK 2: OTHER COMPONENTS  
# -----------------------------------------

# 1. DNS = Domain Name System
DNS_kaam = "Naam ko IP mein badalta hai"
example = "google.com -> 142.250.185.78"
yaad_rakho = "DNS = Phone Book"

# 2. COOKIES
cookies = "Tujhe yaad rakhta hai"
use = "Login karke dubara password na daalna pade"
yaad_rakho = "Cookies = Yaad-dasht"

# 3. CDN = Content Delivery Network  
CDN_kaam = "Website tez load karata hai"
kaise = "Images/files tere sheher ke server se deta hai"
yaad_rakho = "CDN = Nazdeek Wali Dukaan"

# 4. LOAD BALANCER
load_balancer = "Traffic ko 10 servers pe baant deta hai"
use = "1 lakh log ek saath aayen to site crash na ho"

# -----------------------------------------
#   TASK 3: HOW WEB SERVERS WORK
# -----------------------------------------

# WEBSITE KHULNE KE 5 STEPS:
def website_kaise_khulti_hai():
    step1 = "REQUEST: Tu browser mein google.com likhti"
    step2 = "DNS LOOKUP: Computer puchta 'IP kya hai?'"
    step3 = "SERVER PROCESSING: Server file dhoondta hai"
    step4 = "RESPONSE: Server HTML, CSS, Images bhejta hai" 
    step5 = "RENDER: Browser sab jod ke website dikhata hai"
    return "Website ready!"

# WEB SERVER TYPES:
servers = {
    "Apache": "Purana hai, sabse zyada use hota",
    "Nginx": "Naya aur tez hai, TryHackMe isi pe chalta",
    "IIS": "Microsoft ka, Windows servers ke liye"
}

# -----------------------------------------
#   1 MINUTE REVISION - EXAM SE PEHLE DEKH LENA
# -----------------------------------------

quick_revision = """
DNS     = Phone Book
HTTP    = Postman 
200     = All OK
404     = Page Gum Ho Gaya
Cookies = Yaad-dasht
CDN     = Nazdeek Wali Dukaan
POST    = Data Bhejna
GET     = Data Maangna
"""

print("Notes complete. Cyber Security mein basic strong kar le Asiya!")
