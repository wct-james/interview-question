from utilities.generate_data_utils import generate
from main import company_transformation, company_financials_transformation


def test_column_names():
    """Test Requirement 1"""
    companies = generate()

    clean_companies = company_transformation(companies)

    assert list(clean_companies.columns).sort() == [
        "Legacy ID",
        "Company Name",
        "Company Type",
        "Company URL",
        "Sector",
        "Geographies",
        "Target Status",
        "Owner",
        "Business Description",
    ].sort()


def test_data_mapping():
    """Test Requirement 2"""
    companies = generate()

    clean_companies = company_transformation(companies)

    cleaned_sectors = set(
        clean_companies["Sector"].to_list()
    )

    assert cleaned_sectors == {
        "Technology",
        "Real Estate",
        "Healthcare",
        "Infrastructure",
        "General",
        "Entertainment",
    }

    cleaned_geographies = list([
        i.split("; ") for i in
        clean_companies["Geographies"].to_list()
        ])
    
    cleaned_geographies = set(list([i for r in cleaned_geographies for i in r]))

    assert cleaned_geographies == {
        "United States",
        "Europe",
        "South America",
        "Africa",
        "Asia",
        "",
    }

def test_company_financials():
    """Test Requirement 3
    """
    companies = generate()

    clean_company_financials = company_financials_transformation(companies)

    assert list(clean_company_financials.columns).sort() == [
        "Legacy ID",
        "Company",
        "Fiscal Year",
        "EBITDA",
    ].sort()

    fiscal_years = set(clean_company_financials["Fiscal Year"].to_list())

    assert fiscal_years == {
        "FY22",
        "FY23",
        "FY24",
    }
