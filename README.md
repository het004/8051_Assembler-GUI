
# 8051 Microcontroller Assembler

A simple web-based 8051 microcontroller assembler and simulator built using **Python** and **Streamlit**. This project supports a subset of 8051 assembly instructions and provides a real-time visualization of register and flag states for educational purposes.

---

## 📖 Introduction to the 8051 Microcontroller

The 8051 microcontroller is a popular microcontroller architecture developed by Intel in the 1980s. It is widely used in embedded systems due to its simplicity, versatility, and ease of programming. The 8051 microcontroller features:

- **8-bit CPU**: The 8051 processes 8-bit data and has an 8-bit data bus.
- **Memory**: It includes 4KB of on-chip ROM and 128 bytes of RAM, along with 32 I/O pins.
- **Instruction Set**: The 8051 has a rich instruction set that includes arithmetic, logical, data transfer, and control flow instructions.
- **Timers/Counters**: It has two 16-bit timers/counters for timing operations and event counting.
- **Interrupts**: The 8051 supports five interrupt sources, allowing it to respond to external events.

The 8051 microcontroller is widely used in applications such as automotive systems, consumer electronics, industrial automation, and robotics.

---

## ✨ Features

- ✅ Supports a subset of 8051 instructions: 
  - **Data Transfer**: MOV
  - **Arithmetic Operations**: ADD, SUBB, INC, DEC
  - **Logical Operations**: ANL, ORL, XRL, CPL
  - **Bit Manipulation**: RL, RR, RLC, RRC, SWAP
- ✅ Works with registers (A, R0–R7, DPTR) and immediate values (#10H, #0x1F)
- ✅ Simulates flag updates: Carry (CY), Auxiliary Carry (AC), Overflow (OV), and Parity (P)
- ✅ Real-time user interface for inputting code and monitoring changes
- ✅ Error detection for invalid instructions or operands

---

## 🔧 Prerequisites

- Python 3.8 or higher
- Streamlit
- Other dependencies listed in `requirements.txt`

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/het004/8051_Assembler-GUI.git
   cd 8051_Assembler-GUI

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/8051-assembler.git
   cd 8051-assembler
   ```
   > Replace the URL with the actual repository if applicable.

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

Run the Streamlit app:

```bash
streamlit run main.py
```

Then, open your browser and go to [http://localhost:8501](http://localhost:8501).

### Example Code:

```asm
MOV A, #4F
SUBB A, #10H
ANL A, #0FH
CPL A
```

**Expected Result:**
- `A` changes from `4FH` → `3FH` → `00H` → `FFH`

---

## 🗂️ Project Structure

```
8051_Microcontroller_Assembler/
├── main.py              # Streamlit app entry point
├── assembler_gui.py     # UI and state management
├── parser.py            # Parses assembly code
├── executor.py          # Executes parsed instructions
├── state.py             # Defines registers and flags
├── flags.py             # Handles flag updates
├── utils.py             # Utility functions
├── requirements.txt     # Required Python packages
└── Instructions/
    ├── __init__.py
    ├── arithmetic.py    # ADD, SUBB, INC, DEC
    ├── logic.py         # ANL, ORL, XRL, CPL
    ├── data_transfer.py # MOV
    ├── shift_rotate.py  # RL, RR, RLC, RRC, SWAP
    └── control_flow.py  # (Future expansion)
```

---

## 🧩 Contributing

1. **Fork** the repo
2. Create a new branch:  
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Added feature XYZ"
   ```
4. Push to the branch:  
   ```bash
   git push origin feature-branch
   ```
5. **Open a pull request**

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🛠️ Troubleshooting

| Issue                                 | Solution                                                                 |
|--------------------------------------|--------------------------------------------------------------------------|
| `ModuleNotFoundError: No module named 'state'` | Ensure `state.py` exists in the root directory and you're running `main.py`. |
| UI not loading                        | Check for errors in terminal; ensure all dependencies are installed.     |
| Invalid instruction error            | Use valid syntax (`#10H`, not `#10`) and check register names.           |

---

## 🙏 Acknowledgments

- Built using [Streamlit](https://streamlit.io/)
- Inspired by educational tools for learning 8051 microcontroller assembly
