import csv
import random

# Function to generate a diverse set of ethical and moral topics
def generate_topics(num_topics=3000):
    # Core ethical issue categories
    categories = [
        "Medical Ethics",
        "Social Justice",
        "Technology Ethics",
        "Environmental Ethics",
        "Business Ethics",
        "Educational Ethics",
        "Political Ethics",
        "Animal Rights",
        "Privacy Rights",
        "Criminal Justice",
        "Cultural Ethics",
        "Family Ethics",
        "Media Ethics",
        "Information Ethics",
        "Research Ethics",
        "International Relations Ethics",
        "Religious Freedom",
        "Bioethics",
        "Public Health Ethics",
        "Military Ethics",
        "Economic Ethics"
    ]
    
    # Topic templates for each category
    topic_templates = {
        "Medical Ethics": [
            "Euthanasia for terminally ill patients",
            "Mandatory vaccination policies",
            "Right to refuse medical treatment",
            "Physician-assisted suicide legalization",
            "Allocation of scarce medical resources",
            "Organ donation opt-out systems",
            "Genetic testing without consent",
            "Surrogate pregnancy regulations",
            "Experimental treatments for terminal patients",
            "Healthcare resource allocation based on age",
            "Placebo use in clinical trials",
            "Medical care rationing during crises",
            "Disclosure of medical errors to patients",
            "Conscientious objection by healthcare providers",
            "Mandatory genetic screening for newborns",
            "Medical tourism ethics",
            "Cognitive enhancement medication use",
            "Patient autonomy vs. medical paternalism",
            "DNR orders without patient consultation",
            "Remote patient monitoring privacy",
            "Embryonic stem cell research",
            "Artificial wombs for human gestation",
            "Brain death criteria for organ donation",
            "Mandated psychological evaluations",
            "Priority of preventive vs. curative medicine"
        ],
        "Social Justice": [
            "Affirmative action in education",
            "Universal basic income implementation",
            "Wealth redistribution policies",
            "Reparations for historical injustices",
            "Immigration quotas based on national origin",
            "Hate speech legislation",
            "Mandatory diversity training",
            "Social media content moderation",
            "Gender-neutral public facilities",
            "Religious exemptions from anti-discrimination laws",
            "Cultural appropriation boundaries",
            "Social credit systems",
            "Equity vs. equality in public policy",
            "Abolishing standardized testing",
            "Eliminating cash bail systems",
            "Mandatory implicit bias testing",
            "School choice voucher systems",
            "Free speech limitations",
            "Mask mandates during pandemics",
            "Mandatory voting laws",
            "Subsidized housing in affluent areas",
            "Corporate diversity quotas",
            "Racial identity verification requirements",
            "Gentrification intervention policies",
            "Cancel culture as accountability"
        ],
        "Technology Ethics": [
            "AI decision-making in criminal sentencing",
            "Facial recognition in public spaces",
            "Robot rights and obligations",
            "Brain-computer interface regulation",
            "Algorithmic content curation",
            "Genetic modification of human embryos",
            "Autonomous weapons systems",
            "Internet access as a human right",
            "Digital immortality services",
            "Neuromarketing regulations",
            "Virtual reality addiction interventions",
            "Social media age restrictions",
            "Predictive policing algorithms",
            "Deepfake regulation",
            "Electronic surveillance of employees",
            "Digital right to be forgotten",
            "Smart city privacy concerns",
            "Emotional AI in customer service",
            "Algorithmic transparency requirements",
            "Human microchipping consent",
            "Biometric data collection and storage",
            "Quantum computing encryption standards",
            "Synthetic media authentication",
            "Metaverse governance structures",
            "Transhumanism movement ethics"
        ],
        "Environmental Ethics": [
            "Carbon taxation policies",
            "Geoengineering to combat climate change",
            "Rights of nature in legal systems",
            "Mandatory environmental impact assessments",
            "Wildlife population control methods",
            "Wilderness preservation vs. resource utilization",
            "Lab-grown meat regulation",
            "Plastic product bans",
            "Climate refugee status recognition",
            "Individual carbon footprint limits",
            "Intergenerational climate justice",
            "Rewilding urban spaces",
            "Deep sea mining moratoriums",
            "National park commercialization",
            "Climate activism disruption tactics",
            "Ecotourism impact on local ecosystems",
            "Space exploration environmental safeguards",
            "Endangered species gene editing",
            "Water privatization",
            "Nuclear energy as climate solution",
            "Mandatory climate education",
            "Tradeable pollution permits",
            "Environmental reparations from corporations",
            "Sustainable development certification",
            "Future generations' rights"
        ],
        "Business Ethics": [
            "CEO-to-worker pay ratio caps",
            "Corporate political contributions",
            "Whistleblower protection policies",
            "Ethical investing requirements",
            "Supply chain transparency mandates",
            "Planned obsolescence regulation",
            "Workplace surveillance disclosure",
            "Executive compensation clawbacks",
            "Corporate social responsibility requirements",
            "Targeted advertising limitations",
            "Gig economy worker classification",
            "Shareholder vs. stakeholder primacy",
            "Zero-hour contracts regulation",
            "Consumer data as corporate asset",
            "Mandatory diversity on corporate boards",
            "Tax havens utilization",
            "Hostile takeover restrictions",
            "Corporate personhood limitations",
            "Algorithmic pricing transparency",
            "Automation displacement responsibility",
            "Corporate carbon footprint reporting",
            "Executive bonus during layoffs",
            "Workplace wellness program mandates",
            "Profit-sharing requirements",
            "Cross-border labor standards"
        ],
        "Educational Ethics": [
            "School surveillance systems",
            "Student data privacy protections",
            "Academic freedom limitations",
            "Standardized testing emphasis",
            "Homeschooling regulation",
            "Religious education funding",
            "Critical thinking vs. cultural sensitivity",
            "Zero-tolerance disciplinary policies",
            "Gifted education programs",
            "College legacy admissions",
            "AI in grading student work",
            "Ideological diversity in curriculum",
            "Student loan forgiveness programs",
            "Trigger warnings in education",
            "School resource officer presence",
            "Free speech on college campuses",
            "Grade inflation practices",
            "Student social media monitoring",
            "Behavioral tracking in education",
            "Performance-based teacher pay",
            "Digital divide intervention",
            "Character education requirements",
            "Charter school expansion",
            "Mandatory community service",
            "History curriculum standardization"
        ],
        "Political Ethics": [
            "Term limits for elected officials",
            "Mandatory voting laws",
            "Campaign finance restrictions",
            "Lobbying regulation",
            "Political party dissolution powers",
            "Gerrymandering reform",
            "Felony disenfranchisement",
            "Ranked choice voting implementation",
            "Truth in political advertising laws",
            "Online political microtargeting",
            "Compulsory military service",
            "Citizenship requirements for voting",
            "International election monitoring",
            "Recall election provisions",
            "Executive privilege limitations",
            "Intelligence agency oversight",
            "Political dynasty restrictions",
            "Judicial appointment processes",
            "National emergency powers",
            "Diplomatic immunity limitations",
            "Secession rights of regions",
            "Mandatory civic education",
            "Social media platform regulation",
            "Political deepfake criminalization",
            "Political polarization interventions"
        ],
        "Animal Rights": [
            "Factory farming regulations",
            "Animal testing for cosmetics",
            "Sport hunting bans",
            "Zoos and aquariums ethics",
            "Animal personhood recognition",
            "Horse racing industry regulation",
            "Pet breeding restrictions",
            "Animal experimentation alternatives",
            "Livestock transportation regulations",
            "Wildlife trophy hunting",
            "Feral animal management policies",
            "Animal entertainment industry",
            "Ritual animal slaughter practices",
            "Meat consumption taxation",
            "Fur farming prohibition",
            "Animal cognition research methods",
            "Captive animal breeding programs",
            "Animal agriculture subsidies",
            "Exotic pet ownership restrictions",
            "Habitat conservation mandates",
            "Laboratory animal welfare standards",
            "Animal-assisted therapy regulation",
            "Dairy industry practices",
            "Endangered species conservation priorities",
            "Service animal certification requirements"
        ],
        "Privacy Rights": [
            "Mass surveillance programs",
            "Genetic privacy protections",
            "Smart device data collection",
            "Digital health record sharing",
            "Child privacy online",
            "Location tracking regulations",
            "Browser cookie consent requirements",
            "Biometric identification systems",
            "Social media data ownership",
            "Government facial recognition databases",
            "Privacy by design requirements",
            "Data broker regulations",
            "Encryption backdoor requirements",
            "Identity verification standards",
            "Anonymity in online spaces",
            "Employee monitoring disclosures",
            "Student data protection",
            "Digital estate privacy",
            "Smart city surveillance",
            "Medical research data sharing",
            "Digital right to be forgotten",
            "Behavioral advertising opt-out",
            "Privacy impact assessments",
            "Cross-border data transfers",
            "Privacy rights of public figures"
        ],
        "Criminal Justice": [
            "Death penalty implementation",
            "Mandatory minimum sentencing",
            "Private prison systems",
            "Facial recognition in policing",
            "Restorative justice programs",
            "Solitary confinement limitations",
            "Decriminalization of drug possession",
            "Bail system reform",
            "Civil asset forfeiture",
            "Predictive policing algorithms",
            "Three strikes laws",
            "Juvenile justice system reform",
            "DNA database expansion",
            "Police body camera requirements",
            "Criminal record expungement",
            "Community policing initiatives",
            "Prison labor compensation",
            "White collar crime sentencing",
            "Plea bargaining limitations",
            "Victims' rights in criminal proceedings",
            "Non-citizen deportation for crimes",
            "Rehabilitation vs. punishment focus",
            "Child offender identity protection",
            "Criminalization of homelessness",
            "Remote video court proceedings"
        ],
        "Cultural Ethics": [
            "Cultural heritage repatriation",
            "Language preservation policies",
            "Indigenous land rights",
            "Cultural appropriation boundaries",
            "Historical monument preservation",
            "Traditional knowledge protection",
            "Religious exemption scope",
            "Minority language education rights",
            "Cultural representation in media",
            "Diaspora community recognition",
            "Intangible cultural heritage protection",
            "Traditional practice regulation",
            "Cultural sensitivity in tourism",
            "Hate speech vs. free expression",
            "Cultural assimilation expectations",
            "Religious freedom in public spaces",
            "Multicultural education requirements",
            "Cultural relativism vs. universal rights",
            "National identity promotion",
            "Immigrant integration policies",
            "Cultural diversity quotas",
            "Religious symbols in public institutions",
            "Digital colonialism prevention",
            "Cultural impact assessments",
            "Collective vs. individual rights"
        ],
        "Family Ethics": [
            "Parental rights termination",
            "Child discipline methods",
            "Non-traditional family recognition",
            "Reproductive technology access",
            "Child custody determination",
            "Elder care responsibility",
            "Parental monitoring of children",
            "Family reunification policies",
            "Adolescent medical autonomy",
            "Polygamous relationship recognition",
            "Gestational surrogacy regulation",
            "Mandatory family counseling",
            "Adoption eligibility criteria",
            "Parental leave policies",
            "Intergenerational wealth transfer",
            "Child social media presence",
            "Parent-child confidentiality",
            "Child genetic testing",
            "Family privacy protection",
            "Grandparent visitation rights",
            "Filial responsibility laws",
            "Family-based immigration",
            "Child beauty pageant regulation",
            "Embryo custody disputes",
            "Family separation in immigration"
        ],
        "Media Ethics": [
            "Fake news regulation",
            "Journalistic source protection",
            "Media ownership concentration",
            "Content moderation standards",
            "Depiction of violence regulation",
            "Reality television ethics",
            "Privacy invasion by journalists",
            "Celebrity privacy boundaries",
            "Public figure harassment coverage",
            "Graphic content warnings",
            "Native advertising disclosure",
            "Election coverage balance",
            "Social media platform accountability",
            "Victim identification protocols",
            "Image manipulation disclosure",
            "Children's advertising restrictions",
            "Public service broadcasting mandates",
            "Trauma-informed reporting",
            "Algorithmic news curation",
            "Digital media literacy education",
            "Representation diversity standards",
            "Crisis reporting guidelines",
            "Commentary vs. news separation",
            "Documentary subject consent",
            "Clickbait content regulation"
        ],
        "Information Ethics": [
            "Disinformation criminalization",
            "Open access research requirements",
            "Algorithmic decision transparency",
            "Digital divide interventions",
            "Intellectual property duration",
            "Data localization requirements",
            "Scientific research data sharing",
            "Archival access restrictions",
            "Information literacy education",
            "Historical information revision",
            "Digital commons governance",
            "Search engine neutrality",
            "Information access equity",
            "Classified information protection",
            "Cultural knowledge appropriation",
            "Citizen science ethics",
            "Paywalled information ethics",
            "Citation and attribution standards",
            "Content recommendation transparency",
            "Misinformation liability",
            "Public domain expansion",
            "Information asymmetry regulation",
            "Knowledge graph ownership",
            "Deep learning dataset transparency",
            "Library collection development"
        ],
        "Research Ethics": [
            "Human subject research consent",
            "Animal research alternatives",
            "Placebo use in clinical trials",
            "Genetic modification research",
            "Dual-use research oversight",
            "Indigenous knowledge research",
            "Research funding transparency",
            "Scientific misconduct penalties",
            "Open science requirements",
            "Embryonic research limitations",
            "Conflict of interest disclosure",
            "Data management plan mandates",
            "Research participant compensation",
            "Historical artifact research",
            "Biosecurity research protocols",
            "Vulnerable population research",
            "Collaborative research credit",
            "Replication crisis interventions",
            "Peer review process reform",
            "Publication bias prevention",
            "Research ethics education",
            "Predatory journal regulation",
            "Post-research subject care",
            "Neuroscience research boundaries",
            "Scientific censorship criteria"
        ],
        "International Relations Ethics": [
            "Humanitarian intervention criteria",
            "Economic sanctions morality",
            "Refugee admission quotas",
            "Foreign aid conditionality",
            "Border wall construction",
            "International climate obligations",
            "Diplomatic immunity limitations",
            "Immigration detention conditions",
            "Nuclear weapons possession",
            "Cultural heritage protection",
            "Cross-border data sovereignty",
            "International criminal jurisdiction",
            "Asylum seeker treatment",
            "Maritime territorial disputes",
            "Pandemic response cooperation",
            "International democracy promotion",
            "Military drone strike authorization",
            "Foreign election interference",
            "Extradition treaty limitations",
            "International trade fairness",
            "Cyber warfare boundaries",
            "Resource nationalism",
            "Global governance structures",
            "Colonial reparations",
            "Climate refugee status"
        ],
        "Religious Freedom": [
            "Religious exemptions from laws",
            "Religious symbols in public spaces",
            "Religious education in schools",
            "Workplace religious accommodation",
            "Religious freedom vs. LGBTQ+ rights",
            "Religious headwear restrictions",
            "Religious organization tax exemptions",
            "Religious hate speech regulation",
            "Religious objections to healthcare",
            "Faith-based initiative funding",
            "Religious slaughter practices",
            "Proselytizing regulation",
            "Religious property development",
            "Religious holiday recognition",
            "Religious courts authority",
            "Religious counseling regulation",
            "Religious institution autonomy",
            "Religious discrimination protections",
            "Religious minority protection",
            "Religious oaths in legal proceedings",
            "Religious influence in politics",
            "Sacred site protection",
            "Religion in military regulations",
            "Religious objections to technology",
            "Religious curriculum oversight"
        ],
        "Bioethics": [
            "CRISPR gene editing regulation",
            "Cloning technology applications",
            "Cognitive enhancement ethics",
            "Synthetic biology safeguards",
            "Human-animal chimera research",
            "Anti-aging intervention access",
            "Biological enhancement fairness",
            "Biometric identification ethics",
            "Brain-computer interface regulation",
            "Biological weapons research",
            "Germline modification moratorium",
            "Xenotransplantation safety",
            "Biobank consent requirements",
            "Biohacking regulation",
            "Genetic privacy protection",
            "Neurotechnology governance",
            "Synthetic embryo research",
            "Bio-surveillance ethics",
            "De-extinction priorities",
            "Gene drive deployment",
            "Digital biomarker collection",
            "Gain-of-function research",
            "Predictive genetic testing",
            "Mitochondrial replacement therapy",
            "Biological intellectual property"
        ],
        "Public Health Ethics": [
            "Vaccine mandate implementation",
            "Pandemic travel restrictions",
            "Public health data privacy",
            "Quarantine enforcement powers",
            "Sugar tax implementation",
            "Tobacco advertising bans",
            "Drug decriminalization",
            "E-cigarette regulation",
            "Mental health resource allocation",
            "Obesity intervention programs",
            "Alcohol consumption restrictions",
            "Antibiotic stewardship programs",
            "Healthcare resource rationing",
            "Recreational marijuana legalization",
            "Harm reduction strategies",
            "Maternal health prioritization",
            "Prescription drug price controls",
            "Universal healthcare implementation",
            "Disease reporting requirements",
            "School vaccination requirements",
            "Public health emergency powers",
            "Infectious disease containment",
            "Food safety regulation stringency",
            "Public health misinformation",
            "Behavioral health nudges"
        ],
        "Military Ethics": [
            "Autonomous weapons systems",
            "Civilian casualty tolerance",
            "Targeted killing authorization",
            "Military conscription policies",
            "Torture use in interrogation",
            "Private military contractor use",
            "Naval blockade ethics",
            "Preemptive strike doctrine",
            "Nuclear deterrence policy",
            "Biological weapon development",
            "Peacekeeping force composition",
            "Military humanitarian intervention",
            "Cyberwarfare boundaries",
            "Military technology transfer",
            "Dual-use technology export",
            "Combat zone civilian protection",
            "Military draft gender equality",
            "Weapons sales to authoritarian regimes",
            "Military medical experimentation",
            "Military environmental impact",
            "Insurgent combatant status",
            "Military chaplaincy diversity",
            "Wartime cultural heritage protection",
            "Defense budget allocation ethics",
            "Post-conflict reconstruction"
        ],
        "Economic Ethics": [
            "Wealth tax implementation",
            "Minimum wage levels",
            "Universal basic income",
            "Corporate tax avoidance",
            "Housing affordability interventions",
            "Predatory lending regulation",
            "Financial transaction tax",
            "Inheritance tax rates",
            "Cryptocurrency regulation",
            "Algorithmic trading oversight",
            "Economic sanctions targeting",
            "Sovereign debt forgiveness",
            "Trickle-down economics policy",
            "Monopoly power intervention",
            "Gig economy worker protections",
            "Carbon pricing mechanisms",
            "Resource nationalism policies",
            "Inflation targeting ethics",
            "Labor union right to organize",
            "Offshore financial centers",
            "Automation displacement response",
            "Luxury goods taxation",
            "Microfinance interest caps",
            "Currency manipulation prevention",
            "International trade agreement ethics"
        ]
    }
    
    # Generate an expanded set of topics beyond the templates by combining elements
    expanded_topics = []
    for category in categories:
        base_topics = topic_templates[category]
        expanded_topics.extend(base_topics)
        
        # Generate additional topics through combinations
        for i in range(min(20, len(base_topics))):
            topic1 = random.choice(base_topics)
            topic2 = random.choice(base_topics)
            if topic1 != topic2:
                combined = f"{topic1} in relation to {topic2}"
                expanded_topics.append(combined)
    
    # If we need even more topics, generate additional variations
    while len(expanded_topics) < num_topics * 2:  # Generate extra for selection
        category = random.choice(categories)
        topics = topic_templates[category]
        topic = random.choice(topics)
        
        # Add qualifiers to create variations
        qualifiers = [
            "global perspectives on", "cultural considerations in", 
            "ethical implications of", "religious views on", 
            "historical evolution of", "philosophical examination of",
            "future challenges regarding", "moral dimensions of",
            "legal framework for", "psychological impact of",
            "corporate responsibility in", "community-based approaches to",
            "educational aspects of", "technological impact on",
            "generational differences in", "rights-based approach to",
            "utilitarian perspective on", "deontological analysis of",
            "virtue ethics applied to", "consequentialist view of"
        ]
        
        variation = f"{random.choice(qualifiers)} {topic}"
        expanded_topics.append(variation)
    
    # Ensure we have enough unique topics
    unique_topics = list(set(expanded_topics))
    if len(unique_topics) < num_topics:
        # If we don't have enough unique topics, generate more combinations
        while len(unique_topics) < num_topics:
            cat1 = random.choice(categories)
            cat2 = random.choice(categories)
            topic1 = random.choice(topic_templates[cat1])
            topic2 = random.choice(topic_templates[cat2])
            combined = f"Intersection of {topic1} and {topic2}"
            unique_topics.append(combined)
            unique_topics = list(set(unique_topics))
    
    # Select the required number of topics
    selected_topics = random.sample(unique_topics, num_topics)
    return selected_topics

