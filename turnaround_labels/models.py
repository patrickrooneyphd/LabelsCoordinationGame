from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np
import random

author = 'Patrick Rooney'

doc = """
Labels and Turnarounds
"""


class Constants(BaseConstants):
    name_in_url = 'lat'
    players_per_group = 4
    num_rounds = 4
    bonus = 200

    # == Sentences for each round == #
    solution1 = 'Earnings are public.'
    solution2 = 'Old products have been replaced.'
    solution3 = 'The CEO is on vacation.'
    solution4 = 'Inventory is full.'

    # == Payoff matrices for control and treatments, resp. == #
    payoff_list = np.array([(200, 200, 200, 200, 200),
                           (150, 210, 210, 210, 210),
                           (100, 160, 220, 220, 220),
                           (50, 110, 170, 230, 230),
                           (0, 60, 120, 180, 240)])


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            #Set Paying Rounds and Randomly Assign Conditions#
            paying_round_a = random.randint(1, Constants.num_rounds/2)
            paying_round_b = random.randint(Constants.num_rounds/2 + 1,  Constants.num_rounds)
            for p in self.get_players():
                p.paying_round_a = paying_round_a
                p.paying_round_b = paying_round_b
                p.participant.vars['paying_round_a'] = paying_round_a
                p.participant.vars['paying_round_b'] = paying_round_b
            # conditions = ['Control', 'Treatment']
            # conditions = ['Treatment']
            conditions = ['Control']
            random.shuffle(conditions)
            for p in self.get_players():
                p.participant.vars['condition'] = conditions[0]
                p.condition = p.participant.vars['condition']
            #Group Randomly in Round 1. Reshuffle groups at start of 2nd part. Maintain previous rounds' groups o/w#
            self.group_randomly()
        elif self.round_number == (Constants.num_rounds / 2 + 1):
            for p in self.get_players():
                if p.participant.vars['condition'] == 'Control':
                    self.group_randomly()
                if p.participant.vars['condition'] == 'Treatment':
                    pass
        else:
            self.group_like_round(self.round_number - 1)  # Group like previous round

    def assign_buckets(self):
        players = self.get_players()
        player_indices = []
        midpoint = 0
        for p in self.get_players():
            if p.participant.vars['condition'] == 'Treatment':
                indices = [p.index for p in players]
                ids = [p.id_in_subsession for p in players]
                dictionary = dict(zip(ids, indices))
                sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1]))
                player_indices = [*sorted_dict]
                midpoint = int(self.session.num_participants / 2)
            if p.id_in_subsession in player_indices[:midpoint]:
                p.participant.vars['bucket'] = "Low"
                p.bucket = 'Low'
            if p.id_in_subsession in player_indices[midpoint:]:
                p.participant.vars['bucket'] = "High"
                p.bucket = 'High'

    def assign_new_groups_treatment(self):
        # == Gather players from equal sized High and Low bins == #
        players = self.get_players()

        high_players = [p for p in players if p.participant.vars['bucket'] == 'High']
        low_players = [p for p in players if p.participant.vars['bucket'] == 'Low']

        group_matrix = []

        # == Fill in groups for second part == #
        while high_players:
            new_group = [
                high_players.pop(),
                high_players.pop(),
                high_players.pop(),
                high_players.pop(),
            ]
            group_matrix.append(new_group)

        while low_players:
            new_group = [
                low_players.pop(),
                low_players.pop(),
                low_players.pop(),
                low_players.pop(),
            ]
            group_matrix.append(new_group)

        self.set_group_matrix(group_matrix)
        print('Groups have been assigned')

    def assign_payoff_display(self):
        players = self.get_players()
        for p in self.get_players():
            payoff_list = [p.payoff for p in players]
            ids = [p.id_in_subsession for p in players]
            dictionary = dict(zip(ids, payoff_list))
            sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1]))
            player_ranking = [*sorted_dict]
            print(player_ranking)
            print(player_ranking[0])
            p.participant.vars['rank'] = player_ranking.index(p.id_in_subsession) + 1
            two_cutoff = int(self.session.num_participants * (3/8))
            three_cutoff = int(self.session.num_participants * (5/8))
            four_cutoff = int(self.session.num_participants * (7/8))
            if p.id_in_subsession in player_ranking[:two_cutoff]:
                p.participant.vars['payoff_display'] = 2.00
            if p.id_in_subsession in player_ranking[two_cutoff:three_cutoff]:
                p.participant.vars['payoff_display'] = 3.00
            if p.id_in_subsession in player_ranking[three_cutoff:four_cutoff]:
                p.participant.vars['payoff_display'] = 4.00
            if p.id_in_subsession in player_ranking[four_cutoff:]:
                p.participant.vars['payoff_display'] = 5.00


