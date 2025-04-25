
import random
import streamlit as st

st.set_page_config(page_title="Sexy Prompt Generator", layout="centered")

locations = [
    "bedroom", "kitchen", "bathroom", "rooftop", "gym", "nightclub",
    "closet", "beach", "shower", "couch", "office", "balcony", "spa",
    "garage", "library", "poolside", "vanity", "car", "fireplace",
    "dressing room", "hotel room", "hot tub", "sauna", "garden",
    "studio", "lounge", "backyard", "rainy window", "mirror-lit hallway",
    "open field", "convertible car", "neon-lit room"
]

outfits = [
    "red lace lingerie", "oversized shirt", "towel wrap", "tight leather outfit",
    "sports bra and shorts", "bodycon dress", "robe half-open", "thong bikini",
    "fishnet bodysuit", "silk slip dress", "corset and garter", "crop top and panties",
    "latex suit", "sheer robe", "pencil skirt and blouse", "high heels and stockings",
    "denim shorts and tied shirt", "see-through top", "nothing but a towel",
    "transparent nightgown", "wet white t-shirt", "off-shoulder sweater",
    "mini dress", "g-string and boots", "lingerie with feather robe",
    "long silk gown with high slit", "schoolgirl skirt and tight blouse"
]

poses = [
    "lying on her stomach, looking back seductively",
    "arching her back on the bed",
    "sitting on the counter, biting her lip",
    "crawling on all fours toward the camera",
    "leaning against the wall with one leg raised",
    "lounging sideways with legs slightly apart",
    "posing with arms above her head",
    "stretching on a yoga mat seductively",
    "bending over in front of a mirror",
    "teasing with a playful smirk",
    "kneeling with hands behind her head",
    "posing topless from behind with loose hair",
    "straddling a chair backwards, licking her lips",
    "posing in front of a fogged mirror with smudged glass",
    "standing with one hip cocked, tugging at her thong",
    "resting on elbows with legs up against the wall",
    "sitting on a stool with legs spread and a teasing look",
    "biting on a necklace, hands tangled in hair",
    "wrapped in fairy lights, back arched on floor",
    "sprawled across a fur rug, chin resting on hands"
]

vibes = [
    "soft and romantic", "bold and dominant", "playful and cheeky",
    "luxurious and elegant", "wet and wild"
]

def generate_prompt(vibe=None):
    location = random.choice(locations)
    outfit = random.choice(outfits)
    pose = random.choice(poses)
    prompt = f"Scene in a {location}, model wearing {outfit}, {pose}."
    if vibe:
        prompt += f" The vibe is {vibe}."
    return prompt

st.title("🔥 Sexy Prompt Generator")
st.markdown("Create spicy and creative prompts for AI image generation")

selected_vibe = st.selectbox("Choose a Vibe (Optional):", ["Random"] + vibes)
num_prompts = st.slider("Number of Prompts", 1, 20, 5)

generate = st.button("Generate Prompts")

if generate:
    st.subheader("Generated Prompts")
    for _ in range(num_prompts):
        vibe = None if selected_vibe == "Random" else selected_vibe
        st.write(generate_prompt(vibe))