# Function to generate compelling for arguments
def generate_for_argument(topic):
    # Common argument structures
    structures = [
        "The principle of {principle} strongly supports {topic}. {evidence} Furthermore, {consequence}.",
        "From a {perspective} standpoint, {topic} is justified because {reason}. {example} This demonstrates {conclusion}.",
        "Supporting {topic} aligns with the core value of {value}. {elaboration} History has shown that {historical_example}.",
        "The ethical framework of {framework} provides clear support for {topic}. {explanation} This leads to {outcome}.",
        "Research indicates that {topic} results in {positive_outcome}. {data_point} This suggests {implication}.",
        "When examining {topic} through the lens of {lens}, we find compelling reasons to support it: {reasons}. {additional_point}",
        "The moral obligation to {obligation} necessitates support for {topic}. {reasoning} This is particularly evident when considering {consideration}.",
        "Proponents of {topic} emphasize {key_benefit}, which serves the greater good by {mechanism}. {supporting_evidence}",
        "Implementing {topic} honors the principle of {principle}, as demonstrated by {example}. {additional_benefit}",
        "The ethical justification for {topic} stems from {foundation}. {explanation} This creates a society where {vision}."
    ]
    
    # Values and principles that can be inserted
    principles = [
        "autonomy", "beneficence", "justice", "non-maleficence", "utility", "dignity", 
        "equality", "liberty", "compassion", "integrity", "solidarity", "transparency", 
        "sustainability", "stewardship", "responsibility", "fairness", "reciprocity"
    ]
    
    perspectives = [
        "utilitarian", "deontological", "virtue ethics", "rights-based", "care ethics", 
        "communitarian", "consequentialist", "social contract", "natural law", "pragmatic", 
        "feminist", "libertarian", "egalitarian", "religious", "secular humanist"
    ]
    
    values = [
        "human dignity", "personal liberty", "collective welfare", "procedural justice", 
        "cultural integrity", "traditional values", "scientific objectivity", 
        "democratic process", "individual rights", "social harmony", 
        "institutional integrity", "equal treatment", "free expression"
    ]
    
    frameworks = [
        "utilitarianism", "Kantian ethics", "virtue theory", "social contract theory", 
        "natural rights", "religious ethics", "discourse ethics", "communitarianism", 
        "principlism", "feminist ethics", "moral particularism", "care ethics"
    ]
    
    # Randomly select structure and fill with appropriate content
    structure = random.choice(structures)
    
    # Replace placeholders with topic-appropriate content
    argument = structure.replace("{topic}", topic)
    argument = argument.replace("{principle}", random.choice(principles))
    argument = argument.replace("{perspective}", random.choice(perspectives))
    argument = argument.replace("{value}", random.choice(values))
    argument = argument.replace("{framework}", random.choice(frameworks))
    
    # Generate topic-specific content
    if "Medical Ethics" in topic or "euthanasia" in topic.lower() or "vaccination" in topic.lower():
        evidence = "Medical studies demonstrate positive outcomes in regions where this approach is implemented."
        consequence = "patients maintain dignity and autonomy in their healthcare decisions"
        reason = "it enhances patient autonomy and reduces unnecessary suffering"
        example = "For instance, in countries with progressive medical policies, patient satisfaction and health outcomes have improved."
        conclusion = "that respect for individual medical choices strengthens the doctor-patient relationship"
    elif "Social Justice" in topic or "equality" in topic.lower() or "discrimination" in topic.lower():
        evidence = "Data from social equality initiatives shows significant improvements in community outcomes."
        consequence = "societal inequalities can be systematically addressed and reduced"
        reason = "it addresses historical injustices and creates more equitable opportunities"
        example = "Communities that have implemented such approaches show improved social cohesion and reduced disparities."
        conclusion = "that intentional equity measures lead to stronger, more unified societies"
    elif "Technology Ethics" in topic or "AI" in topic or "digital" in topic.lower():
        evidence = "Technological innovation governed by ethical frameworks has shown greater sustainability and public trust."
        consequence = "we can harness technological advancement while minimizing potential harms"
        reason = "it balances innovation with necessary safeguards against potential misuse"
        example = "Companies that have adopted stringent ethical guidelines for technology development have earned greater consumer trust."
        conclusion = "ethical technology development is not only morally right but also economically advantageous"
    elif "Environmental Ethics" in topic or "climate" in topic.lower() or "sustainable" in topic.lower():
        evidence = "Environmental protection measures have demonstrated long-term economic and ecological benefits."
        consequence = "future generations will inherit a more habitable and sustainable planet"
        reason = "it acknowledges our responsibility as stewards of the environment"
        example = "Regions that have prioritized environmental protection have experienced improved quality of life and economic resilience."
        conclusion = "environmental stewardship is both a moral imperative and practical necessity"
    elif "Business Ethics" in topic or "corporate" in topic.lower() or "workplace" in topic.lower():
        evidence = "Ethically-run businesses consistently outperform competitors in long-term stability and stakeholder satisfaction."
        consequence = "businesses can thrive while contributing positively to society"
        reason = "it recognizes that corporations have responsibilities beyond profit maximization"
        example = "Companies with strong ethical practices show greater employee retention and customer loyalty."
        conclusion = "that ethical business practices create sustainable competitive advantages"
    else:
        # Generic content for other topics
        evidence = "Evidence from both empirical studies and theoretical analyses supports this position."
        consequence = "we can create a more just and ethically sound society"
        reason = "it balances competing moral concerns in a way that respects fundamental values"
        example = "Similar approaches have proven successful in comparable contexts."
        conclusion = "that this approach offers the most ethically sound path forward"
    
    argument = argument.replace("{evidence}", evidence)
    argument = argument.replace("{consequence}", consequence)
    argument = argument.replace("{reason}", reason)
    argument = argument.replace("{example}", example)
    argument = argument.replace("{conclusion}", conclusion)
    
    # Fill in remaining placeholders with generic content
    generic_replacements = {
        "{elaboration}": "When properly implemented, this approach ensures that ethical considerations remain at the forefront.",
        "{historical_example}": "societies that uphold this value have consistently demonstrated better outcomes for all stakeholders",
        "{explanation}": "This framework prioritizes the balance between competing values that must be considered.",
        "{outcome}": "more equitable and sustainable outcomes for all parties involved",
        "{positive_outcome}": "measurable improvements in well-being and ethical outcomes",
        "{data_point}": "Multiple studies across different contexts confirm this correlation.",
        "{implication}": "this approach represents an ethically optimal solution",
        "{lens}": "stakeholder impact analysis",
        "{reasons}": "respect for dignity, promotion of welfare, and alignment with widely shared values",
        "{additional_point}": "Additionally, it stands up to scrutiny from multiple ethical traditions",
        "{obligation}": "respect human dignity and promote well-being",
        "{reasoning}": "Without this moral commitment, we risk undermining fundamental ethical principles",
        "{consideration}": "the most vulnerable stakeholders",
        "{key_benefit}": "the balancing of competing legitimate interests",
        "{mechanism}": "creating systems that respect both individual rights and collective welfare",
        "{supporting_evidence}": "Evidence from diverse contexts supports the efficacy of this approach",
        "{additional_benefit}": "This also helps establish a precedent for addressing similar ethical challenges",
        "{foundation}": "respect for the inherent worth of all persons",
        "{vision}": "fundamental rights and responsibilities are properly recognized"
    }
    
    
    for placeholder, replacement in generic_replacements.items():
        if placeholder in argument:
            argument = argument.replace(placeholder, replacement)
    
    return argument

