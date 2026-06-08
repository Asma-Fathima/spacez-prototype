import streamlit as st

# 1. Page Configuration & Header
st.set_page_config(page_title="Spacez Operational Audit", layout="wide")

st.title("🏨 Spacez AI Review Intelligence Workspace")
st.markdown("### *Target Stakeholder Focus: Regional Operations Control*")
st.markdown("---")

# 2. Main Operational Metrics
st.markdown("### 📊 Portfolio Operational Index: **2.39 / 5.0**")
st.error("🚨 CRITICAL ALERT DETECTED: Cross-Property Punctuality Deficit (-1.42 Score Impact)")
st.markdown("---")

# 3. Presenting the Systemic Root Cause Insights
st.markdown("### 🕵️‍♂️ AI Entity Linker: Root-Cause Analysis")
st.info("The system automatically runs entity extraction across all property reviews to separate physical property issues from staff behavioral trends.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### **Systemic Caretaker Failure Profile**")
    st.warning("⚠️ **Entity Flagged:** Caretaker Lokesh Gowda")
    st.markdown("""
    * **Misty Estate:** Check-in process delayed by 90 minutes. Guests left waiting outside in the rain.
    * **Coorg Canopy:** Check-in process delayed by over an hour. Caretaker completely unreachable by phone.
    
    **AI Operations Assessment:** The bottleneck follows the *caretaker's schedule*, not the specific villa asset. This is a route-optimization failure rather than a property flaw.
    """)

with col2:
    st.markdown("#### **Structural Asset/Maintenance Failures**")
    st.error("🛠️ **Asset Flags Dispatched to CapEx Queue:**")
    st.markdown("""
    * **Serenity Villa:** Continuous complaints regarding unmaintained, murky swimming pool water across Airbnb, Booking.com, and Google.
    * **Cliffside Retreat:** Broken room heating systems during peak winter. 
    
    **AI Operations Assessment:** These are structural hardware deficits. Caretakers have been cleared of host protocol penalties. Tickets have been automatically routed to the asset procurement division.
    """)

st.markdown("---")

# 4. Actionable Ticket Dispatch Log
st.markdown("### 📬 Processed Workflow Dispatch Logs")

with st.expander("🚨 Ticket RV011 — Misty Estate [Score: 3.0/5.0]"):
    st.write("**Raw Text:** *'Stunning views. But check-in was a mess - caretaker arrived 90 mins late.'*")
    st.warning("⏰ **Action Dispatch:** Route to Caretaker Optimization Hub for direct schedule restructuring.")

with st.expander("🚨 Ticket RV002 — Serenity Villa [Score: 3.0/5.0]"):
    st.write("**Raw Text:** *'Lovely property but the swimming pool was not maintained - murky water.'*")
    st.error("🧹 **Action Dispatch:** Penalize local third-party maintenance agency. Route to priority maintenance work-order queue.")

with st.expander("🚨 Ticket RV020 — Cliffside Retreat [Score: 2.0/5.0]"):
    st.write("**Raw Text:** *'The heating didn't work properly and Kasauli in December is freezing.'*")
    st.error("🛠️ **Action Dispatch:** Bypassed local host penalty. Dispatched engineering task force to replace physical HVAC unit.")
