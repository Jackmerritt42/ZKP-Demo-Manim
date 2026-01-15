# Zero-Knowledge Proofs Visualized

A high-fidelity educational animation suite built with [Manim](https://www.manim.community/) (Mathematical Animation Engine). This project visualizes the complex cryptographic concept of **Zero-Knowledge Proofs (ZKPs)** using three intuitive analogies.

## The Animations

This repository contains a narrative animation  that breaks down ZKPs into three examples:

1.  **The Intuition (Colorblind Friend):** Explains the core logic of interactive proofs using probability. How do you prove two balls are different colors to someone who sees them as identical?
2.  **The "Where's Waldo" Problem:** A visual demonstration of a non-interactive proof. Proving you know the location of a secret on a map without revealing its coordinates (using a giant shield).
3.  **The Classic Analogy (Ali Baba's Cave):** The  cryptographic story demonstrating how to prove possession of a secret key without displaying the key itself.

## Getting Started

### Prerequisites
* [Python 3.7+](https://www.python.org/)
* [FFmpeg](https://ffmpeg.org/) (Required for Manim video rendering)
* LaTeX (Optional, but might cause issues for rendering mathematical equations)

### Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/Jackmerritt42/ZKP-Demo-Manim)
    cd threshold-crypto-visualized
    ```

2.  **Install Dependencies**
    It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

##  Usage

To render the full animation in **High Quality (1080p, 60fps)**:

```bash
manim -pqh scene.py ZKP_Demo