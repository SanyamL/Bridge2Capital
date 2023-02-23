from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.mail import send_mail
from general import ContactFormFilled

ghseet_cred = {
  "type": "service_account",
  "project_id": "xtracap",
  "private_key_id": "4172ff89ea79d5749549d4c7430ca477709c61cf",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC3VqnQ2ee1lMlB\n4xyFYKPrbaZyMidS7JLFRNef8Imhgk6nSgfJUnoly6olTvF34MondbmJSPZwAL/2\npaIKzjmql4GJ5sB0JXaPs8GNNFz+rHDjm197UwD+5/KWU8jxf7ww+1QJwHBHxKsj\nS6cOCZq18/6jOh5LDRkVttdvnLnDqp1x2bAqKPepxVqV5FkIzi1XpK1wo1c3yS+Z\n4NXFZXKfB+YsdCYh5hsqaeUIf1udeLjt77oSv0r0Gh0j2GKfEbEHF/cZDD8t5NwS\nKrVYzEZSlxgvMCJsGrWbYsXcguYrMKkSwuQP4Lu3oV4N9wGGSgTfzuK3J5leI8Od\nRhN3v+AFAgMBAAECggEAWrVVFZEKVEvF+4RLcy4qS+wXYv6veBa2U0XJTUesQK2B\nDsHQ8mmNJ7AJgaX6UG52dmmHn4Xq7+VfFMBEWQZJf76wB7OUWqLCczzjsWJL9HEK\n9YHFDvY1UukdnATeMaYaTT28CYsdwlRqu+7NO2PDGO0celPh8w4K8DRjiMRJIKYt\nFWLxgS3BgTxnD/rVy4JKqnJnhD44xpqeQ+wMmBh28F0cp66AZHRgX+GBGN/K4or1\n6rE3BEfJWkSqn6PEiZrO3qXsfaXoGdwsIpZRjGAYl+FIp6Dc1OLOc735VrHnHJvN\nTH24BwKosJsjn19FxvSTdYc0UkXVe5Ap0p1gZSjFbQKBgQDuyVH+LCovrsySTGeX\n46RZAvcVeP3qeyozIRp5QctiLV1xQM2l1G0xPT6ecNeCY9NZ1Uo2NIDovb1OmEuP\n+A69fx/wRw2SEObN8rR6MjRf8brvt+4FGZWdMj6x/m0Kf4BslB4tvhmJjs3+R5Iz\n8qpb2wzO5IpYG75vuC17M/7tGwKBgQDEjhTEPKQhs2k08+mlZBpQZ65gIr1tA7a0\nSkUdI3xi2NLI8zyEJd09G43QsPXgzUdKEPy6Jrb6GULJCCn3ZLifZ5/EB+BEIB/m\n1KbbLgiMTYidhx+X5XuiYcN0ynjRPLUDe0ep8SblNBPeI/3TVJYIZB5JNrs6EFHY\n7AK5pB7ZXwKBgQCTqkvaMtWjxyUbE8S8WTo5EWxbCwd7Cc9+7unAMr/jZspyTvDd\nrBAacxVWRdIAAFujIhNSkgVl6HA5OlUAIxZ6eTL3E/mAapNQqNaS+pkI/CPuOoAn\nBztOitPanswvwclZW/+NqhGAz57zsK7pERfo1f2FtC8ZbY7G5864cd8kIQKBgQCz\n6amwhiFmh6aBRdJUBXDgsEa40JO7OW7/UAw7Q8QTZoxqS9rUyyPbT2Fb6N7nSn86\nmJn8ent6Ka0r/kELpjIoFt3yvZLWSOFqlLO2ZEiGxGGMb6bHjtLAK+SQ/tPgEkVO\nToWmVIpZunWFHES2L/K084+VTHfMCiwg9sb3zfY+2QKBgF53MR6aT0HMztRmGH7/\n4MgDLrUfd41JziKQpl6nN9p7d0EVl6ChXo6G8PfB/1NrRIM56u+seBDdljjnXbK+\nBnDe6N0ZWoXCNGAOAZadyPS3sYGxVN1K/5OQSDiM9k3KfGBGc3IV6R5vh4Z6XXfS\nG5ThxNobI5Lrr7oDCeDg4hhH\n-----END PRIVATE KEY-----\n",
  "client_email": "authorisation@xtracap.iam.gserviceaccount.com",
  "client_id": "103680487274495195073",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/authorisation%40xtracap.iam.gserviceaccount.com"
}

