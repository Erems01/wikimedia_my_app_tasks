from django.shortcuts import render
from .models import Bug

# View to register a bug into the database

def register_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug_list') # Redirect to a bug list view or another appropriate page
        else:
            form = BugForm()

        return render(request, 'bug_register.html', {'form': form})


# View to view the fields of the bug

def bug_view(request, bug_id):
    # Retrieve the bug record from the database using the bug_id
    bug = Bug.objects.get(id=bug_id)
    return render(request, 'bug_detail.html', {'bug': bug})


# View list of all bugs in the database

def bug_list(request):
    bugs = Bug.objects.all()
    return render(request, 'bug_list.html', {'bugs': bugs})
