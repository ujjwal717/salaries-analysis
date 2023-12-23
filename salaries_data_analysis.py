import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("salaries_usable.csv")


def different_level():  # This function displays average salary of job titles according to experience level

    df_exp = df.query(
        '(Job_title == "Data Scientist" '  # Loading data from dataframe according to requirements
        'or Job_title == "Data Analyst"'
        ' or Job_title == "Machine Learning Engineer"  or Job_title == "Data Engineer"'
        ' or Job_title == "BI Analyst") and Experience_level != "Executive" '
    )

    df_exp["salary_usd_mean"] = df_exp.groupby(["Job_title", "Experience_level"])[
        "Salary_in_USD"
    ].transform(
        "mean"
    )  # Creating a mean salary column according to required grouping

    fig_1 = px.histogram(
        df_exp,
        x="Job_title",
        y="salary_usd_mean",  # Gave dataframe and assigned columns to both axes
        title="AVERAGE SALARY(USD) IN DIFFERENT TITLES ACROSS VARIOUS EXPERIENCE LEVELS",  # Provided title
        color="Job_title",  # Gave legend/color value
        histfunc="avg",  # Gave "average" as histogram function
        facet_col="Experience_level",  # Created different visuals according to experience level
        facet_col_spacing=0.1,  # Gave required spacing between visuals
        height=700,
        width=1500,  # assigned required height and width
        color_discrete_map={
            "Data scientist": "#AB63FA",  # separate colors for certain Job title
            "Machine Learning Engineer": "#8C564B",
        },
    ).update_layout(
        xaxis_title="Job Title", yaxis_title="Average Salary", legend_title="Job Title"
    )  # Fixed layout

    fig_1.update_traces(
        hovertemplate="<br>Job Title: %{x}<br>Average Salary (USD): %{y}"
    )  # Fixed hover template

    for axis in fig_1.layout:
        if (
            type(fig_1.layout[axis]) == go.layout.YAxis
        ):  # Used "For" loop to remove the unnecessary axes titles
            fig_1.layout[axis].title.text = ""
        if type(fig_1.layout[axis]) == go.layout.XAxis:
            fig_1.layout[axis].title.text = ""

    fig_1.show()  # Displaying the visual


def salary_across_years():  # This function shows average salary in various job titles across year 2021 - 2023
    df_across_years = df.query(
        '(Job_title == "Data Scientist" or Job_title == "Data Analyst"'  # Loading data from df according to requirement
        ' or Job_title == "ML Engineer"  or Job_title == "Data Engineer" )'
        " and (Year > 2020 and Year <= 2023)"
    )

    df_across_years["salary_mean"] = df_across_years.groupby(["Job_title", "Year"])[
        "Salary_in_USD"
    ].transform(
        "mean"
    )  # Created column having mean salary according to required grouping

    fig_2 = px.area(
        df_across_years,
        x="Year",
        y="salary_mean",  # Gave dataframe and assigned columns to both axes
        title="THE AVERAGE SALARY RANGE FROM 2021-2023 IN DIFFERENT TITLES",  # Gave Visual Title
        color="Job_title",  # Gave legend/color
        line_group="Job_title",  # Gave line plot according to need
        facet_col="Job_title",  # Created different visuals according to Job title
        facet_col_wrap=2,
        facet_col_spacing=0.1,  # Gave required spacing between visuals
    )

    fig_2.update_traces(
        hovertemplate="<br>Year: %{x}<br>Average Salary (USD): %{y}"
    )  # Updated hover template

    for axis in fig_2.layout:
        if (
            type(fig_2.layout[axis]) == go.layout.YAxis
        ):  # Used For loop to remove the unnecessary axis titles
            fig_2.layout[axis].title.text = ""

    fig_2.show()  # Displaying the visuals


def salaries_vs_countries():  # This Function shows average salary in different countries according to experience level

    df_salary = df.query(
        '( Job_title == "Data Engineer" '  # Loading data from df according to requirement
        'or Job_title == "Data Analyst"'
        ' or Job_title == "Data Scientist" or Job_title == "Machine Learning Engineer")'
        ' and (Company_location == "United States" or Company_location == "United Kingdom"'
        ' or Company_location == "Canada" or Company_location == "Germany" '
        'or Company_location == "France") and Experience_level != "Executive" '
    )

    df_salary["Salary_mean"] = df_salary.groupby(
        ["Experience_level", "Job_title", "Company_location"]
    )["Salary_in_USD"].transform(
        "mean"
    )  # Created column having mean salary by required grouping

    fig_3 = px.histogram(
        df_salary,
        x="Job_title",
        y="Salary_mean",  # Gave dataframe and assigned columns to both axes
        facet_col="Experience_level",  # Created different visuals according to experience level
        color_discrete_map={
            "United Kingdom": "#B6E880"
        },  # Gave custom color for required visual
        title="THE AVERAGE SALARY OF VARIOUS EXPERIENCE LEVEL IN DIFFERENT COUNTRIES",  # Gave title
        color="Company_location",  # Gave legend/color as needed
        histfunc="avg",  # Gave "average" to histogram funtion
    ).update_layout(
        xaxis_title=" ", yaxis_title=" ", legend_title="Company Location"
    )  # Layout update

    fig_3.update_traces(
        hovertemplate="<br> Job Title  : %{x}<br> Average Salary (USD) : %{y}"
    )  # Updated hover template

    for axis in fig_3.layout:
        if (
            type(fig_3.layout[axis]) == go.layout.YAxis
        ):  # Used For loop to remove the unnecessary axes titles
            fig_3.layout[axis].title.text = ""
        if type(fig_3.layout[axis]) == go.layout.XAxis:
            fig_3.layout[axis].title.text = ""

    fig_3.show()  # Display the visuals


