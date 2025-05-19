import random
import csv

# Extended topic templates for Educational Ethics with 25 items
topic_templates = {
    "Educational Ethics": [
        "School surveillance systems in public education",
        "Student data privacy protections in digital learning",
        "Academic freedom limitations in controversial topics",
        "Standardized testing emphasis over creative thinking",
        "Homeschooling regulation and oversight requirements",
        "Religious education funding in public institutions",
        "Critical thinking vs. cultural sensitivity balance",
        "Zero-tolerance disciplinary policies in urban schools",
        "Gifted education programs and equity concerns",
        "College legacy admissions and meritocracy debate",
        "AI-powered grading systems in student assessment",
        "Ideological diversity in curriculum development",
        "Student loan forgiveness programs and fiscal responsibility",
        "Trigger warnings in university course materials",
        "School resource officer presence and student safety",
        "Free speech limitations on college campuses",
        "Grade inflation practices and academic integrity",
        "Student social media monitoring by administrations",
        "Behavioral tracking systems in K-12 education",
        "Performance-based teacher pay structures",
        "Digital divide intervention strategies in rural areas",
        "Character education requirements in public schools",
        "Charter school expansion and public funding debates",
        "Mandatory community service for high school graduation",
        "National history curriculum standardization efforts"
    ]
}

def generate_educational_ethics_topics(num_topics=1000):
    base_topics = topic_templates["Educational Ethics"]
    return random.sample(base_topics, min(num_topics, len(base_topics)))

def generate_for_argument(topic):
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
    
    ethical_components = {
        "principles": ["educational equity", "academic freedom", "student welfare", 
                      "institutional accountability", "pedagogical integrity"],
        "perspectives": ["progressive education", "outcome-based learning", 
                        "holistic development", "social reconstructionism",
                        "essentialist pedagogy"],
        "values": ["intellectual growth", "critical inquiry", "diverse perspectives",
                  "lifelong learning", "educational access"],
        "frameworks": ["constructivist ethics", "critical pedagogy", 
                      "transformative learning theory", "social learning ethics",
                      "distributive educational justice"]
    }

    structure = random.choice(structures)
    argument = structure.replace("{topic}", topic)
    
    # First-level replacements
    argument = argument.replace("{principle}", random.choice(ethical_components["principles"]))
    argument = argument.replace("{perspective}", random.choice(ethical_components["perspectives"]))
    argument = argument.replace("{value}", random.choice(ethical_components["values"]))
    argument = argument.replace("{framework}", random.choice(ethical_components["frameworks"]))
    
    # Education-specific content
    education_replacements = {
        "{evidence}": "Longitudinal studies in educational psychology demonstrate",
        "{consequence}": "improved learning outcomes and more equitable systems",
        "{reason}": "it addresses systemic inequities while maintaining academic rigor",
        "{example}": "As seen in the success of Scandinavian education models",
        "{conclusion}": "this approach fosters both individual and societal growth",
        "{elaboration}": "When implemented with proper safeguards and resources",
        "{historical_example}": "the GI Bill's impact on higher education access",
        "{explanation}": "This framework prioritizes student needs over bureaucratic convenience",
        "{outcome}": "a more engaged and empowered student population",
        "{positive_outcome}": "higher graduation rates and reduced achievement gaps",
        "{data_point}": "NCES data shows correlations with improved social mobility",
        "{implication}": "educational policy should prioritize this approach",
        "{lens}": "critical race theory in education",
        "{reasons}": "equity, accessibility, and pedagogical effectiveness",
        "{additional_point}": "This aligns with UNESCO's education sustainability goals",
        "{obligation}": "provide equal educational opportunities",
        "{reasoning}": "Educational ethics demand we address systemic barriers",
        "{consideration}": "underrepresented student populations",
        "{key_benefit}": "democratization of educational resources",
        "{mechanism}": "leveling the playing field for disadvantaged students",
        "{supporting_evidence}": "Peer-reviewed research from leading education journals confirms",
        "{additional_benefit}": "This also strengthens community-school partnerships",
        "{foundation}": "the fundamental right to quality education",
        "{vision}": "every learner can achieve their full potential"
    }
    
    for placeholder, replacement in education_replacements.items():
        argument = argument.replace(placeholder, replacement)
        
    return argument