def gs_writer(sheet_name,dataframe,sheet_url,boolean,row=1,col=1):
    import gspread
    from gspread_dataframe import get_as_dataframe, set_with_dataframe
    import google.oauth2
    from oauth2client.service_account import ServiceAccountCredentials
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(ghseet_cred,scope)
    gc = gspread.authorize(credentials)
    sht2 = gc.open_by_url(sheet_url)
    try:
        sht = sht2.worksheet(sheet_name)
    except:
        sht = sht2.add_worksheet(sheet_name,100,26)
    set_with_dataframe(sht,dataframe,resize = boolean,row=row,col=col)

def gs_reader(sheet_name,col,sheet_url):
    import gspread
    from gspread_dataframe import get_as_dataframe, set_with_dataframe
    import google.oauth2
    from oauth2client.service_account import ServiceAccountCredentials
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(ghseet_cred,scope)
    gc = gspread.authorize(credentials)
    sht2 = gc.open_by_url(sheet_url)
    sht = sht2.worksheet(sheet_name)
    if col ==0:
        c = get_as_dataframe(sht,evaluate_formulas=True)
        return c
    else:
        c = get_as_dataframe(sht,usecols=col,evaluate_formulas=True)
        return c

def gs_clear(sheet_name,first_column_withstart,last_column_with_end,sheet_url):
    import gspread
    from gspread_dataframe import get_as_dataframe, set_with_dataframe
    import google.oauth2
    from oauth2client.service_account import ServiceAccountCredentials
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(ghseet_cred,scope)
    gc = gspread.authorize(credentials)
    sht2 = gc.open_by_url(sheet_url)
    sht2.values_clear(sheet_name+"!"+str(first_column_withstart)+""+":"+""+str(last_column_with_end)+"")

def gsCreate(folder_id,title,sheet_name,dataframe,boolean,row=1,col=1):
    import gspread
    from gspread_dataframe import get_as_dataframe, set_with_dataframe
    import google.oauth2
    from oauth2client.service_account import ServiceAccountCredentials
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive.metadata']
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(ghseet_cred,scope)
    gc = gspread.authorize(credentials)
    spreadsheet = gc.create(title=title,folder_id=folder_id)
    try:
        sheet = spreadsheet.worksheet(sheet_name)
    except:
        sheet = spreadsheet.add_worksheet(sheet_name,100,26)
    set_with_dataframe(sheet,dataframe,resize = boolean,row=row,col=col)

def home(request):

    template = 'english/home.html'

    section1 = HomeSection1.objects.filter(language="English")
    section2 = HomeSection2.objects.filter(language="English")
    section3 = HomeSection3.objects.filter(language="English")
    section4 = HomeSection4.objects.filter(language="English")
    section5_c1 = HomeSection5.objects.filter(language="English")[:7]
    section5_c2 = HomeSection5.objects.filter(language="English")[7:15]
    meta_tags = HomeMetaTag.objects.filter(language="English")
    meta_descriptions = HomeMetaDescription.objects.filter(language="English")
    section6 = HomeSection6.objects.filter(language="English")
    testimonials = TestimonialsTestimonial.objects.filter(language="English")
    section7 = HomeSection7.objects.filter(language="English")
    section8 = HomeSection8.objects.filter(language="English")
    news = PressNews.objects.filter(language="English").order_by('-date')[:3]

    pageTitle = HomePageTitle.objects.filter(language="English")

    if request.method == 'POST':

        fullName = request.POST.get('fullName')
        if request.POST.get('mobileNumber'):
            mobileNumber = request.POST.get('mobileNumber')
        else:
            mobileNumber = ''
        email = request.POST.get('email')
        company = request.POST.get('company')
        message = request.POST.get('message')

        send_mail(
            'Partnership Form Query: ' + fullName + ' | Contact Number: ' + mobileNumber + ' | Organisation: ' + company,
            message,
            email,
            ['contact@xtracapindia.com','riaz@xtracapindia.com','ankitv@xtracapindia.com']
            )
        
        return redirect('index')

    context = {
        'section1':section1,
        'section2':section2,
        'section3':section3,
        'section4':section4,
        'section5_c1':section5_c1,
        'section5_c2':section5_c2,
        'meta_tags':meta_tags,
        'meta_descriptions':meta_descriptions,
        'section6':section6,
        'testimonials':testimonials,
        'section7':section7,
        'section8':section8,
        'news':news,
        'pageTitle': pageTitle,
    }

    return render(request, template, context)

