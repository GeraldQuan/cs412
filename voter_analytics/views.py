from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Voter
from django import forms
import plotly.express as px
import plotly.io as pio
from django.db import models
import pandas as pd  # Import pandas for DataFrame conversion

# Filter form to filter voter records based on specified criteria
class VoterFilterForm(forms.Form):
    party_affiliation = forms.ChoiceField(
        choices=[('', 'Any')] + [(party, party) for party in Voter.objects.values_list('party_affiliation', flat=True).distinct()],
        required=False
    )
    min_birth_year = forms.IntegerField(widget=forms.Select(choices=[(year, year) for year in range(1900, 2023)]), required=False)
    max_birth_year = forms.IntegerField(widget=forms.Select(choices=[(year, year) for year in range(1900, 2023)]), required=False)
    voter_score = forms.ChoiceField(
        choices=[('', 'Any')] + [(score, score) for score in Voter.objects.values_list('voter_score', flat=True).distinct()],
        required=False
    )
    v20state = forms.BooleanField(required=False)
    v21town = forms.BooleanField(required=False)
    v21primary = forms.BooleanField(required=False)
    v22general = forms.BooleanField(required=False)
    v23town = forms.BooleanField(required=False)

# List view to display and filter voter records
class VoterListView(ListView):
    model = Voter
    template_name = 'voter_analytics/voter_list.html'
    context_object_name = 'voters'
    paginate_by = 100

    def get_queryset(self):
        queryset = Voter.objects.all()
        form = VoterFilterForm(self.request.GET)

        if form.is_valid():
            if form.cleaned_data['party_affiliation']:
                queryset = queryset.filter(party_affiliation=form.cleaned_data['party_affiliation'])
            if form.cleaned_data['min_birth_year']:
                queryset = queryset.filter(date_of_birth__year__gte=form.cleaned_data['min_birth_year'])
            if form.cleaned_data['max_birth_year']:
                queryset = queryset.filter(date_of_birth__year__lte=form.cleaned_data['max_birth_year'])
            if form.cleaned_data['voter_score']:
                queryset = queryset.filter(voter_score=form.cleaned_data['voter_score'])
            if form.cleaned_data['v20state']:
                queryset = queryset.filter(v20state=True)
            if form.cleaned_data['v21town']:
                queryset = queryset.filter(v21town=True)
            if form.cleaned_data['v21primary']:
                queryset = queryset.filter(v21primary=True)
            if form.cleaned_data['v22general']:
                queryset = queryset.filter(v22general=True)
            if form.cleaned_data['v23town']:
                queryset = queryset.filter(v23town=True)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = VoterFilterForm(self.request.GET or None)
        return context

# Detail view to display details of a single voter record
class VoterDetailView(DetailView):
    model = Voter
    template_name = 'voter_analytics/voter_detail.html'
    context_object_name = 'voter'

# View to display graphs of aggregated voter data with filtering capabilities
class GraphsView(ListView):
    model = Voter
    template_name = 'voter_analytics/graphs.html'
    context_object_name = 'voters'

    def get_queryset(self):
        queryset = Voter.objects.all()
        form = VoterFilterForm(self.request.GET)

        if form.is_valid():
            if form.cleaned_data['party_affiliation']:
                queryset = queryset.filter(party_affiliation=form.cleaned_data['party_affiliation'])
            if form.cleaned_data['min_birth_year']:
                queryset = queryset.filter(date_of_birth__year__gte=form.cleaned_data['min_birth_year'])
            if form.cleaned_data['max_birth_year']:
                queryset = queryset.filter(date_of_birth__year__lte=form.cleaned_data['max_birth_year'])
            if form.cleaned_data['voter_score']:
                queryset = queryset.filter(voter_score=form.cleaned_data['voter_score'])
            if form.cleaned_data['v20state']:
                queryset = queryset.filter(v20state=True)
            if form.cleaned_data['v21town']:
                queryset = queryset.filter(v21town=True)
            if form.cleaned_data['v21primary']:
                queryset = queryset.filter(v21primary=True)
            if form.cleaned_data['v22general']:
                queryset = queryset.filter(v22general=True)
            if form.cleaned_data['v23town']:
                queryset = queryset.filter(v23town=True)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        voters = self.get_queryset()

        # Histogram by Year of Birth
        birth_years = voters.values_list('date_of_birth__year', flat=True)
        fig_birth = px.histogram(
            x=birth_years,
            nbins=80,
            labels={'x': 'Year of Birth', 'y': 'Count'},
            title=f'Voter distribution by Year of Birth (n={len(birth_years)})'
        )
        fig_birth.update_layout(bargap=0.1)
        context['birth_year_graph'] = pio.to_html(fig_birth, full_html=False)

        # Pie chart by Party Affiliation with data checks
        party_counts = voters.values('party_affiliation').annotate(count=models.Count('party_affiliation'))
        party_counts_df = pd.DataFrame(list(party_counts))  # Convert queryset to DataFrame

        if not party_counts_df.empty and 'party_affiliation' in party_counts_df.columns and 'count' in party_counts_df.columns:
            fig_party = px.pie(
                party_counts_df,
                values='count',
                names='party_affiliation',
                title=f'Voter distribution by Party Affiliation (n={voters.count()})'
            )
            context['party_affiliation_graph'] = pio.to_html(fig_party, full_html=False)
        else:
            context['party_affiliation_graph'] = "<p>No data available for party affiliation distribution.</p>"

        # Histogram by Participation in Elections
        election_counts = {
            'v20state': voters.filter(v20state=True).count(),
            'v21town': voters.filter(v21town=True).count(),
            'v21primary': voters.filter(v21primary=True).count(),
            'v22general': voters.filter(v22general=True).count(),
            'v23town': voters.filter(v23town=True).count(),
        }
        fig_elections = px.bar(
            x=list(election_counts.keys()),
            y=list(election_counts.values()),
            labels={'x': 'Election', 'y': 'Vote Count'},
            title=f'Vote Count by Election (n={voters.count()})'
        )
        fig_elections.update_layout(bargap=0.1)
        context['election_participation_graph'] = pio.to_html(fig_elections, full_html=False)

        # Add filter form to context
        context['filter_form'] = VoterFilterForm(self.request.GET or None)
        return context
