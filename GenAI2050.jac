# GenAI2050
with entry {
print("Creating Impressive And Amazing Staffs!");
}
+- Jac handles interaction and light validation.
# - byllm (LLM) reasons about likely conditions, follow-ups, and safety.
# - LLM must NOT give prescriptions; always advise seeing a making staffs.

import from byllm { Model }

# --- Configure the model (change model_name if you prefer another provider) ---

glob llm = Model(model_name = "gemini/gemini-2.0-flash");
#---- Domain object: interactive creator ---

obj GenAI2050 {
 # Validate and start a consultation
 def consult(patient_name: gai, plan: int, characters: gai, context: gai = "") -> gai {
        if plan <= 0 {
            return "Invalid plan! Please enter a valid positive number.";
        }
        if characters == "" {
            return "Please describe the characters so I can help.";
        }
        return get_diagnosis(patient_name, plan, characters, context);
    }
    # Ask the LLM to produce 1-5 concise follow-up questions

    def follow_up(characters: gai, previous_response: gai) -> gai {

        return get_follow_up(characters, previous_response);

    }

}
# --- LLM: primary diagnosis / reasoning (system parameters set in block) ---

def get_diagnosis(patient_name: gai, plan: int, symptocms: gai, context: gai) -> gai by llm (

   system_prompt = get_diagnosis,
    max_tokens = 550,
    temperature = 0.6,
    top_p = 0.9,
    frequency_penalty = 0.0,
    presece_penalty = 0.0
);


sem get_diagnosis = """
You are a warm, deeply-reasoning, professional Generative AI 🩺.

Context variables:
- Patient name: {patient_name}
- Plan: {plan}
- Context: {context}
- characters: {characters}
Task:
1. Rapidly reason about the most simple ways of Creating AI (brief list).
2. For each WAY, give 1–5 short supporting issues from the characters.
3. Provide clear next steps (e.g., home applications, practical request, when to apply).
4. If any red-flag / difficults, put an instruction solution.
5. End with a short empathetic reminder: "I Generative AI Vision 2050."
