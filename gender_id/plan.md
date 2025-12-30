# Project Plan: Survey Gender Question Research

## Overview

This project aims to research and compare how different large-scale surveys operationalize and ask about gender/sex. The goal is to create a systematic comparison of question wording, response options, skip logic, and methodological approaches across a diverse range of survey organizations (research, government, and NGO).

## Overall Goal

Create a comprehensive comparative analysis of how gender/sex is measured across major survey programs, documenting:
- Exact question wording
- Response options
- Whether questions measure "sex assigned at birth", "gender identity", or use a two-step SOGI (Sexual Orientation and Gender Identity) approach
- Skip logic and routing
- Mode of administration
- Institutional context and design constraints

## Target Surveys

### Primary Focus (Starting Set)
1. **General Social Survey (GSS)** - Research survey
2. **American National Election Studies (ANES)** - Research survey

### U.S. Government Surveys
3. **American Community Survey (ACS)** - U.S. Census Bureau
   - Canonical example of binary "sex" item as demographic classifier
   - High-impact survey with "Why we ask" documentation
   - Census has conducted/testing work on SOGI measurement

4. **Current Population Survey (CPS)** - Census Bureau & Bureau of Labor Statistics
   - Core U.S. labor force survey
   - Compare framing for labor-market stratification vs. political surveys

5. **Behavioral Risk Factor Surveillance System (BRFSS)** - CDC (state-administered)
   - Optional SOGI module with standardized transgender question wording
   - Important methodological note: Optional modules create cross-state/year heterogeneity

6. **National Health Interview Survey (NHIS)** - NCHS/CDC
   - Flagship health survey
   - Historically did not include adult gender identity (useful contrast with BRFSS)

### International NGO / UN System Surveys
7. **Demographic and Health Surveys (DHS)** - DHS Program (USAID-associated)
   - Globally dominant household survey program
   - Gender embedded structurally (separate women's and men's questionnaires, eligibility rules)

8. **Multiple Indicator Cluster Surveys (MICS)** - UNICEF
   - Global flagship focused on women/children/households
   - Shows how sex/gender is treated in international monitoring contexts

### Cross-National Academic / Research Consortia
9. **World Values Survey (WVS)**
   - Standard for cross-national values measurement
   - Includes respondent sex/gender variable plus extensive gender attitudes modules

10. **European Social Survey (ESS)**
    - Strong documentation and harmonization discipline
    - Useful for tracing exact wording, routing, and module design

## Methodology

### Comparative Coding Template

Create a structured comparison framework with one row per survey containing:
- **Survey name and organization**
- **Construct labels** (what the question claims to measure)
- **Exact item text** (verbatim question wording)
- **Response options** (all available choices)
- **Skip logic** (routing and conditional questions)
- **Mode** (phone, in-person, online, mixed)
- **Measurement approach** (sex assigned at birth, gender identity, two-step SOGI, binary sex, other)
- **Institutional context** (why this approach was chosen, constraints)
- **Year/version** (temporal variation in question wording)
- **Coverage notes** (optional modules, state-level variation, etc.)

## Project Steps

### Phase 1: Initial Research and Data Collection ✓ COMPLETED
- [x] Research GSS gender/sex question wording and documentation
  - [x] Locate current and historical question text
  - [x] Document response options and any skip logic
  - [x] Note any changes over time
  - [ ] Review actual GSS data to infer SEX recode logic (crosstab SEXBIRTH1 × SEXNOW1 × SEX) - *Future task*
  
- [x] Research ANES gender/sex question wording and documentation
  - [x] Locate current and historical question text
  - [x] Document response options and any skip logic
  - [x] Note any changes over time

- [x] Research U.S. Government surveys
  - [x] ACS: Review Census documentation and "Why we ask" materials
  - [x] CPS: Review labor force survey documentation
  - [x] BRFSS: Review SOGI module documentation and standardized wording
  - [x] NHIS: Review historical approach and any recent changes

