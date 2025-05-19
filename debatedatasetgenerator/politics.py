import random
import csv

# Extended political ethics topics (25 items)
topic_templates = {
    "Political Ethics": [
        "Campaign finance reform and transparency",
        "Lobbying regulations and influence peddling",
        "Political corruption prosecution standards",
        "Freedom of speech vs. hate speech legislation",
        "Voter ID laws and election accessibility",
        "Gerrymandering and electoral district integrity",
        "Whistleblower protections in government agencies",
        "Mass surveillance programs and national security",
        "Truth in political advertising regulations",
        "Conflict of interest disclosure requirements",
        "Transparency in government contracting processes",
        "Corporate donations in political campaigns",
        "Political nepotism and cronyism prevention",
        "Media ownership and political bias controls",
        "Digital privacy rights vs. state surveillance",
        "Ethical arms trade and foreign policy decisions",
        "Campaign promise accountability mechanisms",
        "Special interest group lobbying restrictions",
        "Ethical vetting of political appointees",
        "Public trust in governmental institutions",
        "Whistleblower anonymity protections",
        "Political polarization mitigation strategies",
        "PAC funding transparency requirements",
        "Campaign fundraising ethical guidelines",
        "Social media manipulation in elections"
    ]
}

def generate_political_ethics_topics(num_topics=1000):
    base_topics = topic_templates["Political Ethics"]
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
    
    political_components = {
        "principles": ["democratic accountability", "transparency", "justice", 
                      "fair representation", "institutional integrity"],
        "perspectives": ["liberal democracy", "social contract theory", 
                        "constitutional ethics", "civic republicanism",
                        "participatory governance"],
        "values": ["civic virtue", "public trust", "electoral integrity",
                  "pluralistic discourse", "governmental accountability"],
        "frameworks": ["deliberative democracy", "cosmopolitan ethics", 
                      "justice as fairness", "discourse ethics",
                      "republican political theory"]
    }

    structure = random.choice(structures)
    argument = structure.replace("{topic}", topic)
    
    argument = argument.replace("{principle}", random.choice(political_components["principles"]))
    argument = argument.replace("{perspective}", random.choice(political_components["perspectives"]))
    argument = argument.replace("{value}", random.choice(political_components["values"]))
    argument = argument.replace("{framework}", random.choice(political_components["frameworks"]))
    
    politics_replacements = {
        "{evidence}": "Comparative political analysis demonstrates",
        "{consequence}": "strengthened democratic institutions and public trust",
        "{reason}": "it addresses systemic power imbalances while preserving civil liberties",
        "{example}": "As evidenced by Nordic countries' political transparency initiatives",
        "{conclusion}": "this approach fosters more ethical governance structures",
        "{elaboration}": "When implemented with proper checks and balances",
        "{historical_example}": "the Watergate reforms' impact on political accountability",
        "{explanation}": "This framework prioritizes citizen sovereignty over special interests",
        "{outcome}": "more responsive and ethical government institutions",
        "{positive_outcome}": "reduced corruption and increased voter participation",
        "{data_point}": "OECD governance indicators show clear correlations",
        "{implication}": "political systems should institutionalize these reforms",
        "{lens}": "critical democratic theory",
        "{reasons}": "accountability, transparency, and civic empowerment",
        "{additional_point}": "This aligns with UN anti-corruption conventions",
        "{obligation}": "protect democratic processes from undue influence",
        "{reasoning}": "Political ethics demand we address systemic vulnerabilities",
        "{consideration}": "marginalized communities disproportionately affected",
        "{key_benefit}": "the democratization of political influence",
        "{mechanism}": "equalizing access to political participation",
        "{supporting_evidence}": "Cross-national studies of reform outcomes confirm",
        "{additional_benefit}": "This also strengthens international diplomatic standing",
        "{foundation}": "the social contract between citizens and state",
        "{vision}": "political power truly serves the public interest"
    }
    
    for placeholder, replacement in politics_replacements.items():
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
        "Critics of {topic} highlight {key_concern}, which threatens political ethics by {mechanism}. {supporting_evidence}",
        "Implementing {topic} violates the principle of {principle}, as demonstrated by {example}. {additional_concern}",
        "The ethical case against {topic} centers on {foundation}. {explanation} This risks creating a polity where {negative_vision}."
    ]

    political_components = {
        "principles": ["limited government", "individual liberty", "federalism", 
                      "free association", "proportionality"],
        "perspectives": ["libertarian", "constitutional originalism", 
                        "realist", "public choice theory",
                        "conservative reform"],
        "values": ["personal freedom", "decentralized power", "market autonomy",
                  "political pluralism", "spontaneous order"],
        "frameworks": ["negative liberty", "public choice economics", 
                      "Austrian economics", "constitutional conservatism",
                      "minarchist political theory"]
    }

    structure = random.choice(structures)
    argument = structure.replace("{topic}", topic)
    
    argument = argument.replace("{principle}", random.choice(political_components["principles"]))
    argument = argument.replace("{perspective}", random.choice(political_components["perspectives"]))
    argument = argument.replace("{value}", random.choice(political_components["values"]))
    argument = argument.replace("{framework}", random.choice(political_components["frameworks"]))
    
    politics_replacements = {
        "{evidence}": "Public choice theory analysis reveals",
        "{consequence}": "unintended erosion of civil liberties and innovation",
        "{reason}": "it expands bureaucratic overreach while solving nothing",
        "{example}": "As seen in failed regulatory regimes throughout history",
        "{conclusion}": "this approach enables government overreach",
        "{elaboration}": "When considering the law of unintended consequences",
        "{historical_example}": "the PATRIOT Act's impact on privacy rights",
        "{explanation}": "This framework ignores the self-interest of political actors",
        "{outcome}": "concentrated power and reduced civic autonomy",
        "{negative_outcome}": "stifled political innovation and dissent",
        "{data_point}": "Cato Institute studies document these effects",
        "{implication}": "we must preserve political market diversity",
        "{lens}": "public choice economics",
        "{problems}": "regulatory capture, rent-seeking, and perverse incentives",
        "{additional_point}": "Voluntary solutions exist without state coercion",
        "{imperative}": "protect individual sovereignty from state encroachment",
        "{reasoning}": "Political ethics require minimizing power concentration",
        "{consideration}": "the slippery slope of government overreach",
        "{key_concern}": "the normalization of surveillance states",
        "{mechanism}": "centralizing power in unaccountable institutions",
        "{supporting_evidence}": "Historical precedents demonstrate these dangers",
        "{additional_concern}": "This creates chilling effects on political speech",
        "{foundation}": "the primacy of individual rights over collective mandates",
        "{negative_vision}": "citizens become subjects of an overbearing state"
    }
    
    for placeholder, replacement in politics_replacements.items():
        argument = argument.replace(placeholder, replacement)
        
    return argument

def create_politicalethics_debates_csv(filename, num_records=1000):
    topics = generate_political_ethics_topics(num_records)
    
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
create_politicalethics_debates_csv('ethical.csv', 1000)