def investors(request):

    template = 'english/investors.html'
    
    section1 = InvestorsOneButtonBanner.objects.filter(language="English")
    section2 = InvestorsYellowStripSection.objects.filter(language="English")
    section3 = InvestorsOurTeam.objects.filter(language="English")
    section4 = InvestorsOurApproach.objects.filter(language="English")
    section5 = InvestorsOurBusinessModel.objects.filter(language="English")
    section6 = TestimonialsTestimonial.objects.filter(language="English")
    news = PressNews.objects.filter(language="English").order_by('-date')[:3]
    meta_tags = InvestorsMetaTag.objects.filter(language="English")
    meta_description = InvestorsMetaDescription.objects.filter(language="English")
    pageTitle = InvestorsPageTitle.objects.filter(language="English")

    context = {
        'section1':section1,
        'section2':section2,
        'section3':section3,
        'section4':section4,
        'section5':section5,
        'section6':section6,
        'news':news,
        'meta_tags':meta_tags,
        'meta_description':meta_description,
        'pageTitle': pageTitle,
    }

    return render(request, template, context)

def investorsForm(request):

    if request.method == "POST":

        form = ContactFormFilled(request.POST or None)

        if form.is_valid():

            form.save()
            fullname = request.POST['fname']
            contactnumber = request.POST['contactnumber']
            email = request.POST['email']
            message = request.POST['message']
            send_mail(
                'Investor Page Enquiry From: ' + fullname,
                message,
                email,
                ['contact@xtracapindia.com']
            )

            return render(request,'investors.html',{
                'fullname':fullname
            })

        else:

            fname = request.POST['fname']
            contactnumber = request.POST['contactnumber']
            email = request.POST['email']
            message = request.POST['message']
            messages.success(request,('There was an Error, please try again!'))

            return render(request,'investors.html',{
                'fname':fname,
                'contactnumber':contactnumber,
                'email':email,
                'message':message
            })

    else:

        return render(request,'investors.html',{})

def homeNews(request):

    template = 'english/pressNews.html'

    news_list = PressNews.objects.filter(featured=False).order_by('-date')
    metatags = PressMetaTag.objects.filter(language="English")
    metadescriptions = PressMetaDescription.objects.filter(language="English")
    blogs = PressBlog.objects.filter(featured=False).order_by('-date')
    featured_news = PressNews.objects.filter(featured=True)
    featured_blogs = PressBlog.objects.filter(featured=True)
    pageTitle = PressPageTitleNews.objects.filter(language="English")

    context = {
        'news_list':news_list,
        'meta_tags':metatags,
        'meta_descriptions':metadescriptions,
        'blogs':blogs,
        'featured_news':featured_news,
        'featured_blogs':featured_blogs,
        'pageTitle': pageTitle,
    }

    return render(request, template, context)

def news(request,slug_text):
    
    template = 'english/news.html'
    
    news = get_object_or_404(PressNews, slug = slug_text)
    
    context = {
       'news':news, 
    }
    
    return render(request, template, context)