- [x] Research International NGO/UN surveys
  - [x] DHS: Review questionnaire hub and survey description pages
  - [x] MICS: Review UNICEF model questionnaires

- [x] Research Cross-national academic surveys
  - [x] WVS: Review Wave 8+ questionnaire instruments
  - [x] ESS: Review source questionnaires and gender module documentation

- [x] Research Additional surveys
  - [x] Afrobarometer: Review questionnaire and documentation

### Phase 1.5: Develop Evaluation Criteria
- [x] Develop criteria for evaluating different SOGI measurement methods
- [x] Document evaluation criteria in `sogi_survey.md`

### Phase 2: Data Extraction and Coding
- [ ] Extract exact question wording for each survey
- [ ] Document response options systematically
- [ ] Note skip logic and routing patterns
- [ ] Identify measurement approach classification
- [ ] Document temporal changes (if applicable)
- [ ] Note methodological constraints and institutional context

### Phase 3: Comparative Analysis
- [ ] Create structured comparison table/database
- [ ] Identify patterns across survey types (government vs. research vs. NGO)
- [ ] Document evolution over time
- [ ] Note methodological innovations (e.g., two-step SOGI)
- [ ] Identify gaps and inconsistencies

### Phase 4: Documentation and Output
- [ ] Create comprehensive documentation of findings
- [ ] Develop visualizations comparing approaches
- [ ] Write summary report
- [ ] Create reusable coding template for future surveys

## Resources and Documentation Links

### U.S. Government Surveys
- **ACS**: Census.gov documentation, "Why we ask" explainer
- **CPS**: Census Bureau & BLS documentation
- **BRFSS**: CDC SOGI module documentation
- **NHIS**: NCHS/CDC archive documentation

### International NGO/UN Surveys
- **DHS**: DHS Program questionnaire hub and survey description pages
- **MICS**: UNICEF MICS model questionnaires

### Cross-National Academic Surveys
- **WVS**: World Values Survey Wave 8+ questionnaires
- **ESS**: European Social Survey source questionnaires and Round 11 documentation

## Current Status

**Status:** Initial research phase completed - documentation created for 11 surveys

**Last Updated:** 2024

**Completed Surveys:**
- ✓ GSS (General Social Survey)
- ✓ ANES (American National Election Studies)
- ✓ ACS (American Community Survey)
- ✓ CPS (Current Population Survey)
- ✓ BRFSS (Behavioral Risk Factor Surveillance System)
- ✓ NHIS (National Health Interview Survey)
- ✓ DHS (Demographic and Health Surveys)
- ✓ MICS (Multiple Indicator Cluster Surveys)
- ✓ WVS (World Values Survey)
- ✓ ESS (European Social Survey)
- ✓ Afrobarometer

**Documentation:** All survey documentation compiled in `sogi_survey.md`

## Notes and Considerations

1. **Methodological Heterogeneity**: Optional modules (like BRFSS SOGI) create cross-state/year variation that needs to be documented carefully.

2. **Temporal Changes**: Many surveys have evolved their gender/sex questions over time. Need to track both current and historical approaches.

3. **Institutional Context**: Understanding why different organizations choose different approaches (legal requirements, policy constraints, research goals) is important for interpretation.

4. **Structural Embedding**: Some surveys (like DHS) embed gender structurally through eligibility rules and separate questionnaires, not just through direct questions.

5. **Mode Effects**: Different modes of administration may affect question wording and response options.

## Next Steps

**Completed:**
- ✓ Initial research and documentation for 11 surveys completed
- ✓ Comprehensive documentation created in `sogi_survey.md`

**Future Tasks:**
1. Review actual GSS data to infer SEX recode logic (crosstab SEXBIRTH1 × SEXNOW1 × SEX)
2. Verify remaining question wordings and variable names from official questionnaires
3. Create structured comparison table/database (Phase 2)
4. Develop comparative analysis and visualizations (Phase 3)
5. Create summary report and reusable coding template (Phase 4)

