from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from django.http import HttpResponse
from django.shortcuts import render

languageChoices = [
    ("Hindi", "Hindi"),
    ("English", "English"),
]
# ------- HOMEPAGE --------- #
class HomePageTitle(models.Model):

    title = models.TextField()
    language = models.CharField(max_length=100, choices=languageChoices,default="English")

    def __str__(self):
        return self.title
        
    class Meta:
        db_table = 'homepage_pagetitle'
        verbose_name = 'Home: Page Title'
        verbose_name_plural = 'Home: Page Title'

class HomeMetaTag(models.Model):
    tags = models.CharField(max_length=20000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.tags

    class Meta:
        db_table = 'homepage_meta_tag'
        verbose_name = 'Home: Meta Tag'

class HomeMetaDescription(models.Model):
    description = models.CharField(max_length=200000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.description
    
    class Meta:
        db_table = 'homepage_meta_description'
        verbose_name = 'Home: Meta Description'

class HomeSection1(models.Model):
    heading_1 = models.CharField(max_length=200,blank=False,default="Get Money To Make Money - Quickly, Easily, Clearly")
    heading_2 = models.CharField(max_length=200,blank=False,default="Aap Ka Vishwaas, Humari Takneek")
    subtext = models.CharField(max_length=300,blank=False,default="It’s simple: we pay your suppliers first, then you repay us later.")
    btn1_text = models.CharField(max_length=100,blank=False,default="For Shopkeepers")
    btn1_url = models.TextField(max_length=100000,blank=False)
    btn2_text = models.CharField(max_length=100,blank=False,default="For Shopkeepers")
    btn2_url = models.TextField(max_length=100000,blank=False)
    image = models.ImageField(upload_to='homepage/images')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.heading_1

    class Meta:
        db_table = 'homepage_section1'
        verbose_name = 'Home: First Section - Two Button'
        verbose_name_plural = 'Home: First Section - Two Button'
       
class HomeSection2(models.Model):
    heading_1 = models.CharField(max_length=1000,blank=False)
    heading_2 = models.CharField(max_length=1000,blank=True)
    heading_3 = models.CharField(max_length=1000,blank=True)
    url = models.TextField(blank=False)
    btn_text = models.CharField(max_length=200,blank=False)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.heading_1
    
    class Meta:
        db_table = 'homepage_section2'
        verbose_name = 'Home: Learn More - Information Section'
        verbose_name_plural = 'Home: Learn More - Information Section'

class HomeSection3(models.Model):
    image_text = models.CharField(max_length=10000,blank=False)
    step_text = models.CharField(max_length=3,blank=False)
    image = models.ImageField(upload_to='homepage/images/')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.image_text
    
    class Meta:
        db_table = 'homepage_section3'
        verbose_name = 'Home: Steps - Image Carousel Section'
        verbose_name_plural = 'Home: Steps - Image Carousel Section'

class HomeSection4(models.Model):
    image_text = models.CharField(max_length=10000,blank=False)
    step_text = models.CharField(max_length=3,blank=False)
    image = models.ImageField(upload_to='homepage/images/')
    url = models.TextField(max_length=100000,blank=False)
    url_text = models.CharField(max_length=200)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.image_text
    
    class Meta:
        db_table = 'homepage_section4'
        verbose_name = 'Home: How Bridge2Capital Works - Section'
        verbose_name_plural = 'Home: How Bridge2Capital Works - Section'

class HomeSection5(models.Model):
    header = models.CharField(max_length=1000,verbose_name='Benefit Header')
    description = models.CharField(max_length=10000,verbose_name='Benefit Description')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.header
    
    class Meta:
        db_table = 'homepage_section5'
        verbose_name = 'Home: Benefit'
        verbose_name_plural = 'Home: Benefits'

class HomeSection6(models.Model):
    image = models.ImageField(upload_to='homepage/images/')
    heading = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.heading
    
    class Meta:
        db_table = 'homepage_section6'
        verbose_name = 'Home: Why Bridge2Capital?'
        verbose_name_plural = 'Home: Why Bridge2Capital?'

class HomeSection7(models.Model):
    image = models.ImageField(upload_to='homepage/images')
    name = models.CharField(max_length=1000,verbose_name='Partner Name')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'homepage_section7'
        verbose_name = 'Home: Partner'

class HomeSection8(models.Model):
    url = models.TextField(max_length=100000,blank=False,verbose_name='Video URL')
    name = models.CharField(verbose_name='Video Name',max_length=1000)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'homepage_section8'
        verbose_name = 'Home: What our Users are saying'
        verbose_name_plural = 'Home: What our Users are saying'

# -------- INVESTORS --------- #
class InvestorsPageTitle(models.Model):

    title = models.TextField()
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.title
        
    class Meta:
        db_table = 'investors_pagetitle'
        verbose_name = 'Investors: Page Title'
        verbose_name_plural = 'Investors: Page Title'

class InvestorsMetaTag(models.Model):

    tags = models.CharField(max_length=20000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.tags

    class Meta:
        db_table = 'investors_meta_tag'
        verbose_name = 'Investors: Meta Tag'

class InvestorsMetaDescription(models.Model):

    description = models.CharField(max_length=200000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.description

    class Meta:
        db_table = 'investors_meta_description'
        verbose_name = 'Investors: Meta Description'

class InvestorsOneButtonBanner(models.Model):

    header = models.CharField(max_length=1000000,verbose_name='Heading')
    paragraph = models.CharField(max_length=1000000,verbose_name='Paragraph')
    subtext = RichTextField(blank=False)
    button_text = models.CharField(max_length=100000,verbose_name='Button Text')
    button_url = models.TextField(max_length=100000,verbose_name='Button URL')
    image = models.ImageField(upload_to='investors/images')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.header

    class Meta:
        db_table = 'investors_onebuttonbanner'
        verbose_name = 'Investors: First Banner - One Button'

        verbose_name_plural = 'Investors: First Banner - One Button'

class InvestorsYellowStripSection(models.Model):

    header = models.CharField(max_length=1000000,verbose_name='Heading')
    paragraph = RichTextField(verbose_name='Paragraph')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.header

    class Meta:
        db_table = 'investors_yellowstripsection'
        verbose_name = 'Investors: Yellow Strip Banner'

        verbose_name_plural = 'Investors: Yellow Strip Banner'

class InvestorsOurTeam(models.Model):

    header = models.CharField(max_length=1000000,verbose_name='Heading')
    paragraph = RichTextField(verbose_name='Paragraph')
    image = models.ImageField(upload_to='investors/images')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.header



    class Meta:
        db_table = 'investors_ourteam'
        verbose_name = 'Investors: Our Team Banner'

        verbose_name_plural = 'Investors: Our Team Banner'



class InvestorsOurApproach(models.Model):

    header = models.CharField(max_length=1000000,verbose_name='Heading')
    paragraph = RichTextField(verbose_name='Paragraph')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.header



    class Meta:
        db_table = 'investors_ourapproach'
        verbose_name = 'Investors: Our Approach Banner'

        verbose_name_plural = 'Investors: Our Approach Banner'


class InvestorsOurBusinessModel(models.Model):

    header = models.CharField(max_length=1000000,verbose_name='Heading')
    paragraph = RichTextField(verbose_name='Paragraph')
    image = models.ImageField(upload_to='investors/images')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.header

    class Meta:
        db_table = 'investors_ourbusinessmodel'
        verbose_name = 'Investors: Our Business Model Banner'

        verbose_name_plural = 'Investors: Our Business Model Banners'

class InvestorsContactForm(models.Model):

    fname = models.CharField(verbose_name='Full Name',max_length=200)
    contactnumber = models.CharField(verbose_name='Contact Number',max_length=12)
    email = models.EmailField(verbose_name='Email Address',max_length=200)
    message = models.CharField(verbose_name='Message',max_length=600)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    class Meta:
        db_table = 'investors_contactform'
        verbose_name = 'Investors: Contact Form'

        verbose_name_plural = 'Investors: Contact Form'

    def __str__(self):

        return self.message

# ---------- PRESS -------- #
class PressPageTitleNews(models.Model):

    title = models.TextField()
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.title

        
    class Meta:
        db_table = 'news_pagetitlenews'
        verbose_name = 'Press: News Page Title'
        verbose_name_plural = 'Press: News Page Title'

class PressPageTitleBlog(models.Model):

    title = models.TextField()
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.title
        
    class Meta:
        db_table = 'news_pagetitleblog'
        verbose_name = 'Press: Blog Page Title'
        verbose_name_plural = 'Press: Blog Page Title'

class PressNews(models.Model):
    title = models.CharField(max_length=100,blank=False)
    by_tag = models.CharField(max_length=1000,blank=False,default="By Xtracap India")
    description = models.CharField(max_length=1000,blank=False)
    body = RichTextField(blank=False)
    image = models.ImageField(upload_to='news/images/')
    url = models.TextField(max_length=100000,blank=True)
    alt_tag = models.CharField(max_length=1000,blank=False,default='Bridge2Capital')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(blank=False)
    featured = models.BooleanField(default=False,verbose_name='Featured Post?')
    slug = models.SlugField(max_length=300,blank=False)
    meta_tags = models.CharField(max_length=1000000,blank=True,verbose_name='Meta Tags')
    meta_description = models.CharField(max_length=1000000,blank=True,verbose_name='Meta Description')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'news_news'
        verbose_name = 'Press: News'
        verbose_name_plural = 'Press: News'

class PressMetaTag(models.Model):
    tags = models.CharField(max_length=20000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.tags
    class Meta:
        db_table = 'news_meta_tag'
        verbose_name = 'Press: Meta Tag'

class PressMetaDescription(models.Model):
    description = models.CharField(max_length=200000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.description
    
    class Meta:
        db_table = 'news_meta_description'
        verbose_name = 'Press: Meta Description'

class PressBlog(models.Model):
    title = models.CharField(max_length=100,blank=False)
    by_tag = models.CharField(max_length=1000,blank=False,default="By Xtracap India")
    description = models.CharField(max_length=1000,blank=False)
    body = RichTextField(blank=False)
    image = models.ImageField(upload_to='news/images/')
    alt_tag = models.CharField(max_length=1000,blank=False,default='Bridge2Capital')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(blank=False)
    featured = models.BooleanField(default=False,verbose_name='Featured Post?')
    slug = models.SlugField(max_length=300,blank=False)
    meta_tags = models.CharField(max_length=1000000,blank=True,verbose_name='Meta Tags')
    meta_description = models.CharField(max_length=1000000,blank=True,verbose_name='Meta Description')
    url = models.TextField(max_length=100000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'news_blog'
        verbose_name = 'Press: Blog'
        verbose_name_plural = 'Press: Blog'

# ---------- ABOUT US -------- #
class AboutUsPageTitle(models.Model):

    title = models.TextField()
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.title
        
    class Meta:
        db_table = 'about_us_pagetitle'
        verbose_name = 'About Us: Page Title'
        verbose_name_plural = 'About Us: Page Title'

class AboutUsMetaTag(models.Model):

    tags = models.CharField(max_length=20000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    


    def __str__(self):

        return self.tags

    class Meta:
        db_table = 'about_us_meta_tag'
        verbose_name = 'About Us: Meta Tag'

class AboutUsMetaDescription(models.Model):

    description = models.CharField(max_length=200000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.description

    class Meta:
        db_table = 'about_us_meta_description'
        verbose_name = 'About Us: Meta Description'

class AboutUsMainBannerTwoButton(models.Model):

    header = models.CharField(max_length=10000,verbose_name='Heading')
    paragraph1 = models.CharField(max_length=1000000,verbose_name='Paragraph 1')
    paragraph2 = models.CharField(max_length=1000000,verbose_name='Paragraph 2')
    paragraph3 = models.CharField(max_length=1000000,verbose_name='Paragraph 3')
    button1_text = models.CharField(max_length=100000,verbose_name='Button 1 - Text')
    button2_text = models.CharField(max_length=100000,verbose_name='Button 2 - Text',blank=True)
    button1_url = models.TextField(max_length=100000,verbose_name='Button 1 - URL')
    button2_url = models.TextField(max_length=100000,verbose_name='Button 2 - URL',blank=True)
    image = models.ImageField(upload_to='about_us/images')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    class Meta:
        db_table = 'about_us_mainbannertwobutton'
        verbose_name = 'About Us: Main Banner - Two Button'
        verbose_name_plural = 'About Us: Main Banner - Two Button'



    def __str__(self):

        return self.header


class AboutUsGreenBorderSection(models.Model):

    header = models.CharField(max_length=100000,verbose_name='Heading')
    paragraph = models.CharField(max_length=1000000,verbose_name='Paragraph')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.header

    class Meta:
        db_table = 'about_us_greenbordersection'
        verbose_name = 'About Us: Green Radius - Text Banner'
        verbose_name_plural = 'About Us: Green Radius - Text Banner'

class AboutUsOurStory(models.Model):

    header = models.CharField(max_length=100000,verbose_name='Heading')
    paragraph1 = models.CharField(max_length=1000000,verbose_name='Paragraph 1')
    paragraph2 = models.CharField(max_length=1000000,verbose_name='Paragraph 2')
    image = models.ImageField(upload_to='about_us/images')
    person1_name = models.CharField(max_length=100000,verbose_name='Person 1 - Left - Name')
    person1_designation = models.CharField(max_length=100000,verbose_name='Person 1 - Left - Designation')
    person2_name = models.CharField(max_length=100000,verbose_name='Person 2 - Right - Name',blank=True)
    person2_designation = models.CharField(max_length=100000,verbose_name='Person 2 - Right - Designation',blank=True)
    person3_name = models.CharField(max_length=100000,verbose_name='Person 3 - Right - Name',blank=True)
    person3_designation = models.CharField(max_length=100000,verbose_name='Person 3 - Right - Designation',blank=True)  
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.header

    class Meta:
        db_table = 'about_us_ourstory'
        verbose_name = 'About Us: Our Story'
        verbose_name_plural = 'About Us: Our Story'

class AboutUsOurStoryParagraphs(models.Model):

    header = models.CharField(max_length=100000,verbose_name='Heading')
    paragraph = RichTextField(blank=False)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.header

    class Meta:
        db_table = 'about_us_ourstoryparagraphs'
        verbose_name = 'About Us: Our Story - Paragraphs'
        verbose_name_plural = 'About Us: Our Story - Paragraphs'

class AboutUsUpcomingProducts(models.Model):

    header = models.CharField(max_length=1000,verbose_name='Product Name')
    image = models.ImageField(upload_to='about_us/images',verbose_name='Logo')
    step = models.CharField(max_length=10,verbose_name='Step')
    description = models.CharField(max_length=1000,verbose_name='Product Description')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.header
    
    class Meta:
        db_table = 'about_us_upcomingproducts'
        verbose_name = 'About Us: Upcoming Product'
        verbose_name_plural = 'About Us: Upcoming Products'

class AboutUsAlternateBusinessModelSection(models.Model):

    header = models.CharField(max_length=100000,verbose_name='Heading')
    image = models.ImageField(upload_to='about_us/images',verbose_name='Image')
    paragraph = RichTextField(blank=False,verbose_name='Paragraph')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.header

    class Meta:
        db_table = 'about_us_alternatebusinessmodelsection'
        verbose_name = 'About Us: Business Model'
        verbose_name_plural = 'About Us: Business Models'

# ---------- CONTACT US -------- #
class ContactUsPageTitle(models.Model):

    title = models.TextField()
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.title
        
    class Meta:
        db_table = 'contact_us_pagetitle'
        verbose_name = 'Contact Us: Page Title'
        verbose_name_plural = 'Contact Us: Page Title'

class ContactUsMetaTag(models.Model):

    tags = models.CharField(max_length=20000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.tags

    class Meta:
        db_table = 'contact_us_meta_tag'
        verbose_name = 'Contact Us: Meta Tag'

class ContactUsMetaDescription(models.Model):

    description = models.CharField(max_length=200000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.description

    class Meta:
        db_table = 'contact_us_meta_description'
        verbose_name = 'Contact Us: Meta Description'

class ContactUsContactDetails(models.Model):

    address = RichTextField(blank=False)
    contact = RichTextField(blank=False)
    facebook_url = models.TextField(max_length=100000,blank=False,verbose_name='Facebook URL')
    linkedin_url = models.TextField(max_length=100000,blank=False,verbose_name='Linkedin URL')
    twitter_url = models.TextField(max_length=100000,blank=False,verbose_name='Twitter URL')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    class Meta:
        db_table = 'contact_us_contactdetails'
        verbose_name = 'Contact Us: Contact Details'
        verbose_name_plural = 'Contact Us: Contact Details'

    def __str__(self):

        return 'Contact Details'

class ContactUsContactForm(models.Model):

    fname = models.CharField(verbose_name='Full Name',max_length=200)
    contactnumber = models.CharField(verbose_name='Contact Number',max_length=12)
    email = models.EmailField(verbose_name='Email Address',max_length=200)
    message = models.CharField(verbose_name='Message',max_length=600)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    class Meta:
        db_table = 'contact_us_contactform'
        verbose_name = 'Contact Us: Contact Form'
        verbose_name_plural = 'Contact Us: Contact Form'

    def __str__(self):

        return self.message

# ---------- CREDIT PRODUCT -------- #
class CreditProductPageTitle(models.Model):

    title = models.TextField()
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.title
        
    class Meta:
        db_table = 'credit_product_pagetitle'
        verbose_name = 'Credit Product: Page Title'
        verbose_name_plural = 'Credit Product: Page Title'

class CreditProductMetaTag(models.Model):

    tags = models.CharField(max_length=20000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.tags

    class Meta:
        db_table = 'credit_product_meta_tag'
        verbose_name = 'Credit Product: Meta Tag'

class CreditProductMetaDescription(models.Model):

    description = models.CharField(max_length=200000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.description

    class Meta:
        db_table = 'credit_product_meta_description'
        verbose_name = 'Credit Product: Meta Description'

class CreditProductTwoButtonSection(models.Model):

    header = models.CharField(max_length=1000,verbose_name='Heading')
    paragraph1 = models.CharField(max_length=1000,verbose_name='Paragraph 1')
    paragraph2 = models.CharField(max_length=1000,verbose_name='Paragraph 2')
    button1_text = models.CharField(max_length=1000,verbose_name='Button 1 - Text')
    button1_url = models.TextField(max_length=10000,blank=True)
    button2_url = models.TextField(max_length=10000,blank=True)
    button2_text = models.CharField(max_length=1000,verbose_name='Button 2 - Text',blank=True)
    image = models.ImageField(upload_to='credit_product/images')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.header

    class Meta:
        db_table = 'credit_product_twobuttonsection'
        verbose_name = 'Credit Product: Section 1 - Two Button'
        verbose_name_plural = 'Credit Product: Section 1 - Two Button'

class CreditProductOneButtonSection(models.Model):

    header = RichTextField(verbose_name='Heading',blank=True)
    paragraph = RichTextField(verbose_name='Paragraph',blank=True)
    button1_text = models.CharField(max_length=1000,verbose_name='Button 1 - Text',blank=True)
    button1_url = models.TextField(max_length=10000,blank=True)
    image = models.ImageField(upload_to='credit_product/images')
    alt_tag = models.CharField(verbose_name='Image Alt Tag',max_length=1000)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.alt_tag

    class Meta:
        db_table = 'credit_product_onebuttonsection'
        verbose_name = 'Credit Product: Section 2 - One Button'
        verbose_name_plural = 'Credit Product: Section 2 - One Button'

class CreditProductProductFeatures(models.Model):

    icon = models.ImageField(upload_to='credit_product/images')
    header = RichTextField(verbose_name='Heading',blank=False)
    paragraph = RichTextField(verbose_name='Paragraph',blank=False)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.header

    class Meta:
        db_table = 'credit_product_productfeatures'
        verbose_name = 'Credit Product: Product Features'
        verbose_name_plural = 'Credit Product: Product Features'

class CreditProductProductTnCs(models.Model):

    icon = models.ImageField(upload_to='credit_product/images')
    header = RichTextField(verbose_name='Heading',blank=False,)
    paragraph = RichTextField(verbose_name='T&Cs',blank=False)
    button = models.TextField(verbose_name="Button Text",default="View")
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.header

    class Meta:
        db_table = 'credit_product_producttncs'
        verbose_name = 'Cerdit Product: Product TNCs'
        verbose_name_plural = 'Credit Product: Product TNCs'

# ---------- FAQ -------- #
class FAQPageTitle(models.Model):

    title = models.TextField()
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.title
        
    class Meta:
        db_table = 'faq_pagetitle'
        verbose_name = 'FAQ: Page Title'
        verbose_name_plural = 'FAQ: Page Title'

class FAQMetaTag(models.Model):

    tags = models.CharField(max_length=20000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.tags

    class Meta:
        db_table = 'faq_meta_tag'
        verbose_name = 'FAQ: Meta Tag'

class FAQMetaDescription(models.Model):

    description = models.CharField(max_length=200000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.description

    class Meta:
        db_table = 'faq_meta_description'
        verbose_name = 'FAQ: Meta Description'

class FAQQuestionAnswer(models.Model):

    question = models.CharField(max_length=100000000,verbose_name='Question')
    answer = RichTextField(blank=False)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    class Meta:
        db_table = 'faq_questionanswer'
        verbose_name = 'FAQ: Q&A'
        verbose_name_plural = 'FAQ: Q&A'

    def __str__(self):

        return self.question

# ---------- PRIVACY -------- #
class PrivacyPageTitle(models.Model):

    title = models.TextField()
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.title
        
    class Meta:
        db_table = 'privacy_pagetitle'
        verbose_name = 'Privacy: Page Title'
        verbose_name_plural = 'Privacy: Page Title'

class PrivacyMetaTag(models.Model):

    tags = models.CharField(max_length=20000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.tags

    class Meta:
        db_table = 'privacy_meta_tag'
        verbose_name = 'Privacy: Meta Tag'

class PrivacyMetaDescription(models.Model):

    description = models.CharField(max_length=200000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.description

    class Meta:
        db_table = 'privacy_meta_description'
        verbose_name = 'Privacy: Meta Description'

class PrivacyPrivacyPolicy(models.Model):

    header = models.CharField(max_length=10000,verbose_name='Heading')
    subheader = RichTextField(blank=False,verbose_name='Sub Heading')
    paragraph = RichTextField(blank=False)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    class Meta:
        db_table = 'privacy_privacypolicy'
        verbose_name = 'Privacy: Privacy Policy'
        verbose_name_plural = 'Privacy: Privacy Policy'

    def __str__(self):

        return self.header

# ---------- TERMS & CONDITIONS -------- #
class TNCPageTitle(models.Model):

    title = models.TextField()
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.title
        
    class Meta:
        db_table = 'terms_conditions_pagetitle'
        verbose_name = 'TNC: Page Title'
        verbose_name_plural = 'TNC: Page Title'

class TNCMetaTag(models.Model):

    tags = models.CharField(max_length=20000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.tags

    class Meta:
        db_table = 'terms_conditions_meta_tag'
        verbose_name = 'TNC: Meta Tag'

class TNCMetaDescription(models.Model):

    description = models.CharField(max_length=200000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.description

    class Meta:
        db_table = 'terms_conditions_meta_description'
        verbose_name = 'TNC: Meta Description'

class TNCTermsConditions(models.Model):

    header = models.CharField(max_length=10000,verbose_name='Heading')
    subheader = RichTextField(blank=False,verbose_name='Sub Heading')
    paragraph = RichTextField(blank=False)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    class Meta:
        db_table = 'terms_conditions_termsconditions'
        verbose_name = 'TNC: Terms & Conditions'
        verbose_name_plural = 'TNC: Terms & Conditions'

    def __str__(self):

        return self.header

# ---------- TESTIMONIALS -------- #
class TestimonialsPageTitle(models.Model):

    title = models.TextField()
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):
        return self.title
        
    class Meta:
        db_table = 'testimonials_pagetitle'
        verbose_name = 'Testimonials: Page Title'
        verbose_name_plural = 'Testimonials: Page Title'

class TestimonialsMetaTag(models.Model):

    tags = models.CharField(max_length=20000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.tags

    class Meta:
        db_table = 'testimonials_meta_tag'
        verbose_name = 'Testimonials: Meta Tag'

class TestimonialsMetaDescription(models.Model):

    description = models.CharField(max_length=200000,blank=True)
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.description

    class Meta:
        db_table = 'testimonials_meta_description'
        verbose_name = 'Testimonials: Meta Description'

class TestimonialsTestimonial(models.Model):

    name = models.CharField(max_length=1000,verbose_name='Customer Name')
    category = models.CharField(max_length=1000,verbose_name='Business Type')
    image = models.ImageField(upload_to='testimonials/images/',verbose_name='Customer Image')
    body = models.CharField(max_length=1000,verbose_name='Customer Message')
    description = models.CharField(max_length=1000,verbose_name='Message Snippet (For Homepage)')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")
    
    def __str__(self):

        return self.name

    class Meta:
        db_table = 'testimonials_testimonial'
        verbose_name = 'Testimonials: Testimonial'
        verbose_name_plural = 'Testimonials: Testimonials'

class TestimonialsSection1(models.Model):

    heading_1 = models.CharField(max_length=1000,blank=False,default="What Business Owners Like You Are Saying",verbose_name='Heading')
    subtext = models.CharField(max_length=1000,blank=False,default="Listen to what fast-expanding Bridge2Capital family thinks.",verbose_name='Sub Text')
    image = models.ImageField(upload_to='testimonials/images/')
    language = models.CharField(max_length=100, choices=languageChoices,default="English")

    def __str__(self):

        return self.heading_1

    class Meta:
        db_table = 'testimonials_section1'
        verbose_name = 'Testimonials: First Section'
        verbose_name_plural = 'Testimonials: First Section'

class CreditLandingForm(models.Model):

    name = models.TextField(blank=True,null=True)
    email = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    business = models.TextField(blank=True, null=True)
    product = models.TextField(blank=True, null=True)
    gst = models.BooleanField(blank=True,default=False)
    pan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'credit_leads'
        verbose_name = 'Credit Leads'
        verbose_name_plural = 'Credit Leads'
