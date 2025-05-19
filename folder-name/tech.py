import random
import csv

# Extended technology ethics topics (25 items)
topic_templates = {
    "Technology Ethics": [
        "Facial recognition in public surveillance",
        "Algorithmic bias in hiring platforms",
        "Autonomous weapons and military AI",
        "Data privacy in consumer devices",
        "Right to repair digital products",
        "Deepfake technology and misinformation",
        "Ethics of brain-computer interfaces",
        "AI-driven predictive policing",
        "Genetic data sharing and consent",
        "Social media addiction and design responsibility",
        "Self-driving cars and accident liability",
        "Ethical use of drones in civilian life",
        "Digital divide in access to emerging technologies",
        "Tech company monopolies and antitrust regulation",
        "Biometric authentication and identity theft",
        "Quantum computing and cryptography ethics",
        "Open-source software and intellectual property",
        "Ethical design of persuasive technologies",
        "Internet censorship by private platforms",
        "Digital legacy and posthumous data rights",
        "Wearable health tech and medical privacy",
        "Automation and job displacement",
        "Cybersecurity and ethical hacking",
        "Virtual reality and psychological effects",
        "NFTs and digital ownership rights"
    ]
}

def generate_technology_ethics_topics(num_topics=1000):
    base_topics = topic_templates["Technology Ethics"]
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
    
    tech_components = {
        "principles": ["innovation", "user autonomy", "digital justice",
                      "transparency", "responsible stewardship"],
        "perspectives": ["techno-progressivism", "utilitarianism", 
                        "rights-based digital ethics", "open access philosophy",
                        "human-centered design"],
        "values": ["accessibility", "security", "transparency",
                  "empowerment", "digital inclusion"],
        "frameworks": ["responsible innovation", "privacy by design", 
                      "algorithmic fairness", "AI ethics",
                      "digital humanism"]
    }

    structure = random.choice(structures)
    argument = structure.replace("{topic}", topic)
    
    argument = argument.replace("{principle}", random.choice(tech_components["principles"]))
    argument = argument.replace("{perspective}", random.choice(tech_components["perspectives"]))
    argument = argument.replace("{value}", random.choice(tech_components["values"]))
    argument = argument.replace("{framework}", random.choice(tech_components["frameworks"]))
    
    tech_replacements = {
        "{evidence}": "Empirical studies in technology ethics demonstrate",
        "{consequence}": "increased trust and broader adoption of new technologies",
        "{reason}": "it balances technological advancement with fundamental rights",
        "{example}": "As seen in the European GDPR framework",
        "{conclusion}": "this approach sets a benchmark for ethical tech governance",
        "{elaboration}": "When implemented with robust oversight and transparency",
        "{historical_example}": "the open-source movement's transformative impact",
        "{explanation}": "This framework ensures technology serves human interests",
        "{outcome}": "safer, more equitable digital environments",
        "{positive_outcome}": "greater innovation and reduced harm",
        "{data_point}": "IEEE reports show positive outcomes from ethical tech adoption",
        "{implication}": "tech development should be guided by these principles",
        "{lens}": "algorithmic impact assessment",
        "{reasons}": "fairness, accountability, and user empowerment",
        "{additional_point}": "This aligns with international digital rights charters",
        "{obligation}": "protect users from foreseeable digital harms",
        "{reasoning}": "Ethical tech requires proactive risk mitigation",
        "{consideration}": "the needs of digitally marginalized groups",
        "{key_benefit}": "trustworthy and inclusive technology",
        "{mechanism}": "embedding ethics into design and deployment",
        "{supporting_evidence}": "Peer-reviewed studies confirm these benefits",
        "{additional_benefit}": "This also fosters global interoperability",
        "{foundation}": "the right to digital self-determination",
        "{vision}": "technology enhances, rather than undermines, human flourishing"
    }
    
    for placeholder, replacement in tech_replacements.items():
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
        "Critics of {topic} highlight {key_concern}, which threatens tech ethics by {mechanism}. {supporting_evidence}",
        "Implementing {topic} violates the principle of {principle}, as demonstrated by {example}. {additional_concern}",
        "The ethical case against {topic} centers on {foundation}. {explanation} This risks creating a digital world where {negative_vision}."
    ]

    tech_components = {
        "principles": ["user consent", "minimal intervention", "open competition",
                      "privacy", "individual autonomy"],
        "perspectives": ["technological libertarianism", "market-driven innovation", 
                        "skeptical empiricism", "digital pluralism",
                        "open-source advocacy"],
        "values": ["freedom of choice", "market efficiency", 
                  "flexibility", "user control", "innovation"],
        "frameworks": ["minimal regulation", "market ethics", 
                      "pluralistic digital ethics", "individual rights theory",
                      "bottom-up governance"]
    }

    structure = random.choice(structures)
    argument = structure.replace("{topic}", topic)
    
    argument = argument.replace("{principle}", random.choice(tech_components["principles"]))
    argument = argument.replace("{perspective}", random.choice(tech_components["perspectives"]))
    argument = argument.replace("{value}", random.choice(tech_components["values"]))
    argument = argument.replace("{framework}", random.choice(tech_components["frameworks"]))
    
    tech_replacements = {
        "{evidence}": "Critical assessments of tech regulation reveal",
        "{consequence}": "reduced innovation and increased compliance burdens",
        "{reason}": "it risks stifling creativity and competitive markets",
        "{example}": "As seen in the slow adoption of new medical devices under strict regimes",
        "{conclusion}": "this approach could limit technological progress",
        "{elaboration}": "When considering the rapid pace of digital change",
        "{historical_example}": "the chilling effects of early internet censorship",
        "{explanation}": "This framework underestimates the adaptability of users and markets",
        "{outcome}": "fragmented digital ecosystems and user frustration",
        "{negative_outcome}": "barriers to entry for small innovators",
        "{data_point}": "Tech industry reports show regulatory drag on startups",
        "{implication}": "flexible, adaptive approaches may be preferable",
        "{lens}": "market impact analysis",
        "{problems}": "overregulation, innovation bottlenecks, and loss of user agency",
        "{additional_point}": "Open standards can achieve similar goals without heavy-handed rules",
        "{imperative}": "preserve the freedom to innovate",
        "{reasoning}": "Ethical tech policy should avoid unintended negative side effects",
        "{consideration}": "the needs of emerging tech sectors",
        "{key_concern}": "the risk of centralized control over digital life",
        "{mechanism}": "imposing uniform solutions on diverse technologies",
        "{supporting_evidence}": "Case studies of regulatory overreach confirm these risks",
        "{additional_concern}": "This may drive innovation offshore",
        "{foundation}": "the value of decentralized digital ecosystems",
        "{negative_vision}": "users are disempowered and progress stalls"
    }
    
    for placeholder, replacement in tech_replacements.items():
        argument = argument.replace(placeholder, replacement)
        
    return argument

def create_technologyethics_debates_csv(filename, num_records=1000):
    topics = generate_technology_ethics_topics(num_records)
    
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
create_technologyethics_debates_csv('ethical.csv', 1000)
