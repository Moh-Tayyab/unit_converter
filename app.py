import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Unit Converter",
    page_icon="🔄",
    layout="centered",
    initial_sidebar_state="collapsed"
)
 
# Custom CSS for styling with animations and enhanced visuals
st.markdown("""
<style>
    /* Global styles and animations */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    body {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        background-attachment: fixed;
    }
    
    .stApp {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.2);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 20px;
        margin: 20px auto;
        max-width: 1000px;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    @keyframes slideIn {
        from { transform: translateX(-20px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    /* Header styles */
    .main-header {
        font-size: 2.8rem;
        background: linear-gradient(90deg, #4776E6 0%, #8E54E9 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 700;
        animation: fadeIn 1s ease-out;
    }
    
    .sub-header {
        font-size: 1.3rem;
        color: #5a6270;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 400;
        animation: fadeIn 1.2s ease-out;
    }
    
    /* Button styles */
    .stButton>button {
        background: linear-gradient(90deg, #4776E6 0%, #8E54E9 100%);
        color: white;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 15px rgba(71, 118, 230, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 7px 20px rgba(71, 118, 230, 0.4);
    }
    
    .stButton>button:active {
        transform: translateY(1px);
    }
    
    /* Input fields styling */
    .stSelectbox [data-baseweb="select"] {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    
    .stSelectbox [data-baseweb="select"]:focus-within {
        border-color: #4776E6;
        box-shadow: 0 0 0 2px rgba(71, 118, 230, 0.2);
    }
    
    .stNumberInput [data-baseweb="input"] {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    
    .stNumberInput [data-baseweb="input"]:focus-within {
        border-color: #4776E6;
        box-shadow: 0 0 0 2px rgba(71, 118, 230, 0.2);
    }
    
    /* Result container with animation */
    .result-container {
        background: linear-gradient(135deg, #ffffff 0%, #f5f7fa 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 2.5rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
        animation: fadeIn 0.8s ease-out;
        border: 1px solid rgba(142, 84, 233, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .result-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.12);
    }
    
    .result-value {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #4776E6 0%, #8E54E9 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: pulse 2s infinite ease-in-out;
    }
    
    .result-unit {
        font-size: 1.4rem;
        color: #5a6270;
        margin-top: 0.5rem;
        font-weight: 500;
    }
    
    /* Formula expander styling */
    .streamlit-expanderHeader {
        font-weight: 600;
        color: #4776E6;
        background-color: rgba(71, 118, 230, 0.05);
        border-radius: 8px;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background-color: rgba(71, 118, 230, 0.1);
    }
    
    .streamlit-expanderContent {
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 0 0 8px 8px;
        padding: 1rem;
        border: 1px solid rgba(71, 118, 230, 0.1);
        animation: slideIn 0.5s ease-out;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 4rem;
        color: #8E54E9;
        font-size: 0.9rem;
        padding: 1rem;
        border-top: 1px solid rgba(142, 84, 233, 0.2);
        animation: fadeIn 1.5s ease-out;
    }
    
    /* Category icons */
    .category-icon {
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
        display: block;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Conversion dictionaries for each category
# Length conversions (to meters as base unit)
length_conversions = {
    "Meter": 1,
    "Kilometer": 1000,
    "Centimeter": 0.01,
    "Millimeter": 0.001,
    "Mile": 1609.34,
    "Yard": 0.9144,
    "Foot": 0.3048,
    "Inch": 0.0254
}

# Weight conversions (to kilograms as base unit)
weight_conversions = {
    "Kilogram": 1,
    "Gram": 0.001,
    "Milligram": 0.000001,
    "Metric Ton": 1000,
    "Pound": 0.453592,
    "Ounce": 0.0283495,
    "Stone": 6.35029
}

# Volume conversions (to liters as base unit)
volume_conversions = {
    "Liter": 1,
    "Milliliter": 0.001,
    "Cubic Meter": 1000,
    "Cubic Centimeter": 0.001,
    "Gallon (US)": 3.78541,
    "Quart (US)": 0.946353,
    "Pint (US)": 0.473176,
    "Cup (US)": 0.236588,
    "Fluid Ounce (US)": 0.0295735
}

# Category to conversion dictionary mapping
category_to_conversions = {
    "Length": length_conversions,
    "Weight": weight_conversions,
    "Volume": volume_conversions
}

# Function to convert between units
def convert_units(value, from_unit, to_unit, conversions):
    if value is None or from_unit is None or to_unit is None:
        return None
    
    try:
        # Convert to base unit first, then to target unit
        base_value = value * conversions[from_unit]
        result = base_value / conversions[to_unit]
        return result
    except Exception as e:
        st.error(f"Error during conversion: {e}")
        return None

# Main app layout
st.markdown('<h1 class="main-header">Unit Converter</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Convert between different units of measurement</p>', unsafe_allow_html=True)

# Category icons mapping
category_icons = {
    "Length": "📏",
    "Weight": "⚖️",
    "Volume": "🧪"
}

# Create three columns for the main inputs
col1, col2, col3 = st.columns(3)

# Category selection
with col1:
    st.markdown(f'<span class="category-icon">{category_icons["Length"]}</span>', unsafe_allow_html=True)
    category = st.selectbox(
        "Select Category",
        options=["Length", "Weight", "Volume"],
        index=0,
        key="category_select"
    )
    # Update the category icon when selection changes
    st.markdown(f'<span class="category-icon">{category_icons[category]}</span>', unsafe_allow_html=True)

# Get the appropriate conversion dictionary based on category
conversions = category_to_conversions[category]
unit_options = list(conversions.keys())

# Input and output unit selection
with col2:
    # Use the swapped value if available
    from_index = 0
    if st.session_state.get('swap_requested') and 'temp_to' in st.session_state:
        # Check if the stored unit exists in the current category's options
        if st.session_state.temp_to in unit_options:
            from_index = unit_options.index(st.session_state.temp_to)
        
    from_unit = st.selectbox(
        "From Unit",
        options=unit_options,
        index=from_index,
        key="from_unit"
    )

with col3:
    # Use the swapped value if available
    to_index = 1
    if st.session_state.get('swap_requested') and 'temp_from' in st.session_state:
        # Check if the stored unit exists in the current category's options
        if st.session_state.temp_from in unit_options:
            to_index = unit_options.index(st.session_state.temp_from)
        
    to_unit = st.selectbox(
        "To Unit",
        options=unit_options,
        index=to_index,
        key="to_unit"
    )

# Input value
input_value = st.number_input(
    "Enter Value",
    value=1.0,
    format="%f",
    step=0.1
)

# Swap button and functionality with enhanced styling
if 'swap_requested' not in st.session_state:
    st.session_state.swap_requested = False

# Add a container with custom styling for the swap button
swap_container = st.container()
with swap_container:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("↔️ Swap Units"):
            # Set a flag in session state to indicate swap is requested
            st.session_state.swap_requested = True
            # Rerun to apply changes
            st.rerun()

# Handle the swap if requested
if st.session_state.swap_requested:
    # Reset the flag
    st.session_state.swap_requested = False
    # Store current values to use in the next selectbox calls
    st.session_state.temp_from = from_unit
    st.session_state.temp_to = to_unit

# Perform conversion
result = convert_units(input_value, from_unit, to_unit, conversions)

# Display result with enhanced visual presentation
if result is not None:
    st.markdown('<div class="result-container">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #5a6270; margin-bottom: 0.5rem; font-size: 1.1rem;">Conversion Result</h3>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-value">{result:.6g}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-unit">{to_unit}</div>', unsafe_allow_html=True)
    
    # Add a visual representation of the conversion
    st.markdown(f'<div style="margin-top: 1rem; font-size: 1.1rem; color: #5a6270; animation: fadeIn 1.3s ease-out;"><span>{input_value} {from_unit}</span><span style="margin: 0 10px;">➡️</span><span>{result:.6g} {to_unit}</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Formula display with enhanced styling
with st.expander("✨ Conversion Formula & Details"):
    if from_unit and to_unit:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""<div style='padding: 10px; background-color: rgba(71, 118, 230, 0.05); border-radius: 8px; margin-bottom: 10px;'>
                        <span style='font-weight: 600; color: #4776E6;'>Base Unit Conversion:</span><br>
                        1 {from_unit} = {conversions[from_unit]} base units<br>
                        1 {to_unit} = {conversions[to_unit]} base units
                        </div>""", unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""<div style='padding: 10px; background-color: rgba(142, 84, 233, 0.05); border-radius: 8px; margin-bottom: 10px;'>
                        <span style='font-weight: 600; color: #8E54E9;'>Conversion Rate:</span><br>
                        1 {from_unit} = {conversions[from_unit]/conversions[to_unit]:.6g} {to_unit}
                        </div>""", unsafe_allow_html=True)
        
        st.markdown("<span style='font-weight: 600; color: #5a6270;'>Formula:</span>", unsafe_allow_html=True)
        formula = f"{input_value} {from_unit} × ({conversions[from_unit]}/{conversions[to_unit]}) = {result:.6g} {to_unit}"
        st.code(formula, language="python")
        
        # Add a visual explanation
        st.markdown(f"""<div style='margin-top: 10px; font-size: 0.9rem; color: #5a6270;'>
                    This conversion takes your input value ({input_value} {from_unit}), 
                    multiplies it by the conversion factor ({conversions[from_unit]}/{conversions[to_unit]}), 
                    and gives you the equivalent value in {to_unit}.
                    </div>""", unsafe_allow_html=True)

# Footer with enhanced styling
st.markdown('<div class="footer">✨ Created with Streamlit • Unit Converter App • 2025 ✨</div>', unsafe_allow_html=True)

# Add a subtle animation at the bottom
st.markdown('''
<div style="text-align: center; margin-top: 1rem; animation: fadeIn 2s ease-out;">
    <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🔄</div>
    <div style="font-size: 0.8rem; color: #8E54E9; opacity: 0.7;">Instant conversions at your fingertips</div>
</div>
''', unsafe_allow_html=True)