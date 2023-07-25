import pandas as pd
from utilities.generate_data_utils import generate

def company_transformation(companies: pd.DataFrame) -> pd.DataFrame:
    """Company Transformation Function
    Implement requirements 1& 2 from the readme below!

    Args:
        companies (pd.DataFrame): Take in a pandas dataframe of generated company data

    Returns:
        pd.DataFrame: Return a clean dataframe of company data
    """

    return companies

def company_financials_transformation(companies: pd.DataFrame) -> pd.DataFrame:
    """Company Financials Transformation Function
    Implement the 3rd "Financials" requirement from the readme below!

    Args:
        companies (pd.DataFrame): Take in a pandas dataframe of generated company data

    Returns:
        pd.DataFrame: Return a clean dataframe of company financials data
    """
    company_financials = companies.copy()


    return  company_financials

# generate random companies

companies = generate()

# apply transformations
clean_companies = company_transformation(companies)
clean_company_financials = company_financials_transformation(companies)

# output data below in .csv format...

