import os
import glob
from pathlib import Path

scripts_dir = Path('scripts')
for py_file in scripts_dir.glob('*.py'):
    text = py_file.read_text(encoding='utf-8')
    
    # Update CSV path
    text = text.replace("'zomato-data-analysis/Zomato data .csv'", "'data/Zomato data .csv'")
    text = text.replace('"zomato-data-analysis/Zomato data .csv"', '"data/Zomato data .csv"')
    text = text.replace("'Zomato data .csv'", "'data/Zomato data .csv'")
    
    # Use the file's stem to name the saved figure
    stem = py_file.stem.replace(' ', '_').lower()
    save_code = f"plt.savefig('assets/{stem}.png', bbox_inches='tight')\n# plt.show()"
    text = text.replace('plt.show()', save_code)
    
    py_file.write_text(text, encoding='utf-8')
    
print("Successfully patched scripts!")
