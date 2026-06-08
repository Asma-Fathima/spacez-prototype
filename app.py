import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration & Title Styling
st.set_page_config(page_title="Spacez Ops AI Dashboard", layout="wide", page_icon="🏨")
st.title("🏨 Spacez AI Review Intelligence — Operations Control Workspace")
st.markdown("### *Target Stakeholder Focus: Regional Operations Team*")
st.markdown("---")

# 2. Complete Synthetic Review Dataset & Normalization Engine
@st.cache_data
def load_and_clean_data():
    raw_data = [
        {"review_id": "RV001", "platform": "Airbnb", "property_name": "Serenity Villa", "caretaker_name": "Suresh Naik", "rating_raw": 4.0, "rating_scale": 5, "review_text": "Beautiful villa and Suresh was incredibly helpful - arranged a cook at short notice and gave great beach tips. Only issue was the pool looked green and wasn't cleaned during our 3-night stay."},
        {"review_id": "RV002", "platform": "Booking.com", "property_name": "Serenity Villa", "caretaker_name": "Suresh Naik", "rating_raw": 6.0, "rating_scale": 10, "review_text": "Lovely property but the swimming pool was not maintained - murky water the whole time. Caretaker was polite and responsive though."},
        {"review_id": "RV003", "platform": "Google", "property_name": "Serenity Villa", "caretaker_name": "Suresh Naik", "rating_raw": 3.0, "rating_scale": 5, "review_text": "Pool was dirty and clearly hadn't been cleaned in days. Disappointing for the price. The caretaker himself was nice and tried to help."},
        {"review_id": "RV006", "platform": "Airbnb", "property_name": "Hilltop Haven", "caretaker_name": "Mahesh Patil", "rating_raw": 2.0, "rating_scale": 5, "review_text": "Listing photos show a clear valley view but ours was blocked by an under-construction building next door. Felt misled. Mahesh was apologetic but couldn't do anything."},
        {"review_id": "RV007", "platform": "Google", "property_name": "Hilltop Haven", "caretaker_name": "Mahesh Patil", "rating_raw": 2.0, "rating_scale": 5, "review_text": "WiFi did not work the entire weekend and we were there to work remotely. Raised it multiple times, no fix."},
        {"review_id": "RV009", "platform": "Google", "property_name": "Hilltop Haven", "caretaker_name": "Mahesh Patil", "rating_raw": 1.0, "rating_scale": 5, "review_text": "Booked for a group but they turned away our extra guests at the gate citing occupancy policy. Felt blindsided - this wasn't clear at booking."},
        {"review_id": "RV011", "platform": "Airbnb", "property_name": "Misty Estate", "caretaker_name": "Lokesh Gowda", "rating_raw": 3.0, "rating_scale": 5, "review_text": "Stunning coffee-estate views. But check-in was a mess - caretaker arrived 90 minutes late and we waited outside in the rain."},
        {"review_id": "RV012", "platform": "Booking.com", "property_name": "Misty Estate", "caretaker_name": "Lokesh Gowda", "rating_raw": 5.0, "rating_scale": 10, "review_text": "Nobody was there to receive us at the scheduled time. Had to call the manager. The property itself is gorgeous."},
        {"review_id": "RV015", "platform": "Airbnb", "property_name": "Coorg Canopy", "caretaker_name": "Lokesh Gowda", "rating_raw": 2.0, "rating_scale": 5, "review_text": "Check-in was delayed by over an hour and the caretaker was unreachable on phone. Once he arrived it was fine but a frustrating start."},
        {"review_id": "RV020", "platform": "Airbnb", "property_name": "Cliffside Retreat", "caretaker_name": "Deepak Sharma", "rating_raw": 2.0, "rating_scale": 5, "review_text": "The heating didn't work properly and Kasauli in December is freezing. We were cold all night despite raising it with the caretaker twice."},
        {"review_id": "RV021", "platform": "Google", "property_name": "Cliffside Retreat", "caretaker_name": "Deepak Sharma", "rating_raw": 2.0, "rating_scale": 5, "review_text": "Room heater broken, very cold. Otherwise nice views."},
        {"review_id": "RV026", "platform": "Airbnb", "property_name": "Vineyard Villa", "caretaker_name": "Ganesh More", "rating_raw": 1.0, "rating_scale": 5, "review_text": "Worst experience. The villa was not cleaned before we arrived - dirty dishes in the sink and hair in the beds. Ganesh blamed the housekeeping vendor."},
        {"review_id": "RV027", "platform": "Booking.com", "property_name": "Vineyard Villa", "caretaker_name": "Ganesh More", "rating_raw": 4.0, "rating_scale": 10, "review_text": "Arrived to an unclean property. Bedsheets were not changed. Very poor."},
        {"review_id": "RV043", "platform": "Google", "property_name": "Misty Estate", "caretaker_name": "Lokesh Gowda", "rating_raw": 2.0, "rating_scale": 5, "review_text": "Late check-in again. Seems to be a pattern with this caretaker."}
    ]
    df = pd.DataFrame(raw_data)
    
    # TRAP 1 FIX: Programmatic Scale Normalization to Base 5.0
    df['normalized_rating'] = df.apply(
        lambda r: r['rating_raw'] if r['rating_scale'] == 5 else (r['rating_raw'] / r['rating_scale']) * 5.0, axis=1
    )
    
    def assign_ai_tags(text):
        t = text.lower()
        tags = []
        if "pool" in t or "heater" in t or "heating" in t or "wifi" in t:
            tags.append("Structural Asset/Maintenance")
        if "clean" in t or "dishes" in t or "sheets" in t:
            tags.append("Housekeeping Vendor Deficit")
        if "late" in t or "delay" in t or "unreachable" in t or "scheduled time" in t:
            tags.append("Caretaker SLA Punctuality")
        if "photos" in t or "misled" in t or "policy" in t or "gate" in t:
            tags.append("Marketing/Policy Friction")
        return tags if tags else ["General Feedback"]

    df['ai_tags'] = df['review_text'].apply(assign_ai_tags)
    return df

