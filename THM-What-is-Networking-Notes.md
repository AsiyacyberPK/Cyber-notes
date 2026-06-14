# TryHackMe: What is Networking? - Complete Notes

**Room Progress:** 90% ✅  

## 1. Basic Definitions
- **Network**: Aisi devices jo aapas mein connected hon.  
    - Example: Phone + Laptop + Router = 1 Network

## 2. IP Address Basics
| Term | Full Form | Matlab | Yaad Rakhne Ka Tareeka |
| --- | --- | --- | --- |
| **IP** | Internet Protocol | Har device ka ghar ka address | IP = Internet ka Pata |
| **Octet** | 8-bit section | IP address ka 1 hissa | Oct = 8, jaise October 10th month tha |
| **IPv4** | Version 4 | 4 sections wala IP | 192.168.1.1 = 4 hisse hain |

**Example IPv4:** `10.10.10.10`  
- 4 sections/octets hain  
- Har section 0-255 tak ho sakta hai  

## 3. MAC Address
- **MAC**: Media Access Control  
- Device ka **permanent physical address** hota hai  
- Factory se hi chip mein likha aata hai  
- Example: `00:1A:2B:3C:4D:5E`  
- **Spoofing**: MAC address nakli laga kar website ko dhoka dena  

## 4. Ping & ICMP
| Concept | Detail | Command |
| --- | --- | --- |
| **Ping** | Check karna ke device zinda hai ya nahi | `ping 10.10.10.10` |
| **ICMP** | Internet Control Message Protocol | Ping isi ko use karta hai |
| **Use** | Network testing, server up/down check | `ping 8.8.8.8` = Google DNS |

## 5. Flags From Room
1. **MAC Spoofing Lab**: `THM{YOU_GOT_ON_TRYHACKME}`  
2. **Ping Lab**: `THM{I_PINGED_THE_SERVER}`  

## 6. Next Steps - Task 5
- **Intro to LAN**: Agla room  
- **100% XP Boost** is par use karna unlock hone ke baad  

## Quick Revision - 1 Minute Mein
1. **Network** = Connected devices  
2. **IP** = Internet Protocol = Device ka address  
3. **IPv4** = 4 octets = `x.x.x.x`  
4. **MAC** = Media Access Control = Device ka permanent ID  
5. **Ping** = ICMP use karta hai = Server check karne ke liye  

**Pro Tip:** IP address = Ghar ka address jo badal sakta hai. MAC address = CNIC number jo permanent hai.
