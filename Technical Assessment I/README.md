# Arithmetic Sequence Generator
by Natanael Jansudin Siregar (https://www.natanaelsiregar.me/)

This Python project provides a class to generate an arithmetic sequence and display it as a string. It accepts a user input specifying the number of terms and outputs the arithmetic sequence.

# Getting Started

## Prerequisites

- Python 3 should be installed on your system.


## Features

- **Arithmetic Sequence Generation:** Generates an arithmetic sequence using the first term and the common difference.
- **Customizable Parameters:** By default, the sequence starts from 2 with a common difference of 3. These can be customized if needed.
- **Input Handling:** The program ensures that the user inputs a positive integer.

## Penjelasan Kode (Dalam Bahasa Indonesia):

### Kelas ArithmeticSequence:

* __init__: Menginisialisasi atribut first_term dan difference dengan nilai default.
* generate_sequence: Menghasilkan deret aritmatika berdasarkan jumlah N yang dimasukkan oleh pengguna.
* sequence_to_string: Menghasilkan deret aritmatika dan mengembalikannya sebagai string tanpa spasi.

### Fungsi main:
* Mengambil input dari pengguna untuk jumlah suku 𝑁
* Memastikan bahwa input adalah bilangan bulat positif.
* Membuat instance dari kelas ArithmeticSequence dan mendapatkan deret sebagai string.
* Menampilkan hasil deret aritmatika.

## Installation

### 1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/natanaelsiregar/Sr_SE_Natanael-Jansudin-Siregar_Technical-Assessment_241003.git
   cd /Technical Assessment I
   ```

### Navigate into the project directory:
```bash
cd arithmetic-sequence-generator
```

### Run the program:
```bash
python arithmetic_sequence.py
```

### Input the number of terms for the arithmetic sequence when prompted:
```bash
Input: 5
```

### The program will output the generated arithmetic sequence as a string:
```bash
Output: 2,5,8,11,14
```

### Example
To generate an arithmetic sequence with 5 terms (starting from 2 with a difference of 3):
```bash
Input: 7
Output: 2,5,8,11,14,17,20 
```
