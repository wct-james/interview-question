# DealCloud Interview Question Repo

## Introduction
Data Transformation and data mapping are common tasks in DealCloud implementations. As part of this task, you will generate a random "messy" dataset and be presented with a list of requirements to transform the data.

You will use PyTest to confirm that the shape of the outputted transformation is successful.

## Requirements
### 1. Column Renaming
The column headers need to be renamed as below - FY22, FY23, FY24 can be droppped from the output as they will be addressed later on:

Old Field Name | New Field Name
--- | ---
id | Legacy ID
company_name | Company Name
company_type | Company Type
website | Company URL
sector | Sector
geographies | Geographies
target_status | Target Status
owner | Owner
business_description | Business Description

### 2. Categorical Data Mapping
Two of the columns require the categorical data within them to be adjusted/mapped so that they contain regular values. The "mapping tables" are described below:

#### Sectors
Old Sector Value | New Sector Value
--- | ---
Tech | Technology
Real Estate | Real Estate
Healthcare | Healthcare
Infrastructure | Infrastructure
Entertainment | Entertainment
_ | General
N/A | General
infra | Infrastructure
Technology Projects | Technology
re | Real Estate

#### Geographies
Old Geography Value | New Geography Value
--- | --- 
US | United States
Europe | Europe
South America | South America
Africa | Africa
Asia | Asia
United States | United States
asia | Asia
afria | Africa
Spain | Europe

### 3. Company Financials
The dataset contains three columns: 
- EBITDA FY22
- EBITDA FY23
- EBITDA FY23

It is not scalable to track annual/time-series data in individual fields, as you would need to add "FY24" as a field to track the next year of financials. This requirement is to parse this historically tracked data into a new table "Company Financials", with the following schema:

Field | Description
--- | ---
Legacy ID | A sensible unique identifier that can be the primary key for a given "company financial" record - it should not be randomly generated.
Company | Containing the ID of the company the "company financial" has been derived from.
Fiscal Year | The fiscal year, for historic data, it should contain on of "FY22", "FY23" and "FY24", however in the future it will contain more years.
EBITDA | The EBITDA value for that fiscal year.

### Example

This record:
id | ebitda_fy22 | ebitda_fy23
--- | --- | ---
companyid1 | 200 | 300

Would become:
