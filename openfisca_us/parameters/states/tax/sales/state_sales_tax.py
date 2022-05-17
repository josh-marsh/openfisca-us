from openfisca_us.model_api import *


class state_sales_tax(Variable):
    value_type = float
    entity = TaxUnit
    label = "State sales tax"
    unit = USD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        # Add
        # Example: https://github.com/PolicyEngine/openfisca-us-data/blob/master/openfisca_us_data/datasets/ce/ce.py#L275
    #     ce["/household/emissions/co2_kg"] = sum(
    #     [
    #         emission_coefficients[category] * ce[group_prefix + category][:]
    #         for category in emission_coefficients.keys()
    #     ]
    # )
