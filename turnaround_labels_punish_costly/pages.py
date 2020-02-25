from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    form_model = 'player'
    form_fields = ['consent']

    def is_displayed(self):
        return self.round_number == 1
    pass


class Practice(Page):
    form_model = 'player'
    form_fields = ['practice_response1', 'practice_response2', 'practice_response3', 'practice_response4',
                   'practice_response5', 'practice_response6', 'practice_response_a', 'practice_response_b',
                   'practice_response_c', 'true_false1', 'true_false2']

    def is_displayed(self):
        return self.round_number == 1


class WaitForInstructions(WaitPage):
    def is_displayed(self):
        return self.round_number == 1


class Matrix(Page):
    timeout_seconds = 30

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.player.assign_random_number()
    pass


class AssignNewGroupsInfo(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_roundsr / 2 + 1
    pass


class AssignMaintainGroups(WaitPage):
    wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number > (Constants.num_roundsr / 2)

    def after_all_players_arrive(self):
        self.subsession.assign_new_groups()


class ClickNext(Page):  # Need this page to match punish regime text to condition
    def is_displayed(self):
        return self.round_number == Constants.num_roundsr / 2 + 1

    def before_next_page(self):
        self.group.punish_regime_display()  # Assign the punishment regime for the approp. condition.
    pass


class PunishInfo(Page):

    def is_displayed(self):
        return self.round_number == (Constants.num_roundsr / 2 + 1) and \
               (self.participant.vars['condition'] == 'Punish_RandomAudit' or 'Punish_AllRounds')

    def vars_for_template(self):
        return {
            'punish_regime': self.participant.vars['punish_regime'],
        }
    pass


class SecondPartWait(WaitPage):
    wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number > (Constants.num_roundsr / 2)
    pass


class Round(Page):
    form_model = 'player'
    form_fields = ['submitted_answer1', 'submitted_answer2', 'submitted_answer3', 'submitted_answer4', 'reflection']
    timeout_seconds = 60

    def before_next_page(self):
        self.player.check_correct()
        self.player.sum_sentences()


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()
        self.group.show_result()
    pass


class PunishVote(Page):
    form_model = 'player'
    form_fields = ['vote']

    def is_displayed(self):
        return self.round_number > (Constants.num_roundsr / 2) \
               and (self.participant.vars['condition'] == 'Punish_AllRounds' or
                    self.round_number == self.participant.vars['rand_audit_a'] or
                    self.round_number == self.participant.vars['rand_audit_b'])
    pass


class ResultsWaitPage2(WaitPage):

    def is_displayed(self):
        return self.round_number > (Constants.num_roundsr / 2)

    def after_all_players_arrive(self):
        self.group.set_payoffs()
        self.group.show_result()
    pass


class BeliefsAboutOtherPlayers(Page):
    form_model = 'player'
    form_fields = ['guess1', 'guess2', 'guess3']

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.player.set_guess_bonus()
        self.player.calculate_index()
    pass


class BeliefsWaitPage(WaitPage):
    wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number == 1

    def after_all_players_arrive(self):
        self.subsession.assign_second_half_groupings()
    pass


class Results(Page):
    timeout_seconds = 15

    def is_displayed(self):
        return self.round_number < (Constants.num_roundsr / 2 + 1)

    def vars_for_template(self):
        return {
            'player_in_all_rounds': self.player.in_all_rounds(),
        }

    def before_next_page(self):
        self.player.set_payoffs()
    pass


class ResultsSecondPart(Page):
    timeout_seconds = 20

    def is_displayed(self):
        return self.round_number > (Constants.num_roundsr / 2)

    def vars_for_template(self):
        return {
            'player_in_all_rounds': self.player.in_all_rounds(),
        }

    def before_next_page(self):
        self.player.set_payoffs()
    pass


class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'race', 'volunteer', 'donate', 'first_pd_strategy',
                   'later_pd_strategy', 'zero_opinion', 'four_opinion', 'second_firm_feelings',
                   'later_second_firm_feelings']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    pass


class AversionPage(Page):
    form_model = 'player'
    form_fields = ['risk1', 'risk2', 'risk3', 'risk4', 'risk5', 'amb1', 'amb2', 'amb3', 'amb4', 'amb5', 'amb6', 'amb7']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def before_next_page(self):
        self.player.add_bonus()
        self.player.extra_payments()
    pass


class OpenComments(Page):
    form_model = 'player'
    form_fields = ['open_comments']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    pass


class DebriefingSheet(Page):
    form_model = 'player'
    form_fields = ['debrief_1', 'debrief_2', 'debrief_3', 'debrief_4', 'debrief_5', 'debrief_6',]

    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    pass


class PaymentWaitPage(WaitPage):
    wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def after_all_players_arrive(self):
        self.subsession.assign_payoff_display()
    pass


class FinalPayment(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'paying_round_a': self.participant.vars['paying_round_a'],
            'payoff_a': self.participant.vars['payoff_a'],
            'paying_round_b': self.participant.vars['paying_round_b'],
            'payoff_b': self.participant.vars['payoff_b'],
            'point_payoff': self.participant.payoff_plus_participation_fee(),
            'payoff': self.participant.payoff,
            'risk_payoff': self.participant.vars['risk_payoff'],
            'amb_payoff': self.participant.vars['amb_payoff'],
            'bonus': self.participant.vars['bonus'],
            'rank': self.participant.vars['rank'],
            'payoff_display': self.participant.vars['payoff_display']
            # 'payoff': self.participant.payoff_plus_participation_fee(),
        }
    pass


class Thanks(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    pass


page_sequence = [
    Introduction,
    # Practice,
    WaitForInstructions,
    Matrix,
    AssignNewGroupsInfo,
    AssignMaintainGroups,
    ClickNext,
    PunishInfo,
    SecondPartWait,
    Round,
    ResultsWaitPage,
    PunishVote,
    ResultsWaitPage2,
    BeliefsAboutOtherPlayers,
    BeliefsWaitPage,
    Results,
    ResultsSecondPart,
    # Questionnaire,
    AversionPage,
    # OpenComments,
    # DebriefingSheet,
    PaymentWaitPage,
    FinalPayment,
    Thanks
]
