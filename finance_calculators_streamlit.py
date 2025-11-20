import streamlit as st

# Main header for the app
st.header("Investment / Bond Repayment Calculator", divider='rainbow')

# Radio buttons for user to choose between investment or bond repayment
# calculations
user_calc_choice = st.radio(
    "Choose what to calculate:",
    ["Future Investment Value", "Bond Repayment Amount"],
    horizontal=True,
)


def interest_calc(P, r, t, interest_type):
    # Calculate the investment value based on the interest type
    if interest_type == "simple":
        # Formula: A = P * (1 + r * t)
        A = round(P * (1 + r * t), 2)
    elif interest_type == "compound":
        # Formula: A = P * (1 + r)^t
        A = round(P * (1 + r)**t, 2)
    else:
        # Defensive programming: should never reach this point if inputs are
        # valid
        assert False, \
            "This point should never be reached.  Function input is incorrect."
    return A


# -------------------------------------------------------------------------
# If the user selects the "Future Investment Value" calculator
# -------------------------------------------------------------------------
if user_calc_choice == "Future Investment Value":
    try:
        deposit_str = st.text_input("Enter a deposit amount:")
        deposit_amt = float(deposit_str)
    except ValueError:
        if deposit_str != "":
            st.write("Not a number")

    interest_type = st.radio(
        "Select the interest type:",
        ["Simple", "Compound"],
        horizontal=True,
    ).lower()

    interest_perc = st.slider(
        "Select an interest rate:",
        min_value=0.0,
        max_value=30.0,
        step=0.25,
        value=8.0
    ) / 100

    try:
        no_years_str = st.text_input("How long will the deposit be invested \
(in years)?")
        no_years = int(no_years_str)
    except ValueError:
        # First check if input is a float (but not an integer)
        try:
            float(no_years_str)
            st.write("Not an integer")
        except ValueError:
            # If not convertible to number at all, show error
            if no_years_str != "":
                st.write("Not a number")

    # Perform calculation only if required variables exist
    if ("deposit_amt" in locals()) and ("no_years" in locals()):
        output_value = interest_calc(deposit_amt, interest_perc, no_years,
                                     interest_type)
        # Display the result with dividers and styled text
        st.divider()
        st.markdown("Investment Amount:")
        st.subheader(f"R{output_value:,.2f}".replace(",", " "))
        st.divider()

# -------------------------------------------------------------------------
# If the user selects the "Bond Repayment Amount" calculator
# -------------------------------------------------------------------------
else:
    try:
        # Request current house value
        house_pv_str = st.text_input("Enter the current value of the house:")
        house_pv = float(house_pv_str)  # Convert to float
    except ValueError:
        if house_pv_str != "":
            st.write("Not a number")

    # Slider for annual nominal interest rate (%), converted to monthly
    # decimal value
    interest_perc = st.slider(
        "Select an annual nominal interest rate:",
        min_value=0.0,
        max_value=30.0,
        step=0.25,
        value=8.0
    ) / 100
    mnthly_interest_perc = interest_perc / 12

    try:
        # Request repayment period in months
        repayment_months_str = st.text_input("How long will the deposit be \
invested (in years)?")
        repayment_months = int(repayment_months_str)
    except ValueError:
        # First check if input is a float (but not an integer)
        try:
            float(repayment_months_str)
            st.write("Not an integer")
        except ValueError:
            # If not convertible to number at all, show error
            if repayment_months_str != "":
                st.write("Not a number")

    # --------------------------------------------------------------------
    # Perform calculation only if required variables exist
    if ("house_pv" in locals()) and ("repayment_months" in locals()):
        # Calcualte the repayment amount using the bond repayment formula:
        # Repayment = (i * P) / (1 - (1 + i)^(-n))
        repayment_amt = round(
            (mnthly_interest_perc * house_pv) /
            (1 - (1 + mnthly_interest_perc) ** (-repayment_months)),
            2,
        )
        # Display the result with dividers and styled text
        st.divider()
        st.markdown("Your monthly bond repayment:")
        st.subheader(f"R{repayment_amt:,.2f}".replace(",", " "))
        st.divider()
