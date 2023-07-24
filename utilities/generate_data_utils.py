from faker import Faker
from faker.providers import DynamicProvider
import uuid
import pandas as pd
import regex as re
import random


def generate() -> pd.DataFrame:
    """Generate 20,000 Companies

    Returns:
        pd.DataFrame: A pandas dataframe containing the generated companies
    """

    fake = Faker()

    internal_team = DynamicProvider(
        provider_name="internal_team", elements=["Investor Relations", "Deal Team"]
    )

    sectors = DynamicProvider(
        provider_name="sectors",
        elements=[
            # clean
            "Tech",
            "Real Estate",
            "Healthcare",
            "Infrastructure",
            "Entertainment",
            # unclean
            "_",
            "N/A",
            "infra",
            "Technology Projects",
            "re",
        ],
    )

    fake.add_provider(internal_team)
    fake.add_provider(sectors)

    def generate_user() -> tuple:
        id = str(uuid.uuid4())
        name = fake.name()
        first_name = name.split(" ")[0]
        last_name = " ".join(name.split(" ")[1:])
        email = "{first_name}.{last_name}@dealcloud-capital.com".format(
            first_name=first_name, last_name=last_name
        ).lower()
        team = fake.internal_team()
        sector = fake.sectors()

        return (id, first_name, last_name, email, team, sector)

    def generate_users(count: int = 50) -> pd.DataFrame():
        data = list((generate_user() for _ in range(count)))
        headers = ["id", "first_name", "last_name", "email", "team", "sector"]
        df = pd.DataFrame(data=data, columns=headers)
        return df

    users = generate_users(50)

    geography = DynamicProvider(
        provider_name="geography",
        elements=[
            # clean
            "United States",
            "Europe",
            "South America",
            "Africa",
            "Asia",
            # unclean
            "US",
            "asia",
            "afria",
            "Spain",
        ],
    )

    company_types = DynamicProvider(
        provider_name="company_types",
        elements=[
            "Operating Company",
            "General Partner",
            "Limited Partner",
            "Service Provider",
        ],
    )

    target_status = DynamicProvider(
        provider_name="target_status", elements=["Watchlist", "Yes", None]
    )

    user_ids = DynamicProvider(
        provider_name="user_ids", elements=users["email"].to_list()
    )

    deal_team = DynamicProvider(
        provider_name="deal_team",
        elements=users[users["team"] == "Deal Team"]["email"].to_list(),
    )

    ir_team = DynamicProvider(
        provider_name="ir_team",
        elements=users[users["team"] == "Investor Relations"]["email"].to_list(),
    )

    fake.add_provider(user_ids)
    fake.add_provider(deal_team)
    fake.add_provider(ir_team)
    fake.add_provider(geography)
    fake.add_provider(company_types)
    fake.add_provider(target_status)

    def progress(value, i, var):
        value_i = value + (i * random.randint(-var, var))
        return value_i

    def generate_company() -> tuple:
        id = str(uuid.uuid4())
        company_name = fake.company()
        company_type = fake.company_types()
        website = "https://{}.com".format(
            re.sub("[^a-zA-Z0-9\n\.]", "", company_name)
        ).lower()
        sector = fake.sectors()
        geographies = "; ".join(
            list([fake.unique.geography() for _ in range(random.randint(0, 3))])
        )
        target_status = (
            fake.target_status() if company_type == "Operating Company" else None
        )
        owner = (
            fake.deal_team() if company_type == "Operating Company" else fake.ir_team()
        )
        business_description = fake.text()

        ebitda_fy22 = random.randint(100, 1000)
        ebitda_fy23 = progress(ebitda_fy22, 1, 10)
        ebitda_fy24 = progress(ebitda_fy23, 1, 10)

        fake.unique.clear()

        return (
            id,
            company_name,
            company_type,
            website,
            sector,
            geographies,
            target_status,
            owner,
            business_description,
            ebitda_fy22,
            ebitda_fy23,
            ebitda_fy24,
        )

    def generate_companies(count: int = 1000) -> pd.DataFrame():
        data = list((generate_company() for _ in range(count)))
        headers = [
            "id",
            "company_name",
            "company_type",
            "website",
            "sector",
            "geographies",
            "target_status",
            "owner",
            "business_description",
            "ebitda_fy22",
            "ebitda_fy23",
            "ebitda_fy24",
        ]

        df = pd.DataFrame(data=data, columns=headers)
        return df

    companies = generate_companies(20000)

    return companies
