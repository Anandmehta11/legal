from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///legal_link.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this to a secure secret key
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Lawyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=True)  # Add address column
    phone = db.Column(db.String(20), nullable=True)    # Add phone column
     
    def __repr__(self):
        return f'Lawyer {self.name}'
    
with app.app_context():
    db.create_all()
   
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password', 'error')
            return render_template('auth.html', error='Invalid email or password')
    
    return render_template('auth.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validate required fields
        if not all([name, email, password, confirm_password]):
            flash('All fields are required', 'error')
            return render_template('auth.html', error='All fields are required')
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('auth.html', error='Passwords do not match')
        
        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered', 'error')
            return render_template('auth.html', error='Email already registered')
        
        try:
            hashed_password = generate_password_hash(password)
            new_user = User(name=name, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while creating your account', 'error')
            return render_template('auth.html', error='Error creating account')
    
    # GET request - show the signup form
    return render_template('auth.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect(url_for('index'))

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    search_query = request.args.get('search_query')
    lawyers = []
    
    if search_query:
        if not session.get('user_id'):
            flash('Please login to search for lawyers', 'error')
            return redirect(url_for('login'))
        lawyers = Lawyer.query.filter(
            Lawyer.name.ilike(f"%{search_query}%") |
            Lawyer.address.ilike(f"%{search_query}%") |
            Lawyer.phone.ilike(f"%{search_query}%")
        ).all()
    
    return render_template('index.html', 
                         lawyers=lawyers, 
                         search_query=search_query, 
                         user=session.get('user_name'))

@app.route('/find-lawyer')
def find_lawyer():
    lawyers = Lawyer.query.all()
    return render_template('find-lawyer.html', lawyers=lawyers)

@app.route('/divorce')
def divorce():
    return render_template('divorce.html')  # Render a new template for Divorce


@app.route('/child-custody')
def child_custody():
    return render_template('child-custody.html')  # Render a new template for Child Custody

@app.route('/medical-negligence')
def medical_negligence():
    return render_template('medical-negligence.html')  # Render a new template for Medical Negligence

@app.route('/criminal')
def criminal():
    return render_template('criminal.html')  # Render a new template for Criminal

@app.route('/cyber-crime')
def cyber_crime():
    return render_template('cyber-crime.html')  # Render a new template for Cyber Crime

@app.route('/property')
def property():
    return render_template('property.html')  # Render a new template for Property

@app.route('/labour-services')
def labour_services():
    return render_template('labour-services.html')  # Render a new template for Labour & Services  

@app.route('/landlord-tenant')
def landlord_tenant():
    return render_template('landlord-tenant.html')  # Render a new template for Landlord/Tenant

@app.route('/real-estate')
def real_estate():
    return render_template('real-estate.html')  # Render a new template for Real Estate  

@app.route('/trademark-rights')
def trademark_rights():
    return render_template('trademark-rights.html')  # Render a new template for Trademark & Rights

@app.route('/customs-central-excise')
def customs_central_excise():
    return render_template('customs-central-excise.html')  # Render a new template for Customs & Central Excise

@app.route('/startup')
def startup():
    return render_template('startup.html')  # Render a new template for Startup  

@app.route('/banking-finance')
def banking_finance():
    return render_template('banking-finance.html')  # Render a new template for Banking/Finance

@app.route('/corporate')
def corporate():
    return render_template('corporate.html')  # Render a new template for Corporate

@app.route('/gst-tax')
def gst_tax():
    return render_template('gst-tax.html')  # Render a new template for GST/Tax

@app.route('/consumer-court')
def consumer_court():
    return render_template('consumer-court.html')  # Render a new template for Consumer Court

@app.route('/civil')
def civil():
    return render_template('civil.html')  # Render a new template for Civil


@app.route('/cheque-bounce')
def cheque_bounce():
    return render_template('cheque-bounce.html')  # Render a new template for Cheque Bounce

@app.route('/rera')
def rera():
    return render_template('rera.html')  # Render a new template for RERA

@app.route('/litigation')
def litigation_dispute_resolution():
    return render_template('litigation.html')  # Render a new template for Litigation and Dispute Resolution

@app.route('/cat')
def cat():
    return render_template('cat.html')  # Render a new template for CAT

@app.route('/drt')
def drt():
    return render_template('drt.html')  # Render a new template for DRT

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')  # Render a new template for Documentation

@app.route('/insurance')
def insurance():
    return render_template('insurance.html')  # Render a new template for Insurance


@app.route('/immigration')
def immigration():
    return render_template('immigration.html')  # Render a new template for Immigration

@app.route('/international-law')
def international_law():
    return render_template('international-law.html')  # Render a new template for International Law

@app.route('/mat')
def mat():
    return render_template('mat.html')  # Render a new template for MAT

@app.route('/ipc-sections')
def ipc_sections():
    return render_template('ipc-sections.html')  # Render a new template for IPC Sections

@app.route('/crpc-sections')
def crpc_sections():
    return render_template('crpc-sections.html')  # Render a new template for CRPC Sections

@app.route('/bns-sections')
def bns_sections():
    return render_template('bns-sections.html')  # Render a new template for BNS Sections

@app.route('/bnss-sections')
def bnss_sections():
    return render_template('bnss-sections.html')  # Render a new template for BNSS Sections

@app.route('/cpc-sections')
def cpc_sections():
    return render_template('cpc-sections.html')  # Render a new template for CPC Sections

@app.route('/dowry-prohibition-act')
def dowry_prohibition_act():
    return render_template('dowry-prohibition-act.html')  # Render a new template for The Dowry Prohibition Act

@app.route('/domestic-violence-act')
def domestic_violence_act():
    return render_template('domestic-violence-act.html')

@app.route('/bharatiya-sakshya-adhiniyam-act')
def bharatiya_sakshya_adhiniyam_act():
    return render_template('bharatiya-sakshya-adhiniyam-act.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')  # Render privacy policy page

@app.route('/terms')
def terms():
    return render_template('terms.html')  # Render terms of service page

@app.route('/category/<specialty>')
def category(specialty):
    lawyers = Lawyer.query.filter_by(specialty=specialty).all()
    return render_template('index.html', lawyers=lawyers, category=specialty)

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Here you would typically:
        # 1. Save to database
        # 2. Send email notification
        # 3. Send confirmation email to user
        
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('home'))

@app.route('/lawyer/<lawyer_id>')
def lawyer_profile(lawyer_id):
    # Convert lawyer_id to a format that matches our data
    lawyer_id = lawyer_id.replace('-', ' ').title()
    
    # Find the lawyer in our data
    lawyer = None
    if lawyer_id == "Sudhakar Musale":
        lawyer = {
            "name": "Sudhakar Musale",
            "specialty": "Corporate Law & Legal Advisor",
            "address": "Grasim Industries Pvt.Ltd., Hanuman Nagar, Worli, Mumbai",
            "phone": "+91 99307 94321",
            "location": "Mumbai"
        }
    elif lawyer_id == "Adv Yatin V Gujrathi":
        lawyer = {
            "name": "Adv Yatin V Gujrathi",
            "specialty": "Marital, Property & Cheating Cases",
            "address": "Mezzanine Floor, Sterling Tower, Syndicate Bus Stop, Kalyan West",
            "phone": "+91 93205 19026",
            "email": "yatingujrathi@yahoo.co.in",
            "location": "Kalyan West"
        }
    elif lawyer_id == "Adv Aslesha Y Gujrathi":
        lawyer = {
            "name": "Adv Aslesha Y Gujrathi",
            "specialty": "Marital & Civil Law",
            "address": "Mezzanine Floor, Sterling Tower, Syndicate Bus Stop, Kalyan West",
            "phone": "+91 98691 93019",
            "location": "Kalyan West"
        }
    
    if lawyer:
        return render_template('lawyer_profile.html', lawyer=lawyer)
    else:
        flash('Lawyer not found', 'error')
        return redirect(url_for('home'))

@app.route('/search-feature')
def search_feature():
    return render_template('search_feature.html')

@app.route('/profile-feature')
def profile_feature():
    return render_template('profile_feature.html')

@app.route('/community-feature')
def community_feature():
    return render_template('community_feature.html')

@app.route('/articles-feature')
def articles_feature():
    return render_template('articles_feature.html')

if __name__ == '__main__':   
    app.run(debug=True)

