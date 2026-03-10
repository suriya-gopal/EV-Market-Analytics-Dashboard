# Global EV Market Intelligence & Analytics System

## Overview

An end-to-end business intelligence solution built using Power BI to analyze trends, performance, and market dynamics in the global electric vehicle industry. The project transforms raw EV market data into a structured analytical model with interactive dashboards designed to support executive decision-making and strategic analysis.

## Objectives

- Create a unified analytical view of the global EV market
- Enable comparison across manufacturers, battery technologies, and regions
- Surface key performance indicators and sales trends
- Support data-driven decision-making through interactive dashboards

## Tech Stack

- Power BI (dashboards, DAX measures, Power Query ETL)
- Python (data cleaning and preprocessing)
- Star Schema data modeling

## Data Model

A Power BI-native data mart was designed using a star schema with the following structure:

**Fact Table:** FactEV — contains measures for total units sold, revenue, battery capacity, range, charging time, average price, and range per kWh efficiency.

**Dimension Tables:** DimManufacturer, DimModel, DimBattery, DimCharging, DimCountry, DimTime, DimColor, DimTech

All relationships are Many-to-One with single-direction filtering to ensure accurate aggregations and prevent ambiguity.

## ETL Process

Raw data was cleaned using a Python script (`ETL.py`) that handles column standardization, type conversion, duplicate removal, and feature engineering (range per kWh). The cleaned dataset was then imported into Power BI for further transformation using Power Query.

## Dashboards

**Dashboard 1: Market Overview**
Sales trends from 2015 to 2024, top 10 manufacturers by units sold, geographic distribution, and battery type breakdown.

**Dashboard 2: Technology & Performance Analysis**
Battery range benchmarks, charging time by charging standard, range-per-kWh efficiency by manufacturer, and battery capacity vs driving range scatter analysis.

**Dashboard 3: Market Forecast & Financial Insights**
Revenue vs units sold correlation, 3-year sales forecast, revenue share by battery type, and top manufacturers by total revenue.

**Dashboard 4: Consumer & Vehicle Attribute Insights**
Price vs driving range positioning, top manufacturers by safety rating, average warranty coverage, and a multi-attribute comparison matrix.

## Key Findings

- Ferrari, Nissan, and VinFast rank among top performers by units sold
- Lithium-based battery types dominate revenue and sales share
- Higher battery capacity generally correlates with increased driving range
- Faster charging standards reduce charge time but remain less widely adopted
- EV pricing has remained stable with moderate growth aligned to revenue trends
- Sales forecasts indicate continued market growth over the next three years

## Dataset

The dataset is a simulated EV market dataset approximating real-world industry characteristics.

Source: [Kaggle - EV Electrical Vehicles Dataset (3K Records, 2025)](https://www.kaggle.com/datasets/pratyushpuri/ev-electrical-vehicles-dataset-3krecords-2025)

## How to View the Dashboard

Download the `Global_EV_Market_Analysis.pbix` file and open it in Power BI Desktop (free download from Microsoft).

## Repository Structure

```
Global-EV-Market-Analytics/
├── Global_EV_Market_Analysis.pbix
├── Global_EV_Market_Analysis_Dashboard.pdf
├── Final_Project_Report.pdf
├── ETL.py
├── data/
│   ├── electric_vehicles_dataset.csv
│   ├── electric_vehicles_dataset.json
│   └── clean_ev_data.csv
└── README.md
```

## Author

Suriyavardhan Gopal | 
Master of Science in Information Management, University of Illinois Urbana-Champaign