def homeBlogs(request):

    template = 'english/pressBlogs.html'

    news_list = PressNews.objects.filter(featured=False).order_by('-date')
    metatags = PressMetaTag.objects.filter(language="English")
    metadescriptions = PressMetaDescription.objects.filter(language="English")
    blogs = PressBlog.objects.filter(featured=False).order_by('-date')
    featured_news = PressNews.objects.filter(featured=True)
    featured_blogs = PressBlog.objects.filter(featured=True)
    pageTitle = PressPageTitleBlog.objects.filter(language="English")

    context = {
        'news_list':news_list,
        'meta_tags':metatags,
        'meta_descriptions':metadescriptions,
        'blogs':blogs,
        'featured_news':featured_news,
        'featured_blogs':featured_blogs,
        'pageTitle': pageTitle,
    }

    return render(request, template, context)

def blog(request,slug_text):

    template = 'english/blog.html'

    blog = get_object_or_404(PressBlog, slug = slug_text)
    
    context = {
        'blog':blog,
    }
    
    return render(request, template, context)

def aboutUs(request):

    template = 'english/about_us.html'

    section1 = AboutUsMainBannerTwoButton.objects.filter(language="English")
    section2 = AboutUsGreenBorderSection.objects.filter(language="English")
    section3 = AboutUsOurStory.objects.filter(language="English")
    section4 = AboutUsOurStoryParagraphs.objects.filter(language="English")
    section5 = AboutUsUpcomingProducts.objects.filter(language="English")
    section6_left = AboutUsAlternateBusinessModelSection.objects.filter(language="English")[::2]
    section6_right = AboutUsAlternateBusinessModelSection.objects.filter(language="English")[1::2]
    section6 = section6_left + section6_right
    section7 = TestimonialsTestimonial.objects.filter(language="English")
    meta_tags = AboutUsMetaTag.objects.filter(language="English")
    meta_description = AboutUsMetaDescription.objects.filter(language="English")
    pageTitle = AboutUsPageTitle.objects.filter(language="English")

    context = {
        'section1':section1,
        'section2':section2,
        'section3':section3,
        'section4':section4,
        'section5':section5,
        'section6':section6,
        # 'section6_right':section6_right,
        'section7':section7,
        'meta_tags':meta_tags,
        'meta_description':meta_description,
        'pageTitle': pageTitle,
    }

    return render(request, template, context)

def contactUs(request):

    template = 'english/contact_us.html'

    section1 = ContactUsContactDetails.objects.filter(language="English")
    meta_tags = ContactUsMetaTag.objects.filter(language="English")
    meta_description = ContactUsMetaDescription.objects.filter(language="English")
    pageTitle = ContactUsPageTitle.objects.filter(language="English")

    context = {
        'section1':section1,
        'meta_tags':meta_tags,
        'meta_description':meta_description,
        'pageTitle': pageTitle,
    }

    return render(request, template, context)

def contactPageForm(request):

    if request.method == "POST":

        form = ContactFormFilled(request.POST or None)

        if form.is_valid():

            form.save()
            fullname = request.POST['fname']
            contactnumber = request.POST['contactnumber']
            email = request.POST['email']
            message = request.POST['message']

            try:
                send_mail(
                    'Contact Us Page Enquiry From: ' + fullname,
                    message,
                    email,
                    ['contact@xtracapindia.com']
                )
            except:
                print("Error in sending mail!!")

            return render(request, 'english/contact_us.html', {
                'fullname':fullname
            })

        else:

            fname = request.POST['fname']
            contactnumber = request.POST['contactnumber']
            email = request.POST['email']
            message = request.POST['message']
            messages.success(request,('There was an Error, please try again!'))

            return render(request,'english/contact_us.html',{
                'fname':fname,
                'contactnumber':contactnumber,
                'email':email,
                'message':message
            })

    else:

        return render(request,'english/contact_us.html',{})

def creditProduct(request):

    template = 'english/credit_product.html'    

    section1 = CreditProductTwoButtonSection.objects.filter(language="English")
    section2 = CreditProductOneButtonSection.objects.filter(language="English")
    section3 = CreditProductProductFeatures.objects.filter(language="English")
    section4 = CreditProductProductTnCs.objects.filter(language="English")
    meta_tags = CreditProductMetaTag.objects.filter(language="English")
    meta_description = CreditProductMetaDescription.objects.filter(language="English")
    pageTitle = CreditProductPageTitle.objects.filter(language="English")

    context = {
        'section1':section1,
        'section2':section2,
        'section3':section3,
        'section4':section4,
        'meta_tags':meta_tags,
        'meta_description':meta_description,
        'pageTitle': pageTitle,
    }

    return render(request, template, context)

