# 🔄 Unit Converter

A beautiful, interactive web application for converting between different units of measurement with real-time results and animated UI elements.

![Unit Converter App](https://i.imgur.com/placeholder.png) <!-- Replace with actual screenshot when available -->

## ✨ Features

- **Multiple Measurement Categories**:
  - 📏 **Length**: Convert between meters, kilometers, centimeters, millimeters, miles, yards, feet, and inches
  - ⚖️ **Weight**: Convert between kilograms, grams, milligrams, metric tons, pounds, ounces, and stones
  - 🧪 **Volume**: Convert between liters, milliliters, cubic meters, cubic centimeters, gallons, quarts, pints, cups, and fluid ounces

- **User-Friendly Interface**:
  - Intuitive category selection with appropriate icons
  - Easy unit selection with dropdown menus
  - Real-time conversion results
  - Unit swap functionality with a single click

- **Enhanced Visual Experience**:
  - Smooth animations and transitions
  - Responsive design with beautiful gradients
  - Interactive elements with hover effects
  - Detailed conversion formulas and explanations

- **Educational Component**:
  - Expandable section showing the conversion formula
  - Visual representation of conversion rates
  - Detailed explanation of the conversion process

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone this repository or download the source code

2. Navigate to the project directory
   ```bash
   cd unit_converter
   ```

3. Install the required dependencies
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

1. Start the Streamlit application
   ```bash
   streamlit run app.py
   ```

2. The application will open in your default web browser at `http://localhost:8501`

3. Using the converter:
   - Select a measurement category (Length, Weight, or Volume)
   - Choose the source unit from the "From Unit" dropdown
   - Choose the target unit from the "To Unit" dropdown
   - Enter the value you want to convert
   - View the conversion result instantly
   - Click "Swap Units" to reverse the conversion direction
   - Expand the "Conversion Formula & Details" section to see the mathematical explanation

## 🧮 Supported Conversions

### Length Units
- Meter (base unit)
- Kilometer
- Centimeter
- Millimeter
- Mile
- Yard
- Foot
- Inch

### Weight Units
- Kilogram (base unit)
- Gram
- Milligram
- Metric Ton
- Pound
- Ounce
- Stone

### Volume Units
- Liter (base unit)
- Milliliter
- Cubic Meter
- Cubic Centimeter
- Gallon (US)
- Quart (US)
- Pint (US)
- Cup (US)
- Fluid Ounce (US)

## 🛠️ Technologies Used

- **Streamlit**: For the web application framework
- **Pandas**: For data handling
- **HTML/CSS**: For styling and animations
- **Python**: For core functionality and conversion logic

## 📝 How It Works

The application uses a base unit for each measurement category:
- Length: Meter
- Weight: Kilogram
- Volume: Liter

When converting between units, the application:
1. Converts the input value to the base unit
2. Converts from the base unit to the target unit
3. Displays the result with appropriate formatting

This two-step conversion process ensures accuracy and consistency across all unit conversions.

## 🤝 Contributing

Contributions are welcome! Feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

✨ Created with Streamlit • Unit Converter App • 2025 ✨