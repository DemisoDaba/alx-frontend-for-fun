# Markdown to HTML Converter

## Overview

This repository hosts a Python script designed to convert Markdown files into HTML, offering insights into the underlying mechanics of Markdown processing.

## Requirements

- Python 3.7 or newer
- Ubuntu 18.04 LTS environment
- PEP 8 style compliance

## Tasks

### 1. Script Setup

- Create `markdown2html.py` Python script.
- Handle command-line arguments for input and output files.
- Implement error handling for missing files.

### 2. Headings

- Parse Markdown heading syntax (#, ##, ###, etc.).
- Generate corresponding HTML heading tags (`<h1>`, `<h2>`, etc.).

### 3. Unordered Lists

- Parse unordered list syntax (-).
- Generate HTML unordered list tags (`<ul>` and `<li>`).

### 4. Ordered Lists

- Parse ordered list syntax (*).
- Generate HTML ordered list tags (`<ol>` and `<li>`).

### 5. Paragraphs and Line Breaks

- Parse paragraphs and line breaks in Markdown.
- Generate HTML paragraph (`<p>`) and line break (`<br/>`) tags.

### 6. Bold and Emphasis

- Parse bold (**) and emphasis (__) syntax.
- Generate HTML bold (`<b>`) and emphasis (`<em>`) tags.

### 7. Special Syntax

- Parse custom syntax:
  - `[[text]]`: Convert to MD5 hash (lowercase).
  - `((text))`: Remove all "c" characters (case-insensitive).

## Repository

- GitHub repository: [alx-frontend-for-fun](https://github.com/DemisoDaba/alx-frontend-for-fun)
- Main file: `markdown2html.py`
