from django.shortcuts import render, redirect
from django.contrib import messages
from members.models import Member
from members.forms import MemberForm
from books.models import Book

def dashboard(request):
    highlight_member_code = None

    if request.method == "POST":
        member_form = MemberForm(request.POST)

        if member_form.is_valid():
            new_member = member_form.save()

            messages.success(
                request,
                f"Member '{new_member.full_name}' added successfully"
            )
            return redirect(f"{request.path}?new_member={new_member.member_code}")
    else:
        member_form = MemberForm()
        highlight_member_code = request.GET.get('new_member')
    
    members = Member.objects.all()
    books = Book.objects.all()

    return render(request,
                   "dashboard/dashboard.html", 
                   {'members': members,
                     'books': books,
                     'member_form': member_form,
                     'highlight_member_code': highlight_member_code,
                     },
                     )