def faq(request):

    template = 'english/faq.html'

    section1 = FAQQuestionAnswer.objects.filter(language="English")
    meta_tags = FAQMetaTag.objects.filter(language="English")
    meta_description = FAQMetaDescription.objects.filter(language="English")
    pageTitle = FAQPageTitle.objects.filter(language="English")

    context = {
        'section1':section1,
        'meta_tags':meta_tags,
        'meta_description':meta_description,
        'pageTitle': pageTitle,
    }

    return render(request, template, context)

def privacy(request):

    template = 'english/privacy.html'

    section1 = PrivacyPrivacyPolicy.objects.filter(language="English")
    meta_tags = PrivacyMetaTag.objects.filter(language="English")
    meta_description = PrivacyMetaDescription.objects.filter(language="English")
    pageTitle = PrivacyPageTitle.objects.filter(language="English")

    context = {
        'section1':section1,
        'meta_tags':meta_tags,
        'meta_description':meta_description,
        'pageTitle': pageTitle,
    }

    return render(request, template, context)

def tnc(request):

    template = 'english/tncs.html'

    section1 = TNCTermsConditions.objects.filter(language="English")
    meta_tags = TNCMetaTag.objects.filter(language="English")
    meta_description = TNCMetaDescription.objects.filter(language="English")
    pageTitle = TNCPageTitle.objects.filter(language="English")

    context = {
        'section1':section1,
        'meta_tags':meta_tags,
        'meta_description':meta_description,
        'pageTitle': pageTitle,
    }

    return render(request, template, context)

def testimonials(request):

    template = 'english/testimonials.html'

    section1 = TestimonialsSection1.objects.filter(language="English")
    testimonials = TestimonialsTestimonial.objects.filter(language="English")
    section2 = HomeSection8.objects.filter(language="English")
    meta_tags = TestimonialsMetaTag.objects.filter(language="English")
    meta_description = TestimonialsMetaDescription.objects.filter(language="English")
    pageTitle = TestimonialsPageTitle.objects.filter(language="English")

    context = {
        'section1':section1,
        'testimonials':testimonials,
        'section2':section2,
        'meta_tags':meta_tags,
        'meta_description':meta_description,
        'pageTitle': pageTitle,
    }

    return render(request, template, context)

def hissab(request):

    template = 'english/hissab.html'

    context = {}

    return render(request, template, context)

def sitemap(request):

    template = 'english/sitemap.xml'

    context = {}

    return render(request, template, content_type='application/xml')

def gold(request):
    template = 'english/gold.html'

    context = {}

    return render(request, template, context)

def health(request):
    template = 'english/health.html'

    context = {}

    return render(request, template, context)

def creditLanding(request):
    import datetime
    import pandas as pd
    template = 'english/credit-landing.html'

    if request.method == 'POST':
        import time
        start = time.perf_counter()
        today = datetime.datetime.now().date()
        sheetUrl = "https://docs.google.com/spreadsheets/d/1QY6s0DxVmBC_TUeRieIuSaBxNZIQWiCjl4a632xGX5o/edit#gid=0"

        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('mobile')
        business = request.POST.get('business')
        product = request.POST.get('product')
        gst = request.POST.get('gst')
        pan = request.POST.get('pan')
        formEntry = CreditLandingForm.objects.create(name=name, email=email, number=number, business=business, product=product, gst=gst, pan=pan)
        context={}
        return redirect('creditLandingSubmit')
    else:
        pass

    context = {}

    return render(request, template, context)

def creditLandingSubmit(request):
    template = 'english/form-submission.html'
    
    context = {}
    
    return render(request, template, context)


def fhc(request):

    template = 'english/fhc.html'

    context = {}

    return render(request, template, context)
