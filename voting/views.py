import hashlib
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.conf import settings
from django.db import IntegrityError
from .models import Candidate, Vote
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    candidates = Candidate.objects.all()
    # Check if user has voted
    has_voted = False
    if request.user.is_authenticated:
        voter_hash = hashlib.sha256(f"{request.user.id}{settings.SECRET_KEY}".encode('utf-8')).hexdigest()
        has_voted = Vote.objects.filter(voter_hash=voter_hash).exists()
        
    return render(request, 'voting/home.html', {
        'candidates': candidates, 
        'has_voted': has_voted
    })

@login_required
def cast_vote(request, candidate_id):
    if request.method == 'POST':
        candidate = get_object_or_404(Candidate, id=candidate_id)
        
        # Cryptographic representation of the voter
        voter_hash = hashlib.sha256(f"{request.user.id}{settings.SECRET_KEY}".encode('utf-8')).hexdigest()
        
        try:
            Vote.objects.create(voter_hash=voter_hash, candidate=candidate)
            messages.success(request, f"Your vote for {candidate.name} has been securely cast!")
        except IntegrityError:
            # The voter_hash already exists
            messages.error(request, "You have already cast your vote. Duplicate voting is mathematically prevented.")
            
    return redirect('home')

def results(request):
    candidates = Candidate.objects.all()
    results_data = []
    total_votes = 0
    for candidate in candidates:
        count = candidate.votes.count()
        total_votes += count
        results_data.append({
            'name': candidate.name,
            'votes': count
        })
    
    # Optional: Calculate percentages
    for data in results_data:
        data['percentage'] = (data['votes'] / total_votes * 100) if total_votes > 0 else 0
        
    return render(request, 'voting/results.html', {
        'results_data': results_data,
        'total_votes': total_votes
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
