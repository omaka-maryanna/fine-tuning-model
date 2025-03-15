def get_data():
    unilag_data = [
        {
            "input": "What is the University of Lagos known for?",
            "output": "UNILAG is known for academic excellence, research, and producing influential graduates in various fields."
        },
        {
            "input": "Does UNILAG offer online learning options?",
            "output": "Yes, UNILAG offers online and distance learning programs through its Distance Learning Institute (DLI)."
        },
        {
            "input": "How can I apply for admission to UNILAG?",
            "output": "Applicants must register for JAMB UTME, meet the cut-off mark, and apply through the university’s portal."
        },
        {
            "input": "What faculties are available at UNILAG?",
            "output": "UNILAG has 12 faculties, including Engineering, Medicine, Law, and Social Sciences."
        },
        {
            "input": "Does UNILAG offer postgraduate programs?",
            "output": "Yes, UNILAG offers Master's and PhD programs through its School of Postgraduate Studies."
        },
        {
            "input": "What notable alumni have graduated from UNILAG?",
            "output": "Notable alumni include Yemi Osinbajo, Akinwumi Adesina, and Genevieve Nnaji."
        },
        {
            "input": "Does UNILAG provide scholarships?",
            "output": "Yes, UNILAG offers merit-based and need-based scholarships to students."
        },
        {
            "input": "What is the student population at UNILAG?",
            "output": "UNILAG has a student population of over 50,000, including undergraduate and postgraduate students."
        },
        {
            "input": "Where is UNILAG located?",
            "output": "UNILAG is located in Akoka, Lagos State, Nigeria, with campuses in Yaba and Idi-Araba."
        },
        {
            "input": "What courses does UNILAG offer?",
            "output": "UNILAG offers courses in Arts, Sciences, Engineering, Medicine, Management Sciences, and more."
        },
        {
            "input": "What is UNILAG's motto?",
            "output": "UNILAG's motto is 'In Deed and in Truth.'"
        },
        {
            "input": "When was UNILAG established?",
            "output": "UNILAG was established in 1962 as one of Nigeria's first-generation universities."
        },
        {
            "input": "Does UNILAG have hostel accommodation?",
            "output": "Yes, UNILAG provides hostel accommodation, but spaces are limited."
        },
        {
            "input": "What is the tuition fee for UNILAG?",
            "output": "UNILAG's tuition fees vary by faculty and program but are generally affordable."
        },
        {
            "input": "Does UNILAG have a medical school?",
            "output": "Yes, UNILAG has a College of Medicine in Idi-Araba, Lagos."
        },
        {
            "input": "What is UNILAG's official website?",
            "output": "UNILAG's official website is https://unilag.edu.ng/"
        },
        {
            "input": "Does UNILAG have international partnerships?",
            "output": "Yes, UNILAG collaborates with various international universities for research and exchange programs."
        },
        {
            "input": "Are there part-time programs at UNILAG?",
            "output": "Yes, UNILAG offers part-time programs through its Distance Learning Institute."
        },
        {
            "input": "Does UNILAG have sports facilities?",
            "output": "Yes, UNILAG has a stadium, gym, swimming pool, and courts for various sports."
        },
        {
            "input": "How can I check my UNILAG admission status?",
            "output": "You can check your admission status on the UNILAG portal or JAMB CAPS."
        }
    ]
    return unilag_data

import lamini

# Set the API key

lamini.api_key = "d73c8a86d34fd594b8ec68637cbefae2562a80f90501f008ac0a86232cd2cd09"
# Initialize the Lamini model
llm = lamini.Lamini("meta-llama/Meta-Llama-3.1-8B-Instruct")

# Get the dataset
data = get_data()

# Fine-tune the model on the dataset
llm.tune(data_or_dataset_id=data,
         finetune_args={"learning_rate": 1e-5},
         )


# COmmon hyperparameters that cna be used
# learning_rate: float = 1e-5
# num_train_epochs: int = 3
# batch_size: int = 4
# weight_decay: float = 0.01
# early_stopping_patience: int = 3v