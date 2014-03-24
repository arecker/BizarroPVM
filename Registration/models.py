from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):

    sex_choices = (
        ('M', "Male"),
        ('F', "Female")
    )

    social_security = models.CharField(max_length=9, blank=True, verbose_name="SSN")
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    middle_name = models.CharField(max_length=100, verbose_name="Middle Name", blank=True, null=True)
    sex = models.CharField(max_length=1, verbose_name="Sex", choices=sex_choices)
    birthday = models.DateField(verbose_name="Birthday")
    street = models.CharField(max_length=150, verbose_name="Street")
    street_second = models.CharField(max_length=150, verbose_name="Unit", blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name="City")
    state = models.CharField(max_length=2, verbose_name="State")
    zip = models.CharField(max_length=5, verbose_name="ZIP")
    phone = models.CharField(blank=True, max_length=11, verbose_name="Phone")

    employer = models.ForeignKey("Employer", verbose_name="Employer")
    physician = models.CharField(max_length=200, verbose_name="Primary Care Physician")
    notes = models.TextField(max_length=300, blank=True, null=True, verbose_name="Notes")

    def __unicode__(self):
        return self.last_name + ", " + self.first_name



class Clinic(models.Model):
    short = models.CharField(max_length=5, verbose_name="Short Name")
    description = models.CharField(max_length=100, verbose_name="Clinic Name")
    contact = models.CharField(max_length=200, verbose_name="Contact")
    street = models.CharField(max_length=150, verbose_name="Street")
    street_second = models.CharField(max_length=150, verbose_name="Unit", blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name="City")
    state = models.CharField(max_length=2, verbose_name="State")
    zip = models.CharField(max_length=5, verbose_name="ZIP")
    phone = models.CharField(blank=True, max_length=11, verbose_name="Phone")

    # Billing
    attn = models.CharField(max_length=200, verbose_name="Attention")
    bill_street = models.CharField(max_length=150, verbose_name="Street")
    bill_unit = models.CharField(max_length=150, verbose_name="Unit", blank=True, null=True)
    bill_city = models.CharField(max_length=100, verbose_name="City")
    bill_state = models.CharField(max_length=2, null=True, blank=True, verbose_name="State")
    bill_zip = models.CharField(max_length=5, verbose_name="ZIP")

    def __unicode__(self):
        return self.short


class Physician(models.Model):

    yes_or_no = (
        (True, "Yes"),
        (False, "No")
    )

    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    middle_name = models.CharField(max_length=100, verbose_name="Middle Name", blank=True, null=True)
    account = models.ForeignKey(User, verbose_name="User Account")
    active = models.BooleanField(choices=yes_or_no, default=False, verbose_name="Active")
    member = models.BooleanField(choices=yes_or_no, default=False, verbose_name="Member")
    ref_physician = models.BooleanField(choices=yes_or_no, default=False, verbose_name="Referring Physician")
    uses_sched = models.BooleanField(choices=yes_or_no, default=False, verbose_name="Uses Scheduler")
    UPIN = models.CharField(max_length=10, verbose_name="UPIN")
    NPI = models.CharField(max_length=10, verbose_name="Provider NPI")
    fed_tax_id = models.CharField(max_length=10, verbose_name="Federal Tax ID")
    taxonomy_code = models.CharField(max_length=10, verbose_name="Taxonomy Code")

    def __unicode__(self):
        return self.last_name + ", " + self.first_name


class Employer(models.Model):
    yes_or_no = (
        (True, "Yes"),
        (False, "No")
    )

    active_or_not = (
        (True, "Active"),
        (False, "Inactive")
    )

    statement_type_choices = [
        ("Detail","Detail"),
        ("Summary","Summary"),
        ("Combo","Combo")
    ]

    payment_term_choices = [
        ("NET 15", "NET 15"),
        ("NET 20", "NET 20"),
        ("NET 30","NET 30"),
        ("NET 45", "NET 45")
    ]

    name = models.CharField(max_length=200, verbose_name="Name")
    contact = models.CharField(max_length=200, verbose_name="Contact")
    street = models.CharField(max_length=150, verbose_name="Street")
    street_second = models.CharField(max_length=150, verbose_name="Unit", blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name="City")
    state = models.CharField(max_length=2, null=True, blank=True, verbose_name="State")
    zip = models.CharField(max_length=5, verbose_name="ZIP")
    phone = models.CharField(blank=True, max_length=11, verbose_name="Phone")

    # Billing info
    verified = models.BooleanField(choices=yes_or_no, default=False, verbose_name="Verfied")
    status = models.BooleanField(choices=active_or_not, default=False, verbose_name="Status")
    statement_type = models.CharField(max_length=10, choices=statement_type_choices, blank=True, null=True, verbose_name="Statement Type")
    print_statement = models.BooleanField(choices=yes_or_no, default=False, verbose_name="Print Statement")
    print_ssn = models.BooleanField(choices=yes_or_no, default=False, verbose_name="Print SSN")
    payment_term = models.CharField(max_length=20, choices=payment_term_choices, null=True, blank=True, verbose_name="Payment Term")

    def __unicode__(self):
        return self.name



