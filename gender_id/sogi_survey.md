# Survey Gender Identity Questions: Evaluation Criteria

## Criteria for Evaluating Gender Identity Measurement Methods

The following criteria should be used to evaluate how well different surveys measure sex and gender identity:

### 1. Classification Accuracy

**Criterion:** Collected data makes it possible to correctly classify cis men and women and trans men and women, and others who don't consider themselves to be in any of those categories.

**Rationale:** The measurement approach should enable accurate identification of five groups (cis men, cis women, trans men, trans women, none of those) with minimal misclassification.

### 2. Error Checking

**Criterion:** Questions should include error checking to avoid minimize error rates.

**Rationale:** Because cis people are a large majority, if even 1% of them are misclassified, the number of misclassified cis people could be comparable to the number of actual trans people. Error checking mechanisms (such as confirmation questions or consistency checks) help prevent misclassification of cisgender respondents.

### 3. Comprehensibility

**Criterion:** Questions should be understandable to all respondents.

**Rationale:** All respondents, regardless of education level, language proficiency, or familiarity with gender identity concepts, should be able to understand what is being asked.

### 4. Response Options Coverage

**Criterion:** All respondents should be able to choose a response that reflects their identity accurately.

**Rationale:** Response options should be inclusive and comprehensive enough that every respondent can find an option that accurately represents their identity, without being forced to choose an inaccurate option.

### 5. Clarity of Intent

**Criterion:** All respondents should be confident they are answering as intended—they should not have to infer intent.

**Rationale:** Question wording should be explicit and clear about what is being asked. Respondents should not need to guess or infer the survey's intent, which could lead to inconsistent interpretations and responses.

### 6. Respectful Wording

**Criterion:** Wording of questions should be respectful.

**Rationale:** Questions should use respectful, inclusive language that acknowledges the dignity of all respondents, regardless of their gender identity or expression.

### 7. Non-Partisan Language

**Criterion:** Wording of questions should avoid eliciting partisan attitudes.

**Rationale:** Questions should be framed neutrally to avoid triggering political or ideological responses that could affect data quality. The focus should be on accurate measurement, not political positioning.

---

# Survey Gender Identity Questions: General Social Survey (GSS)

## Survey Overview

**Organization:** National Opinion Research Center (NORC) at the University of Chicago  
**Survey Name:** General Social Survey (GSS)  
**Website:** https://gss.norc.org  
**Mode:** Face-to-face interviews (historically), with web-based collection introduced in 2021

## Historical Context

### Pre-2021 Approach

According to GSS documentation, **prior to 2021**, GSS respondents were **not asked to self-report their sex**. Instead, the GSS used a combination of:
- Interviewer observation
- Household rosters

This information was used to create the variable `SEX`, the standard male/female variable.

### 2021 Transition

In **2021**, as neither household roster nor interviewer observation were available (likely due to COVID-19 pandemic changes in data collection), respondents were **directly asked two questions**:
1. Their sex assigned at birth
2. Their current gender identity

These two items, `SEXBIRTH1` and `SEXNOW1`, are now the **standard way of measuring sex in the GSS**.

