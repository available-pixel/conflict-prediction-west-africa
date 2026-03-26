from fpdf import FPDF

# ---------------------------
# PDF Setup with page numbers
# ---------------------------
class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", 'I', 8)
        self.cell(0, 10, f"Page {self.page_no()}", align='C')

pdf = PDF(format='A4', unit='mm')
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# ---------------------------
# Fonts
# ---------------------------
pdf.add_font('DejaVu', '', 'dejavu-sans/DejaVuSans.ttf', uni=True)
pdf.add_font('DejaVu', 'B', 'dejavu-sans/DejaVuSans-Bold.ttf', uni=True)
pdf.add_font('DejaVu', 'I', 'dejavu-sans/DejaVuSans-Oblique.ttf', uni=True)

# ---------------------------
# Title Page
# ---------------------------
pdf.set_font("DejaVu", 'B', 18)
pdf.multi_cell(0, 10, "Predicting Conflict Events in West Africa Using Climate, Socio-Economic, and Population Data", align='C')
pdf.set_font("DejaVu", 'I', 12)
pdf.set_x(0)
pdf.cell(0, 8, "A Data-Driven Machine Learning Study", align='C', ln=True)
pdf.ln(10)
pdf.set_font("DejaVu", 'B', 12)
pdf.cell(0, 8, "Author: Fadil Owolara ADELABOU", ln=True, align='C')
pdf.set_font("DejaVu", 'I', 12)
pdf.cell(0, 8, "Aspiring Data Scientist | AI & Social Impact Researcher", ln=True, align='C')
pdf.set_font("DejaVu", '', 12)
pdf.cell(0, 8, "Date: January 2026", ln=True, align='C')
pdf.ln(10)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())
pdf.ln(5)

# ---------------------------
# Function to add sections
# ---------------------------
def add_section(title, text):
    pdf.set_font("DejaVu", 'B', 14)
    pdf.cell(0, 8, title, ln=True)
    pdf.set_font("DejaVu", '', 12)
    pdf.multi_cell(0, 6, text)
    pdf.ln(4)

# ---------------------------
# Executive Summary
# ---------------------------
executive_summary_text = """This study presents a data-driven approach to predicting conflict events in West Africa by combining climate data, socio-economic indicators, and population metrics. Using a Random Forest Regressor, the model identifies key drivers of conflict, including population size and unemployment. Predictions for 2024 and 2027 provide actionable insights for policymakers and humanitarian organizations.

The research demonstrates how artificial intelligence can support decision-making, resource allocation, and early intervention strategies, contributing to the broader goal of promoting peace and stability in the region."""
add_section("Executive Summary", executive_summary_text)

# ---------------------------
# Abstract
# ---------------------------
abstract_text = """Conflicts in West Africa continue to pose significant challenges to human security, economic development, and regional stability. Accurately anticipating conflict events can support better policy planning and early intervention strategies.

This study applies machine learning techniques to predict the number of conflict events across West African countries. The model integrates climate variables (temperature and rainfall) with socio-economic indicators (GDP, unemployment, poverty rate) and population data.

A Random Forest Regressor is implemented to capture complex, non-linear relationships between these variables. The model is trained and evaluated using standard performance metrics, achieving a high level of predictive accuracy (R² ≈ 0.94).

Results indicate that population size and unemployment are the most influential predictors of conflict. The findings demonstrate the potential of data-driven approaches to support decision-making in conflict prevention and resource allocation."""
add_section("Abstract", abstract_text)
pdf.ln(10)

# ---------------------------
# Research Background
# ---------------------------
research_background_text = """West Africa has experienced persistent security challenges driven by a combination of political, economic, and environmental factors. Understanding the drivers of conflict is essential for developing effective prevention strategies.

Traditional conflict analysis often focuses on political or historical explanations. However, recent advances in data science provide new opportunities to analyze large-scale datasets and identify hidden patterns.

Climate conditions such as temperature and rainfall may influence resource availability, while socio-economic factors like unemployment and poverty can increase vulnerability to instability. Population growth further amplifies these pressures.

This research aims to provide a comprehensive, data-driven understanding of conflict dynamics in the region."""
add_section("Research Background", research_background_text)

