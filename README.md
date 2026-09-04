# Steganography Image Creator

A simple Python tool for hiding and revealing secret text messages inside images using the Least Significant Bit (LSB) steganography technique.

> **Repository:** `RaxingR/Stegnography_Image_Creator`
> **Main script:** `steganography.py`
> **Sample cover image:** `cover.png`
> **License:** [CC0 1.0 Universal](LICENSE)

---

## Overview

**Steganography** is the practice of concealing information within another, seemingly ordinary file — in this case, a digital image — so that the hidden data is invisible to a casual observer. Unlike encryption, which scrambles data so it *cannot* be read, steganography hides data so its *existence* is not obvious in the first place.

This project provides a lightweight Python script (`steganography.py`) that can embed a secret text message into a cover image and later extract that message from the modified image. A sample cover image (`cover.png`) is included so you can test the tool immediately after cloning the repository.

---

## Features

- Hide a text message inside a cover image
- Extract a previously hidden message from a stego image
- Uses the Least Significant Bit (LSB) technique for minimal, imperceptible image changes
- Ships with a ready-to-use sample cover image (`cover.png`)
- Simple, single-file Python script that's easy to read and modify
- Educational-focused: a great starting point for learning how LSB steganography works

> **Note:** This tool is intended for educational and demonstration purposes. It does **not** provide cryptographic security — anyone using a similar LSB extraction method could potentially recover the hidden message.

---

## How It Works

Image steganography using LSB relies on the fact that changing the *least significant bit* of a pixel's color channel value produces a change so small (at most 1 out of 255) that it is imperceptible to the human eye.

For each bit of the secret message, one color channel's last bit is cleared and replaced with that message bit:


$$\text{Modified Channel Value} = (\text{Original Channel Value} \mathbin{\&} 0b11111110) \mathbin{|} \text{Secret Bit}$$

The message is first converted into its binary representation, and a delimiter (a special end-of-message marker) is typically appended so the decoder knows where the hidden data stops. Since a standard RGB image provides 3 channels per pixel, the approximate storage capacity of an image is:


$$\text{Storage Capacity (characters)} \approx \left\lfloor \frac{\text{Width} \times \text{Height} \times 3}{8} \right\rfloor$$

In practice, the real usable capacity is slightly lower than this estimate, since a few bits are reserved for the end-of-message delimiter or a length header.

---

## Requirements

- Python 3.7+
- [Pillow](https://python-pillow.org/) (PIL fork) for image manipulation

Install the dependency with:

```bash
pip install Pillow
