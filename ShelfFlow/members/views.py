from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Member


def delete_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.delete()

    messages.success(request,
                     f"Member {member.full_name} deleted.")
    
    return redirect('dashboard')