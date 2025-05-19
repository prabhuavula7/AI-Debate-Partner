import random
import csv

# Extended health ethics topics (25 items)
topic_templates = {
    "Health Ethics": [
        "Mandatory vaccination policies",
        "Physician-assisted suicide legalization",
        "Universal healthcare as a human right",
        "Genetic editing of embryos",
        "Organ donation opt-out systems",
        "Healthcare rationing in pandemics",
        "Confidentiality vs. duty to warn",
        "AI diagnosis and medical liability",
        "Pharmaceutical patent protections",
        "Mental health parity in insurance",
        "Telemedicine and patient privacy",
        "Resource allocation for rare diseases",
        "Drug decriminalization and public health",
        "Quarantine enforcement and civil liberties",
        "Compulsory treatment for infectious diseases",
        "End-of-life decision-making autonomy",
        "Direct-to-consumer genetic testing",
        "Healthcare for undocumented immigrants",
        "Medical experimentation on prisoners",
        "Advertising prescription drugs to consumers",
        "Parental refusal of life-saving treatment for children",
        "Mandatory reporting of infectious diseases",
        "Cosmetic surgery for minors",
        "Nutritional labeling mandates",
        "Ethics of placebo use in clinical trials"
    ]
}

def generate_health_ethics_topics(num_topics=1000):
    base_topics = topic_templates["Health Ethics"]
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
    
    health_components = {
        "principles": ["beneficence", "justice", "autonomy", "non-maleficence", "solidarity"],
        "perspectives": ["public health ethics", "bioethics", "utilitarianism", "rights-based ethics", "care ethics"],
        "values": ["well-being", "equity", "patient dignity", "accessibility", "prevention"],
        "frameworks": ["principlism", "distributive justice", "virtue ethics", "capabilities approach", "health equity"]
    }

    structure = random.choice(structures)
    argument = structure.replace("{topic}", topic)
    
    argument = argument.replace("{principle}", random.choice(health_components["principles"]))
    argument = argument.replace("{perspective}", random.choice(health_components["perspectives"]))
    argument = argument.replace("{value}", random.choice(health_components["values"]))
    argument = argument.replace("{framework}", random.choice(health_components["frameworks"]))
    
    health_replacements = {
        "{evidence}": "Extensive medical research supports this position",
        "{consequence}": "improved population health outcomes and reduced disparities",
        "{reason}": "it balances individual rights with collective well-being",
        "{example}": "As demonstrated by successful vaccination campaigns",
        "{conclusion}": "this approach is both ethical and effective",
        "{elaboration}": "When implemented with sensitivity to patient needs",
        "{historical_example}": "the eradication of smallpox through global cooperation",
        "{explanation}": "This framework ensures fairness and respect for all patients",
        "{outcome}": "more just and resilient healthcare systems",
        "{positive_outcome}": "higher life expectancy and quality of life",
        "{data_point}": "WHO data consistently links these policies to better outcomes",
        "{implication}": "health policy should reflect these ethical priorities",
        "{lens}": "social determinants of health analysis",
        "{reasons}": "justice, compassion, and evidence-based practice",
        "{additional_point}": "This aligns with the Universal Declaration of Bioethics and Human Rights",
        "{obligation}": "protect vulnerable populations from preventable harm",
        "{reasoning}": "Health ethics demand proactive and inclusive approaches",
        "{consideration}": "the needs of the most marginalized patients",
        "{key_benefit}": "universal access to essential care",
        "{mechanism}": "removing barriers to treatment and prevention",
        "{supporting_evidence}": "Peer-reviewed studies confirm these benefits",
        "{additional_benefit}": "This also strengthens public trust in healthcare",
        "{foundation}": "the intrinsic value of human health",
        "{vision}": "everyone enjoys the highest attainable standard of health"
    }
    
    for placeholder, replacement in health_replacements.items():
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
        "Critics of {topic} highlight {key_concern}, which threatens health ethics by {mechanism}. {supporting_evidence}",
        "Implementing {topic} violates the principle of {principle}, as demonstrated by {example}. {additional_concern}",
        "The ethical case against {topic} centers on {foundation}. {explanation} This risks creating a healthcare system where {negative_vision}."
    ]

    health_components = {
        "principles": ["personal autonomy", "privacy", "least harm", "proportionality", "subsidiarity"],
        "perspectives": ["libertarian bioethics", "classical liberalism", "market-based health ethics", "minimal state theory", "individual rights theory"],
        "values": ["freedom of choice", "confidentiality", "personal responsibility", "innovation", "efficiency"],
        "frameworks": ["minimal intervention", "market ethics", "negative liberty", "pluralistic bioethics", "rights-based minimalism"]
    }

    structure = random.choice(structures)
    argument = structure.replace("{topic}", topic)
    
    argument = argument.replace("{principle}", random.choice(health_components["principles"]))
    argument = argument.replace("{perspective}", random.choice(health_components["perspectives"]))
    argument = argument.replace("{value}", random.choice(health_components["values"]))
    argument = argument.replace("{framework}", random.choice(health_components["frameworks"]))
    
    health_replacements = {
        "{evidence}": "Critical analysis of health mandates reveals",
        "{consequence}": "reduced personal freedom and unintended negative outcomes",
        "{reason}": "it can override individual rights and informed consent",
        "{example}": "As seen in controversies over compulsory quarantine",
        "{conclusion}": "this approach risks undermining trust in healthcare",
        "{elaboration}": "When considering diverse patient values and beliefs",
        "{historical_example}": "the backlash to forced sterilization policies",
        "{explanation}": "This framework may neglect the importance of autonomy",
        "{outcome}": "patient disengagement and non-compliance",
        "{negative_outcome}": "inefficiency and inequity in care delivery",
        "{data_point}": "Health policy reviews show mixed results from mandates",
        "{implication}": "cautious, patient-centered approaches are preferable",
        "{lens}": "autonomy-based health analysis",
        "{problems}": "loss of trust, reduced innovation, and ethical conflicts",
        "{additional_point}": "Flexible models may better respect diversity",
        "{imperative}": "preserve patient choice and informed consent",
        "{reasoning}": "Ethics require respecting each person's health decisions",
        "{consideration}": "the rights of dissenting patients",
        "{key_concern}": "the risk of medical paternalism",
        "{mechanism}": "imposing top-down mandates without patient input",
        "{supporting_evidence}": "Case studies show that voluntary approaches can succeed",
        "{additional_concern}": "This may discourage innovation in care",
        "{foundation}": "the primacy of patient autonomy",
        "{negative_vision}": "healthcare becomes coercive and impersonal"
    }
    
    for placeholder, replacement in health_replacements.items():
        argument = argument.replace(placeholder, replacement)
        
    return argument

def create_healthethics_debates_csv(filename, num_records=1000):
    topics = generate_health_ethics_topics(num_records)
    
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
create_healthethics_debates_csv('ethical.csv', 1000)