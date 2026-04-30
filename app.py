from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import streamlit as st


# ---------- Waste Info ----------
waste_info = {
    "0 cardboard": {
        "name": "CARDBOARD 📦",
        "color": "#FDE68A",
        "carbon": (
            "Cardboard production releases a large amount of CO2 because it requires cutting down trees "
            "and using machines that consume electricity and water. Recycling cardboard reduces these emissions "
            "by about 50% and helps in saving both trees and energy."
        ),
        "impact": (
            "When cardboard is thrown away in landfills, it breaks down slowly and produces methane gas, "
            "which contributes to climate change. Large amounts of cardboard waste also take up valuable landfill space. "
            "Recycling keeps it in use and protects forests."
        ),
        "tips": (
            "- Flatten boxes before recycling to save space.\n"
            "- Keep cardboard clean and dry for easy recycling.\n"
            "- Remove plastic, tape, or staples before recycling.\n"
            "- Reuse cardboard boxes for storage or crafts."
        ),
        "importance": (
            "Managing cardboard waste properly helps save trees, reduces air pollution from factories, "
            "and conserves energy used in paper production."
        ),
        "fact": "Did you know? Recycling one ton of cardboard saves about 17 trees and 7,000 gallons of water!",
        "sdg": [
            {"img": "sdg goals/12.png", "desc": "Responsible Consumption"},
            {"img": "sdg goals/13.png", "desc": "Climate Action"},
            {"img": "sdg goals/14.png", "desc": "Life Below Water"},
            {"img": "sdg goals/15.png", "desc": "Life on Land"}
        ],
    },

    "1 plastic": {
        "name": "PLASTIC 🥤",
        "color": "#C7D2FE",
        "carbon": (
            "Plastic is made from oil and gas, which are fossil fuels. "
            "The process of creating plastic releases large amounts of CO2 into the air. "
            "Recycling plastic uses about two-thirds less energy than making new plastic from scratch."
        ),
        "impact": (
            "Plastic pollution affects oceans, rivers, and wildlife. "
            "It can take more than 400 years to break down, and tiny microplastics are found even in the food we eat. "
            "Burning plastic releases toxic chemicals that harm people and animals."
        ),
        "tips": (
            "- Avoid single-use items like straws, cups, and bags.\n"
            "- Reuse containers and bottles whenever possible.\n"
            "- Separate plastic types before recycling (e.g., PET, HDPE).\n"
            "- Support brands using biodegradable or recycled plastic."
        ),
        "importance": (
            "Proper plastic management keeps our oceans clean, saves marine animals, "
            "and reduces the need to extract more fossil fuels."
        ),
        "fact": "Did you know? Every year, over 8 million tons of plastic end up in the ocean — that’s like dumping a garbage truck every minute!",
        "sdg": [
            {"img": "sdg goals/6.jpg", "desc": "Clean Water"},
            {"img": "sdg goals/12.png", "desc": "Responsible Consumption"},
            {"img": "sdg goals/14.png", "desc": "Life Below Water"},
            {"img": "sdg goals/15.png", "desc": "Life on Land"}
        ],
    },

    "2 glass": {
        "name": "GLASS 🍾",
        "color": "#A7F3D0",
        "carbon": (
            "Glass is made from sand, soda ash, and limestone, heated to very high temperatures. "
            "This process consumes a lot of energy and releases CO2. However, glass can be recycled endlessly "
            "without losing quality, saving both raw materials and emissions."
        ),
        "impact": (
            "Glass doesn’t decompose naturally and can stay in landfills forever. "
            "Broken glass is hazardous to animals and humans. Recycling glass prevents waste buildup and reduces the need to mine new sand, "
            "helping preserve ecosystems."
        ),
        "tips": (
            "- Clean glass bottles and jars before recycling.\n"
            "- Avoid mixing glass with ceramics or light bulbs.\n"
            "- Reuse jars for storage, crafts, or decoration.\n"
            "- Dispose of broken glass safely by wrapping it."
        ),
        "importance": (
            "Glass recycling saves natural resources, reduces waste, and lowers carbon emissions."
        ),
        "fact": "Did you know? Recycling just one glass bottle saves enough energy to power a light bulb for four hours!",
        "sdg": [
            {"img": "sdg goals/12.png", "desc": "Responsible Consumption"},
            {"img": "sdg goals/14.png", "desc": "Life Below Water"}
        ],
    },

    "3 metal": {
        "name": "METAL 🛠️",
        "color": "#FECACA",
        "carbon": (
            "Producing metals like aluminum and steel emits a lot of CO2 because mining and smelting use high heat and energy. "
            "Recycling metal saves up to 95% of the energy compared to making it from ore."
        ),
        "impact": (
            "Improperly dumped metals can leak chemicals into soil and water. "
            "Mining causes deforestation and pollutes rivers. Recycling metals protects the environment "
            "and reduces the demand for destructive mining."
        ),
        "tips": (
            "- Sort different metals (aluminum, steel, copper) before recycling.\n"
            "- Rinse metal cans and remove labels.\n"
            "- Donate or sell scrap metal instead of throwing it away.\n"
            "- Avoid mixing metal waste with plastic or food."
        ),
        "importance": (
            "Metal recycling saves natural resources, reduces pollution, and cuts down greenhouse gas emissions."
        ),
        "fact": "Did you know? Recycling one aluminum can saves enough energy to run a TV for three hours!",
        "sdg": [
            {"img": "sdg goals/3.png", "desc": "Good Health"},
            {"img": "sdg goals/6.jpg", "desc": "Clean Water"},
            {"img": "sdg goals/12.png", "desc": "Responsible Consumption"},
            {"img": "sdg goals/14.png", "desc": "Life Below Water"}
        ],
    },

    "4 paper": {
        "name": "PAPER 📄",
        "color": "#FDE2FF",
        "carbon": (
            "Paper is made from trees, water, and chemicals, producing CO2 during manufacturing. "
            "Every ton of recycled paper saves about 17 trees and reduces air pollution by 70%."
        ),
        "impact": (
            "Paper in landfills produces methane as it decomposes. "
            "Recycling reduces deforestation, conserves biodiversity, and keeps our air and water cleaner."
        ),
        "tips": (
            "- Recycle newspapers, notebooks, and magazines separately.\n"
            "- Avoid recycling greasy or wet paper (like food wrappers).\n"
            "- Use both sides of the paper before discarding.\n"
            "- Switch to digital bills and notes whenever possible."
        ),
        "importance": (
            "Paper recycling helps save forests, reduces climate change, and protects wildlife habitats."
        ),
        "fact": "Did you know? The average person uses about 700 pounds of paper products every year!",
        "sdg": [
            {"img": "sdg goals/12.png", "desc": "Responsible Consumption"},
            {"img": "sdg goals/13.png", "desc": "Climate Action"},
            {"img": "sdg goals/14.png", "desc": "Life Below Water"},
            {"img": "sdg goals/15.png", "desc": "Life on Land"}
        ],
    },

    "5 trash": {
        "name": "TRASH 🗑️",
        "color": "#E5E7EB",
        "carbon": (
            "General trash, especially food and organic waste, produces methane gas in landfills — "
            "a greenhouse gas 25 times more powerful than CO2. Composting reduces these emissions "
            "and turns waste into useful fertilizer."
        ),
        "impact": (
            "Mixed waste pollutes soil, air, and water. "
            "Burning trash releases harmful smoke that affects human health and climate. "
            "Proper waste separation ensures recyclables are recovered and pollution is minimized."
        ),
        "tips": (
            "- Separate dry (plastic, paper, metal) and wet (food, garden) waste.\n"
            "- Compost organic waste at home or community centers.\n"
            "- Avoid littering — dispose of trash responsibly.\n"
            "- Reduce waste by buying only what you need."
        ),
        "importance": (
            "Managing trash correctly keeps cities cleaner, reduces pollution, "
            "and helps in creating sustainable waste management systems."
        ),
        "fact": "Did you know? Around 60% of household waste can actually be composted instead of going to landfills!",
        "sdg": [
            {"img": "sdg goals/11.png", "desc": "Sustainable Cities"},
            {"img": "sdg goals/12.png", "desc": "Responsible Consumption"}
        ],
    }
}

