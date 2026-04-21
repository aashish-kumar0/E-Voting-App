import os
import django
import sys

# Add project root to sys.path if not present
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evoting_project.settings')
django.setup()

from django.contrib.auth.models import User
from voting.models import Candidate, Vote
import hashlib
from django.conf import settings
import random

def populate():
    print("Clearing db...")
    # Be careful in real life, but ok for dummy data
    User.objects.all().delete()
    Candidate.objects.all().delete()
    Vote.objects.all().delete()

    print("Creating superuser admin/admin...")
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')

    print("Creating candidates...")
    candidates_data = [
        {"name": "Alice Johnson", "desc": "Advocating for technological advancement and universal basic internet."},
        {"name": "Bob Smith", "desc": "Focused on environmental sustainability and green energy initiatives."},
        {"name": "Charlie Davis", "desc": "Prioritizing cybersecurity, privacy rights, and decentralized finance."}
    ]
    
    candidates = []
    for c in candidates_data:
        cand = Candidate.objects.create(
            name=c["name"], 
            platform_description=c["desc"],
            image_url=f"https://ui-avatars.com/api/?name={c['name'].replace(' ', '+')}&background=random&color=fff&size=150"
        )
        candidates.append(cand)

    print("Creating 15 dummy voters and casting votes...")
    for i in range(1, 16):
        username = f"voter{i}"
        user = User.objects.create_user(username=username, password='password123')
        
        # Bias the election a tiny bit for realistic-looking results
        weights = [0.2, 0.5, 0.3]
        candidate_to_vote_for = random.choices(candidates, weights=weights, k=1)[0]
        
        voter_hash = hashlib.sha256(f"{user.id}{settings.SECRET_KEY}".encode('utf-8')).hexdigest()
        Vote.objects.create(voter_hash=voter_hash, candidate=candidate_to_vote_for)

    print("Added a demo user 'demo_user' / 'password123' who HAS NOT voted yet.")
    User.objects.create_user(username='demo_user', password='password123')

    print("Database populated successfully for demonstration!")

if __name__ == '__main__':
    populate()
