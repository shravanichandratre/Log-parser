import matplotlib.pyplot as plt

# Read error code data with error handling
try:
    error_codes = []
    counts = []
    
    with open('error_codes_for_viz.txt', 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                count, code = parts
                error_codes.append(int(code))
                counts.append(int(count))
    
    # Debugging: print parsed data
    print("Error Codes:", error_codes)
    print("Counts:", counts)
    
    # Create bar chart with enhanced styling
    plt.figure(figsize=(10, 6))
    plt.bar(error_codes, counts, color='skyblue', edgecolor='navy')
    plt.title('Error Code Frequency', fontsize=15)
    plt.xlabel('Error Codes', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.xticks(error_codes)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('error_code_frequency.png', dpi=300)
    plt.close()
    
except FileNotFoundError:
    print("Error: File 'error_codes_for_viz.txt' not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
