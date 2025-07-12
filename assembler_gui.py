import streamlit as st
from streamlit_ace import st_ace
import pandas as pd
from parser import parse_code
from executor import execute_instructions
from state import REGISTERS, FLAGS

def show_gui():
    st.markdown("<h2 style='text-align: center;'>8051 Assembler</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns((2, 3))

    with c1:
        code = st_ace(
            value="",
            language="assembly_x86",  # No specific 8051 mode, using x86 as fallback
            theme="monokai",
            font_size=20,
            key="code_editor"
        )
        if st.button("Compile", use_container_width=True):
            instructions, errors = parse_code(code)
            with c2:
                if errors:
                    for error in errors:
                        st.markdown(f"<h7 style='text-align: left; color: red;'>{error}</h7>", unsafe_allow_html=True)
                else:
                    try:
                        execute_instructions(instructions)
                        st.markdown("<h6 style='text-align: center; color: orange;'>Register Status</h6>", unsafe_allow_html=True)
                        registers_df = pd.DataFrame(REGISTERS, index=['|'])
                        st.table(registers_df)
                        st.markdown("<h6 style='text-align: center; color: orange;'>Program Status Word</h6>", unsafe_allow_html=True)
                        flags_df = pd.DataFrame(FLAGS, index=['|'])
                        st.table(flags_df)
                    except ValueError as e:
                        st.markdown(f"<h7 style='text-align: left; color: red;'>Execution Error: {str(e)}</h7>", unsafe_allow_html=True)