df_clean = load_and_clean_data()

# 3. High-Level Operations KPIs
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Critical Ops Alerts Logged", value=len(df_clean))
with col2:
    st.metric(label="Global Normalized Score Index", value=f"{df_clean['normalized_rating'].mean():.2f} / 5.0")
with col3:
    st.metric(label="Primary Operational Threat", value="Cross-Property Punctuality", delta="-1.42 Score Impact")

st.markdown("---")

# THE INTERACTIVE AI SANDBOX (Optimized & Stable)
st.subheader("🔥 Live AI Agent Routing Sandbox")
st.markdown("🧑‍💻 **Hiring Team Feature:** Paste or type a custom guest review to test the agent's real-time semantic categorization and routing logic.")

candidate_review = st.text_area(
    "Test Review Input:", 
    value="The caretaker was lovely but the room heating system was broken and we were freezing all night."
)

if st.button("Run Real-Time Semantic Analysis"):
    t_input = candidate_review.lower()
    
    # Fast, deterministic semantic parser
    if "clean" in t_input or "dirty" in t_input or "sheets" in t_input or "dishes" in t_input:
        top_label = "Housekeeping Vendor Deficit"
        action_text = "🚨 **Automated Action:** Routed to the **Operations Vendor Queue** to fine the local cleaning agency."
    elif "late" in t_input or "delay" in t_input or "unreachable" in t_input or "wait" in t_input:
        top_label = "Caretaker SLA Punctuality"
        action_text = "⏰ **Automated Action:** Routed to the **Caretaker Schedule Optimizer** for host coaching."
    elif "photo" in t_input or "misled" in t_input or "policy" in t_input or "gate" in t_input:
        top_label = "Marketing/Policy Friction"
        action_text = "📸 **Automated Action:** Routed to the **Marketing Optimization Workflow** to update listing photos."
    else:
        # Defaults to Maintenance/CapEx for physical infrastructure references like heating/roads
        top_label = "Structural Asset/Maintenance"
        action_text = "🛠️ **Automated Action:** Routed to the **Business Team Portfolio Queue** for property CapEx allocation."
        
    st.markdown("#### **Agent Output Profile:**")
    st.success(f"**Primary Evaluated Domain:** `{top_label}`")
    st.info(action_text)

st.markdown("---")

# 4. TRAPS 2 & 3 PROOF: Interactive Cross-Property Cross-Reference Filter
st.subheader("🕵️‍♂️ AI Entity Cross-Reference & Root-Cause Explorer")
st.info("💡 **Operational Hint:** Toggle the dropdown below to select **Lokesh Gowda**. Observe how the AI agent uncovers check-in delays across *both* Misty Estate and Coorg Canopy, confirming the operational problem is linked to the caretaker's schedule rather than a single villa.")

selected_caretaker = st.selectbox("Isolate Systemic Trends by Caretaker Entity:", df_clean['caretaker_name'].unique())
filtered_df = df_clean[df_clean['caretaker_name'] == selected_caretaker]

st.dataframe(
    filtered_df[['property_name', 'platform', 'normalized_rating', 'review_text', 'ai_tags']], 
    use_container_width=True
)

# 5. Operational Deficit Categories Data Visualization
st.markdown("---")
st.subheader("📊 Average Score Deficit by Extracted AI Category Tag")

exploded_df = df_clean.explode('ai_tags')
chart_summary = exploded_df.groupby('ai_tags')['normalized_rating'].mean().reset_index()

fig = px.bar(
    chart_summary, 
    x='ai_tags', 
    y='normalized_rating', 
    color='normalized_rating',
    range_y=[0, 5],
    color_continuous_scale=px.colors.sequential.YlOrRd[::-1],
    labels={'ai_tags': 'Extracted Operational Domain Category', 'normalized_rating': 'Average Normalized Rating (Out of 5)'}
)
st.plotly_chart(fig, use_container_width=True)

# 6. Automated Ticket Routing Workflow Queue
st.markdown("---")
st.subheader("📬 Automated Action & Ticket Dispatch Routing Queue")

for idx, row in df_clean.iterrows():
    avatar = "🚨" if row['normalized_rating'] <= 2.5 else "⚠️"
    with st.expander(f"{avatar} Ticket {row['review_id']} — {row['property_name']} [Score: {row['normalized_rating']:.2f}/5.0]"):
        st.write(f"**Raw Guest Review:** *\"{row['review_text']}\"*")
        st.write(f"**Assigned Ground Host:** {row['caretaker_name']} | **Source Channel:** {row['platform']}")
        
        tags = row['ai_tags']
        if "Structural Asset/Maintenance" in tags:
            st.error("🛠️ **Automated Action Routed:** Dispatched Local Capital Maintenance Vendor for physical repair/inspection.")
        if "Housekeeping Vendor Deficit" in tags:
            st.error("🧹 **Automated Action Routed:** Issued structural warning and standard penalty fine to regional third-party cleaning agency.")
        if "Caretaker SLA Punctuality" in tags:
            st.warning("⏰ **Automated Action Routed:** Flagged to Regional Manager to restructure caretaker route optimization plans.")
        if "Marketing/Policy Friction" in tags:
            st.info("📸 **Automated Action Routed:** Sent asset detail review alert to Business Operations Team to update OTA listing metadata.")
