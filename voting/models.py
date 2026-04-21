from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    platform_description = models.TextField()
    image_url = models.URLField(blank=True, null=True, help_text="URL for the candidate's photo")

    def __str__(self):
        return self.name

class Vote(models.Model):
    voter_hash = models.CharField(max_length=64, unique=True, help_text="SHA-256 hash to guarantee anonymity and prevent double voting")
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='votes')
    cast_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vote for {self.candidate.name} at {self.cast_timestamp}"
