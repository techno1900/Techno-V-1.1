from django.shortcuts import render,redirect

from .forms import contactForm


def contact(req):
    form = contactForm()
    
    if req.method == "POST":
        form = contactForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        
    contaxt = {'contactform':form}
    return render(req, 'technocontact/contact.html', contaxt)
