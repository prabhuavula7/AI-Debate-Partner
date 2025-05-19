import random
import csv

# Extended societal ethics topics (25 items)
topic_templates = {
    "Societal Ethics": [
        "Universal basic income implementation",
        "Facial recognition technology in public spaces",
        "Mandatory vaccination policies",
        "Social media censorship and misinformation",
        "Affirmative action in employment",
        "Genetic engineering for human enhancement",
        "Public funding for the arts",
        "Data privacy in the age of big tech",
        "Universal healthcare access",
        "Decriminalization of recreational drugs",
        "Ethical use of predictive policing",
        "Right to be forgotten online",
        "Regulation of gig economy platforms",
        "Compulsory military or civic service",
        "Ethical consumption and fair trade",
        "Animal rights in industrial agriculture",
        "Climate change mitigation responsibilities",
        "Digital divide and internet access equity",
        "Hate speech regulation in society",
        "Surveillance capitalism and consumer rights",
        "Reparations for historical injustices",
        "Universal childcare support",
        "Ethics of euthanasia and assisted dying",
        "Urban gentrification and displacement",
        "Cashless society and financial inclusion"
    ]
}

def generate_societal_ethics_topics(num_topics=1000):
    base_topics = topic_templates["Societal Ethics"]
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
    
    societal_components = {
        "principles": ["social justice", "solidarity", "dignity", 
                      "collective responsibility", "reciprocity"],
        "perspectives": ["communitarianism", "social contract theory", 
                        "utilitarianism", "capabilities approach",
                        "care ethics"],
        "values": ["inclusion", "equity", "mutual respect",
                  "public welfare", "compassion"],
        "frameworks": ["distributive justice", "rights-based ethics", 
                      "virtue ethics", "intersectional analysis",
                      "sustainability ethics"]
    }

    structure = random.choice(structures)
    argument = structure.replace("{topic}", topic)
    
    argument = argument.replace("{principle}", random.choice(societal_components["principles"]))
    argument = argument.replace("{perspective}", random.choice(societal_components["perspectives"]))
    argument = argument.replace("{value}", random.choice(societal_components["values"]))
    argument = argument.replace("{framework}", random.choice(societal_components["frameworks"]))
    
    society_replacements = {
        "{evidence}": "Extensive sociological research demonstrates",
        "{consequence}": "greater social cohesion and reduced inequality",
        "{reason}": "it addresses longstanding disparities while fostering community resilience",
        "{example}": "As seen in the success of Nordic welfare models",
        "{conclusion}": "this approach promotes a more just and inclusive society",
        "{elaboration}": "When implemented with attention to marginalized groups",
        "{historical_example}": "the civil rights movement's impact on social norms",
        "{explanation}": "This framework centers marginalized voices and collective well-being",
        "{outcome}": "enhanced trust and cooperation among citizens",
        "{positive_outcome}": "improved quality of life and social mobility",
        "{data_point}": "UN Human Development Index trends support these outcomes",
        "{implication}": "social policy should reflect these priorities",
        "{lens}": "intersectional social analysis",
        "{reasons}": "justice, solidarity, and the common good",
        "{additional_point}": "This aligns with the Universal Declaration of Human Rights",
        "{obligation}": "reduce preventable suffering and injustice",
        "{reasoning}": "Societal ethics require proactive measures for vulnerable populations",
        "{consideration}": "the needs of historically marginalized communities",
        "{key_benefit}": "broad-based social empowerment",
        "{mechanism}": "removing systemic barriers to opportunity",
        "{supporting_evidence}": "Meta-analyses in social policy literature confirm",
        "{additional_benefit}": "This also fosters intergenerational equity",
        "{foundation}": "the inherent worth of every person",
        "{vision}": "everyone can participate fully in society"
    }
    
    for placeholder, replacement in society_replacements.items():
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
        "Critics of {topic} highlight {key_concern}, which threatens social ethics by {mechanism}. {supporting_evidence}",
        "Implementing {topic} violates the principle of {principle}, as demonstrated by {example}. {additional_concern}",
        "The ethical case against {topic} centers on {foundation}. {explanation} This risks creating a society where {negative_vision}."
    ]

    societal_components = {
        "principles": ["personal autonomy", "subsidiarity", "proportionality", 
                      "freedom of association", "individual responsibility"],
        "perspectives": ["libertarianism", "classical liberalism", 
                        "cultural conservatism", "minimal state theory",
                        "pluralism"],
        "values": ["self-determination", "voluntary cooperation", 
                  "tradition", "privacy", "market freedom"],
        "frameworks": ["minimal state ethics", "rights-based libertarianism", 
                      "cultural relativism", "virtue conservatism",
                      "negative liberty"]
    }

    structure = random.choice(structures)
    argument = structure.replace("{topic}", topic)
    
    argument = argument.replace("{principle}", random.choice(societal_components["principles"]))
    argument = argument.replace("{perspective}", random.choice(societal_components["perspectives"]))
    argument = argument.replace("{value}", random.choice(societal_components["values"]))
    argument = argument.replace("{framework}", random.choice(societal_components["frameworks"]))
    
    society_replacements = {
        "{evidence}": "Critical analysis of social interventions reveals",
        "{consequence}": "reduced personal freedom and unintended social stratification",
        "{reason}": "it imposes collective solutions at the expense of individual rights",
        "{example}": "As seen in the failures of some large-scale welfare programs",
        "{conclusion}": "this approach risks undermining social diversity",
        "{elaboration}": "When considering the diversity of values in society",
        "{historical_example}": "the unintended effects of prohibition policies",
        "{explanation}": "This framework overlooks the importance of voluntary association",
        "{outcome}": "dependency and decreased civic engagement",
        "{negative_outcome}": "inefficiency and bureaucratic overreach",
        "{data_point}": "World Bank reports highlight mixed results",
        "{implication}": "caution is warranted before large-scale implementation",
        "{lens}": "classical liberal social theory",
        "{problems}": "loss of initiative, crowding out of private solutions, and cultural homogenization",
        "{additional_point}": "Decentralized approaches may better respect diversity",
        "{imperative}": "safeguard freedom of choice and association",
        "{reasoning}": "Ethical pluralism values a diversity of social arrangements",
        "{consideration}": "the rights of minority or dissenting groups",
        "{key_concern}": "the expansion of state power over daily life",
        "{mechanism}": "centralizing authority in distant institutions",
        "{supporting_evidence}": "Comparative studies show more flexible models can succeed",
        "{additional_concern}": "This can erode trust in voluntary civil society",
        "{foundation}": "the value of decentralized social organization",
        "{negative_vision}": "individuals lose agency and community bonds weaken"
    }
    
    for placeholder, replacement in society_replacements.items():
        argument = argument.replace(placeholder, replacement)
        
    return argument

def create_societalethics_debates_csv(filename, num_records=1000):
    topics = generate_societal_ethics_topics(num_records)
    
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
create_societalethics_debates_csv('ethical.csv', 1000)
