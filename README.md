# Steganography Image Creator

**Python-Based Image Steganography Tool**  
🖼️ Hide secret text messages inside images using LSB steganography  
🔓 Extract hidden messages from steganographic images  
🐍 Built with Python & Pillow  
🔬 Designed for cybersecurity learning, research & digital forensics  
👤 Created by **Rajatava Ghosh · RaxingR**

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)
![Pillow](https://img.shields.io/badge/Pillow-required-yellow)
![License](https://img.shields.io/badge/license-CC0--1.0-green)

---

## 🧬 Overview

**Steganography Image Creator** is a lightweight Python tool that allows users to **hide and extract secret text messages inside digital images** using the **Least Significant Bit (LSB)** steganography technique.

Unlike encryption, which transforms information into unreadable ciphertext, steganography focuses on **concealing the existence of the information itself**.

This project provides a simple implementation for understanding how image-based steganography works at the pixel level.

---

## ✨ Key Features

- 📝 **Hide Messages** — Embed secret text inside an image
- 🔓 **Extract Messages** — Recover hidden text from a stego image
- 🖼️ **LSB Steganography** — Uses pixel least significant bits for data embedding
- ⚡ **Lightweight** — Simple Python implementation
- 🧪 **Educational** — Useful for cybersecurity and steganography learning
- 🛠️ **Easy to Modify** — Simple source code for experimentation
- 📦 **Sample Image** — Includes `cover.png` for testing

---

## 🧠 How It Works

The project uses **Least Significant Bit (LSB)** steganography.

An RGB image contains three color channels:

```text
Red   → 0–255
Green → 0–255
Blue  → 0–255
```

The least significant bit of a channel can be changed with only a very small numerical difference.

Example:

```text
Original:
10110110

Secret Bit:
       ↓
10110111
```

Only the final bit changes.

### Encoding

```text
                  SECRET MESSAGE
                         │
                         ▼
                 Convert to Binary
                         │
                         ▼
                  LSB Encoding
                         │
                         ▼
                 Modify Image Pixels
                         │
                         ▼
                    STEGO IMAGE
```

### Decoding

```text
                    STEGO IMAGE
                         │
                         ▼
                   Read Pixel LSBs
                         │
                         ▼
                  Reconstruct Binary
                         │
                         ▼
                   Decode Text
                         │
                         ▼
                 ORIGINAL MESSAGE
```

---

## 📐 Encoding Formula

The basic LSB operation can be represented as:

```text
Modified Channel Value =
(Original Channel Value & 11111110) | Secret Bit
```

This clears the least significant bit and replaces it with a bit from the secret message.

---

## 🚀 Quick Start

### Requirements

- Python **3.7+**
- Pillow
- Git

Install Pillow:

```bash
pip install Pillow
```

Or:

```bash
pip3 install Pillow
```

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/RaxingR/Stegnography_Image_Creator.git
```

Enter the project directory:

```bash
cd Stegnography_Image_Creator
```

Install the dependency:

```bash
pip install Pillow
```

---

## ▶️ Run

Start the program:

```bash
python steganography.py
```

Or:

```bash
python3 steganography.py
```

Follow the application's prompts to hide or extract a message.

---

## 🖼️ Sample Image

The repository includes:

```text
cover.png
```

This image can be used as a sample carrier image when experimenting with the project.

---

## 📁 Project Structure

```text
Stegnography_Image_Creator/
│
├── steganography.py    # Main steganography program
├── cover.png           # Sample cover image
├── README.md           # Project documentation
├── LICENSE             # CC0 1.0 Universal
└── .gitignore          # Git configuration
```

---

## 🔍 Encoding Workflow

```text
TEXT MESSAGE
     │
     ▼
Convert Message → Binary
     │
     ▼
Add End Marker
     │
     ▼
Read Cover Image Pixels
     │
     ▼
Replace Pixel LSBs
     │
     ▼
Generate Stego Image
```

---

## 🔓 Decoding Workflow

```text
STEGO IMAGE
     │
     ▼
Read Pixel Channels
     │
     ▼
Extract LSBs
     │
     ▼
Reconstruct Binary Data
     │
     ▼
Detect End Marker
     │
     ▼
Convert Binary → Text
     │
     ▼
RECOVERED MESSAGE
```

---

## 📊 Image Capacity

For a standard RGB image, three color channels are available per pixel.

A simplified theoretical capacity is:

```text
Available Bits ≈ Width × Height × 3
```

Example:

```text
Image:
1000 × 1000 pixels

RGB channels:
3

Approximate available bits:
1000 × 1000 × 3

= 3,000,000 bits
```

The practical capacity is lower depending on the implementation and message termination data.

---

## 🛡️ Security Considerations

Steganography is **not encryption**.

This tool hides information inside an image, but the hidden message is not automatically cryptographically protected.

```text
Steganography ≠ Encryption
```

Anyone who knows the embedding technique may potentially recover the hidden message.

For sensitive information, encryption should be used before embedding when appropriate.

---

## ⚠️ Limitations

- LSB steganography can be vulnerable to statistical analysis
- Image resizing can destroy hidden information
- Image compression may corrupt embedded data
- Editing the image may remove the hidden message
- Detection resistance is not guaranteed
- The project does not provide cryptographic security by default
- Large messages may exceed the image's available capacity

---

## 🎯 Learning Objectives

This project can help develop practical knowledge in:

- Image steganography
- LSB encoding
- Pixel-level image manipulation
- Binary data representation
- Python programming
- Pillow image processing
- Cybersecurity fundamentals
- Digital forensics
- Covert-data techniques

---

## 🔬 Cybersecurity & Research Use

This project can be used for:

- 🧪 Cybersecurity laboratories
- 🎓 Academic projects
- 🔬 Security research
- 🕵️ Digital-forensics education
- 🧠 Steganography demonstrations
- 🧰 Controlled security experiments

Use the project only with images and information you are authorized to handle.

---

## 🔮 Future Improvements

```text
[ ] AES encryption before embedding
[ ] Password-protected messages
[ ] Improved error handling
[ ] Image capacity calculator
[ ] Multiple image-format support
[ ] GUI interface
[ ] Drag-and-drop support
[ ] Batch encoding / decoding
[ ] Message length validation
[ ] Steganography detection mode
[ ] Detailed analysis reports
[ ] Improved extraction reliability
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Core implementation |
| **Pillow** | Image processing |
| **LSB Steganography** | Data embedding method |

---

## 📌 Project Information

| Category | Details |
|---|---|
| **Project Type** | Cybersecurity / Steganography |
| **Language** | Python |
| **Technique** | LSB Steganography |
| **Image Library** | Pillow |
| **Python Version** | 3.7+ |
| **Database** | Not required |
| **License** | CC0 1.0 Universal |

---

## 🤝 Contributing

Contributions, bug reports, improvements, and feature suggestions are welcome.

```text
Fork
  ↓
Create Branch
  ↓
Make Changes
  ↓
Test
  ↓
Commit
  ↓
Pull Request
```

For major changes, consider opening an issue first.

---

## 📜 License

This project is released under the **CC0 1.0 Universal** license.

See the [`LICENSE`](LICENSE) file for complete license information.

---

## 👨‍💻 Creator

**Rajatava Ghosh**  
**RaxingR**

Cybersecurity enthusiast focused on:

- 🛡️ Cybersecurity & Ethical Hacking
- 🔍 Digital Forensics
- 🧪 Security Research
- 💻 Technology & Software
- 🤖 AI & Emerging Technologies

### GitHub

[![GitHub](https://img.shields.io/badge/GitHub-RaxingR-black?logo=github)](https://github.com/RaxingR)

---

## ⚠️ Disclaimer

**FOR EDUCATIONAL, RESEARCH & AUTHORIZED USE ONLY**

This project is provided for:

- Cybersecurity education
- Research
- Academic projects
- Laboratory experimentation
- Authorized security analysis

Users are solely responsible for ensuring that their use of this software complies with applicable laws, regulations, and authorization requirements.

Do not use this project to conceal, access, or distribute information without proper authorization.

---

## ⭐ Support

If you find this project useful for learning about **steganography, Python, image processing, or cybersecurity**, consider giving the repository a star.

---

**Hide the data. Understand the technique. Explore steganography.** 🔐
