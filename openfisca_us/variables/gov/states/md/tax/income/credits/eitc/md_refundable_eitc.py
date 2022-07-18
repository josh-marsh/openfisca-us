from openfisca_us.model_api import *


class md_refundable_eitc(Variable):
    value_type = float
    entity = TaxUnit
    label = "MD EITC refundable State tax credit"
    unit = USD
    documentation = "Refundable EITC credit reducing MD State income tax."
    definition_period = YEAR
    reference = "https://casetext.com/statute/code-of-maryland/article-tax-general/title-10-income-tax/subtitle-7-income-tax-credits/section-10-704-effective-until-6302023-for-earned-income"

    def formula(tax_unit, period, parameters):
        eligible = tax_unit("md_qualifies_for_single_childless_eitc", period)
        non_refundable_eitc = tax_unit("md_non_refundable_eitc", period)
        p = parameters(period).gov.states.md.tax.income.credits.eitc
        income_tax = tax_unit("md_income_tax_before_credits", period)
        excess = max_(0, non_refundable_eitc - income_tax)
        return eligible * p.refundable_match * excess