# ---------- Classify ----------
def classify_waste(img):
    model = load_model("keras_model.h5", compile=False)
    class_names = open("labels.txt").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    img = img.convert("RGB")
    img = ImageOps.fit(img, (224, 224), Image.Resampling.LANCZOS)
    img_array = np.asarray(img)
    data[0] = (img_array.astype(np.float32) / 127.5) - 1
    prediction = model.predict(data)
    index = np.argmax(prediction)
    confidence = float(prediction[0][index]*100)  # ✅ numeric value (e.g. 0.9732)
    label = class_names[index].strip()

    return label, confidence

# ---------- AI Carbon Info ----------


# ---------- Streamlit UI ----------
st.set_page_config(page_title="Smart Waste Management System", layout='wide')
st.markdown("<h1 style='text-align:center;color:green'>♻️ Smart Waste Management System 🌱</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray'>Upload an image to identify waste type, see carbon footprint, environmental impact, and SDG goals.</p>", unsafe_allow_html=True)

with st.sidebar:
    st.header("💡 About SDG Goals")
    st.markdown("""
### 🌏 **What are SDG Goals?**

The **Sustainable Development Goals (SDGs)** are **17 global goals** created by the **United Nations**.  
They are a shared plan to make our world a better place by **ending poverty**, **protecting the planet**, and **ensuring peace and prosperity** for everyone by **the year 2030**.  

Each goal focuses on a specific global challenge — like clean water, climate change, or responsible consumption.  
When we manage waste properly, we actually support **many of these SDGs** at the same time! ♻️  

Below are some SDG goals related to **waste management and environmental protection:**  

---

### ❤️ **Goal 3: Good Health and Well-Being**
- Promotes healthy lives for all people.  
- Clean surroundings reduce diseases caused by pollution and waste.  
- Proper waste management keeps our air, water, and communities safe from harmful germs and chemicals.  

---

### 💧 **Goal 6: Clean Water and Sanitation**
- Ensures everyone has access to safe water and proper sanitation.  
- Prevents garbage and toxic waste from entering rivers and lakes.  
- Clean water means healthier people and safer ecosystems.  

---

### ⚡ **Goal 7: Affordable and Clean Energy**
- Focuses on using energy that is safe, clean, and renewable.  
- Recycling materials like metal, glass, and paper saves huge amounts of energy.  
- Organic waste can even be turned into **biogas**, a clean energy source for homes and communities.  

---

### 🌍 **Goal 12: Responsible Consumption and Production**
- Encourages us to **Reduce, Reuse, and Recycle**.  
- Teaches people to make smart choices — buy less, waste less, and use what we have wisely.  
- Helps reduce landfill waste and saves natural resources.  

---

### 🌿 **Goal 13: Climate Action**
- Aims to reduce global warming and protect the planet.  
- When we recycle and compost waste, we reduce greenhouse gases like methane and CO₂.  
- Small actions like separating waste and saving energy help fight climate change.  

---

### 🐠 **Goal 14: Life Below Water**
- Protects oceans, seas, and marine life.  
- Reducing plastic waste prevents pollution that harms fish, turtles, and corals.  
- Clean oceans help keep the Earth’s climate balanced and provide food for millions of people.  

---

### 🌳 **Goal 15: Life on Land**
- Works to protect forests, soil, and animals on land.  
- Recycling paper reduces the number of trees cut down.  
- Proper waste disposal prevents soil pollution and helps plants and animals thrive.  

---

### ♻️ **Remember:**  
Every small action — like recycling, composting, or avoiding plastic — supports multiple SDG goals at once.  
By managing waste wisely, **you’re helping build a cleaner, greener, and healthier planet for everyone! 🌱**
""")

