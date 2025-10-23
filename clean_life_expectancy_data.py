import pandas as pd

RAW_INPUT_FILE = "life-expectancy-data.csv"
CLEANED_OUTPUT_FILE = "life-expectancy-data-cleaned.csv"

# load the uncleaned data
df = pd.read_csv(RAW_INPUT_FILE)

# update variable names for consistency
rename_map = {
    "Country": "Country",
    "Region": "Region",
    "Year": "Year",
    "Infant_deaths": "InfantDeathsPer1k",
    "Under_five_deaths": "Under5DeathsPer1k",
    "Adult_mortality": "AdultMortalityPer1k",
    "Alcohol_consumption": "AlcoholLitersPerCapita",
    "Hepatitis_B": "HepatitisBCoveragePercentage",
    "Measles": "MeaslesCoveragePercentage",
    "BMI": "BmiMean",
    "Polio": "PolioCoveragePercentage",
    "Diphtheria": "DiphtheriaCoveragePercentage",
    "Incidents_HIV": "HivIncidentsPer1k",
    "GDP_per_capita": "GdpPerCapitalUsd",
    "Population_mln": "PopulationMillions",
    "Thinness_ten_nineteen_years": "Thinness10To19Percentage",
    "Thinness_five_nine_years": "Thinness5To9Percentage",
    "Schooling": "AvgSchoolingYears",
    "Economy_status_Developed": "IsDeveloped",
    "Economy_status_Developing": "IsDeveloping",
    "Life_expectancy": "LifeExpectancyYears"
}

# rename the columns
df.rename(columns=rename_map, inplace=True)

# save the cleaned data
df.to_csv(CLEANED_OUTPUT_FILE, index=False)

print(f"✅ [cleaned] {RAW_INPUT_FILE} -> {CLEANED_OUTPUT_FILE}")