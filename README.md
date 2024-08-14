# OwlCrypt

OwlCrypt is a Python project designed for basic steganography. It allows users to embed messages into images using various techniques (which is LSB only), with the added flexibility to modify its behavior through custom scripts. However, this project is currently on indefinite hold.

## Features

- **Basic Steganography**: Embed messages into images using straightforward steganographic techniques.
- **Scriptable Behavior**: Customize the steganography process with user-defined scripts.
- **Image Processing**: Support for common image formats and basic manipulation.

## Installation

To install OwlCrypt, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/owlcrypt.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd owlcrypt
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Basic Usage**:
    Run the main application script to start using OwlCrypt:
    ```bash
    python owlcrypt.py
    ```

2. **Custom Scripts**:
    Place your custom scripts in the `scripts/` directory. You can modify the behavior of OwlCrypt by defining how messages are embedded or extracted.

3. **Examples**:
    ```python
    python main.py --input-path misc/4.1.01.tiff --output-path misc/4.1.01-processed.tiff --mode lsb --data "You can't find me!" 
    ```

## Contributing

Contributions to OwlCrypt are welcome! Please note that the project is currently on indefinite hold, so updates should not be expected. Contribution are free-for-all and no guidelines exist thanks to the project's current scale.

## License

This project is licensed under the MIT License.

## Contact

For any questions or further information, please contact the project maintainer:

- **Name**: AjinGixtas
- **Email**: ajingixtascontact@example.com
- **GitHub**: [My GitHub Profile](https://github.com/AjinGixtas)

---

Thank you for your interest in OwlCrypt!
