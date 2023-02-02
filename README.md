# XML-Visualisation
[![Generic badge](https://img.shields.io/badge/Python-3.6|3.7|3.8|3.9-blue.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/PyPI-0.1.0-green.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/License-MIT-red.svg)](https://shields.io/)

This is a project to visualise XML files in a tree structure. It is written in Python and uses the Tkinter library for the GUI.

## Compresseion
The XML files are compressed and decompressed using LZ77 algorithm. The algorithm is implemented in the `compressor.py` file. The compression is done using the `compress` function and the decompression is done using the `decompress` function.

## Visualisation
The visualisation is done using the NetworkX library. The `visualise` function in the `visualiser.py` file takes the decompressed XML file and returns a NetworkX graph. The graph is then visualised using the `draw` function in the `visualiser.py` file.

## GUI
The GUI is done using the Tkinter library. The `gui.py` file contains the GUI code. The GUI has 3 buttons:

- `Compress` button: This button compresses the XML file and asks the user to save the compressed file.
- `Decompress` button: This button decompresses the XML file and asks the user to save the decompressed file.
- `Analyse` button: This button analyses the XML file and shows the analysis in a new window.
- `Visualise` button: This button visualises the XML file and shows the visualisation in a new window.

## Installation
To install the project, you need to have [Python 3](https://www.python.org/downloads/) installed. Then you can clone the repository and install the dependencies with pip:

Clone the repository and install the dependencies:
```
    git clone

    cd xml-visualisation

    pip install -r requirements.txt
```
## Usage

    python main.py

## Authors

- David Ayman - [GitHub](https://github.com/X3nonC0der) | [LinkedIn](https://www.linkedin.com/in/david-ayman/)
- Kerolos Sameh - [GitHub](https://github.com/KahrabaVv) | [LinkedIn](https://www.linkedin.com/in/kerolos--sameh/)
- Andrew Adel - [GitHub](https://github.com/Andrew-Adel) | [LinkedIn](https://www.linkedin.com/in/andrew-adel-7b8578206)
- Mark Emad - [GitHub](https://github.com/Markadies)
- Andrew Samir - [GitHub](https://github.com/AndrewSamir278)

## Acknowledgements

- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [LZ77](https://en.wikipedia.org/wiki/LZ77_and_LZ78)
- [NetworkX](https://networkx.org/)
- [Matplotlib](https://matplotlib.org/)

## License

[MIT](https://choosealicense.com/licenses/mit/)