# ---------------------------
# Timeline Section
# ---------------------------
timeline_text = """Timeline of Key Conflict Events (2015–2027):
- 2015: Significant unrest in Nigeria and Mali
- 2016–2017: Rising conflicts in Burkina Faso
- 2018: Escalation in northern Niger
- 2019–2020: Conflict spreads in Côte d’Ivoire and Ghana
- 2021–2023: Peaks in regional instability
- 2024: Model predicts high conflict in Burkina Faso, Nigeria
- 2027: Predicted trends indicate increasing risks in Togo and Mauritania"""
add_section("Timeline of Conflict Events", timeline_text)

# ---------------------------
# Research Questions
# ---------------------------
research_questions_text = """1. Can conflict events in West Africa be predicted using climate and socio-economic data?
2. Which factors contribute most significantly to conflict occurrence?
3. What is the impact of population growth on conflict risk?
4. How do climate variables influence instability?
5. How reliable are machine learning models in predicting conflict trends?"""
add_section("Research Questions", research_questions_text)

# ---------------------------
# Methodology
# ---------------------------
methodology_text = """1. Data Collection
   - Conflict data from ACLED
   - Socio-economic data from World Bank
   - Climate data from public datasets

2. Data Preparation
   - Cleaning and merging datasets
   - Handling missing values
   - Creating a unified dataset

3. Feature Selection
   - Population, GDP, unemployment, poverty rate
   - Average temperature and rainfall

4. Model Development
   - Random Forest Regressor

5. Model Evaluation
   - Train-test split
   - Metrics: R², MAE, RMSE

6. Prediction
   - Forecast conflict events for 2024 and 2027

7. Visualization
   - Interactive dashboard using Streamlit"""
add_section("Methodology", methodology_text)

# ---------------------------
# Results with Images
# ---------------------------
results_text = """The model demonstrates strong predictive performance:

- R² Score: 0.94
- MAE: 4.81
- RMSE: 7.69

Feature importance:

- Population: 33%
- Unemployment: 29%
- Temperature: 14%
- GDP: 11%
- Rainfall: 7%
- Poverty Rate: 6%

Predictions indicate higher conflict intensity in countries such as Burkina Faso and Nigeria."""
add_section("Results", results_text)
pdf.ln(60)

# Add screenshots
pdf.set_font("DejaVu", 'B', 12)
pdf.cell(0, 8, "Dashboard Screenshots", ln=True)
pdf.ln(2)
pdf.image("images/dashboard_overview.png", w=170)
pdf.ln(5)
pdf.image("images/custom_prediction.png", w=170)
pdf.ln(5)
pdf.image("images/conflict_map.png", w=170)
pdf.ln(5)
pdf.ln(10)

# ---------------------------
# Significance
# ---------------------------
significance_text = """The study highlights the potential of AI in addressing societal challenges.

By predicting conflict events, policymakers and humanitarian organizations can anticipate high-risk regions, allocate resources effectively, and design early intervention strategies."""
add_section("Significance", significance_text)

# ---------------------------
# Limitations
# ---------------------------
limitations_text = """- Data availability may affect accuracy
- Predictions do not capture severity or type
- Long-term forecasts subject to political/environmental uncertainties
- Potential overfitting despite validation"""
add_section("Limitations", limitations_text)

# ---------------------------
# Future Work
# ---------------------------
future_work_text = """- Incorporate governance and education indicators
- Use time-series or deep learning models
- Integrate real-time data feeds
- Expand analysis to other regions"""
add_section("Future Work", future_work_text)

# ---------------------------
# Conclusion
# ---------------------------
conclusion_text = """This study demonstrates that machine learning can effectively predict conflict events using a combination of climate, socio-economic, and population data.

The findings emphasize the importance of demographic and economic factors in driving conflict risk, contributing to AI for social good in West Africa."""
add_section("Conclusion", conclusion_text)

# ---------------------------
# References
# ---------------------------
references_text = """- ACLED Dataset: https://acleddata.com/
- World Bank Open Data: https://data.worldbank.org/
- Scikit-learn Documentation: https://scikit-learn.org/
- Streamlit: https://streamlit.io/"""
add_section("References", references_text)

# ---------------------------
# Footer
# ---------------------------
pdf.ln(10)
pdf.set_font("DejaVu", 'I', 11)
pdf.cell(0, 6, "Author: Fadil Owolara ADELABOU", ln=True, align='R')

# ---------------------------
# Save PDF
# ---------------------------
pdf.output("Conflict_Prediction_Research.pdf")
print("Upgraded PDF with screenshots and timeline generated successfully!")