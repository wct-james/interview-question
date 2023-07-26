import pandas as pd
from utilities.generate_data_utils import generate
from collections import OrderedDict


def company_transformation(companies: pd.DataFrame) -> pd.DataFrame:
    """Company Transformation Function
    Implement requirements 1& 2 from the readme below!

    Args:
        companies (pd.DataFrame): Take in a pandas dataframe of generated company data

    Returns:
        pd.DataFrame: Return a clean dataframe of company data
    """
    companies_cleaning = companies.copy()

    companies_dropped = companies_cleaning.drop(columns=['ebitda_fy22', 'ebitda_fy23', 'ebitda_fy24'])

    # Dropped FY columns

    companies_renamed = companies_dropped.rename(columns={
        'id': 'Legacy ID',
        'company_name': 'Company Name',
        'company_type': 'Company Type',
        'website': 'Company URL',
        'sector': 'Sector',
        'geographies': 'Geographies',
        'target_status': 'Target Status',
        'owner': 'Owner',
        'business_description': 'Business Description'
    })

    # Renamed column headers

    companies_replaced = companies_renamed.replace(to_replace={
      'Sector': {
          '^Tech$': 'Technology',
          '_': 'General',
          'N/A': 'General',
          'infra': 'Infrastructure',
          'Technology Projects': 'Technology',
          "^re$": 'Real Estate'
      },
      'Geographies': {
          'US': 'United States',
          'asia': 'Asia',
          'afria': 'Africa',
          'Spain': 'Europe'
        }
    },
        regex=True)

    companies_replaced['Geographies'] = companies_replaced['Geographies'].apply(
        lambda x: '; '.join(list(dict.fromkeys(x.split('; ')))))

    # Replaced values in sector and geographies columns, using lambda function to remove duplicate values in same cell

    companies = companies_replaced

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

    cf_dropped = company_financials.drop(columns=[
        'company_type',
        'website',
        'sector',
        'geographies',
        'target_status',
        'owner',
        'business_description'])

    # Dropped unnecessary columns

    melted_cf = cf_dropped.melt(id_vars=['id'], value_vars=['ebitda_fy22', 'ebitda_fy23', 'ebitda_fy24'],
                                var_name='Fiscal Year', value_name='EBITDA')
    melted_cf['Fiscal Year'] = 'FY' + melted_cf['Fiscal Year'].str.extract(r'(\d+)')
    melted_cf['Legacy ID'] = melted_cf['id'] + melted_cf['Fiscal Year'].astype(str)
    melted_cf = melted_cf.rename(columns={'id': 'Company'})
    sorted_melted_cf = melted_cf[['Legacy ID', 'Company', 'Fiscal Year', 'EBITDA']]

    # Used pandas.melt() function to pivot columns using multiple values and a single identifier

    company_financials = sorted_melted_cf

    return company_financials

# generate random companies

companies = generate()

# apply transformations
clean_companies = company_transformation(companies)
clean_company_financials = company_financials_transformation(companies)

# output data below in .csv format...
clean_companies.to_csv('Cleaned_Companies.csv', index=False)
clean_company_financials.to_csv('Cleaned_Company_Financials.csv', index=False)
