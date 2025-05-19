import random
import csv

# Extended environmental ethics topics (25 items)
topic_templates = {
    "Environmental Ethics": [
        "Geoengineering to combat climate change",
        "Carbon taxes and emissions trading",
        "Nuclear energy as a green solution",
        "Biodiversity conservation vs. economic development",
        "Animal rights in industrial farming",
        "Plastic bans and consumer freedom",
        "Genetically modified organisms in agriculture",
        "Rewilding and species reintroduction",
        "Environmental justice for marginalized communities",
        "Ecotourism and indigenous land rights",
        "Urban green spaces vs. housing needs",
        "Corporate responsibility for pollution",
        "Renewable energy subsidies",
        "Meat consumption and climate ethics",
        "Water privatization and access rights",
        "Climate refugees and immigration policy",
        "Deep-sea mining and ocean conservation",
        "Deforestation for economic growth",
        "Mandatory recycling laws",
        "Population control and sustainability",
        "Wildlife culling for ecosystem balance",
        "Carbon offset markets and greenwashing",
        "Environmental activism and civil disobedience",
        "Green technology patents vs. open access",
        "Ethics of animal testing for conservation"
    ]
}

def generate_environmental_ethics_topics(num_topics=1000):
    base_topics = topic_templates["Environmental Ethics"]
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
    
    env_components = {
        "principles": ["sustainability", "precautionary principle", "intergenerational justice",
                      "stewardship", "ecological integrity"],
        "perspectives": ["deep ecology", "biocentrism", "environmental pragmatism",
                        "eco-justice", "land ethic"],
        "values": ["biodiversity", "planetary health", "renewability",
                  "resilience", "natural harmony"],
        "frameworks": ["sustainable development", "rights of nature",
                      "environmental virtue ethics", "conservation biology",
                      "ecofeminism"]
    }

    structure = random.choice(structures)
    argument = structure.replace("{topic}", topic)
    
    argument = argument.replace("{principle}", random.choice(env_components["principles"]))
    argument = argument.replace("{perspective}", random.choice(env_components["perspectives"]))
    argument = argument.replace("{value}", random.choice(env_components["values"]))
    argument = argument.replace("{framework}", random.choice(env_components["frameworks"]))
    
    env_replacements = {
        "{evidence}": "Environmental science research consistently demonstrates",
        "{consequence}": "long-term ecosystem stability and human well-being",
        "{reason}": "it addresses urgent ecological crises while balancing human needs",
        "{example}": "As seen in Costa Rica's national reforestation efforts",
        "{conclusion}": "this approach ensures a viable future for all species",
        "{elaboration}": "When guided by the best available ecological evidence",
        "{historical_example}": "the Montreal Protocol's success in ozone recovery",
        "{explanation}": "This framework integrates ethical responsibility with scientific insight",
        "{outcome}": "healthier environments and more resilient societies",
        "{positive_outcome}": "reduced pollution and improved quality of life",
        "{data_point}": "UNEP reports confirm measurable progress with these policies",
        "{implication}": "environmental policy should be proactive and preventive",
        "{lens}": "life-cycle environmental assessment",
        "{reasons}": "justice, sustainability, and respect for natural limits",
        "{additional_point}": "This aligns with the Paris Agreement's global commitments",
        "{obligation}": "protect the planet for future generations",
        "{reasoning}": "Environmental ethics require urgent and collective action",
        "{consideration}": "the most vulnerable ecosystems and communities",
        "{key_benefit}": "preservation of irreplaceable natural capital",
        "{mechanism}": "integrating sustainability into all decision-making",
        "{supporting_evidence}": "Peer-reviewed meta-analyses support this approach",
        "{additional_benefit}": "This also fosters green economic innovation",
        "{foundation}": "the intrinsic value of nature",
        "{vision}": "humanity lives in balance with the environment"
    }
    
    for placeholder, replacement in env_replacements.items():
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
        "Critics of {topic} highlight {key_concern}, which threatens environmental ethics by {mechanism}. {supporting_evidence}",
        "Implementing {topic} violates the principle of {principle}, as demonstrated by {example}. {additional_concern}",
        "The ethical case against {topic} centers on {foundation}. {explanation} This risks creating a world where {negative_vision}."
    ]

    env_components = {
        "principles": ["human welfare", "economic development", "resource sovereignty",
                      "technological optimism", "proportionality"],
        "perspectives": ["anthropocentrism", "free-market environmentalism",
                        "pragmatic utilitarianism", "developmentalism",
                        "risk-benefit analysis"],
        "values": ["prosperity", "innovation", "adaptability",
                  "personal freedom", "market efficiency"],
        "frameworks": ["cost-benefit analysis", "risk assessment",
                      "eco-modernism", "resource economics",
                      "liberal environmentalism"]
    }

    structure = random.choice(structures)
    argument = structure.replace("{topic}", topic)
    
    argument = argument.replace("{principle}", random.choice(env_components["principles"]))
    argument = argument.replace("{perspective}", random.choice(env_components["perspectives"]))
    argument = argument.replace("{value}", random.choice(env_components["values"]))
    argument = argument.replace("{framework}", random.choice(env_components["frameworks"]))
    
    env_replacements = {
        "{evidence}": "Economic analyses of environmental regulation reveal",
        "{consequence}": "reduced economic growth and increased inequality",
        "{reason}": "it can impose disproportionate costs on developing communities",
        "{example}": "As seen in energy crises caused by abrupt policy shifts",
        "{conclusion}": "this approach risks undermining social stability",
        "{elaboration}": "When considering urgent human needs and poverty alleviation",
        "{historical_example}": "the unintended effects of biofuel mandates on food prices",
        "{explanation}": "This framework may ignore local contexts and priorities",
        "{outcome}": "unintended harm to vulnerable populations",
        "{negative_outcome}": "job losses and economic disruption",
        "{data_point}": "World Bank reports highlight mixed results from strict policies",
        "{implication}": "flexible, adaptive approaches are preferable",
        "{lens}": "cost-benefit environmental analysis",
        "{problems}": "regulatory overreach, inefficiency, and stifled innovation",
        "{additional_point}": "Market-based solutions can achieve similar goals",
        "{imperative}": "balance environmental goals with human flourishing",
        "{reasoning}": "Ethical stewardship must consider all stakeholders",
        "{consideration}": "the livelihoods of at-risk populations",
        "{key_concern}": "the risk of eco-authoritarianism",
        "{mechanism}": "imposing top-down mandates without local input",
        "{supporting_evidence}": "Case studies show that voluntary incentives can be effective",
        "{additional_concern}": "This may erode trust in environmental policy",
        "{foundation}": "the priority of human dignity and well-being",
        "{negative_vision}": "environmental policy is used to justify inequity"
    }
    
    for placeholder, replacement in env_replacements.items():
        argument = argument.replace(placeholder, replacement)
        
    return argument

def create_environmentalethics_debates_csv(filename, num_records=1000):
    topics = generate_environmental_ethics_topics(num_records)
    
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
create_environmentalethics_debates_csv('ethical.csv', 1000)