**Source:** [GSS 2021 Methodological Primer](https://sda.berkeley.edu/sdaweb/docs/gss21/DOC/2021XSECR1MethodologicalPrimer.pdf)

## Current Questions (2021-2024)

### Question 1: Sex Assigned at Birth

**Variable Name:** `SEXBIRTH1`

**Question Text (2024):**
> "What sex were you assigned at birth? (For example, on your birth certificate.)"

**Alternative wording (2021-2022):**
> "Was your sex recorded as male or female at birth?"

**Response Options:**
- Male
- Female

**Notes:**
- This question asks about sex assigned at birth (typically on birth certificate)
- Binary response options (male/female only)
- Used for web respondents; for other respondents, SEX may be based on interviewer observation
- Wording appears to have evolved slightly between 2021-2022 and 2024 versions

### Question 2: Current Gender Identity

**Variable Name:** `SEXNOW1`

**Question Text (2024):**
> "Do you currently describe yourself as male, female, or transgender?"

**Alternative wording (2021-2022):**
> "Do you describe yourself as male, female, or transgender?"

**Response Options:**
1. Male
2. Female
3. Transgender
4. None of these

**Notes:**
- This question asks about current gender identity
- Includes transgender as an explicit option
- "None of these" option provides flexibility for non-binary or other gender identities
- 2024 version adds "currently" to the question wording

### Derived Variable: SEX

**Variable Name:** `SEX`

**Derivation:**
- For **web respondents**: Derived from responses to `SEXBIRTH1` and `SEXNOW1`
- For **other respondents**: Based on interviewer observation (maintaining backward compatibility)

**Purpose:** Maintains consistency with historical GSS data using the binary SEX variable

**Recode Logic - NOT DOCUMENTED:**

According to the 2024 GSS codebook: *"For web respondents, SEX is based on a recode of SEXBIRTH1 and SEXNOW2, and for other respondents, based on observation."*

**Important Notes:**
1. **Variable Name Discrepancy:** The 2024 codebook references `SEXNOW2` (not `SEXNOW1`). This may indicate:
   - A typo in the codebook
   - A different variable name in some years
   - Multiple versions of the question
   - **Needs verification**

2. **Recode Logic Not Provided:** The codebook does **not** specify:
   - The exact rules for combining `SEXBIRTH1` and `SEXNOW1`/`SEXNOW2` to create `SEX`
   - How cases where `SEXNOW1` = 3 (Transgender) or 4 (None of these) are handled
   - Whether `SEXBIRTH1` or `SEXNOW1` takes precedence in the recode
   - Any conditional logic or special cases

3. **Interviewer Observation Instructions Not Documented:** The codebook does **not** specify:
   - How interviewers are instructed to determine sex based on observation
   - What criteria or guidelines interviewers use
   - Whether there are standardized protocols for interviewer coding

**Response Options (from available documentation):**
- `SEXBIRTH1`: 1 = Male, 2 = Female
- `SEXNOW1`: 1 = Male, 2 = Female, 3 = Transgender, 4 = None of these
- `SEX`: 1 = Male, 2 = Female (binary, for backward compatibility)

**Documentation Gaps:**
- Exact recode algorithm/logic for web respondents
- Interviewer observation protocols and instructions
- Handling of non-binary responses (Transgender, None of these)
- Resolution of discrepancies between SEXBIRTH1 and SEXNOW1
- Variable name clarification (SEXNOW1 vs SEXNOW2)

**Potential Sources for Missing Information:**
- GSS Methodological Report No. 56 (referenced for trend analysis)
- GSS interviewer training materials or protocols
- Direct consultation with GSS/NORC
- Analysis of actual GSS data to infer recode patterns

**Source:** [GSS 2024 Codebook](https://gss.norc.org/content/dam/gss/get-documentation/pdf/codebook/GSS%202024%20Codebook.pdf) (page 44)

## 2024 Update

**Status:** Methodology remains consistent with 2021 implementation

**Key Points:**
- The two-step approach (`SEXBIRTH1` and `SEXNOW1`) continues unchanged in 2024
- The `SEX` variable remains a composite of these two responses
- **Methodological Report No. 56** is referenced in the 2024 codebook for trend analysis involving the SEX variable (important for researchers analyzing trends across the 2021 break point)
- The 2024 codebook notes (page 44): "Prior to 2021, SEX was interviewer coded. In 2021, SEX is a composite of SEXBIRTH1 and SEXNOW1."
- **2024 codebook states:** "For web respondents, SEX is based on a recode of SEXBIRTH1 and SEXNOW2, and for other respondents, based on observation."
- **Note:** The codebook references `SEXNOW2` (not `SEXNOW1`) - this discrepancy needs clarification

**Question Wording Verification:**
- **SEXBIRTH1 (2024):** "What sex were you assigned at birth? (For example, on your birth certificate.)"
- **SEXNOW1 (2024):** "Do you currently describe yourself as male, female, or transgender?"

**Additional 2024 Content:**
- The 2024 GSS includes a module on gender scales, involving self-administered questionnaires where respondents assess their identification with femininity and masculinity on seven-point scales

**Source:** [GSS 2024 Codebook](https://gss.norc.org/content/dam/gss/get-documentation/pdf/codebook/GSS%202024%20Codebook.pdf)

## Earlier Two-Step Approach (2018)

**Note:** There appears to have been an earlier iteration of two-step gender questions in 2018 with different wording:

### 2018 Version - Question 1: Sex Assigned at Birth

**Question Text:**
> "What sex were you assigned at birth? (For example, on your birth certificate)"

**Response Options:**
- Female
- Male
- Intersex
- No answer

### 2018 Version - Question 2: Current Gender Identity

**Question Text:**
> "What is your current gender?"

**Response Options:**
- Woman
- Man
- Transgender
- A gender not listed here
- No answer

**Differences from Current Version:**
- More detailed wording ("assigned at birth" with birth certificate example)
- Included "Intersex" as an option for sex assigned at birth
- Used "Woman/Man" instead of "Female/Male" for current gender
- Included "A gender not listed here" as an explicit option
- Included "No answer" option

**Source:** [Stanford Gender News](https://gender.stanford.edu/news/more-inclusive-gender-questions-added-general-social-survey)



## Measurement Approach Classification

**Current Approach (2021-2024):** Two-step Gender Identity approach
- Step 1: Sex assigned at birth (`SEXBIRTH1`)
- Step 2: Current gender identity (`SEXNOW1`)
- **Note:** Methodology has remained stable since 2021 implementation

**Historical Approach (pre-2021):** Interviewer observation/household roster (binary sex only)

## Methodological Notes

1. **Mode Effects:** The shift to direct questions in 2021 was necessitated by changes in data collection mode (web-based vs. in-person)

2. **Backward Compatibility:** The derived `SEX` variable maintains compatibility with historical GSS data

3. **Evolution:** The questions have evolved from the 2018 version to the current 2021+ version, with some simplification of response options

4. **Coverage:** Questions are asked of all respondents (not an optional module)

## Documentation Gaps

**Important:** The GSS codebook does not provide complete documentation for the SEX variable derivation:

1. **Recode Logic Not Documented:** While the 2024 codebook states that SEX is "based on a recode of SEXBIRTH1 and SEXNOW2" for web respondents, it does not specify:
   - The exact recode algorithm or rules
   - How to handle cases where SEXNOW1 = 3 (Transgender) or 4 (None of these)
   - Whether SEXBIRTH1 or SEXNOW1 takes precedence
   - Any conditional logic or edge cases

2. **Interviewer Instructions Not Documented:** The codebook states that for non-web respondents, SEX is "based on observation," but does not specify:
   - How interviewers are trained or instructed to determine sex
   - What criteria or protocols are used
   - Whether there are standardized guidelines

3. **Variable Name Discrepancy:** The 2024 codebook references `SEXNOW2` while other documentation and data files use `SEXNOW1` - this needs clarification.

**Implications for Researchers:**
- Researchers cannot fully understand how the SEX variable is constructed
- Trend analysis across the 2021 break point may be affected by unknown recode logic
- Replication and transparency are limited without documented procedures
- May need to use SEXBIRTH1 and SEXNOW1 directly rather than relying on the derived SEX variable

## Documentation Sources

1. **GSS 2021 Methodological Primer:** https://sda.berkeley.edu/sdaweb/docs/gss21/DOC/2021XSECR1MethodologicalPrimer.pdf

2. **GSS 2022 Codebook:** https://gss.norc.org/content/dam/gss/get-documentation/pdf/codebook/GSS%202022%20Codebook.pdf

3. **GSS 2024 Codebook:** https://gss.norc.org/content/dam/gss/get-documentation/pdf/codebook/GSS%202024%20Codebook.pdf

4. **GSS Methodological Report No. 56:** Referenced in 2024 codebook for trend analysis of SEX variable (break point at 2021)

5. **GSS Questionnaires:** https://gss.norc.org/us/en/gss/get-documentation/questionnaires.html

6. **GSS Data Explorer:** https://gssdataexplorer.norc.org/

## Evaluation

### 1. Classification Accuracy
**Rating:** ⚠️ **Partial** - Can classify cis men, cis women, and some trans people, but limited for non-binary identities
- Two-step approach enables identification of cis men, cis women, and trans people (when SEXBIRTH1 ≠ SEXNOW1)
- "None of these" option provides some coverage for non-binary identities, but may not be comprehensive
- Binary sex assigned at birth (no intersex option in current version) limits classification

### 2. Error Checking
**Rating:** ❌ **Poor** - No explicit error checking mechanisms
- No confirmation question for cisgender respondents
- No consistency checks between SEXBIRTH1 and SEXNOW1
- Undocumented recode logic for SEX variable creates uncertainty about error rates
- Risk: 1% error rate among cis people could produce false positives comparable to actual trans population

### 3. Comprehensibility
**Rating:** ⚠️ **Moderate** - Some clarity issues
- "Was your sex recorded as male or female at birth?" is reasonably clear
- "Do you currently describe yourself as male, female, or transgender?" may be unclear:
  - "Transgender" as a standalone category may confuse respondents (transgender is an identity, not a gender)
  - Respondents may not understand what "transgender" means in this context
- "None of these" is vague and doesn't explain what other options might be

### 4. Response Options Coverage
**Rating:** ⚠️ **Partial** - Some gaps in coverage
- Binary sex at birth excludes intersex people (was included in 2018 version)
- "Transgender" as a category may not accurately represent trans men and trans women
- "None of these" provides some flexibility but is vague
- Non-binary respondents may struggle to find accurate representation

### 5. Clarity of Intent
**Rating:** ⚠️ **Moderate** - Some ambiguity
- Purpose of two-step approach may not be clear to respondents
- "Transgender" as a response option may be interpreted differently by different respondents
- Respondents may not understand why both questions are asked
- Undocumented recode logic means even researchers can't be certain of intent

### 6. Respectful Wording
**Rating:** ✅ **Good** - Generally respectful
- Uses "sex assigned at birth" terminology (in 2024 version)
- "Currently describe yourself" acknowledges self-identification
- Generally neutral and non-judgmental language

### 7. Non-Partisan Language
**Rating:** ✅ **Good** - Neutral language
- Questions use neutral, factual language
- No obvious partisan framing
- Focus on demographic classification rather than political positioning

## Next Steps

- [x] Check 2024 codebook for updates
- [ ] **Clarify SEXNOW1 vs SEXNOW2 variable name discrepancy in 2024 codebook**
- [ ] **Obtain exact SEX recode logic** (not provided in codebook - may require GSS Methodological Report No. 56, interviewer protocols, or direct consultation with GSS/NORC)
- [ ] **Obtain interviewer observation instructions/protocols** (not documented in codebook)
- [ ] Verify exact wording from official GSS 2022/2023 questionnaires (to confirm wording evolution)
- [ ] Confirm response option codes and values from 2024 codebook
- [ ] Review GSS Methodological Report No. 56 for trend analysis guidance and recode logic
- [ ] Check for any skip logic or routing
- [ ] Document any changes between 2021, 2022, 2023, and 2024
- [ ] Compare with historical SEX variable coding
- [ ] **Review actual GSS data to infer SEX recode logic** (create crosstab of SEXBIRTH1 × SEXNOW1 × SEX to empirically determine recode rules)

## Comparison Notes for Future Analysis

- **Binary vs. Non-binary:** Current version uses binary options for sex at birth, but includes transgender and "none of these" for current gender
- **Terminology:** Uses "male/female" rather than "man/woman" in current version (simplified from 2018)
- **Intersex:** Not included in current version (was in 2018 version)
- **No answer option:** Not explicitly listed in current version (was in 2018)

---

# Survey Gender Identity Questions: American National Election Studies (ANES)

## Survey Overview

**Organization:** American National Election Studies (ANES)  
**Survey Name:** ANES Time Series Study  
**Website:** https://electionstudies.org  
**Mode:** Mixed mode (web, phone, in-person interviews)

## Current Questions (2024)

### Question 1: Sex

**Variable Name:** `VCF0148a` (2024 Full Release - derived from raw variable `V241550`)

**Question Text:**
> "What is your sex?"

**Response Options:**
1. Male
2. Female

**Notes:**
- Binary response options only
- Self-reported sex (not "sex assigned at birth")
- Separate from gender identity question
- **Note:** Variable name `V241550PRE` was from preliminary release; full release uses `VCF0148a` (derived from `V241550`)

### Question 2: Gender Identity

**Variable Name:** `VCF0148x` (2024 Full Release - derived from `V241551`)

**Question Text:**
> "What is your gender?"

**Response Options:**
1. Man
2. Woman
3. Nonbinary
4. Something else (specify)

**Notes:**
- Includes non-binary option
- "Something else" option allows open-ended specification
- Follow-up question allows respondents to specify their gender identity if they select "Something else"
- Uses "Man/Woman" terminology (different from "Male/Female" in sex question)
- **Note:** Variable name `V241551PRE` was from preliminary release; full release uses `VCF0148x` (derived from `V241551`)

### Question 3: Transgender Identification

**Variable Name:** `V241552` (2024 Full Release - asked directly)

**Question Text:**
> "Do you consider yourself to be transgender?"

**Response Options:**
1. Yes
2. No

**Notes:**
- Direct question about transgender identity
- Binary yes/no response
- Asked separately from gender identity question
- **Important:** ANES explicitly does NOT infer transgender status from sex × gender identity responses
- Respondents may identify as transgender regardless of how they respond to the sex or gender questions
- Examples:
  - A respondent may answer "Nonbinary" and "No, not transgender"
  - A respondent may answer "Man" and "Yes, transgender"
  - A respondent may answer "Male" (sex) and "Woman" (gender) and also "No, not transgender"
- This stands in contrast to GSS, which derives transgender status implicitly by comparing sex assigned at birth to current gender


## Measurement Approach Classification

**Current Approach (2024):** A variant of a two-step GI measure plus a separate transgender item:
- Step 1: Sex (self-reported, binary: Male/Female)
- Step 2: Gender identity (4 categories: Man/Woman/Nonbinary/Something else)
- Supplement: Direct transgender identity question (binary: Yes/No)

**Key Characteristics:**
- **Modified two-step GI approach** (variant of canonical two-step GI)
- Step 1 uses **self-reported sex** (not "sex assigned at birth" like GSS)
- This is an important conceptual difference from GSS:
  - **GSS Step 1:** Sex assigned at birth
  - **ANES Step 1:** Self-reported sex
- Transgender status is asked directly as a separate question (not inferred)
- Gender identity question includes non-binary option
- **Classification:** Most researchers would classify this as a modified two-step GI measure

## 2022 Pilot Study

The ANES 2022 Pilot Study included gender questions with different variable structures:

### Gender (2-category)

**Variable Name:** `gender`

**Response Options:**
1. Male
2. Female

### Gender (4-category)

**Variable Name:** `gender4`

**Response Options:**
1. Man
2. Woman
3. Non-binary
4. Other

**Notes:**
- Pilot study tested both 2-category and 4-category versions
- 4-category version similar to 2024 approach but with "Other" instead of "Something else, please specify"

## Historical Context

**Timeline:**
- **2016 ANES:** No gender identity or transgender items
- **2020 ANES Time Series:** First year that ANES introduced:
  - A gender item ("Man/Woman/Other")
  - A transgender identity module
- **2022 Pilot Study:** Tested expanded GI items (see section below)
- **2024 Time Series:** Full implementation of the 4-category gender identity item

**Note:** ANES did not introduce these questions in 2024; they date to 2020. The 2024 description reflects the current instrument.

## Methodological Notes

1. **Modified Two-Step GI:** ANES uses a variant of a two-step GI design (sex + gender identity) with an added direct transgender question. Key difference from GSS: ANES Step 1 = self-reported sex (not "sex assigned at birth")

2. **Direct Transgender Question:** ANES asks about transgender identity directly as a separate question and explicitly does NOT infer transgender status from sex × gender identity responses. This prevents classification errors that can occur when inferring transgender status.

3. **Why Separate Transgender Question:** ANES states in the 2024 user guide that "Respondents may identify as transgender regardless of how they respond to the sex or gender questions." This means:
   - A respondent may answer "Nonbinary" and "No, not transgender"
   - A respondent may answer "Man" and "Yes, transgender"
   - A respondent may answer "Male" (sex) and "Woman" (gender) and also "No, not transgender"
   - This stands in contrast to GSS, which derives transgender status implicitly by comparing sex assigned at birth to current gender

4. **Terminology:** Uses "Man/Woman" for gender identity and "Male/Female" for sex, maintaining a distinction in terminology

5. **Non-binary Inclusion:** Explicitly includes "Nonbinary" as a response option for gender identity

6. **Open-ended Options:** Gender question includes "Something else (specify)" option for open-ended responses

## Documentation Sources

1. **ANES 2024 Time Series Study Full Release Codebook:** https://sda.berkeley.edu/sdaweb/docs/anes2024full/DOC/hcbk.htm

2. **ANES 2024 Time Series Study Preliminary Release Codebook:** https://sda.berkeley.edu/sdaweb/docs/anes2024prelim/DOC/hcbk0023.htm

3. **ANES 2024 User Guide and Codebook:** https://electionstudies.org/wp-content/uploads/2025/02/anes_timeseries_2024_userguidecodebook_20250219.pdf

4. **ANES 2022 Pilot Study User Guide and Codebook:** https://electionstudies.org/wp-content/uploads/2022/12/anes_pilot_2022_userguidecodebook_20221214.pdf

5. **ANES Official Website:** https://electionstudies.org

## Evaluation

### 1. Classification Accuracy
**Rating:** ✅ **Good** - Can classify all five groups
- Separate sex and gender identity questions enable identification of cis men, cis women, trans men, trans women
- "Nonbinary" option explicitly covers non-binary identities
- "Something else, please specify" provides additional coverage
- Direct transgender question provides additional classification pathway

### 2. Error Checking
**Rating:** ⚠️ **Moderate** - Some protection but not comprehensive
- Direct transgender question provides cross-check against sex/gender relationship
- ANES explicitly states it does NOT infer transgender status from sex × gender identity, reducing misclassification risk
- However, no explicit confirmation question for cisgender respondents
- Risk of misclassification remains, though lower than surveys that infer transgender status

### 3. Comprehensibility
**Rating:** ✅ **Good** - Generally clear
- "What is your sex?" is straightforward
- "What is your gender?" is clear and uses familiar terminology
- "Do you consider yourself to be transgender?" is direct and understandable
- "Nonbinary" is a recognized term
- "Something else, please specify" allows for clarification

### 4. Response Options Coverage
**Rating:** ✅ **Good** - Comprehensive coverage
- Sex question: Male/Female (binary, but appropriate for sex)
- Gender question: Man/Woman/Nonbinary/Something else - covers most identities
- Transgender question: Yes/No - direct and clear
- "Something else, please specify" provides flexibility for additional identities

### 5. Clarity of Intent
**Rating:** ✅ **Good** - Clear purpose
- Three separate questions make the purpose clear
- Direct transgender question eliminates need to infer intent
- ANES documentation explicitly states purpose (does not infer transgender status)
- Respondents understand what is being asked

### 6. Respectful Wording
**Rating:** ✅ **Good** - Respectful language
- Uses "Man/Woman" for gender (more respectful than "Male/Female")
- "Consider yourself to be" acknowledges self-identification
- "Nonbinary" uses recognized, respectful terminology
- Generally inclusive and respectful language

### 7. Non-Partisan Language
**Rating:** ✅ **Good** - Neutral language
- Questions use neutral, factual language
- No obvious partisan framing
- Focus on accurate demographic classification

## Next Steps

- [x] Verify exact question wording from official 2024 full release codebook
- [x] Document historical introduction of these questions (introduced in 2020)
- [x] Verify variable names in full release (updated to VCF0148a, VCF0148x, V241552)
- [ ] Check for any skip logic or routing between questions
- [ ] Document any changes between 2020, 2022 pilot, and 2024 time series
- [ ] Compare response distributions and patterns
- [ ] Review 2020 ANES implementation for comparison

---

# Survey Gender Identity Questions: American Community Survey (ACS)

## Survey Overview

**Organization:** U.S. Census Bureau  
**Survey Name:** American Community Survey (ACS)  
**Website:** https://www.census.gov/programs-surveys/acs  
**Mode:** Mixed mode (mail, online, phone, in-person interviews)  
**Sample Size:** Over 3.5 million households annually

## Current Questions (2024)

### Question 1: Sex

**Question Text:**
> "What is this person's sex?"

**Response Options:**
- Male
- Female

**Notes:**
- Binary response options only
- Asked for each person in the household
- Used to create statistics about males and females
- Aids in planning and funding government programs
- Ensures equitable service delivery
- **Historical approach:** This binary sex question has been the standard approach in ACS

## Measurement Approach Classification

**Current Approach (2024):** Binary sex question only
- Single question asking "What is this person's sex?"
- Binary response options (Male/Female)
- **Not a two-step GI approach** (currently)
- No gender identity question
- No sexual orientation question

**Key Characteristics:**
- Canonical example of a high-impact survey using binary "sex" item as demographic classifier
- Used for demographic statistics and program planning
- No distinction between sex and gender identity
- No non-binary or transgender options

## Planned Changes: Gender Identity Questions (Testing 2024, Implementation 2027)

### Testing Phase (2024)

The Census Bureau initiated testing of Gender Identity questions in the ACS in 2024:
- **Test sample:** 480,000 households
- **Testing methods:** Mail surveys (August 2024), with plans to expand to in-person interviews (spring 2025)

### Proposed Two-Step GI Questions

**Question 1: Sex Assigned at Birth**

**Proposed Question Text:**
> "What sex was [Name] assigned at birth?"

**Proposed Response Options:**
- Male
- Female

**Question 2: Current Gender Identity**

**Proposed Question Text:**
> "What is [Name]'s current gender?"

**Proposed Response Options:**
- Male
- Female
- Transgender
- Nonbinary
- Write-in option (for other terms)

**Notes:**
- Asked for individuals aged 15 and older
- Two-step approach: sex assigned at birth + current gender identity
- Includes transgender and nonbinary options
- Write-in option for other gender identities


### Implementation Timeline

- **2024:** Testing phase initiated
- **2027:** Planned full implementation in ACS
- **2028:** Data from GI questions expected to be available

## Historical Context

**Traditional Approach:**
- ACS has historically used a binary sex question ("What is this person's sex?") with Male/Female options
- This has been the standard demographic classifier for creating statistics about males and females
- Used for planning and funding government programs

**Recent Developments:**
- **September 2023:** Census Bureau proposed testing GI questions in ACS
- **2024:** Testing phase initiated with 480,000 households
- **2027:** Planned implementation of GI questions
- **June 2022:** Executive Order 14075 directed OMB to develop best practices for collecting Gender Identity data in federal statistics

## Policy Context

**Executive Order 14075 (June 2022):**
- Directed the Office of Management and Budget to develop best practices for collecting Gender Identity data in federal statistics
- Supported the inclusion of GI questions in federal surveys

**Executive Order 14168 (January 2025):**
- Defined sex as strictly biological and unchangeable
- Framed gender identity as a subjective sense of self
- Directed federal entities to recognize only binary definitions of sex (male or female) on official documents and policies
- Led Census Bureau to seek permission to eliminate gender identity questions from the Household Trends and Outlook Pulse Survey
- **Impact:** May affect implementation of GI questions in ACS, though testing continues

## Methodological Notes

1. **High-Impact Survey:** ACS is a canonical example of a high-impact survey that has historically used a binary "sex" item as a demographic classifier

2. **Testing Approach:** The Census Bureau is testing GI questions to refine:
   - Question wording
   - Response options
   - Question placement within the survey
   - Methods for protecting confidentiality (e.g., flashcards during in-person interviews, numbered response options)

3. **Confidentiality Measures:** Proposed measures to protect privacy include:
   - Using flashcards during in-person interviews
   - Providing numbered response options
   - Ensuring data confidentiality

4. **Canonical Status:** ACS is often referenced as a standard for how sex/gender is measured in general population surveys, making its evolution to GI questions significant

5. **Census Bureau Research:** The Census Bureau has conducted/testing work on GI measurement, which is helpful for understanding what's being considered and why

## Documentation Sources

1. **Census Bureau ACS Website:** https://www.census.gov/programs-surveys/acs

2. **Census Bureau "Why We Ask" Documentation:** (To be located - mentioned in plan as providing explainer for ACS sex question)

3. **Congressional Research Service Report:** https://www.congress.gov/crs-product/IN12342

4. **Census Bureau GI Research Presentations:** Available through Census Bureau and UNECE documentation

## Comparison with GSS and ANES

**Key Differences:**
- **ACS (current):** Binary sex question only, no gender identity question
- **GSS:** Two-step approach (sex assigned at birth + current gender identity)
- **ANES:** Modified two-step approach (self-reported sex + gender identity + direct transgender question)
- **ACS (planned):** Will use two-step approach similar to GSS (sex assigned at birth + current gender identity)

**Status:**
- ACS is currently the most basic approach (binary sex only)
- Planned evolution to two-step GI approach by 2027
- Policy context (Executive Order 14168) may affect implementation

## Evaluation

**Note:** Evaluation based on proposed/planned GI questions (testing 2024, implementation 2027). Current implementation (binary sex only) does not collect gender identity.

### Proposed Two-Step GI Questions (2027)

### 1. Classification Accuracy
**Rating:** ⚠️ **To be determined** - Depends on final implementation
- Proposed two-step approach (sex assigned at birth + current gender identity) should enable classification
- Proposed options include: Male/Female/Transgender/Nonbinary/Write-in
- Coverage depends on final response options

### 2. Error Checking
**Rating:** ❓ **Unknown** - Not yet specified
- Testing phase may include error checking mechanisms
- Final implementation details not yet available

### 3. Comprehensibility
**Rating:** ⚠️ **To be determined** - Depends on final wording
- Proposed questions appear clear, but final wording may differ
- Testing phase should identify comprehensibility issues

### 4. Response Options Coverage
**Rating:** ⚠️ **To be determined** - Depends on final options
- Proposed options (Male/Female/Transgender/Nonbinary/Write-in) provide good coverage
- Final implementation may differ

### 5. Clarity of Intent
**Rating:** ⚠️ **To be determined** - Depends on final implementation
- Two-step approach should be clear, but depends on final wording and instructions

### 6. Respectful Wording
**Rating:** ⚠️ **To be determined** - Depends on final wording
- Proposed wording appears respectful, but final implementation may differ

### 7. Non-Partisan Language
**Rating:** ⚠️ **To be determined** - Depends on final wording
- Policy context (Executive Order 14168) may affect language choices
- Final wording may be influenced by political considerations

## Next Steps

- [ ] Locate Census Bureau "Why we ask" documentation for ACS sex question
- [ ] Verify exact wording of proposed GI questions from official Census Bureau documentation
- [ ] Document any changes to implementation timeline due to Executive Order 14168
- [ ] Review Census Bureau testing results and methodology reports
- [ ] Check for any updates on 2027 implementation status
- [ ] Document variable names for current sex question and proposed GI questions

---

# Survey Gender Identity Questions: Current Population Survey (CPS)

## Survey Overview

**Organization:** U.S. Census Bureau (data collection) for Bureau of Labor Statistics (BLS)  
**Survey Name:** Current Population Survey (CPS)  
**Website:** https://www.bls.gov/cps  
**Mode:** Mixed mode (phone, in-person interviews)  
**Frequency:** Monthly survey  
**Purpose:** Primary source of labor force statistics for the U.S. population

## Current Questions (2024)

### Question 1: Sex

**Question Text:**
> "What is [NAME]'s sex?"

**Response Options:**
- Male
- Female

**Notes:**
- Binary response options only
- Asked for each person in the household
- **Interviewer instructions:** Interviewers are instructed to ask this question "only if necessary"
- Used for labor force statistics and demographic analysis
- No gender identity question
- No sexual orientation question

## Measurement Approach Classification

**Current Approach (2024):** Binary sex question only
- Single question asking "What is [NAME]'s sex?"
- Binary response options (Male/Female)
- **Not a two-step GI approach**
- No gender identity question
- No sexual orientation question

**Key Characteristics:**
- Core U.S. labor force survey
- Widely used in policy research
- Often operationalizes demographics in ways that become "defaults" across applied social science
- Used for labor-market stratification analysis
- Interviewer-administered (not self-administered)

## Historical Context

**Traditional Approach:**
- CPS has historically used a binary sex question
- Used for creating labor force statistics by sex
- Standard demographic variable for labor market analysis

**Feasibility Study (2017):**
- Bureau of Labor Statistics assessed the feasibility of adding gender identity questions to the CPS
- Conducted focus groups with transgender individuals to explore this addition
- **Result:** Gender identity questions have not been implemented to date
- Study documented in BLS research papers (Technical Paper 77)

## Methodological Notes

1. **Labor Force Focus:** CPS is the core U.S. labor force survey, making its demographic operationalization influential in policy research

2. **Interviewer Instructions:** Interviewers are instructed to ask the sex question "only if necessary," suggesting that sex may be determined through observation or other means when possible

3. **Comparison with Political Surveys:** The plan notes comparing how CPS frames sex/gender for labor-market stratification vs. how political surveys (GSS/ANES) do it

4. **Influence on Applied Social Science:** CPS often sets defaults for how demographics are operationalized across applied social science research

5. **No GI Questions:** Unlike ACS (which is testing GI questions), CPS does not currently include gender identity or sexual orientation questions

6. **Feasibility Study:** The 2017 BLS study indicates awareness of the need for gender identity questions, but implementation has not occurred

## Documentation Sources

1. **BLS CPS Website:** https://www.bls.gov/cps

2. **BLS CPS Definitions:** https://www.bls.gov/cps/definitions.htm

3. **CPS Technical Documentation:** https://www.census.gov/programs-surveys/cps/technical-documentation/complete.22.html

4. **BLS Research Paper (2017):** Assessment of feasibility of adding gender identity questions to CPS
   - https://www.bls.gov/osmr/research-papers/2017/html/st170200.htm
   - https://www.bls.gov/osmr/research-papers/2017/st170200.htm

5. **Census Bureau CPS Website:** https://www.census.gov/programs-surveys/cps

## Comparison with Other Surveys

**Key Differences:**
- **CPS (current):** Binary sex question only, interviewer-administered, "only if necessary" instruction
- **GSS:** Two-step approach (sex assigned at birth + current gender identity)
- **ANES:** Modified two-step approach (self-reported sex + gender identity + direct transgender question)
- **ACS (current):** Binary sex question only, but testing GI questions for 2027 implementation
- **ACS (planned):** Will use two-step approach similar to GSS

**Status:**
- CPS is currently the most basic approach among the surveys reviewed
- No plans announced for GI question implementation (unlike ACS)
- 2017 feasibility study suggests awareness but no action taken

## Next Steps

- [ ] Review BLS 2017 feasibility study in detail for specific findings and recommendations
- [ ] Verify exact interviewer instructions and protocols for sex question
- [ ] Check for any recent developments or announcements about GI questions in CPS
- [ ] Document variable names for sex question
- [ ] Review CPS Technical Paper 77 for detailed methodology
- [ ] Compare CPS approach with ACS approach (both Census Bureau surveys)

---

# Survey Gender Identity Questions: Behavioral Risk Factor Surveillance System (BRFSS)

## Survey Overview

**Organization:** Centers for Disease Control and Prevention (CDC)  
**Survey Name:** Behavioral Risk Factor Surveillance System (BRFSS)  
**Website:** https://www.cdc.gov/brfss  
**Mode:** Telephone interviews (landline and cellular)  
**Frequency:** Annual survey  
**Sample Size:** More than 400,000 adult interviews annually  
**Administration:** State-administered (CDC coordinates)

## Current Questions (2024)

### Core Question: Sex

**Question Text:**
> "Are you..."

**Response Options:**
- Male
- Female

**Interviewer Note:**
> "We ask this question to determine which health related questions apply to each respondent. For example, persons who report males as their sex at birth might be asked about prostate health issues."

**Notes:**
- Binary response options
- Part of core BRFSS questionnaire (asked by all states)
- Used for demographic analysis and health statistics
- **Interviewer note provided:** The questionnaire includes an explanatory note for interviewers, but it is **not clear whether this note is meant to be read to the respondent** or is for interviewer reference only
- The note references "sex at birth" terminology, which may indicate the intended conceptual framework for the question

### Optional Gender Identity Module (2014-present)

The BRFSS includes an **optional Gender Identity module** (note: the module also includes sexual orientation questions, but this document focuses on gender identity) that states can choose to include in their surveys.


#### Question 2: Gender Identity (Transgender)

**Question Text:**
> "Do you consider yourself to be transgender?"

**Response Options:**
1. Yes, Transgender, male-to-female
2. Yes, Transgender, female-to-male
3. Yes, Transgender, gender nonconforming
4. No
7. Don't know/not sure
9. Refused

**Interviewer Note/Clarification:**
> "Some people describe themselves as transgender when they experience a different gender identity from their sex at birth. For example, a person born into a male body, but who feels female or lives as a woman would be transgender. Some transgender people change their physical appearance so that it matches their internal gender identity."

**Notes:**
- Direct question about transgender identity
- Includes three transgender subcategories (male-to-female, female-to-male, gender nonconforming)
- Includes "Don't know" and "Refused" options
- Interviewer note provides clarification/definition
- Part of optional GI module

## Measurement Approach Classification

**Current Approach:** Core binary sex question + optional GI module
- **Core:** Binary sex question (asked by all states)
- **Optional Module:** Sexual orientation question + transgender identity question
- **Not a two-step GI approach** (does not ask "sex assigned at birth" separately)
- Transgender question asks directly about transgender identity with subcategories

**Key Characteristics:**
- **Optional module** creates cross-state/year heterogeneity (important methodological consideration)
- States choose whether to include GI module
- Standardized transgender question wording (explicitly documented)
- Direct transgender question (not inferred from sex/gender relationship)
- Includes transgender subcategories (male-to-female, female-to-male, gender nonconforming)

## Historical Context

**Development:**
- **2013:** CDC developed optional GI module for BRFSS
- **2014:** States could begin including GI module in their surveys
- **2014:** 19 states included GI module
- **2016:** 28 states, including District of Columbia and territories, included GI module
- **2017:** 33 states, including District of Columbia and territories, included GI module
- **2019:** 32 states included GI module

**Question Evolution:**
- In 2018, the sexual orientation question was adjusted to align with the format used in the National Health Interview Survey (NHIS)
- Wording and placement of GI questions have undergone modifications over the years to improve data accuracy and respondent understanding

## State Participation

**Important Methodological Note:** The GI module is **optional**, creating cross-state/year heterogeneity.

**Participation Timeline:**
- **2014:** 19 states
- **2016:** 28 states (including DC and territories)
- **2017:** 33 states (including DC and territories)
- **2019:** 32 states

**Healthy People 2030 Goal:**
- Target: Increase to 55 states and territories (including DC) that include GI questions in BRFSS by 2030

**Implications:**
- Researchers must check which states included the module in any given year
- Cross-state comparisons require careful attention to module inclusion
- Temporal trends may be affected by changing state participation

## Methodological Notes

1. **Optional Module Design:** The GI module is optional, meaning states choose whether to include it. This creates important methodological heterogeneity that researchers must account for.

2. **Standardized Wording:** The transgender question wording is explicitly standardized and publicly documented, making BRFSS a useful reference for transgender question design.

3. **Transgender Subcategories:** BRFSS includes three transgender subcategories (male-to-female, female-to-male, gender nonconforming), providing more granular data than binary transgender/non-transgender questions.

4. **Interviewer Clarification:** The transgender question includes an interviewer note that provides clarification/definition, which may help with respondent understanding.

5. **Sexual Orientation Wording Variation:** The sexual orientation question wording differs slightly for male vs. female respondents (e.g., "Gay" for males vs. "Lesbian or Gay" for females).

6. **Response Codes:** Uses standard BRFSS response codes (7 = Don't know/Not sure, 9 = Refused).

7. **Health Focus:** BRFSS is a health survey, so GI data is used to identify and address health disparities among LGBTQ+ populations.

8. **Contrast with NHIS:** The plan notes that BRFSS includes a transgender item in a module while NHIS historically did not - this contrast is informative about institutional and design constraints.

## Documentation Sources

1. **CDC BRFSS Website:** https://www.cdc.gov/brfss

2. **BRFSS Questionnaires:** https://www.cdc.gov/brfss/questionnaires/index.htm
   - Includes current and historical questionnaires with GI module

3. **BRFSS GI Statistical Brief:** https://www.cdc.gov/brfss/data_documentation/pdf/BRFSS-SOGI-Stat-Brief-508.pdf

4. **CMS SGM Clearinghouse - BRFSS:** https://www.cms.gov/about-cms/agency-information/omh/resource-center/hcps-and-researchers/data-tools/sgm-clearinghouse/brfss

5. **Healthy People 2030 - BRFSS GI Objective:** https://odphp.health.gov/healthypeople/objectives-and-data/browse-objectives/lgbt/increase-number-states-territories-and-dc-include-sexual-orientation-and-gender-identity-questions-brfss-lgbt-03

6. **American Progress - BRFSS GI Data Collection:** https://www.americanprogress.org/article/sexual-orientation-and-gender-identity-data-collection-in-the-behavioral-risk-factor-surveillance-system/

## Evaluation

**Note:** Evaluation applies to the optional GI module. Core BRFSS (binary sex only) does not collect gender identity.

### 1. Classification Accuracy
**Rating:** ⚠️ **Moderate** - Can classify some groups, but limitations
- Direct transgender question with subcategories (male-to-female, female-to-male, gender nonconforming) enables classification
- However, question asks "Do you consider yourself to be transgender?" which may miss some trans people who don't use that term
- Gender nonconforming category provides some coverage for non-binary identities
- Binary sex question (core) does not enable classification on its own

### 2. Error Checking
**Rating:** ⚠️ **Moderate** - Some protection
- Interviewer clarification note helps ensure understanding
- However, no explicit confirmation question
- No consistency checks between core sex question and transgender question
- Risk of misclassification remains, especially given optional module nature

### 3. Comprehensibility
**Rating:** ✅ **Good** - Clear with clarification
- "Do you consider yourself to be transgender?" is direct
- Interviewer note provides helpful clarification/definition
- Subcategories (male-to-female, female-to-male, gender nonconforming) are descriptive
- Response options are clear

### 4. Response Options Coverage
**Rating:** ⚠️ **Moderate** - Good for trans people, limited for non-binary
- Transgender subcategories provide good coverage for trans men, trans women, and some non-binary people
- However, some non-binary people may not identify as "transgender" or "gender nonconforming"
- No explicit non-binary option outside of "gender nonconforming"
- Binary sex question (core) limits coverage

### 5. Clarity of Intent
**Rating:** ✅ **Good** - Clear purpose
- Direct question about transgender identity is clear
- Interviewer note explains what "transgender" means
- Respondents understand what is being asked
- No need to infer intent

### 6. Respectful Wording
**Rating:** ✅ **Good** - Respectful language
- "Consider yourself to be" acknowledges self-identification
- Interviewer note uses respectful, explanatory language
- Subcategories use descriptive, respectful terminology
- Generally inclusive approach

### 7. Non-Partisan Language
**Rating:** ✅ **Good** - Neutral language
- Questions use neutral, factual language
- No obvious partisan framing
- Focus on health data collection rather than political positioning

---

# Survey Gender Identity Questions: National Health Interview Survey (NHIS)

## Survey Overview

**Organization:** National Center for Health Statistics (NCHS), Centers for Disease Control and Prevention (CDC)  
**Survey Name:** National Health Interview Survey (NHIS)  
**Website:** https://www.cdc.gov/nchs/nhis  
**Mode:** Computer-assisted personal interviewing (CAPI) - face-to-face interviews, with some components via telephone  
**Frequency:** Annual survey  
**Purpose:** Flagship health survey monitoring health trends and informing policy decisions

## Current Questions (2024)

### Core Question: Sex

**Question Text:**
> "Are you male or female?"

**Interviewer Instruction (read if necessary):**
> "By sex we mean sex at birth."

**Response Options:**
1. Male
2. Female
7. Refused (sometimes coded)
9. Don't know (rarely coded)

**Notes:**
- Binary response options (Male/Female)
- Part of core NHIS questionnaire
- Used for demographic analysis and health statistics
- **Interviewer instruction provided:** "By sex we mean sex at birth" - this clarifies that the question refers to sex assigned at birth, not current gender identity
- The instruction is read "if necessary" to clarify meaning
- Response codes 7 (Refused) and 9 (Don't know) are sometimes/rarely coded
- This wording has been consistently used in recent years (2022, 2023, and likely 2024)


### Experimental Gender Identity Questions (2022-present)

**Status:** Experimental questions in the Gender Identity (GNI) section

**Availability:** Data from these questions are **NOT included in public-use NHIS files**. They are available only through the NCHS Research Data Center (RDC).

#### 2022 Version: Three-Step Approach

The 2022 NHIS used a **three-step gender identity measurement protocol** in an experimental module administered to the Sample Adult. NCHS implemented a **2×2 experimental design** varying question order and wording.

**Step 1: Current Gender Identity**

**Question Text:**
> "Which of the following best represents how you think of yourself?"

**Response Options:**
1. Male
2. Female
3. Transgender
4. Nonbinary
5. Another gender (SPECIFY)

**Notes:**
- Respondents could select **only one category** (NHIS does not allow multiselect)
- "Another gender" triggered a text entry field for specification
- In 2022, this question appeared either before or after the sex assigned at birth item depending on experimental condition

**Step 2: Sex Assigned at Birth**

**Question Text:**
> "What sex were you assigned at birth, on your original birth certificate?"

**Response Options:**
1. Male
2. Female

**Notes:**
- This followed the standard federal two-step measure recommended by FCSM (Federal Committee on Statistical Methodology)
- In 2022, this question appeared either before or after the gender identity item depending on experimental condition

**Step 3: Confirmation Question**

**Question Text:**
> "Just to confirm, you said that you are [CURRENT GENDER] and that you were assigned [SEX AT BIRTH] at birth. Is that correct?"

**Response Options:**
1. Yes
2. No → If no, the interviewer was instructed to re-ask the items

**Notes:**
- The confirmation step was included to assess misclassification and reduce response error
- This confirmation question was used **ONLY when the two items differed** (current gender identity ≠ sex assigned at birth)
- If respondent answered "No," interviewer was instructed to re-ask the gender identity and sex assigned at birth questions

#### 2023 Modifications

The 2023 NHIS retained the GNI module as an RDC-only experimental component, but made these changes:

**Changes:**
- **Eliminated the 2×2 experimental design** used in 2022
- **Standardized question order** into the conventional two-step format:
  1. Sex assigned at birth
  2. Current gender identity
  3. Confirmation question (if needed)
- **Wording was slightly revised** for clarity but retained the same substantive content
- The module continued to be excluded from public-use microdata; access is available only in the Research Data Center

**Status:**
- NCHS has **not finalized a decision** about integrating these GNI questions into the core NHIS
- The sexual orientation question remains in the public-use data; the gender identity items do not

## Measurement Approach Classification

**Current Approach:**
- **Core:** Binary sex question
- **Sexual Orientation:** Direct question (asked of all adults 18+, since 2013)
- **Gender Identity:** Experimental three-step approach (2022-present, Research Data Center only)

**Key Characteristics:**
- **Sexual orientation:** Standard question since 2013, part of Sample Adult Core
- **Gender identity:** Experimental questions, not in public-use files
- **Three-step approach:** Current gender identity → Sex assigned at birth → Confirmation question
- **Not a standard two-step GI approach** (gender identity questions are experimental)

## Historical Context

**Sexual Orientation:**
- **2013:** Sexual orientation questions introduced in Sample Adult Core
- **2013-2014:** Follow-up questions for "something else" or "I don't know" responses
- **2015:** Follow-up questions discontinued, only main question asked
- **2015-present:** Consistent question format maintained

**Gender Identity:**
- **Pre-2022:** NHIS historically did not include adult gender identity questions 
- **2022:** Experimental gender identity questions introduced (three-step approach with 2x2 experimental design)
- **2023:** Questions modified - standardized sequence and wording, eliminated 2x2 experimental design
- **2024:** Questions continue as experimental, available through Research Data Center only

## Methodological Notes

1. **Contrast with BRFSS:** The plan notes that BRFSS includes a transgender item in an optional module, while NHIS historically did not include adult gender identity - this contrast is informative about institutional and design constraints.

2. **Experimental Status:** Gender identity questions remain experimental and are not included in public-use files, requiring access through Research Data Center.

3. **Three-Step Approach:** The 2022+ experimental gender identity questions use a three-step approach: current gender identity → sex assigned at birth → confirmation question.

4. **Data Collection Method:** NHIS uses computer-assisted personal interviewing (CAPI) with trained interviewers conducting face-to-face interviews. Flashcards are used for sensitive questions like sexual orientation.

5. **Sexual Orientation Wording Variation:** Like BRFSS, the sexual orientation question wording differs slightly for male vs. female respondents.

6. **Follow-up Questions Discontinued:** Initial follow-up questions for sexual orientation (2013-2014) were discontinued in 2015, simplifying the data collection process.

7. **Flagship Health Survey:** NHIS is a flagship health survey, making its approach to GI measurement influential in health research.

## Policy Context

**Executive Order 14168 (January 2025):**
- Directed federal agencies to remove content related to gender identity from federal surveys
- **Impact on NHIS:** Early 2025 reports indicated that the Trump administration directed federal agencies to remove gender identity content from federal surveys, which may affect the experimental gender identity questions in NHIS
- Status of experimental questions post-Executive Order needs verification

## Documentation Sources

1. **CDC NHIS Website:** https://www.cdc.gov/nchs/nhis

2. **NHIS Sexual Orientation Information:** https://archive.cdc.gov/www_cdc_gov/nchs/nhis/sexual_orientation/index.htm

3. **NHIS Survey Description 2022:** https://ftp.cdc.gov/pub/health_Statistics/nchs/Dataset_Documentation/NHIS/2022/srvydesc-508.pdf

4. **NHIS Survey Description 2023:** https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2023/srvydesc-508.pdf

5. **CMS SGM Clearinghouse - NHIS:** https://www.cms.gov/About-CMS/Agency-Information/OMH/resource-center/hcps-and-researchers/data-tools/sgm-clearinghouse/nhis

6. **Census Bureau NHIS Page:** https://www.census.gov/programs-surveys/nhis.html

## Comparison with Other Surveys

**Key Differences:**
- **NHIS:** Sexual orientation standard (since 2013), gender identity experimental (2022+, Research Data Center only)
- **BRFSS:** Optional GI module (sexual orientation + transgender), state-level variation
- **GSS:** Two-step approach (sex assigned at birth + current gender identity) - standard, asked of all respondents
- **ANES:** Modified two-step approach (self-reported sex + gender identity + direct transgender question) - standard
- **ACS:** Binary sex only (currently), testing GI questions for 2027
- **CPS:** Binary sex only, no GI questions

**Unique Features:**
- **NHIS:** Only survey with experimental gender identity questions (not in public-use files)
- **NHIS:** Three-step gender identity approach (current gender → sex at birth → confirmation)
- **NHIS:** Sexual orientation question has been standard since 2013 (longer than most other surveys)
- **NHIS:** Contrast with BRFSS - NHIS historically did not include gender identity while BRFSS has optional module

## Evaluation

**Note:** Evaluation applies to experimental gender identity questions (2022+, Research Data Center only). Core NHIS (binary sex + sexual orientation) does not collect gender identity in public-use files.

### 1. Classification Accuracy
**Rating:** ✅ **Good** - Can classify all five groups
- Three-step approach enables identification of cis men, cis women, trans men, trans women
- "Nonbinary" option explicitly covers non-binary identities
- "Another gender" with specification provides additional coverage
- Confirmation question helps ensure accuracy

### 2. Error Checking
**Rating:** ✅ **Good** - Includes error checking
- **Confirmation question** is a key strength: "Just to confirm, you said that you are [CURRENT GENDER] and that you were assigned [SEX AT BIRTH] at birth. Is that correct?"
- Confirmation question used when responses differ, helping catch errors
- If respondent answers "No," interviewer re-asks the questions
- This addresses the critical need to minimize error rates among cis people

### 3. Comprehensibility
**Rating:** ✅ **Good** - Clear questions
- "Which of the following best represents how you think of yourself?" is clear
- "What sex were you assigned at birth, on your original birth certificate?" is explicit
- Response options (Male/Female/Transgender/Nonbinary/Another gender) are understandable
- Confirmation question clarifies any ambiguity

### 4. Response Options Coverage
**Rating:** ✅ **Good** - Comprehensive coverage
- Current gender: Male/Female/Transgender/Nonbinary/Another gender (with specification)
- Sex assigned at birth: Male/Female (binary, appropriate for this construct)
- "Another gender" with specification provides flexibility
- Good coverage for most identities

### 5. Clarity of Intent
**Rating:** ✅ **Good** - Clear purpose
- Three-step approach makes purpose clear
- Confirmation question demonstrates intent to ensure accuracy
- Respondents understand what is being asked and why

### 6. Respectful Wording
**Rating:** ✅ **Good** - Respectful language
- "Assigned at birth" uses recognized, respectful terminology
- "Best represents how you think of yourself" acknowledges self-identification
- "Nonbinary" uses recognized, respectful terminology
- Generally inclusive and respectful language

### 7. Non-Partisan Language
**Rating:** ✅ **Good** - Neutral language
- Questions use neutral, factual language
- No obvious partisan framing
- Focus on accurate health data collection

## Next Steps

- [ ] Verify exact wording of core sex question from current NHIS questionnaire
- [ ] Verify exact wording of 2022-2023 experimental gender identity questions
- [ ] Document variable names for sex, sexual orientation, and gender identity questions
- [ ] Check status of experimental gender identity questions post-Executive Order 14168 (2025)
- [ ] Review NHIS Survey Description documents for detailed methodology
- [ ] Document any changes to gender identity questions between 2022, 2023, and 2024
- [ ] Compare NHIS three-step approach with other surveys' approaches
- [ ] Review Research Data Center access requirements for gender identity data

---

# Survey Gender Identity Questions: Demographic and Health Surveys (DHS)

## Survey Overview

**Organization:** DHS Program (USAID-associated implementation)  
**Survey Name:** Demographic and Health Surveys (DHS)  
**Website:** https://dhsprogram.com  
**Mode:** Face-to-face household interviews  
**Frequency:** Varies by country (typically every 3-5 years)  
**Coverage:** Globally dominant household survey program, conducted in over 90 countries

## Measurement Approach Classification

**Current Approach:** Gender embedded structurally (not through direct questions)

**Key Characteristics:**
- **Structural embedding:** Gender is embedded structurally through:
  - Separate women's and men's questionnaires
  - Eligibility rules that determine who receives which questionnaire
  - Household roster structure
- **Not a direct question approach:** Unlike other surveys, DHS does not ask "What is your sex?" or "What is your gender?" as a direct question
- **Eligibility-based:** Sex/gender is determined through eligibility criteria for different questionnaire modules

## Structural Design

### Separate Questionnaires

**Women's Questionnaire:**
- Administered to eligible women (typically aged 15-49)
- Contains questions about reproductive health, family planning, maternal health, etc.
- Eligibility determined by age and household structure

**Men's Questionnaire:**
- Administered to eligible men (typically aged 15-59 or 15-64, varies by country)
- Contains questions about men's health, family planning knowledge, etc.
- Eligibility determined by age and household structure

### Household Roster

**Structure:**
- Household roster lists all household members
- Each member's relationship to household head is recorded
- Sex/gender information is typically collected as part of the roster (though exact wording needs verification)

**Notes:**
- The household roster serves as the primary mechanism for identifying sex/gender
- This information then determines eligibility for women's vs. men's questionnaires

## Methodological Notes

1. **Structural Embedding:** DHS embeds gender structurally rather than through direct questions, making it fundamentally different from other surveys in this comparison

2. **Eligibility Rules:** The separation of questionnaires based on eligibility rules means that sex/gender is operationalized through survey design rather than respondent self-identification

3. **Globally Dominant:** As a globally dominant household survey program, DHS's approach influences how gender is measured in international monitoring contexts

4. **Contrast with Other Surveys:** This structural approach contrasts sharply with surveys that ask direct questions about sex or gender identity

5. **Household-Based:** The household roster structure means sex/gender information is collected at the household level, not just for respondents

## Documentation Sources

1. **DHS Program Website:** https://dhsprogram.com

2. **DHS Questionnaire Hub:** (To be located - mentioned in plan as providing standardized instrument approach and eligibility information)

3. **DHS Survey Description Pages:** (To be located - mentioned in plan as providing information about who is eligible for which modules)

4. **DHS Model Questionnaires:** Available through DHS Program website

## Comparison with Other Surveys

**Key Differences:**
- **DHS:** Gender embedded structurally (separate questionnaires, eligibility rules)
- **All other surveys reviewed:** Direct questions about sex/gender identity
- **DHS:** Household roster determines sex/gender
- **Other surveys:** Self-reported sex/gender identity

**Unique Features:**
- **DHS:** Only survey that embeds gender structurally rather than asking direct questions
- **DHS:** Separate questionnaires for women and men
- **DHS:** Eligibility-based approach rather than self-identification

## Next Steps

- [ ] Locate DHS questionnaire hub and review standardized instrument approach
- [ ] Review DHS survey description pages for eligibility rules
- [ ] Examine model questionnaires (women's and men's) for exact wording
- [ ] Document how sex/gender is recorded in household roster
- [ ] Verify eligibility criteria for women's vs. men's questionnaires
- [ ] Review DHS documentation for any recent changes to structural approach
- [ ] Compare DHS structural approach with MICS (also international household survey)

---

# Survey Gender Identity Questions: Multiple Indicator Cluster Surveys (MICS)

## Survey Overview

**Organization:** United Nations Children's Fund (UNICEF)  
**Survey Name:** Multiple Indicator Cluster Surveys (MICS)  
**Website:** https://mics.unicef.org  
**Mode:** Face-to-face household interviews  
**Frequency:** Varies by country (typically every 3-5 years)  
**Coverage:** Global flagship survey focused on women, children, and households

## Measurement Approach Classification

**Current Approach:** Gender/sex treated in international monitoring context (structural approach similar to DHS)

**Key Characteristics:**
- **Focus:** Women, children, and households
- **International monitoring:** Shows how sex/gender is treated in international monitoring contexts
- **Structural approach:** Similar to DHS, gender/sex likely embedded in survey structure rather than direct questions
- **UN system:** Part of UN system household monitoring instruments

## Survey Structure

### Focus Areas

**Primary Focus:**
- Women's health and well-being
- Children's health and development
- Household characteristics
- Maternal and child health indicators

**Questionnaire Structure:**
- Individual women's questionnaire (typically for women aged 15-49)
- Household questionnaire
- Children's questionnaires (for children under 5, etc.)

### Sex/Gender in MICS

**Likely Approach:**
- Sex/gender information likely collected through household roster
- Eligibility rules determine who receives which questionnaire (similar to DHS)
- Focus on women and children means sex/gender is operationalized through eligibility and questionnaire assignment

**Notes:**
- As a UN system household monitoring instrument, MICS likely uses structural approaches similar to DHS
- Exact question wording needs verification from model questionnaires

## Methodological Notes

1. **International Monitoring Context:** MICS shows how sex/gender is treated in international monitoring contexts, particularly for women and children

2. **UN System Approach:** As part of UN system household monitoring instruments, MICS likely follows standardized approaches for collecting demographic information

3. **Structural Similarity to DHS:** Like DHS, MICS likely embeds gender/sex structurally through questionnaire design and eligibility rules rather than direct questions

4. **Women and Children Focus:** The focus on women and children means sex/gender is central to survey design but may be operationalized through eligibility rather than self-identification

5. **Global Flagship:** As a global flagship survey, MICS's approach influences how sex/gender is measured in international development and monitoring contexts

## Documentation Sources

1. **UNICEF MICS Website:** https://mics.unicef.org

2. **MICS Model Questionnaires:** Available through UNICEF MICS website (mentioned in plan as providing model questionnaires, e.g., individual women's questionnaire)

3. **MICS Documentation:** Survey tools, questionnaires, and methodology documents available through UNICEF

## Comparison with Other Surveys

**Key Differences:**
- **MICS:** Gender/sex treated in international monitoring context (structural approach)
- **DHS:** Similar structural approach (separate questionnaires, eligibility rules)
- **All other surveys reviewed:** Direct questions about sex/gender identity
- **MICS:** UN system household monitoring instrument
- **Other surveys:** National or regional surveys with direct questions

**Similarities:**
- **MICS and DHS:** Both use structural approaches rather than direct questions
- **MICS and DHS:** Both are international household surveys focused on women and children
- **MICS and DHS:** Both embed gender/sex through questionnaire design and eligibility

## Next Steps

- [ ] Review UNICEF MICS model questionnaires for exact wording
- [ ] Examine individual women's questionnaire for sex/gender questions
- [ ] Review household questionnaire structure
- [ ] Document how sex/gender is recorded in household roster
- [ ] Verify eligibility criteria for different questionnaires
- [ ] Compare MICS approach with DHS structural approach
- [ ] Review MICS documentation for any recent changes
- [ ] Document any differences between MICS and DHS in how gender/sex is operationalized

---

# Survey Gender Identity Questions: World Values Survey (WVS)

## Survey Overview

**Organization:** World Values Survey Association  
**Survey Name:** World Values Survey (WVS)  
**Website:** https://www.worldvaluessurvey.org  
**Mode:** Face-to-face interviews  
**Frequency:** Every 4-5 years (waves)  
**Coverage:** Cross-national values measurement, conducted in nearly 100 countries since 1981

## Current Questions

### Core Variable: Sex of Respondent

**Variable Name:** `q260` (Wave 7), `Q260` (Wave 8 - uppercase convention)

**Field Label:**
> "Sex (of respondent):"

**Response Options:**
1. Male
2. Female

**Notes:**
- **Interviewer-coded variable:** This is an interviewer observation/recording, **not a spoken question** to the respondent
- The wording "Sex (of respondent)" is simply the field label in the questionnaire
- Interviewer records respondent's sex using this fixed field
- Binary response options (Male/Female only)
- Standard demographic variable included in all waves
- Used for demographic analysis and cross-national comparisons
- Part of core questionnaire (not optional)
- **No interviewer script or respondent-facing text** - it is a recorded observation

**Note:** WVS does not include direct questions about respondents' **gender identity** or **sexual orientation**.



## Methodological Notes

1. **Cross-National Standard:** WVS is a standard for cross-national values measurement, making its approach to sex/gender influential

2. **No GI Questions:** WVS does not ask about **individual gender identity** or **sexual orientation**

3. **Binary Sex Only:** Uses interviewer-coded binary sex variable (Male/Female) without gender identity options

4. **Standard Demographic:** Sex of respondent is a standard demographic variable, not an optional module

## Documentation Sources

1. **WVS Official Website:** https://www.worldvaluessurvey.org

2. **WVS Wave 8 Questionnaire:** https://www.worldvaluessurvey.org/documents/WVS-8_QUESTIONNAIRE_V11_FINAL_Jan_2024.pdf

3. **WVS Codebooks:** Available through WVS website for each wave

4. **WVS Data Portal:** Access to survey data and documentation

## Comparison with Other Surveys

**Key Differences:**
- **WVS:** Interviewer-coded binary sex variable only (no GI questions)
- **GSS:** Two-step GI approach (sex assigned at birth + current gender identity)
- **ANES:** Modified two-step approach (self-reported sex + gender identity + direct transgender question)
- **All other surveys reviewed:** Either direct GI questions or structural approaches

**Unique Features:**
- **WVS:** Interviewer-coded sex variable (not respondent-reported)
- **WVS:** Cross-national standard for values measurement
- **WVS:** No gender identity or sexual orientation questions

**Similarities:**
- **WVS and others:** Binary sex variable/question (similar to ACS, CPS, BRFSS core)
- **WVS and ESS:** Both have binary sex variable and do not ask about individual GI

## Next Steps

- [x] Verify exact wording of sex variable from Wave 8 questionnaire (confirmed: interviewer-coded field label "Sex (of respondent)")
- [ ] Document variable names for current wave (Wave 8)
- [ ] Review Wave 8 questionnaire for any new gender-related questions
- [ ] Check if Wave 8 includes any gender identity or sexual orientation questions
- [ ] Compare sex question wording across waves

---

# Survey Gender Identity Questions: European Social Survey (ESS)

## Survey Overview

**Organization:** European Social Survey European Research Infrastructure Consortium (ESS ERIC)  
**Survey Name:** European Social Survey (ESS)  
**Website:** https://www.europeansocialsurvey.org  
**Mode:** Face-to-face interviews  
**Frequency:** Biennial (every 2 years)  
**Coverage:** Cross-national survey across European countries (24 countries in Round 11)

## Current Questions (Round 11, 2023/24)

### Core Question: Gender of Respondent

**Variable Name:** `gndr` (standard across all rounds)

**Question Text:**
> "Are you male or female?"

**Response Options:**
1. Male
2. Female

**Notes:**
- **Asked directly to respondents** (not interviewer-coded like WVS)
- **Mandatory binary response** - no additional categories (no nonbinary, transgender, or sex assigned at birth options)
- The variable `gndr` explicitly measures **gender**, not sex, according to ESS documentation
- Standard demographic variable included in all rounds since Round 1 (2002)
- Used for demographic analysis and cross-national comparisons
- Part of core questionnaire (not optional)
- ESS has strong documentation and harmonization discipline
- **Question wording is standardized across countries** - only translation varies, not the wording structure
- Gender item has remained strictly binary since Round 1 (2002)

### Sexual Orientation Question

**Variable Name:** `sxorient` (variable name may vary by round)

**Question Text:**
*(Exact wording to be verified from source questionnaires)*

**Response Options:**
*(Exact options to be verified)*

**Notes:**
- Included in **self-completion section** (not interviewer-administered)
- Beginning in multiple recent rounds (e.g., Round 9)
- Part of ESS questionnaire but in self-completion portion

## Measurement Approach Classification

**Current Approach:** Core gender variable + sexual orientation question (self-completion)

**Key Characteristics:**
- **Gender of respondent:** Core demographic variable - mandatory binary (Male/Female only)
- **Sexual orientation:** Included in self-completion section (Round 9+)
- **No gender identity question:** ESS has never included a gender identity question beyond the binary gender item
- **No sex assigned at birth question:** Does not ask about sex assigned at birth
- **No nonbinary/transgender options:** Gender item is strictly binary with no additional categories

## Historical Context

**Core Variable:**
- Gender variable (`gndr`) has been included in all rounds since ESS began (2002)
- Variable explicitly measures **gender**, not sex, according to ESS documentation
- Strong documentation and harmonization discipline across rounds
- Question wording standardized across countries (only translation varies)

**Sexual Orientation:**
- Sexual orientation question (`sxorient`) included in self-completion section beginning in Round 9
- Self-completion section allows for more sensitive questions

## Methodological Notes

1. **Strong Documentation:** ESS has very strong documentation and harmonization discipline, making it useful for tracing exact wording, routing, and module design

2. **Gender Identity:** ESS does not ask about **gender identity** beyond the binary gender item (no nonbinary, transgender, or sex assigned at birth questions)

3. **Sexual Orientation:** ESS includes sexual orientation question in self-completion section (Round 9+)

4. **Cross-National Standard:** ESS is a cross-national standard for European social research, making its approach influential

5. **Harmonization:** ESS's strong harmonization discipline means variable names and question structures are consistent across rounds and countries

6. **Standardized Wording:** Question wording is standardized across countries - only translation varies, not the wording structure

7. **Source Questionnaire:** ESS publishes source questionnaires with exact wording, making it easier to document question text than some other surveys

8. **Self-Completion Section:** Sexual orientation question is in self-completion section, allowing for more sensitive questions

## Documentation Sources

1. **ESS Official Website:** https://www.europeansocialsurvey.org

2. **ESS Round 11 Source Questionnaire:** Available through ESS website (mentioned in plan as providing source questionnaire with exact wording)

3. **ESS Data Portal:** https://www.europeansocialsurvey.org/data-portal

6. **ESS Documentation:** Comprehensive documentation available through ESS website

## Comparison with Other Surveys

**Key Differences:**
- **ESS:** Core gender variable (binary) + sexual orientation (self-completion, Round 9+), no gender identity question
- **WVS:** Interviewer-coded sex variable only (no GI questions)
- **GSS:** Two-step GI approach (sex assigned at birth + current gender identity)
- **ANES:** Modified two-step approach (self-reported sex + gender identity + direct transgender question)
- **All other surveys reviewed:** Either direct GI questions or structural approaches

**Unique Features:**
- **ESS:** Strong documentation and harmonization discipline
- **ESS:** Cross-national European standard
- **ESS:** Source questionnaires published with exact wording
- **ESS:** Gender variable explicitly measures **gender** (not sex) according to ESS documentation
- **ESS:** Sexual orientation in self-completion section (not interviewer-administered)
- **ESS:** Binary gender item has remained strictly binary since Round 1 (2002)

**Similarities:**
- **ESS and WVS:** Both have binary gender/sex variable
- **ESS and others:** Core gender variable (similar to most other surveys)

## Next Steps

- [x] Verify exact wording of core gender question (`gndr`) from Round 11 source questionnaire (confirmed: "Are you male or female?")
- [x] Document response options for `gndr` variable (confirmed: 1=Male, 2=Female, mandatory binary)
- [ ] Verify exact wording of sexual orientation question (`sxorient`) from source questionnaires
- [ ] Document response options for sexual orientation question
- [ ] Verify which rounds include sexual orientation question
- [ ] Review ESS documentation for harmonization details
- [ ] Document any routing or skip logic related to gender questions

---

# Survey Gender Identity Questions: Afrobarometer

## Survey Overview

**Organization:** Afrobarometer Network  
**Survey Name:** Afrobarometer  
**Website:** https://www.afrobarometer.org  
**Mode:** Face-to-face interviews  
**Frequency:** Regular survey rounds (typically every 2-3 years)  
**Coverage:** Pan-African survey across more than 40 African countries

## Current Questions

### Core Variable: Respondent's Gender

**Variable Name:** `Q101` (consistent across Rounds 5, 6, 7, 8, and 9)

**Field Label:**
> "Q101. Respondent's gender"

**Response Options:**
1. Male
2. Female

**Notes:**
- **Interviewer-recorded variable:** This is an **interviewer observation/recording**, **not a spoken question** to the respondent (identical to WVS)
- The wording "Q101. Respondent's gender" is simply the field label in the questionnaire
- Interviewer records respondent's gender using this fixed field
- **No interviewer script or respondent-facing text** - it is a recorded observation
- **Interviewer instruction:** Afrobarometer team explicitly instructs enumerators to record gender **based on observation**, not self-report
- **Mandatory variable:** Q101 is mandatory and universally recorded; interviewers cannot skip this item
- Binary response options (Male/Female only)
- **Terminology note:** Afrobarometer uses the term **"gender"** for Q101, but its content is **biological sex**, not gender identity
- No option for nonbinary or "other"
- No definition is provided
- Part of "Respondent Characteristics" section
- Standard demographic variable included in all rounds
- Used for demographic analysis and cross-country comparisons
- **Data disaggregation:** Data is disaggregated by sex for analysis
- **Stratification variable:** Sex is routinely used as a stratification variable in weighting and analysis
- **Question wording is stable across countries** - only translation varies, not the wording structure

## Measurement Approach Classification

**Current Approach:** Interviewer-recorded binary gender variable only (not GI questions)

**Key Characteristics:**
- **Respondent's gender:** Interviewer-recorded variable (Male/Female) - standard demographic variable
- **Based on observation:** Interviewers record gender based on observation, not self-report
- **No gender identity question:** Afrobarometer has never included gender identity questions in any round
- **No sexual orientation question:** Afrobarometer has **never** included sexual orientation questions in any round (Rounds 1-9)
- **Terminology:** Uses term "gender" but content is biological sex, not gender identity

## Historical Context

**Standard Practice:**
- Respondent's gender variable (Q101) has been included since early rounds
- Variable name Q101 consistent across Rounds 5, 6, 7, 8, and 9
- Binary coding (1=Male, 2=Female) has been consistent
- Interviewer-recorded based on observation (not self-report)
- Used for demographic analysis, disaggregation, and stratification in weighting

## Methodological Notes

1. **Pan-African Standard:** Afrobarometer is a pan-African research network, making its approach influential across African countries

2. **Face-to-Face Interviews:** Surveys conducted through face-to-face interviews in respondent's preferred language

3. **Nationally Representative:** Surveys are nationally representative, covering both urban and rural areas

4. **Data Disaggregation:** Data is disaggregated by sex, urban-rural residence, and other demographic variables

5. **Gender Attitude Items:** Afrobarometer includes several gender attitude items (e.g., perceptions of women's leadership, employment, and political rights), but these are attitudinal and unrelated to GI measurement

6. **Binary Gender Only:** Uses interviewer-recorded binary gender variable (Male/Female) without gender identity options

7. **Mandatory Variable:** Q101 is mandatory and universally recorded; interviewers cannot skip this item

8. **Stratification Variable:** Sex is routinely used as a stratification variable in weighting and analysis

9. **Stable Wording:** Question wording is stable across countries - only translation varies, not the wording structure

## Documentation Sources

1. **Afrobarometer Official Website:** https://www.afrobarometer.org

2. **Afrobarometer Questionnaires:** https://www.afrobarometer.org/surveys-and-methods/questionnaire/

3. **Afrobarometer Survey Resources:** https://www.afrobarometer.org/surveys-and-methods/survey-resources/

4. **Afrobarometer Data Portal:** Online data analysis tools available through website

## Comparison with Other Surveys

**Key Differences:**
- **Afrobarometer:** Interviewer-recorded binary gender variable only (no GI questions)
- **GSS:** Two-step GI approach (sex assigned at birth + current gender identity)
- **ANES:** Modified two-step approach (self-reported sex + gender identity + direct transgender question)
- **WVS:** Interviewer-coded binary sex variable (no GI questions) - similar to Afrobarometer
- **ESS:** Binary gender variable + sexual orientation (self-completion, Round 9+)
- **All other surveys reviewed:** Either direct GI questions or structural approaches

**Unique Features:**
- **Afrobarometer:** Pan-African focus (40+ African countries)
- **Afrobarometer:** Face-to-face interviews in respondent's preferred language
- **Afrobarometer:** Interviewer records gender based on observation (not self-report)
- **Afrobarometer:** Uses term "gender" but content is biological sex
- **Afrobarometer:** Never included sexual orientation questions (unlike ESS)

**Similarities:**
- **Afrobarometer and WVS:** Both use interviewer-recorded binary gender/sex variable (not respondent-reported)
- **Afrobarometer and WVS:** Both do not ask about individual GI
- **Afrobarometer and others:** Binary gender/sex variable (similar to ACS, CPS, BRFSS core)

## Next Steps

- [x] Verify exact wording of gender variable from questionnaire (confirmed: "Q101. Respondent's gender" - interviewer-recorded)
- [x] Document variable name (confirmed: Q101, consistent across Rounds 5-9)
- [x] Verify response options (confirmed: 1=Male, 2=Female)
- [x] Check if Afrobarometer has ever included gender identity or sexual orientation questions (confirmed: never included in any round)
- [ ] Review questionnaire structure and Respondent Characteristics section
- [ ] Document any changes to Q101 across rounds (if any)
- [ ] Compare Afrobarometer approach with WVS (both interviewer-recorded)

