from django.shortcuts import render, get_object_or_404
from english.models import *
from django.core.mail import send_mail
from general import ContactFormFilled
import traceback

def home(request):

    template = 'hindi/home.html'

    section1 = HomeSection1.objects.filter(language="Hindi")
    section2 = HomeSection2.objects.filter(language="Hindi")
    section3 = HomeSection3.objects.filter(language="Hindi")
    section4 = HomeSection4.objects.filter(language="Hindi")
    section5_c1 = HomeSection5.objects.filter(language="Hindi")[:7]
    section5_c2 = HomeSection5.objects.filter(language="Hindi")[7:15]
    meta_tags = HomeMetaTag.objects.filter(language="Hindi")
    meta_descriptions = HomeMetaDescription.objects.filter(language="Hindi")
    section6 = HomeSection6.objects.filter(language="Hindi")
    testimonials = TestimonialsTestimonial.objects.filter(language="Hindi")
    section7 = HomeSection7.objects.filter(language="Hindi")
    section8 = HomeSection8.objects.filter(language="Hindi")
    news = PressNews.objects.filter(language="Hindi").order_by('-date')[:3]

    pageTitle = HomePageTitle.objects.filter(language="Hindi")

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

    template = 'hindi/investors.html'
    
    section1 = InvestorsOneButtonBanner.objects.filter(language="Hindi")
    section2 = InvestorsYellowStripSection.objects.filter(language="Hindi")
    section3 = InvestorsOurTeam.objects.filter(language="Hindi")
    section4 = InvestorsOurApproach.objects.filter(language="Hindi")
    section5 = InvestorsOurBusinessModel.objects.filter(language="Hindi")
    section6 = TestimonialsTestimonial.objects.filter(language="Hindi")
    news = PressNews.objects.filter(language="Hindi").order_by('-date')[:3]
    meta_tags = InvestorsMetaTag.objects.filter(language="Hindi")
    meta_description = InvestorsMetaDescription.objects.filter(language="Hindi")
    pageTitle = InvestorsPageTitle.objects.filter(language="Hindi")

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

        print(request.POST)

        form = ContactFormFilled(data=request.POST)

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

    template = 'hindi/pressNews.html'

    news_list = PressNews.objects.filter(featured=False).order_by('-date')
    metatags = PressMetaTag.objects.filter(language="Hindi")
    metadescriptions = PressMetaDescription.objects.filter(language="Hindi")
    blogs = PressBlog.objects.filter(featured=False).order_by('-date')
    featured_news = PressNews.objects.filter(featured=True)
    featured_blogs = PressBlog.objects.filter(featured=True)
    pageTitle = PressPageTitleNews.objects.filter(language="Hindi")

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
    
    template = 'hindi/news.html'
    
    news = get_object_or_404(PressNews, slug = slug_text)
    
    context = {
       'news':news, 
    }
    
    return render(request, template, context)

def homeBlogs(request):

    template = 'hindi/pressBlogs.html'

    news_list = PressNews.objects.filter(featured=False).order_by('-date')
    metatags = PressMetaTag.objects.filter(language="Hindi")
    metadescriptions = PressMetaDescription.objects.filter(language="Hindi")
    blogs = PressBlog.objects.filter(featured=False).order_by('-date')
    featured_news = PressNews.objects.filter(featured=True)
    featured_blogs = PressBlog.objects.filter(featured=True)
    pageTitle = PressPageTitleBlog.objects.filter(language="Hindi")

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

    template = 'hindi/blog.html'

    blog = get_object_or_404(PressBlog, slug = slug_text)
    
    context = {
        'blog':blog,
    }
    
    return render(request, template, context)

def aboutUs(request):

    template = 'hindi/about_us.html'

    section1 = AboutUsMainBannerTwoButton.objects.filter(language="Hindi")
    section2 = AboutUsGreenBorderSection.objects.filter(language="Hindi")
    section3 = AboutUsOurStory.objects.filter(language="Hindi")
    section4 = AboutUsOurStoryParagraphs.objects.filter(language="Hindi")
    section5 = AboutUsUpcomingProducts.objects.filter(language="Hindi")
    section6_left = AboutUsAlternateBusinessModelSection.objects.filter(language="Hindi")[::2]
    section6_right = AboutUsAlternateBusinessModelSection.objects.filter(language="Hindi")[1::2]
    section6 = section6_left + section6_right
    # section7 = AboutUsTestimonial.objects.filter(language="Hindi")
    meta_tags = AboutUsMetaTag.objects.filter(language="Hindi")
    meta_description = AboutUsMetaDescription.objects.filter(language="Hindi")
    pageTitle = AboutUsPageTitle.objects.filter(language="Hindi")

    context = {
        'section1':section1,
        'section2':section2,
        'section3':section3,
        'section4':section4,
        'section5':section5,
        'section6':section6,
        # 'section6_right':section6_right,
        # 'section7':section7,
        'meta_tags':meta_tags,
        'meta_description':meta_description,
        'pageTitle': pageTitle,
    }

    return render(request, template, context)