# Function to generate compelling against arguments
def generate_against_argument(topic):
    # Common argument structures
    structures = [
        "Opposition to {topic} is grounded in the principle of {principle}. {evidence} Furthermore, {consequence}.",
        "From a {perspective} standpoint, {topic} is problematic because {reason}. {example} This illustrates {conclusion}.",
        "Rejecting {topic} protects the core value of {value}. {elaboration} Historical examples demonstrate {historical_example}.",
        "The ethical framework of {framework} raises serious concerns about {topic}. {explanation} This could lead to {outcome}.",
        "Evidence suggests that {topic} may result in {negative_outcome}. {data_point} This indicates {implication}.",
        "When analyzing {topic} through the lens of {lens}, significant ethical problems emerge: {problems}. {additional_point}",
        "The moral imperative to {imperative} necessitates opposition to {topic}. {reasoning} This becomes clear when considering {consideration}.",
        "Critics of {topic} highlight {key_concern}, which threatens social welfare by {mechanism}. {supporting_evidence}",
        "Implementing {topic} violates the principle of {principle}, as demonstrated by {example}. {additional_concern}",
        "The ethical case against {topic} centers on {foundation}. {explanation} This risks creating a society where {negative_vision}."
    ]
    
    # Values and principles that can be inserted
    principles = [
        "autonomy", "non-maleficence", "justice", "proportionality", "precaution", "dignity", 
        "equality", "liberty", "integrity", "transparency", "accountability", "sovereignty", 
        "subsidiarity", "solidarity", "privacy", "consent", "fairness"
    ]
    
    perspectives = [
        "utilitarian", "deontological", "virtue ethics", "rights-based", "care ethics", 
        "communitarian", "consequentialist", "social contract", "natural law", "pragmatic", 
        "feminist", "libertarian", "egalitarian", "religious", "secular humanist"
    ]
    
    values = [
        "human dignity", "personal freedom", "collective welfare", "scientific progress", 
        "environmental stewardship", "cultural diversity", "self-determination", 
        "democratic participation", "individual rights", "social cohesion", 
        "intergenerational justice", "equal opportunity", "compassionate care"
    ]
    
    frameworks = [
        "utilitarianism", "Kantian ethics", "virtue theory", "social contract theory", 
        "natural rights theory", "care ethics", "discourse ethics", "communitarianism", 
        "principlism", "liberation ethics", "feminist ethics", "pragmatic ethics"
    ]
    
    # Randomly select structure and fill with appropriate content
    structure = random.choice(structures)
    
    # Replace placeholders with topic-appropriate content
    argument = structure.replace("{topic}", topic)
    argument = argument.replace("{principle}", random.choice(principles))
    argument = argument.replace("{perspective}", random.choice(perspectives))
    argument = argument.replace("{value}", random.choice(values))
    argument = argument.replace("{framework}", random.choice(frameworks))
    
    # Generate topic-specific content
    if "Medical Ethics" in topic or "euthanasia" in topic.lower() or "vaccination" in topic.lower():
        evidence = "Medical practitioners express concern about potential abuses and erosion of professional ethics."
        consequence = "doctor-patient trust could be irrevocably damaged"
        reason = "it potentially compromises the medical profession's fundamental commitment to 'do no harm'"
        example = "Several documented cases show concerning unintended consequences when such policies are implemented."
        conclusion = "that medical ethics boundaries exist for crucial protective reasons"
    elif "Social Justice" in topic or "equality" in topic.lower() or "discrimination" in topic.lower():
        evidence = "Well-intentioned social interventions often create new forms of inequality or dependency."
        consequence = "existing social institutions could be undermined without adequate replacements"
        reason = "it may impose uniform solutions that fail to respect legitimate cultural and individual differences"
        example = "Similar programs have sometimes resulted in unintended negative consequences for the very groups they aimed to help."
        conclusion = "that good intentions must be balanced with practical outcomes"
    elif "Technology Ethics" in topic or "AI" in topic or "digital" in topic.lower():
        evidence = "Rapid technological implementation without sufficient ethical guardrails has led to significant societal harm."
        consequence = "fundamental human values like privacy and autonomy could be irreversibly compromised"
        reason = "it outpaces our ethical and regulatory frameworks' ability to ensure responsible implementation"
        example = "Recent technological developments have already demonstrated concerning unintended consequences."
        conclusion = "that technological advancement must proceed with appropriate caution and oversight"
    elif "Environmental Ethics" in topic or "climate" in topic.lower() or "sustainable" in topic.lower():
        evidence = "Environmental policies often disproportionately burden disadvantaged communities and developing nations."
        consequence = "economic development for vulnerable populations could be unjustly restricted"
        reason = "it sometimes prioritizes abstract environmental ideals over immediate human needs"
        example = "Environmental regulations have occasionally created severe economic hardships for communities dependent on traditional industries."
        conclusion = "that environmental policies must carefully balance ecological and human welfare concerns"
    elif "Business Ethics" in topic or "corporate" in topic.lower() or "workplace" in topic.lower():
        evidence = "Regulatory overreach can stifle innovation and economic growth essential for societal advancement."
        consequence = "businesses might relocate to regions with fewer restrictions, harming local economies"
        reason = "it may impose unrealistic standards that ignore market realities and competitive pressures"
        example = "Excessive corporate regulations have sometimes led to unintended negative economic consequences."
        conclusion = "that practical market considerations must inform ethical business frameworks"
    else:
        # Generic content for other topics
        evidence = "Critical analysis reveals significant potential downsides that proponents often overlook."
        consequence = "unintended consequences could undermine the very values this approach claims to uphold"
        reason = "it fails to adequately account for important competing ethical considerations"
        example = "Similar approaches in comparable contexts have revealed significant practical problems."
        conclusion = "that a more nuanced approach is ethically necessary"
    
    argument = argument.replace("{evidence}", evidence)
    argument = argument.replace("{consequence}", consequence)
    argument = argument.replace("{reason}", reason)
    argument = argument.replace("{example}", example)
    argument = argument.replace("{conclusion}", conclusion)
    
    # Fill in remaining placeholders with generic content
    generic_replacements = {
        "{elaboration}": "When examined carefully, this approach creates tensions with other important ethical values.",
        "{historical_example}": "similar interventions have led to problematic unintended consequences",
        "{explanation}": "This raises questions about whether the means justify the ends in this context.",
        "{outcome}": "concerning precedents that could be difficult to reverse",
        "{negative_outcome}": "unintended harmful consequences that proponents often minimize",
        "{data_point}": "Multiple studies raise concerns about its practical implementation.",
        "{implication}": "careful reconsideration is ethically necessary",
        "{lens}": "comprehensive impact analysis",
        "{problems}": "consent violations, dignity concerns, and potential misuse of authority",
        "{additional_point}": "Moreover, viable alternatives exist that avoid these ethical pitfalls",
        "{imperative}": "protect vulnerable populations from unintended consequences",
        "{reasoning}": "Ethical analysis requires considering both intentions and outcomes",
        "{consideration}": "potential misuse in real-world application",
        "{key_concern}": "the problematic power imbalances it creates",
        "{mechanism}": "prioritizing certain interests at the expense of equally valid considerations",
        "{supporting_evidence}": "Historical precedents demonstrate these concerns are well-founded",
        "{additional_concern}": "This creates troubling precedents for future ethical decisions",
        "{foundation}": "respect for pluralism and diverse ethical perspectives",
        "{negative_vision}": "important ethical distinctions are dangerously blurred"
    }
    
    for placeholder, replacement in generic_replacements.items():
        if placeholder in argument:
            argument = argument.replace(placeholder, replacement)
    
    return argument

