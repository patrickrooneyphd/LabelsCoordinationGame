# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2020-02-03 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0004_session_mturk_expiration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('condition', otree.db.models.StringField(max_length=10000, null=True)),
                ('min', otree.db.models.IntegerField(null=True)),
                ('first', otree.db.models.IntegerField(null=True)),
                ('second', otree.db.models.IntegerField(null=True)),
                ('third', otree.db.models.IntegerField(null=True)),
                ('fourth', otree.db.models.IntegerField(null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turnaround_labels_comm_group', to='otree.Session')),
            ],
            options={
                'db_table': 'turnaround_labels_comm_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('bucket', otree.db.models.StringField(max_length=10000, null=True)),
                ('belief_index', otree.db.models.FloatField(null=True)),
                ('belief', otree.db.models.StringField(max_length=10000, null=True)),
                ('random', otree.db.models.FloatField(null=True)),
                ('round_id', otree.db.models.StringField(max_length=10000, null=True)),
                ('condition', otree.db.models.StringField(max_length=10000, null=True)),
                ('consent', otree.db.models.StringField(choices=[('I consent', 'I consent')], max_length=10000, null=True, verbose_name='')),
                ('paying_round_a', otree.db.models.IntegerField(null=True)),
                ('paying_round_b', otree.db.models.IntegerField(null=True)),
                ('payoff_a', otree.db.models.IntegerField(null=True)),
                ('payoff_b', otree.db.models.IntegerField(null=True)),
                ('payoff_display_str', otree.db.models.StringField(max_length=10000, null=True)),
                ('bonus', otree.db.models.IntegerField(null=True)),
                ('round_earnings', otree.db.models.IntegerField(null=True)),
                ('practice_response1', otree.db.models.IntegerField(choices=[(1, 1)], null=True, verbose_name='')),
                ('practice_response2', otree.db.models.IntegerField(choices=[(210, 210)], null=True, verbose_name='')),
                ('practice_response3', otree.db.models.IntegerField(choices=[(0, 0)], null=True, verbose_name='')),
                ('practice_response4', otree.db.models.IntegerField(choices=[(100, 100)], null=True, verbose_name='')),
                ('practice_response5', otree.db.models.IntegerField(choices=[(0, 0)], null=True, verbose_name='')),
                ('practice_response6', otree.db.models.IntegerField(choices=[(200, 200)], null=True, verbose_name='')),
                ('practice_response_a', otree.db.models.IntegerField(null=True, verbose_name='')),
                ('practice_response_b', otree.db.models.IntegerField(null=True, verbose_name='')),
                ('practice_response_c', otree.db.models.IntegerField(null=True, verbose_name='')),
                ('true_false1', otree.db.models.StringField(choices=[('True', 'True')], max_length=10000, null=True, verbose_name='')),
                ('true_false2', otree.db.models.StringField(choices=[('True', 'True')], max_length=10000, null=True, verbose_name='')),
                ('submitted_answer1', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='Earnings are public.')),
                ('submitted_answer2', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='Old products have been replaced.')),
                ('submitted_answer3', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='The CEO is on vacation.')),
                ('submitted_answer4', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='Inventory is full.')),
                ('is_correct1', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('is_correct2', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('is_correct3', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('is_correct4', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('total_sentences', otree.db.models.IntegerField(null=True)),
                ('min_p', otree.db.models.IntegerField(null=True)),
                ('first_p', otree.db.models.IntegerField(null=True)),
                ('second_p', otree.db.models.IntegerField(null=True)),
                ('third_p', otree.db.models.IntegerField(null=True)),
                ('fourth_p', otree.db.models.IntegerField(null=True)),
                ('reflection', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='')),
                ('guess1', otree.db.models.IntegerField(null=True, verbose_name='')),
                ('guess2', otree.db.models.IntegerField(null=True, verbose_name='')),
                ('guess3', otree.db.models.IntegerField(null=True, verbose_name='')),
                ('average_guess', otree.db.models.FloatField(null=True)),
                ('long_reflection', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='')),
                ('age', otree.db.models.IntegerField(null=True, verbose_name='')),
                ('gender', otree.db.models.StringField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Non-Binary', 'Non-Binary'), ('Prefer not to Disclose', 'Prefer not to Disclose')], max_length=10000, null=True, verbose_name='')),
                ('race', otree.db.models.StringField(choices=[('White', 'White'), ('Black', 'Black'), ('East Asian', 'East Asian'), ('South Asian', 'South Asian'), ('Middle Eastern', 'Middle Eastern'), ('Hispanic', 'Hispanic'), ('Multi-racial', 'Multi-racial'), ('Other', 'Other')], max_length=10000, null=True, verbose_name='')),
                ('volunteer', otree.db.models.StringField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10000, null=True, verbose_name='')),
                ('donate', otree.db.models.StringField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10000, null=True, verbose_name='')),
                ('first_pd_strategy', otree.db.models.StringField(max_length=10000, null=True, verbose_name='')),
                ('later_pd_strategy', otree.db.models.StringField(max_length=10000, null=True, verbose_name='')),
                ('zero_opinion', otree.db.models.StringField(max_length=10000, null=True, verbose_name='')),
                ('four_opinion', otree.db.models.StringField(max_length=10000, null=True, verbose_name='')),
                ('second_firm_feelings', otree.db.models.StringField(max_length=10000, null=True, verbose_name='')),
                ('later_second_firm_feelings', otree.db.models.StringField(max_length=10000, null=True, verbose_name='')),
                ('risk1', otree.db.models.StringField(blank=True, choices=[('$7 for certain', '$7 for certain'), ('$10 with probability 50%, $2 with probability 50%', '$10 with probability 50%, $2 with probability 50%')], max_length=10000, null=True, verbose_name='')),
                ('risk2', otree.db.models.StringField(blank=True, choices=[('$6 for certain', '$6 for certain'), ('$10 with probability 50%, $2 with probability 50%', '$10 with probability 50%, $2 with probability 50%')], max_length=10000, null=True, verbose_name='')),
                ('risk3', otree.db.models.StringField(blank=True, choices=[('$5 for certain', '$5 for certain'), ('$10 with probability, $2 with probability 50%', '$10 with probability, $2 with probability 50%')], max_length=10000, null=True, verbose_name='')),
                ('risk4', otree.db.models.StringField(blank=True, choices=[('$4 for certain', '$4 for certain'), ('$10 with probability 50%, $2 with probability 50%', '$10 with probability 50%, $2 with probability 50%')], max_length=10000, null=True, verbose_name='')),
                ('risk5', otree.db.models.StringField(blank=True, choices=[('$3 for certain', '$3 for certain'), ('$10 with probability 50%, $2 with probability 50%', '$10 with probability 50%, $2 with probability 50%')], max_length=10000, null=True, verbose_name='')),
                ('amb1', otree.db.models.StringField(blank=True, choices=[('Bag 1 (containing 16 red balls and 4 black balls)', 'Bag 1 (containing 16 red balls and 4 black balls)'), ('Bag 2 (containing 20 balls)', 'Bag 2 (containing 20 balls)')], max_length=10000, null=True, verbose_name='')),
                ('amb2', otree.db.models.StringField(blank=True, choices=[('Bag 1 (containing 14 red balls and 6 black balls)', 'Bag 1 (containing 14 red balls and 6 black balls)'), ('Bag 2 (containing 20 balls)', 'Bag 2 (containing 20 balls)')], max_length=10000, null=True, verbose_name='')),
                ('amb3', otree.db.models.StringField(blank=True, choices=[('Bag 1 (containing 12 red balls and 8 black balls)', 'Bag 1 (containing 12 red balls and 8 black balls)'), ('Bag 2 (containing 20 balls)', 'Bag 2 (containing 20 balls)')], max_length=10000, null=True, verbose_name='')),
                ('amb4', otree.db.models.StringField(blank=True, choices=[('Bag 1 (containing 10 red balls and 10 black balls)', 'Bag 1 (containing 10 red balls and 10 black balls)'), ('Bag 2 (containing 20 balls)', 'Bag 2 (containing 20 balls)')], max_length=10000, null=True, verbose_name='')),
                ('amb5', otree.db.models.StringField(blank=True, choices=[('Bag 1 (containing 8 red balls and 12 black balls)', 'Bag 1 (containing 8 red balls and 12 black balls)'), ('Bag 2 (containing 20 balls)', 'Bag 2 (containing 20 balls)')], max_length=10000, null=True, verbose_name='')),
                ('amb6', otree.db.models.StringField(blank=True, choices=[('Bag 1 (containing 6 red balls and 14 black balls)', 'Bag 1 (containing 6 red balls and 14 black balls)'), ('Bag 2 (containing 20 balls)', 'Bag 2 (containing 20 balls)')], max_length=10000, null=True, verbose_name='')),
                ('amb7', otree.db.models.StringField(blank=True, choices=[('Bag 1 (containing 4 red balls and 16 black balls)', 'Bag 1 (containing 4 red balls and 16 black balls)'), ('Bag 2 (containing 20 balls)', 'Bag 2 (containing 20 balls)')], max_length=10000, null=True, verbose_name='')),
                ('risk_payoff', otree.db.models.FloatField(null=True)),
                ('risk_payoff_str', otree.db.models.StringField(max_length=10000, null=True)),
                ('amb_payoff', otree.db.models.FloatField(null=True)),
                ('amb_payoff_str', otree.db.models.StringField(max_length=10000, null=True)),
                ('open_comments', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='')),
                ('debrief_1', otree.db.models.StringField(choices=[('A', 'A')], max_length=10000, null=True, verbose_name='')),
                ('debrief_2', otree.db.models.StringField(choices=[('A', 'A')], max_length=10000, null=True, verbose_name='')),
                ('debrief_3', otree.db.models.StringField(choices=[('C', 'C')], max_length=10000, null=True, verbose_name='')),
                ('debrief_4', otree.db.models.StringField(choices=[('A', 'A')], max_length=10000, null=True, verbose_name='')),
                ('debrief_5', otree.db.models.StringField(choices=[('A', 'A')], max_length=10000, null=True, verbose_name='')),
                ('debrief_6', otree.db.models.StringField(choices=[('B', 'B')], max_length=10000, null=True, verbose_name='')),
                ('confirm_payment', otree.db.models.StringField(max_length=10000, null=True, verbose_name='')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='turnaround_labels_comm.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turnaround_labels_comm_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turnaround_labels_comm_player', to='otree.Session')),
            ],
            options={
                'db_table': 'turnaround_labels_comm_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='turnaround_labels_comm_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'turnaround_labels_comm_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turnaround_labels_comm.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turnaround_labels_comm.Subsession'),
        ),
    ]