uploaded_file = st.file_uploader("Upload your waste image:", type=['jpg','png','jpeg'])

if uploaded_file and st.button("Classify Waste"):

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    with col2:
        img_obj = Image.open(uploaded_file)
        label, confidence = classify_waste(img_obj)

        if label in waste_info:
            info = waste_info[label]

            # ✅ Keep confidence between 0–100
            confidence_pct = min(max(confidence * 100, 0), 100)
            confidence_pct = round(confidence_pct, 2)

            # ✅ Result box
            st.markdown(
                f"""
                <div style="
                    background-color:{info['color']};
                    padding:20px;
                    border-radius:12px;
                    box-shadow:0 3px 8px rgba(0,0,0,0.1);
                    margin-bottom:15px;">
                    <h2 style="margin:0;">{info['name']} ✅</h2>
                    <p style="margin:8px 0 0 0; font-size:16px;">
                        <b>Confidence:</b> {confidence_pct}%
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

            # ✅ SDG Section
            with st.expander("🌍 Related SDG Goals"):
                sdgs = info["sdg"]
                cols = st.columns(min(len(sdgs), 4))
                for i, sdg in enumerate(sdgs):
                    with cols[i % len(cols)]:
                        st.image(sdg["img"], use_container_width=True)
                        st.caption(sdg["desc"])

            # ✅ Environmental Info
            with st.expander("📊 Environmental Details & Tips", expanded=True):
                st.markdown(f"**🌍 Carbon Footprint:** {info['carbon']}")
                st.markdown(f"**⚠️ Impact:** {info['impact']}")
                st.markdown(f"**💡 Tips:** {info['tips']}")
                if "fact" in info:
                    st.success(info["fact"])

        else:
            st.error(
                f"Unable to classify image.\nPredicted: {label}, Confidence: {round(confidence*100,2)}%"
            )


        
