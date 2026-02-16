# Invoice Generator (Python)

A command-line Python tool that creates professional PDF invoices for auto repair jobs.  
It supports parts + labor line items, automatic totals, optional sales tax, and exports invoices to a timestamped PDF.

## Features
- Enter customer + vehicle info
- Add **parts** (description + cost)
- Add **labor** (description + hours + rate)
- Auto-calculates subtotal, tax, and total
- Exports a clean PDF invoice to `output/`

## Requirements
- Python 3.x
- reportlab

## Install
```bash
pip install -r requirements.txt