def company_size():  # This function shows average salary across years in "entry" experience level by company size
    df_company = df.query(
        '(Job_title == "Data Analyst" or Job_title == "Data Scientist"'  # Loaded required data
        ' or Job_title == "Data Engineer" or Job_title == "Machine Learning Engineer")'
        ' and (Year > 2020 and Year <= 2023) and Experience_level != "Executive" '
    )

    df_company["salary_mean"] = df_company.groupby(
        ["Experience_level", "Job_title", "Company_size"]
    )["Salary_in_USD"].transform(
        "mean"
    )  # Created column salary mean having required grouping

    fig_4 = px.scatter(
        df_company,
        x="Job_title",
        y="salary_mean",  # Gave dataframe and assigned columns to both axes
        title="THE AVERAGE SALARY FOR DIFFERENT EXPERIENCE LEVEL ACCORDING TO COMPANY SIZE",  # Gave title
        size="salary_mean",  # Gave maximum bubble size
        color="Company_size",  # Gave color/legend as needed
        size_max=60,  # Set the maximum bubble size
        facet_col="Experience_level",  # Created different visual as experience level
    )  # Set 2 visual in 1 horizontal plane, spacing for them

    for axis in fig_4.layout:
        if (
            type(fig_4.layout[axis]) == go.layout.YAxis
        ):  # Used For loop to remove the unnecessary axes titles
            fig_4.layout[axis].title.text = " "
        if type(fig_4.layout[axis]) == go.layout.XAxis:
            fig_4.layout[axis].title.text = " "

    fig_4.update_traces(
        hovertemplate="<br> Job Title  : %{x}<br> Average Salary (USD) : %{y}"
    )  # Fixed hover template

    fig_4.show()  # Display the visuals


def employees_residence():  # This function gives salary average according to employee residence

    df_res = df.query(
        '(Job_title == "Data Engineer" or Job_title == "Data Analyst"'  # Loading necessary data
        ' or Job_title == "Data Scientist" or Job_title == "Machine Learning Engineer"'
        ' or Job_title == "BI Analyst") and (Employee_residence == "United States"'
        ' or Employee_residence == "Canada" or Employee_residence == "Germany"'
        ' or Employee_residence == "Spain" or Employee_residence == "United Kingdom")'
        ' and Experience_level != "Executive" '
    )

    df_res["salary_mean"] = df_res.groupby(
        ["Employee_residence", "Job_title", "Experience_level"]
    )["Salary_in_USD"].transform(
        "mean"
    )  # Creating column salary mean according to required grouping

    fig_5 = px.histogram(
        df_res,
        color_discrete_map={
            "United States": "rgb(27,158,119)",
            "United Kingdom": "rgb(166,118,29)"   # Giving custom colors as required and gave data frame
            "",
            "Canada": "rgb(102,102,102)",
        },
        y="Job_title",
        x="salary_mean",
        color="Employee_residence",  # Gave data to axes and color/legend
        facet_col="Experience_level",  # Creating multiple visuals as needed
        histfunc="avg",  # Giving "average" as the histogram function
        title="THE AVERAGE SALARY FOR VARIOUS EXPERIENCE LEVEL ACCORDING TO EMPLOYEE RESIDENCE",
    ).update_layout(
        legend_title="Employee Residence"
    )  # Updated legend layout

    for axis in fig_5.layout:
        if (
            type(fig_5.layout[axis]) == go.layout.YAxis
        ):  # Used For loop to remove the unnecessary axes titles
            fig_5.layout[axis].title.text = " "
        if type(fig_5.layout[axis]) == go.layout.XAxis:
            fig_5.layout[axis].title.text = " "

    fig_5.update_traces(
        hovertemplate="<br>Average Salary (USD): %{x}<br>Job Title: %{y}"
    )  # Fixed hover template

    fig_5.show()  # Displaying the visuals


employees_residence()
different_level()
salary_across_years()
salaries_vs_countries()
company_size()