def contactUs(request):

    template = 'hindi/contact_us.html'

    section1 = ContactUsContactDetails.objects.filter(language="Hindi")
    meta_tags = ContactUsMetaTag.objects.filter(language="Hindi")
    meta_description = ContactUsMetaDescription.objects.filter(language="Hindi")
    pageTitle = ContactUsPageTitle.objects.filter(language="Hindi")

    context = {
        'section1':section1,
        'meta_tags':meta_tags,
        'meta_description':meta_description,
        'pageTitle': pageTitle,
    }

    return render(request, template, context)

def contactPageForm(request):

    if request.method == "POST":

        form = ContactFormFilled(data=request.POST)

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
                print('Error in sending mail!!!')

            return render(request, 'english/contact_us.html', {
                'fullname':fullname
            })

        else:

            fname = request.POST['fname']
            contactnumber = request.POST['contactnumber']
            email = request.POST['email']
            message = request.POST['message']
            messages.success(request,('There was an Error, please try again!'))

            return render(request,'contact_us.html',{
                'fname':fname,
                'contactnumber':contactnumber,
                'email':email,
                'message':message
            })

    else:

        return render(request,'contact_us.html',{})

def creditProduct(request):

    template = 'hindi/credit_product.html'    

    section1 = CreditProductTwoButtonSection.objects.filter(language="Hindi")
    section2 = CreditProductOneButtonSection.objects.filter(language="Hindi")
    section3 = CreditProductProductFeatures.objects.filter(language="Hindi")
    section4 = CreditProductProductTnCs.objects.filter(language="Hindi")
    meta_tags = CreditProductMetaTag.objects.filter(language="Hindi")
    meta_description = CreditProductMetaDescription.objects.filter(language="Hindi")
    pageTitle = CreditProductPageTitle.objects.filter(language="Hindi")

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

    template = 'hindi/faq.html'

    section1 = FAQQuestionAnswer.objects.filter(language="Hindi")
    meta_tags = FAQMetaTag.objects.filter(language="Hindi")
    meta_description = FAQMetaDescription.objects.filter(language="Hindi")
    pageTitle = FAQPageTitle.objects.filter(language="Hindi")

    context = {
        'section1':section1,
        'meta_tags':meta_tags,
        'meta_description':meta_description,
        'pageTitle': pageTitle,
    }

    return render(request, template, context)

def privacy(request):

    template = 'hindi/privacy.html'

    section1 = PrivacyPrivacyPolicy.objects.filter(language="Hindi")
    meta_tags = PrivacyMetaTag.objects.filter(language="Hindi")
    meta_description = PrivacyMetaDescription.objects.filter(language="Hindi")
    pageTitle = PrivacyPageTitle.objects.filter(language="Hindi")

    context = {
        'section1':section1,
        'meta_tags':meta_tags,
        'meta_description':meta_description,
        'pageTitle': pageTitle,
    }

    return render(request, template, context)

def tnc(request):

    template = 'hindi/tncs.html'

    section1 = TNCTermsConditions.objects.filter(language="Hindi")
    meta_tags = TNCMetaTag.objects.filter(language="Hindi")
    meta_description = TNCMetaDescription.objects.filter(language="Hindi")
    pageTitle = TNCPageTitle.objects.filter(language="Hindi")

    context = {
        'section1':section1,
        'meta_tags':meta_tags,
        'meta_description':meta_description,
        'pageTitle': pageTitle,
    }

    return render(request, template, context)

def testimonials(request):

    template = 'hindi/testimonials.html'

    section1 = TestimonialsSection1.objects.filter(language="Hindi")
    testimonials = TestimonialsTestimonial.objects.filter(language="Hindi")
    section2 = HomeSection8.objects.filter(language="Hindi")
    meta_tags = TestimonialsMetaTag.objects.filter(language="Hindi")
    meta_description = TestimonialsMetaDescription.objects.filter(language="Hindi")
    pageTitle = TestimonialsPageTitle.objects.filter(language="Hindi")

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

    template = 'hindi/hissab.html'

    context = {}

    return render(request, template, context)

def sitemap(request):

    template = 'hindi/sitemap.xml'

    context = {}

    return render(request, template, content_type='application/xml')

def gold(request):
    template = 'hindi/gold.html'

    context = {}

    return render(request, template, context)

def health(request):
    template = 'hindi/health.html'

    context = {}

    return render(request, template, context)

def fhc(request):

    template = 'hindi/fhc.html'

    context = {}

    return render(request, template, context)