from django.contrib import admin
from .models import Candidate, Vote

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'platform_description')
    search_fields = ('name',)

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'cast_timestamp')
    list_filter = ('candidate', 'cast_timestamp')
    # Omit voter_hash from list_display to maintain administrative privacy by default, 
    # though it's hashed so it's technically pseudo-anonymous.
    readonly_fields = ('voter_hash', 'candidate', 'cast_timestamp')

    def has_add_permission(self, request):
        # Prevent manual vote creation via admin
        return False