# Create the CSV with 2500 ethical and moral debate records
def create_ethical_debates_csv(filename, num_records=3000):
    topics = generate_topics(num_records)
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['topic', 'for_argument', 'against_argument']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for topic in topics:
            for_argument = generate_for_argument(topic)
            against_argument = generate_against_argument(topic)
            
            writer.writerow({
                'topic': topic,
                'for_argument': for_argument,
                'against_argument': against_argument
            })

# Generate the CSV file
create_ethical_debates_csv('ethical.csv', 3000)

# Display sample of the dataset
import pandas as pd

try:
    df = pd.read_csv('ethical_moral_debates.csv')
    print(f"Dataset created with {len(df)} records")
    print("\nSample of 5 records from the dataset:")
    print(df.sample(5).to_string())
except Exception as e:
    print(f"Error reading the created CSV: {e}")
    print("Sample of what the dataset would look like:")
    
    # Generate sample records
    sample_topics = generate_topics(5)
    sample_data = []
    for topic in sample_topics:
        for_arg = generate_for_argument(topic)
        against_arg = generate_against_argument(topic)
        sample_data.append({
            'topic': topic,
            'for_argument': for_arg,
            'against_argument': against_arg
        })
    
    sample_df = pd.DataFrame(sample_data)
    print(sample_df.to_string())
    