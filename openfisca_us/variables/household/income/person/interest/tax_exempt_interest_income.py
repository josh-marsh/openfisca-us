from openfisca_us.model_api import *


class tax_exempt_interest_income(Variable):
    value_type = float
    entity = Person
    label = "Tax-exempt interest income"
    unit = USD
    definition_period = YEAR
    reference = "https://www.law.cornell.edu/uscode/text/26/subtitle-A/chapter-1/subchapter-B/part-III"
