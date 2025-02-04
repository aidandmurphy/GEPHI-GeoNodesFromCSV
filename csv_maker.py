import csv

def generate_edges_csv(start_index, num_iterations, output_file="edges.csv"):
    """
    Generate a CSV file with edge data for Gephi.
    
    Args:
        start_index (int): Starting index for the source nodes
        num_iterations (int): Number of edges to generate
        output_file (stsr): Name of the output CSV file
    """
    # Header for the CSV file
    headers = ['Source', 'Target', 'Type', 'Id', 'Label', 'Weight']
    
    # Data to write to CSV
    edges = []
    
    for i in range(num_iterations):
        source = start_index + i
        target = source + 1
        
        # Create label
        label = f"ORG-24.7.3.{i+4}"
        
        edge = {
            'Source': source,
            'Target': target,
            'Type': 'Undirected',
            'Id': i,
            'Label': label,
            'Weight': 1
        }
        edges.append(edge)
    
    # Write to CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(edges)
        
    print(f"CSV file '{output_file}' has been created successfully!")

# Example usage
if __name__ == "__main__":
    start_index = int(input("Enter starting index: "))
    num_iterations = int(input("Enter number of iterations: "))
    generate_edges_csv(start_index, num_iterations)