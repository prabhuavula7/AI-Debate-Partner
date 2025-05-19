import random
import csv

# Extended religious ethics topics (25 items)
topic_templates = {
    "Religious Ethics": [
        "Religious symbols in public spaces",
        "Clergy confidentiality and abuse reporting",
        "Animal sacrifice laws and religious freedom",
        "Religious exemption from medical treatment",
        "Faith-based adoption agency discrimination",
        "Religious dress codes in secular institutions",
        "Blasphemy laws and free speech",
        "Religious conversion therapy practices",
        "Religious extremism and counterterrorism",
        "Sacred site preservation vs. development",
        "Religious education in public schools",
        "Faith healing and child protection laws",
        "Religious dietary laws in public institutions",
        "Proselytization in vulnerable communities",
        "Religious polygamy and civil law",
        "Excommunication and community shunning",
        "Religious objection to LGBTQ+ rights",
        "Circumcision regulations and infant rights",
        "Religious objection to contraception access",
        "Apocalyptic cults and public safety",
        "Religious environmental stewardship duties",
        "Temple funds and financial transparency",
        "Religious genital mutilation practices",
        "Religious objection to autopsies",
        "Sacred text censorship and modernization"
    ]
}

def generate_religion_ethics_topics(num_topics=1000):
    base_topics = topic_templates["Religious Ethics"]
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
    
    religion_components = {
        "principles": ["religious freedom", "divine command", "sacred duty",
                      "spiritual autonomy", "cosmic justice"],
        "perspectives": ["theological ethics", "interfaith dialogue", 
                        "scriptural authority", "religious pluralism",
                        "sacred tradition"],
        "values": ["faith", "devotion", "transcendence",
                  "community harmony", "spiritual growth"],
        "frameworks": ["divine command theory", "natural law theology", 
                      "liberation theology", "virtue theology",
                      "religious existentialism"]
    }

    structure = random.choice(structures)
    argument = structure.replace("{topic}", topic)
    
    argument = argument.replace("{principle}", random.choice(religion_components["principles"]))
    argument = argument.replace("{perspective}", random.choice(religion_components["perspectives"]))
    argument = argument.replace("{value}", random.choice(religion_components["values"]))
    argument = argument.replace("{framework}", random.choice(religion_components["frameworks"]))
    
    religion_replacements = {
        "{evidence}": "Scriptural analysis and theological scholarship demonstrate",
        "{consequence}": "greater interfaith understanding and spiritual fulfillment",
        "{reason}": "it respects millennia of sacred tradition while adapting to modern contexts",
        "{example}": "As seen in the Second Vatican Council reforms",
        "{conclusion}": "this approach honors both divine will and human dignity",
        "{elaboration}": "When guided by compassionate interpretation of sacred texts",
        "{historical_example}": "the Protestant Reformation's impact on religious ethics",
        "{explanation}": "This framework balances eternal truths with contemporary realities",
        "{outcome}": "deeper spiritual connection and ethical coherence",
        "{positive_outcome}": "strengthened faith communities and moral guidance",
        "{data_point}": "Pew Research studies on religious practice confirm",
        "{implication}": "religious ethics should inform societal norms",
        "{lens}": "comparative religious ethics",
        "{reasons}": "divine mandate, community welfare, and moral consistency",
        "{additional_point}": "This aligns with ecumenical councils' historic rulings",
        "{obligation}": "uphold sacred covenants and moral teachings",
        "{reasoning}": "Religious ethics require fidelity to transcendent truths",
        "{consideration}": "the needs of devout practitioners",
        "{key_benefit}": "moral clarity in a secular age",
        "{mechanism}": "grounding ethical decisions in eternal wisdom",
        "{supporting_evidence}": "Centuries of theological discourse support",
        "{additional_benefit}": "This fosters dialogue between faith traditions",
        "{foundation}": "the inherent sacredness of human life",
        "{vision}": "spiritual and ethical truths guide societal development"
    }
    
    for placeholder, replacement in religion_replacements.items():
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
        "Critics of {topic} highlight {key_concern}, which threatens religious ethics by {mechanism}. {supporting_evidence}",
        "Implementing {topic} violates the principle of {principle}, as demonstrated by {example}. {additional_concern}",
        "The ethical case against {topic} centers on {foundation}. {explanation} This risks creating a society where {negative_vision}."
    ]

    religion_components = {
        "principles": ["secularism", "individual rights", "scientific rationalism",
                      "pluralism", "freedom from religion"],
        "perspectives": ["secular humanism", "atheistic ethics", 
                        "religious skepticism", "constitutional law",
                        "cultural relativism"],
        "values": ["reason", "personal autonomy", "scientific progress",
                  "equal treatment", "separation of church and state"],
        "frameworks": ["secular ethics", "human rights law", 
                      "critical theory", "utilitarianism",
                      "post-religious morality"]
    }

    structure = random.choice(structures)
    argument = structure.replace("{topic}", topic)
    
    argument = argument.replace("{principle}", random.choice(religion_components["principles"]))
    argument = argument.replace("{perspective}", random.choice(religion_components["perspectives"]))
    argument = argument.replace("{value}", random.choice(religion_components["values"]))
    argument = argument.replace("{framework}", random.choice(religion_components["frameworks"]))
    
    religion_replacements = {
        "{evidence}": "Historical analysis of religious conflicts shows",
        "{consequence}": "erosion of civil liberties and social cohesion",
        "{reason}": "it imposes particular theological views on pluralistic societies",
        "{example}": "As seen in the European Wars of Religion",
        "{conclusion}": "this approach dangerously conflates church and state",
        "{elaboration}": "When considering diverse belief systems in modern societies",
        "{historical_example}": "the Inquisition's legacy of religious persecution",
        "{explanation}": "This framework prioritizes dogma over human welfare",
        "{outcome}": "discrimination and sectarian conflict",
        "{negative_outcome}": "entrenched bigotry and scientific stagnation",
        "{data_point}": "Gallup polls show declining support for religious influence",
        "{implication}": "strict church-state separation is ethically necessary",
        "{lens}": "secular governance principles",
        "{problems}": "dogmatism, exclusion, and resistance to progress",
        "{additional_point}": "Universal human rights offer better ethical guidance",
        "{imperative}": "protect individual conscience from doctrinal coercion",
        "{reasoning}": "Ethical pluralism requires neutrality in public policy",
        "{consideration}": "non-believers and minority faith groups",
        "{key_concern}": "theocratic tendencies in governance",
        "{mechanism}": "privileging specific beliefs over others",
        "{supporting_evidence}": "Comparative studies of secular democracies confirm",
        "{additional_concern}": "This enables systemic discrimination",
        "{foundation}": "the primacy of reason and individual autonomy",
        "{negative_vision}": "personal freedoms are subordinate to religious dogma"
    }
    
    for placeholder, replacement in religion_replacements.items():
        argument = argument.replace(placeholder, replacement)
        
    return argument

def create_religionethics_debates_csv(filename, num_records=1000):
    topics = generate_religion_ethics_topics(num_records)
    
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
create_religionethics_debates_csv('ethical.csv', 1000)