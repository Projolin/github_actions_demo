name: Python Matrix Build

on:
  push:
    branches:
      - main

jobs:
  test-python:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10]  # Valid Python versions
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}

      - name: Debug Python Version
        run: echo "Using Python version: ${{ matrix.python-version }}"

      - name: Run Array Manipulation Script
        run: python test_array_manipulation.py

