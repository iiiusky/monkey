from mongoengine import DynamicField, EmbeddedDocument, IntField, ListField, StringField

from monkey_island.cc.services.zero_trust.scoutsuite.consts import rule_consts


class ScoutSuiteRule(EmbeddedDocument):
    """
    This model represents ScoutSuite security rule check results:
    how many resources break the security rule
    security rule description and remediation and etc.
    """

    # SCHEMA
    description = StringField(required=True)
    path = StringField(required=True)
    level = StringField(required=True, options=rule_consts.RULE_LEVELS)
    items = ListField()
    dashboard_name = StringField(required=True)
    checked_items = IntField(min_value=0)
    flagged_items = IntField(min_value=0)
    service = StringField(required=True)
    rationale = StringField(required=True)
    remediation = StringField(required=False)
    compliance = DynamicField(required=False)
    references = ListField(required=False)
