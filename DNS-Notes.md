DNS = Domain Name System 
Kaam: Domain name ko IP address mein convert karta hai
Example: google.com → 142.250.182.206

--------------------------------------
1. SUBDOMAIN RULES
--------------------------------------
Max length of subdomain: 63 characters
Max length of full domain name: 253 characters
Allowed characters: a-z, 0-9, hyphen -
NOT allowed: underscore _
Example: blog.example.com ← 'blog' subdomain hai

2. TYPES OF TLD

TLD = Top Level Domain
gTLD = Generic TLD → .com, .org, .net
ccTLD = Country Code TLD → .uk, .in, .pk, .co.uk

3. DNS RECORDS

A Record     → IPv4 address deta hai
AAAA Record  → IPv6 address deta hai  
MX Record    → Mail server batata hai, email kahan bhejni hai
TXT Record   → Text info rakhta hai, verification ke liye use hota hai
CNAME Record → Ek domain ko dusre domain pe point karta hai

4. TYPES OF DNS SERVERS

1. Recursive Resolver/DNS Recursor
   → ISP provide karta hai
   → User ke liye poora kaam karta hai, final IP dhoond ke deta hai

2. Root Server
   → DNS ka starting point
   → Batata hai .com, .org wale TLD server kahan hain

3. TLD Server  
   → .com, .net, .org handle karta hai
   → Batata hai 'google.com' ka authoritative server kaun sa hai

4. Authoritative Server
   → Final server jo domain ke saare records rakhta hai
   → Yahi real IP address batata hai

5. IMPORTANT FIELD

TTL = Time To Live
Kaam: Batata hai DNS record ko kitni der tak cache karna hai
Unit: Seconds mein hota hai
Example: TTL=300 matlab 5 min tak cache rahega

6. COMMANDS

nslookup google.com  → Domain ka IP nikalne ke liye
dig google.com       → Detailed DNS info ke liye

THM QUIZ ANSWERS

Q: Max length of subdomain? → 63
Q: Character not allowed in subdomain? → _
Q: Max length of domain name? → 253  
Q: .co.uk type? → ccTLD
Q: Record for email? → MX
Q: Record for IPv6? → AAAA
Q: Field for cache time? → TTL
Q: ISP wala DNS server? → recursive
Q: Server with all domain records? → authoritative
