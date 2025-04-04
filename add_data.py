from app import app, db, Lawyer

# Add data
lawyers = [
    {
        "name": "A S RAMESHAN",
        "address": "405, Birya House, 265, Bazargate Street, Fort, Mumbai-400001",
        "phone": "9223436705"
    },
    {
        "name": "Aarti Prashant Bhide",
        "address": "A/1, Suman Sudha, Pestom Sagar Road no. 5, Chembur, Mumbai 400 089",
        "phone": "9821152849"
    },
    {
        "name": "AKJS ADVOCATES",
        "address": "81, Sneh Sadan, OPP. Colaba Post Office, 163 Colaba Road, Mumbai-400005",
        "phone": "9969035363"
    },
    {
        "name": "AKS Legal Consultants",
        "address": "Bhupen Chambers 2nd Floor, Office No-48. Opposite BSE, Dalal Street",
        "phone": "Mob. not provided"
    },
    {
        "name": "Amarchand & Mangaldas & Suresh A. Shroff & Co.",
        "address": "Peninsula Chambers, Peninsula Corporate Park, Ganpatrao Kadam Marg, Lower Parel, Mumbai – 400 013",
        "phone": "Mob. not provided"
    },
    {
        "name": "Amit S Gadkari",
        "address": "5/A, Meghdoot Dhara, Rambaug Lane No. 4, Opp. Kalyan Janata bank, Kalyan (W) - 421 304",
        "phone": "9821656595"
    },
    {
        "name": "Anant Narayan",
        "address": "109, Esplanade Mansion, Room No-1, 1st Floor, 144, M. G. Road, Kalaghoda, Mumbai-400023",
        "phone": "9892280791"
    },
    {
        "name": "Aruna Shantaram Pai",
        "address": "Gangotri Co-op, Hsg. Society, Building No. 73, B - Wing, Flat no. 204, Tilaknagar Chembur, Mumbai 400089",
        "phone": "Contact not provided"
    },
    {
        "name": "ASA LAW FIRM",
        "address": "102, Wellington Business Park-1 off Andheri Kurla Road, Marol Andheri East, Mumbai-400059",
        "phone": "9167912510"
    },
    {
        "name": "Atul Patkar",
        "address": "A -1, Bhalchandra Building, Ground Floor, Anandban Co_op, Housing Society, Near Gaodevi Maidan. Naupada Thane (West)",
        "phone": "9821656991",
        "email": "atul.patkar2007@rediffmail.co.in"
    },
    {
        "name": "B Bahulayan",
        "address": "B-9, jal-Usha Co-op. Housing Society Ltd. Jeevan Vikas Kendra Marg Koldongari Vile parle East, Mumbai-400057",
        "phone": "9820139970"
    },
    {
        "name": "Bhave & Co.",
        "address": "65/Old Oriental Building, 2nd Floor, M. G. Road, Opp. Hong Kong bank Bldg., Hutatma Chowk Mumbai -400 023",
        "phone": "Mob. not provided"
    },
    {
        "name": "Bidan Chandran B. G",
        "address": "123, Mittal Court, A- Wing, Nariman Point, Mumbai-400021",
        "phone": "9892852651"
    },
    {
        "name": "Classic Law Associates",
        "address": "The Hub, one India Bulls Tower 2B, 10th Floor 841 Senapati Bapat Marg, Mumbai 400013",
        "phone": "9887798134"
    },
    {
        "name": "Cosulta Juris",
        "address": "Hira Building, 17/19 Mint Road, Mumbai-01",
        "phone": "Ph- 22835050; 22618259"
    },
    {
        "name": "D S K Legal",
        "address": "4th Floor, Express Towers, Nariman Point, Mumbai 400 021",
        "phone": "022/66588060"
    },
    {
        "name": "D. J. Pandya",
        "address": "A-4, Ambe Mahal, N. S. Road, Mulund (W), Mumbai",
        "phone": "9892228818"
    },
    {
        "name": "Dave Girish & Co",
        "address": "1st Floor, Sethna Bldg., 55, Maharshi Karve Road, Near Marine Lines Station, Mumbai-400 002",
        "phone": "Contact not provided"
    },
    {
        "name": "Deepashree S Wantmure",
        "address": "404, Shivam Building, Bhanu Nagar, Kalyan west, Distt- Thane",
        "phone": "9892081205"
    },
    {
        "name": "Dhananjay S. Bhosle",
        "address": "3/ Laxmi Chhaya Niwas, Thane Kokan Nagar, J. M. Road, Bhandup (West), MUMBAI-400 078",
        "phone": "9324527329"
    },
    {
        "name": "Dr. Pravin V Mehta",
        "address": "008/14-A, Sierra Towers, Lokhandwala Complex Kandivil (E), Mumbai – 400 101",
        "phone": "9322232985"
    },
    {
        "name": "ECONOMIC LAW PRACTICE",
        "address": "1502, A WING, Dalamal Towers, Nariman Point, Mumbai- 400021",
        "phone": "Contact not provided"
    },
    {
        "name": "Fatima R Lakdawala",
        "address": "Office No. 7, casa Blanca Trade Place, 4th Latin Chambers, Dalal Street, Fort, Mumbai-01",
        "phone": "9820775186"
    },
    {
        "name": "Goenka Law Associates",
        "address": "Saroosh Building, 251, Dr. D.N. Road, 1st Floor, Fort, Mumbai – 400 001",
        "phone": "022/22612787"
    },
    {
        "name": "Govind Desai Associates",
        "address": "1, Nichi Nivas, Pitamber Lane, Off. Gabriel Road, Mahim, Mumbai – 400 016",
        "phone": "022/24465990",
        "email": "administrator@gdafirm.com"
    },
    {
        "name": "Hiroo Advani",
        "address": "ADVANI & CO. 10, Thakur Nivas, Level 2, 173, J. Tata Road, Churchgate, Mumbai – 400 020",
        "phone": "Mob. not provided"
    }, 
    {
        "name": "J. K. Juris & Advocates",
        "address": "A/107, 1st Floor, Eastern Court, Corner of Tejpal & Parleshwar Rd, Vile Parle (E), Mumbai-57",
        "phone": "9322232211"
    },
    {
        "name": "Jay K Bhatia",
        "address": "A-302, Mangalkunch, Mount Pleasant Road, Malabar Hills, Mumbai- 400006",
        "phone": "Contact not provided"
    },
    {
        "name": "K Balakrishna Adyanthaya",
        "address": "17, Anand, Ashok Nagar Cross No.3, Kandivali (East) Mumbai 400 101, Chambers: 26, Maharashtra Bhavan, 12/14, Bora Masjid Street, Behind Handloom House, Fort, Mumbai 400 001",
        "phone": "9820175484"
    },
    {
        "name": "K.K. Associates",
        "address": "2nd Floor, Suit No 32/33 Ashoka Centre, LT Marg Mumbai 400001",
        "phone": "9167485233"
    },
    {
        "name": "Karunakar S. Shetty",
        "address": "Off No.-6, 4th Floor Bhagvodaya Building, 79, Nagindas Master Road, Fort, Mumbai-400001",
        "phone": "Contact not provided"
    },
    {
        "name": "Kusumakar Kaushik",
        "address": "610A,611 A, Commerce House 140, N.M.Road, Near Rhythem House Fort, Mumbai -400023",
        "phone": "9321210841"
    },
    {
        "name": "Kavita Gupta",
        "address": "A/11/553, Shantinath CHS Shankar Nagar Road 2, Bhind Shell Colony, Chembur Mumbai-400071",
        "phone": "Contact not provided"
    },
    {
        "name": "Kishor Ramesh Nemade",
        "address": "A-3. Gr Floor, Neelkanth Building, Behind Vaishali Theatre, Sarvodaya Nagar, Badlapur (W), Ambarnath, Dist. Thane",
        "phone": "9320674642/9730225718"
    },
    {
        "name": "Legal Pundits International Services Pvt. Ltd",
        "address": "Neelkanth Building, Opposite Flyover Bridge ROC Building , 98-99, Marine Drive Mumbai 400 002",
        "phone": "Mob. not provided"
    },
    {
        "name": "Little & Co.",
        "address": "Central Bank Building, M. G. Road, Mumbai - 400 023",
        "phone": "Mob. not provided"
    },
    {
        "name": "M. Janardhan",
        "address": "111-A, First Floor Karimji Compound, M.G. Road Opp. Mumbai University. Mumbai - 400023",
        "phone": "lexelcel@gmail.com"
    },
    {
        "name": "M. Prabhakaran",
        "address": "2nd Floor , Hira Building, 17-19, Mint Road Mumbai-400001",
        "phone": "Mob. not provided"
    },
    {
        "name": "M. V. Kini & Co",
        "address": "Kini HOUSE |1st Floor|261/263 | Near Citibank | D.N. Road | Fort | Mumbai 400 001",
        "phone": "Mob. not provided"
    },
    {
        "name": "M/s Kavitha S Lalwani",
        "address": "108/T-4, Esplanade Mansion, 144 M G Road Fort, Mumbai 23",
        "phone": "9892395823"
    },
    {
        "name": "M/s. Orbit Law Services",
        "address": "1201, B-wing, Dalmal Towers,211, Free Press Journal Marg, Nariman Point, Mumbai 400021",
        "phone": "9869022636"
    },
    {
        "name": "M/s. MSR & Associates",
        "address": "30, 1st, Hanuman Building, 308 perin Nariman Street, Behind RBI, Fort, Mumbai",
        "phone": "Contact not provided"
    },
    {
        "name": "M/s. MDP Partners",
        "address": "1st Floor, Udyog Bhava, 29, Watchand Hirachand Marg Ballard Estate, Mumbai-400001",
        "phone": "Mob. not provided"
    },
    {
        "name": "M/s. Sanjeev Kanchan & Co.",
        "address": "4, Milan buildings, 189/93, (Bazar Gate Street), Perin Nariman Street, Fort Mumbai-400001",
        "phone": "9820072038; 9967352811"
    },
    {
        "name": "MANDALIK LAW SERVICES",
        "address": "194/2, Ashoka Shopping Centre, GT Hospital Compound, LT Marg, Mumbai-400001",
        "phone": "9892143848"
    },
    {
        "name": "MANEESHA PATEL",
        "address": "Room no. 14 A, First floor,32, Rajabahadur Mansion, Am-balal Doshi Marg, (Hamam street). Fort, Mumbai-400023",
        "phone": "Contact not provided"
    },
    {
        "name": "MANISH D TIWARI",
        "address": "25, 1st Floor, Engineer Bldng, 288, Shahid Bhagat Singh Marg, Fort, Mumbai",
        "phone": "9224166107, 9619302138"
    },
    {
        "name": "Manisha M. Umbrajkar",
        "address": "C 304/305, Royale, Neelkanth Palms, Behind Cine-max, Off Ghod Bunder Road, Kabur Bavdi, Thane West-400607",
        "phone": "9820008867 9322987887"
    },
    {
        "name": "Maravoor Wamorkar & Co",
        "address": "Maravoor Chambers, 30/H, Bomanji Lane, Behind Fire Brigade, Fort, Mumbai -400 001",
        "phone": "Contact not provided"
    },
    {
        "name": "Meharia & Co.",
        "address": "105, Bombay Samachar Marg, R No.-23. 2nd floor, Fort Mumbai-23",
        "phone": "Mob. not provided"
    },
    {
        "name": "Sudhakar Musale",
        "address": "Grasim Industries Pvt.Ltd.,Hanuman Nagar,Worli,Mumbai",
        "phone": "9930794321",
        "specialty": "Corporate Law,legal advisor"
    },
    {
        "name": "Adv Yatin V Gujrathi",
        "address": "Mezzanine Floor,  Sterling towet, Syndicate bus stop, Kalyan west",
        "phone": "9320519026",
        "specialty": " Marital, Property matter, Cheating cases"
    },
    {
        "name": "Adv Aslesha Y Gujrathi",
        "address": "Mezzanine Floor,  Sterling towet, Syndicate bus stop, Kalyan west",
        "phone": "9869193019",
        "specialty": "Marital, Civil"
    },
          ]
          


def add_database():
    with app.app_context():
        db.session.query(Lawyer).delete()

        for lawyer_data in lawyers:
            lawyer = Lawyer(
                name=lawyer_data['name'], 
                address=lawyer_data['address'], 
                phone=lawyer_data['phone'], 
                specialty="General", 
                rating=4.0, 
                image_url="images/avatar1.png"
            )
            db.session.add(lawyer)

        db.session.commit()
        print("Data added successfully!")


if __name__ == "__main__":
    add_database()
