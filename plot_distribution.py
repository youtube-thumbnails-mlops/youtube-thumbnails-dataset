import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    # Path to metadata
    csv_path = 'test_set/metadata.csv'
    
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    # Read csv
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    if 'category_name' not in df.columns:
        print("Error: 'category_name' column not found in CSV.")
        print(f"Columns found: {df.columns.tolist()}")
        return

    # Count classes
    class_counts = df['category_name'].value_counts()
    
    print("Class Counts:")
    print(class_counts)

    # Plot
    plt.figure(figsize=(10, 6))
    bars = class_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Class Distribution in Test Set', fontsize=16)
    plt.xlabel('Category Name', fontsize=12)
    plt.ylabel('Number of Samples', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add counts above bars
    for i, v in enumerate(class_counts):
        plt.text(i, v + 0.5, str(v), ha='center', va='bottom')

    plt.tight_layout()

    # Save plot
    output_path = 'class_distribution.png'
    plt.savefig(output_path)
    print(f"Plot saved to {os.path.abspath(output_path)}")

if __name__ == "__main__":
    main()
