from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Member
from .forms import MemberForm


@require_POST
def delete_member(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if member.borrowrecord_set.filter(return_date__isnull=True).exists():
        messages.error(request,
                       f"{member.full_name} still has unreturned books.")
        return redirect('dashboard')

    member.delete()

    messages.success(request,
                     f"Member {member.full_name} deleted.")

    return redirect('dashboard')

def edit_member(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)

        if form.is_valid():
            form.save()
            messages.success(request, f"Member '{member.full_name}' updated successfully.")
            return redirect('dashboard')
    else:
        form = MemberForm(instance=member)

    return render(request, "members/edit_member.html", {'member' : member, 'form' : form})

