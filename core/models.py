from django.db import models


class ContactInquiry(models.Model):
    """Model to capture contact form submissions from the website."""
    name = models.CharField(max_length=200, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    message = models.TextField(verbose_name="Message")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Submitted At")

    class Meta:
        verbose_name = "Contact Inquiry"
        verbose_name_plural = "Contact Inquiries"
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.name} - {self.email} ({self.submitted_at.strftime('%d %b %Y')})"