class Group(BaseGroup):
    condition = models.StringField()
    min = models.IntegerField()
    first = models.IntegerField()
    second = models.IntegerField()
    third = models.IntegerField()
    fourth = models.IntegerField()

    def set_payoffs(self):
        # == Set Payoffs in Each Round per Group Member == #
        players = self.get_players()
        sentences = [p.total_sentences for p in players]
        sent_random = np.random.choice(sentences, 4, replace=False)
        self.min = min(sentences)
        self.first = sent_random[0]
        self.second = sent_random[1]
        self.third = sent_random[2]
        self.fourth = sent_random[3]
        for p in players:
            p.round_earnings = Constants.payoff_list.item((p.total_sentences, self.min))
            p.first_p = Constants.payoff_list.item((self.first, self.min))
            p.second_p = Constants.payoff_list.item((self.second, self.min))
            p.third_p = Constants.payoff_list.item((self.third, self.min))
            p.fourth_p = Constants.payoff_list.item((self.fourth, self.min))


class Player(BasePlayer):
    bucket = models.StringField()
    random = models.FloatField()
    round_id = models.StringField()
    condition = models.StringField()
    consent = models.StringField(label='', choices=['I consent'], widget=widgets.TextInput)
    paying_round_a = models.IntegerField()
    paying_round_b = models.IntegerField()
    payoff_a = models.IntegerField()
    payoff_b = models.IntegerField()
    bonus = models.IntegerField()
    round_earnings = models.IntegerField()

    practice_response1 = models.IntegerField(label='', choices=[1], widget=widgets.TextInput)
    practice_response2 = models.IntegerField(label='', choices=[210], widget=widgets.TextInput)
    practice_response3 = models.IntegerField(label='', choices=[0], widget=widgets.TextInput)
    practice_response4 = models.IntegerField(label='', choices=[100], widget=widgets.TextInput)
    practice_response5 = models.IntegerField(label='', choices=[0], widget=widgets.TextInput)
    practice_response6 = models.IntegerField(label='', choices=[200], widget=widgets.TextInput)
    practice_response_a = models.IntegerField(label='', widget=widgets.TextInput)
    practice_response_b = models.IntegerField(label='', widget=widgets.TextInput)
    practice_response_c = models.IntegerField(label='', widget=widgets.TextInput)

    true_false1 = models.StringField(label='', choices=['True'], widget=widgets.TextInput)
    true_false2 = models.StringField(label='', choices=['True'], widget=widgets.TextInput)

    submitted_answer1 = models.StringField(label='Earnings are public.', widget=widgets.TextInput, blank=True)
    submitted_answer2 = models.StringField(label='Old products have been replaced.', widget=widgets.TextInput,
                                           blank=True)
    submitted_answer3 = models.StringField(label='The CEO is on vacation.', widget=widgets.TextInput, blank=True)
    submitted_answer4 = models.StringField(label='Inventory is full.', widget=widgets.TextInput, blank=True)

    is_correct1 = models.BooleanField()
    is_correct2 = models.BooleanField()
    is_correct3 = models.BooleanField()
    is_correct4 = models.BooleanField()
    total_sentences = models.IntegerField()
    min_p = models.IntegerField()
    first_p = models.IntegerField()
    second_p = models.IntegerField()
    third_p = models.IntegerField()
    fourth_p = models.IntegerField()

    reflection = models.StringField(label='', widget=widgets.Textarea, blank=True)

    guess1 = models.IntegerField(label='')
    guess2 = models.IntegerField(label='')
    guess3 = models.IntegerField(label='')
    average_guess = models.FloatField()
    index = models.FloatField()

    # == Manipulation Check Questions == #

    manip_1 = models.StringField(label='', widget=widgets.Textarea)
    manip_2 = models.StringField(label='', widget=widgets.Textarea)
    manip_3 = models.StringField(label='', widget=widgets.Textarea)
    manip_4 = models.StringField(label='', widget=widgets.Textarea)
    manip_5 = models.StringField(label='', widget=widgets.Textarea)

    # == Questionnaire variables == #
    age = models.IntegerField(label='', min=0, max=100)
    gender = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Male', 'Female', 'Non-Binary', 'Prefer not to Disclose']
    )
    race = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['White', 'Black', 'East Asian', 'South Asian', 'Middle Eastern', 'Hispanic', 'Multi-racial', 'Other']
    )
    major = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Economics', 'Other Social Science', 'Chemical/Physical/Biological Sciences',
                 'Engineering/Computer Science', 'Humanities', 'Other']
    )
    religion = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Frequently // Once a week', 'Often // Once a month', 'Sometimes // Once every few months',
                 'Seldom // Once or twice a year', 'Never']
    )
    volunteer = models.StringField(label='', widget=widgets.RadioSelect, choices=['Yes', 'No'])
    donate = models.StringField(label='', widget=widgets.RadioSelect, choices=['Yes', 'No'])
    first_pd_strategy = models.StringField(label='', widget=widgets.TextInput)
    later_pd_strategy = models.StringField(label='', widget=widgets.TextInput)
    zero_opinion = models.StringField(label='', widget=widgets.TextInput)
    four_opinion = models.StringField(label='', widget=widgets.TextInput)
    second_firm_feelings = models.StringField(label='', widget=widgets.TextInput)
    later_second_firm_feelings = models.StringField(label='', widget=widgets.TextInput)

    risk1 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['$7 for certain', '$10 with probability 50%, $2 with probability 50%'],
        blank=True
    )
    risk2 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['$6 for certain', '$10 with probability 50%, $2 with probability 50%'],
        blank=True
    )
    risk3 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['$5 for certain', '$10 with probability, $2 with probability 50%'],
        blank=True
    )
    risk4 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['$4 for certain', '$10 with probability 50%, $2 with probability 50%'],
        blank=True
    )
    risk5 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['$3 for certain', '$10 with probability 50%, $2 with probability 50%'],
        blank=True
    )
    amb1 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Bag 1 (containing 16 red balls and 4 black balls)', 'Bag 2 (containing 20 balls)'],
        blank=True
    )
    amb2 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Bag 1 (containing 14 red balls and 6 black balls)', 'Bag 2 (containing 20 balls)'],
        blank=True
    )
    amb3 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Bag 1 (containing 12 red balls and 8 black balls)', 'Bag 2 (containing 20 balls)'],
        blank=True
    )
    amb4 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Bag 1 (containing 10 red balls and 10 black balls)', 'Bag 2 (containing 20 balls)'],
        blank=True
    )
    amb5 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Bag 1 (containing 8 red balls and 12 black balls)', 'Bag 2 (containing 20 balls)'],
        blank=True
    )
    amb6 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Bag 1 (containing 6 red balls and 14 black balls)', 'Bag 2 (containing 20 balls)'],
        blank=True
    )
    amb7 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Bag 1 (containing 4 red balls and 16 black balls)', 'Bag 2 (containing 20 balls)'],
        blank=True
    )
    risk_payoff = models.FloatField()
    risk_payoff_str = models.StringField()
    amb_payoff = models.FloatField()
    amb_payoff_str = models.StringField()

    open_comments = models.StringField(label='', widget=widgets.Textarea, blank=True)

    debrief_1 = models.StringField(label='', widget=widgets.RadioSelect,
                                   choices=['Strategy','Operations', 'Finance'], blank=False)
    debrief_2 = models.StringField(label='', widget=widgets.RadioSelect,
                                   choices=['Number of Sentences Typed', 'Charitable Incentives', 'Group Size'],
                                   blank=False)
    debrief_3 = models.StringField(label='', widget=widgets.RadioSelect,
                                   choices=['Self-Payment', 'Charity Payment',
                                            'Those sorted by initial beliefs and actions'], blank=False)
    debrief_4 = models.StringField(label='', widget=widgets.RadioSelect,
                                   choices=['Those not sorted by initial beliefs and actions', 'Charity Payment',
                                            'Group Size'], blank=False)
    debrief_5 = models.StringField(label='', widget=widgets.RadioSelect,
                                   choices=['Groups with individuals with initial positive beliefs and actions will '
                                            'coordinate better in the “turnaround” period compared to those who are '
                                            'not sorted based on their initial beliefs and actions.', 'Individuals '
                                            'in the treatment group will decide to stop playing in the middle of the '
                                            'experiment because they are ethically disturbed by the game.',
                                            'Individuals will be more likely to choose a job with an NGO following the '
                                            'experiment'], blank=False)
    debrief_6 = models.StringField(label='', widget=widgets.RadioSelect,
                                   choices=['Economics experiments are always only a half an hour long, while '
                                            'psychology experiments can be of any length.', 'Economics experiments are '
                                            'always incentivized and do not practice deception, and psychology '
                                            'experiments may involve deception and are often not incentivized.',
                                            'Economics experiments are always about financial markets, whereas '
                                            'psychology experiments are always about individual mental processes.'],
                                   blank=False)

    confirm_payment = models.StringField(label='', widget=widgets.Textarea, blank=False)

    # == Player Functions == #
    def check_correct(self):
        # == Count number of correct sentences entered in round == #
        self.is_correct1 = (self.submitted_answer1 == Constants.solution1)
        self.is_correct2 = (self.submitted_answer2 == Constants.solution2)
        self.is_correct3 = (self.submitted_answer3 == Constants.solution3)
        self.is_correct4 = (self.submitted_answer4 == Constants.solution4)

    def sum_sentences(self):
        # == Sum number of correct sentences entered in round == #
        self.total_sentences = self.is_correct1 + self.is_correct2 + self.is_correct3 + self.is_correct4

    def set_payoffs(self):
        if self.subsession.round_number == self.participant.vars['paying_round_a']:
            self.payoff_a = round(self.round_earnings, 2)
            self.participant.vars['payoff_a'] = self.payoff_a
            self.payoff = self.payoff_a

        if self.subsession.round_number == self.participant.vars['paying_round_b']:
            self.payoff_b = round(self.round_earnings, 2)
            self.participant.vars['payoff_b'] = self.payoff_b
            self.payoff = self.payoff + self.payoff_b

    def set_guess_bonus(self):
        other_players = self.get_others_in_group()
        sentences = [p.total_sentences for p in other_players]
        sentences.sort()
        guesses = [self.guess1, self.guess2, self.guess3]
        guesses.sort()
        guesses_equal_sentences = (sentences == guesses)
        if guesses_equal_sentences:
            self.participant.vars['bonus'] = Constants.bonus
        else:
            self.participant.vars['bonus'] = 0

    def add_bonus(self):
        if self.participant.vars['bonus'] == Constants.bonus:
            self.payoff = self.payoff + Constants.bonus
        else:
            self.payoff = self.payoff

    def calculate_index(self):
        self.average_guess = (self.guess1 + self.guess2 + self.guess3) / 3
        self.index = self.total_sentences + self.average_guess

    # == Calculate Risk and Ambiguity Aversion Payoffs == #
    def extra_payments(self):
        risk = random.choice([self.risk1, self.risk2, self.risk3, self.risk4, self.risk5])
        risk_dict = {self.risk1: 140, self.risk2: 120, self.risk3: 100, self.risk4: 80, self.risk5: 60}
        amb = random.choice([self.amb1, self.amb2, self.amb3, self.amb4, self.amb5, self.amb6, self.amb7])
        amb_dict = {self.amb1: 80, self.amb2: 70, self.amb3: 60, self.amb4: 50, self.amb5: 40,
                    self.amb6: 30, self.amb7: 20}
        rand1 = random.randint(0, 100)
        rand2 = random.randint(0, 100)

        #== Risk Aversion Payoffs ==#
        if risk == '$10 with probability 50%, $2 with probability 50%':
            if rand1 > 50:
                self.payoff = self.payoff + 200
                self.risk_payoff = 200
            else:
                self.risk_payoff = 40
                self.payoff = self.payoff + 40
        else:
            self.risk_payoff = risk_dict[risk]
            self.payoff = self.payoff + self.risk_payoff

        # == Ambiguity Aversion Payoffs ==#
        if amb == 'Bag 2 (containing 20 balls)':
            if rand1 > rand2:
                self.payoff = self.payoff + 200
                self.amb_payoff = 200
            else:
                self.payoff = self.payoff + 40
                self.amb_payoff = 40
        else:
            amb_val = amb_dict[amb]
            if amb_val > rand2:
                self.payoff = self.payoff + 200
                self.amb_payoff = 200
            else:
                self.payoff = self.payoff + 40
                self.amb_payoff = 40

        self.risk_payoff_str = '{:,.2f}'.format(self.risk_payoff)
        self.participant.vars['risk_payoff'] = self.risk_payoff_str
        self.amb_payoff_str = '{:,.2f}'.format(self.amb_payoff)
        self.participant.vars['amb_payoff'] = self.amb_payoff_str


    pass