def generate_against_argument(topic):
    structures = [
        "Opposition to {topic} is grounded in the principle of {principle}. {evidence} Furthermore, {consequence}.",
        "From a {perspective} standpoint, {topic} is problematic because {reason}. {example} This illustrates {conclusion}.",
        "Rejecting {topic} protects the core value of {value}. {elaboration} Historical examples demonstrate {historical_example}.",
        "The ethical framework of {framework} raises serious concerns about {topic}. {explanation} This could lead to {outcome}.",
        "Evidence suggests that {topic} may result in {negative_outcome}. {data_point} This indicates {implication}.",
        "When analyzing {topic} through the lens of {lens}, significant ethical problems emerge: {problems}. {additional_point}",
        "The moral imperative to {imperative} necessitates opposition to {topic}. {reasoning} This becomes clear when considering {consideration}.",
        "Critics of {topic} highlight {key_concern}, which threatens educational quality by {mechanism}. {supporting_evidence}",
        "Implementing {topic} violates the principle of {principle}, as demonstrated by {example}. {additional_concern}",
        "The ethical case against {topic} centers on {foundation}. {explanation} This risks creating an education system where {negative_vision}."
    ]

    ethical_components = {
        "principles": ["local control", "parental rights", "academic neutrality",
                      "institutional autonomy", "merit-based advancement"],
        "perspectives": ["classical education", "traditional pedagogy", 
                        "conservative reform", "libertarian education",
                        "cultural preservation"],
        "values": ["academic excellence", "individual responsibility", 
                  "curricular stability", "institutional heritage",
                  "pedagogical independence"],
        "frameworks": ["essentialist ethics", "meritocratic principles", 
                      "localism in education", "cultural conservatism",
                      "autonomy-based pedagogy"]
    }

    structure = random.choice(structures)
    argument = structure.replace("{topic}", topic)
    
    # First-level replacements
    argument = argument.replace("{principle}", random.choice(ethical_components["principles"]))
    argument = argument.replace("{perspective}", random.choice(ethical_components["perspectives"]))
    argument = argument.replace("{value}", random.choice(ethical_components["values"]))
    argument = argument.replace("{framework}", random.choice(ethical_components["frameworks"]))
    
    # Education-specific content
    education_replacements = {
        "{evidence}": "Case studies of failed educational initiatives reveal",
        "{consequence}": "erosion of academic standards and parental autonomy",
        "{reason}": "it imposes one-size-fits-all solutions on diverse student populations",
        "{example}": "As evidenced by the Common Core implementation challenges",
        "{conclusion}": "this approach undermines educational diversity and choice",
        "{elaboration}": "When considering the complex realities of classroom dynamics",
        "{historical_example}": "the unintended consequences of No Child Left Behind",
        "{explanation}": "This framework neglects practical implementation challenges",
        "{outcome}": "increased bureaucracy and reduced teacher autonomy",
        "{negative_outcome}": "decreased academic rigor and institutional overreach",
        "{data_point}": "NAEP scores indicate stagnation in critical thinking skills",
        "{implication}": "we must reconsider top-down educational mandates",
        "{lens}": "educational libertarianism",
        "{problems}": "overstandardization, reduced innovation, and cultural erasure",
        "{additional_point}": "This contradicts the OECD's recommendations for educational flexibility",
        "{imperative}": "preserve educational diversity",
        "{reasoning}": "Local communities best understand their students' needs",
        "{consideration}": "the rights of private and homeschooling families",
        "{key_concern}": "the centralization of educational decision-making",
        "{mechanism}": "stifling pedagogical innovation and parental involvement",
        "{supporting_evidence}": "Longitudinal studies of charter school systems demonstrate",
        "{additional_concern}": "This sets dangerous precedents for ideological indoctrination",
        "{foundation}": "the pluralistic nature of educational philosophy",
        "{negative_vision}": "individual learning needs are sacrificed for political agendas"
    }
    
    for placeholder, replacement in education_replacements.items():
        argument = argument.replace(placeholder, replacement)
        
    return argument

def create_educationalethics_debates_csv(filename, num_records=1000):
    topics = generate_educational_ethics_topics(num_records)
    
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
create_educationalethics_debates_csv('ethical.csv', 1000)
