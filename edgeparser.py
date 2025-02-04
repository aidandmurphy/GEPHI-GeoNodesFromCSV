import numpy as np
import pandas as pd


def create_degree_matrix(csv_file):
    """
    Create a MATLAB-style degree matrix from a CSV file containing network edges.
    
    Parameters:
    csv_file (str): Path to the CSV file with columns: Source, Target, Type, Id, Label, Weight
    
    Returns:
    tuple: (degree_matrix as numpy array, node_labels as list, matlab_string as str)
    """
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Get unique nodes from both Source and Target columns
    nodes = sorted(list(set(df['Source'].unique()) | set(df['Target'].unique())))
    n_nodes = len(nodes)
    
    # Create a mapping of node names to indices
    node_to_idx = {node: idx for idx, node in enumerate(nodes)}
    
    # Initialize degree matrix with zeros
    degree_matrix = np.zeros((n_nodes, n_nodes))
    
    # Calculate degrees
    degrees = {}
    for node in nodes:
        # Count occurrences in Source and Target columns
        source_count = df[df['Source'] == node].shape[0]
        target_count = df[df['Target'] == node].shape[0]
        degrees[node] = source_count + target_count
    
    # Fill the diagonal of the degree matrix
    for node, degree in degrees.items():
        idx = node_to_idx[node]
        degree_matrix[idx, idx] = degree
    
    # Create MATLAB-style string representation
    matlab_str = "D = [\n"
    for row in degree_matrix:
        matlab_str += "    " + " ".join(f"{val:g}" for val in row) + "\n"
    matlab_str += "];"
    
    return degree_matrix, nodes, matlab_str

# Example usage
if __name__ == "__main__":
    # Replace 'network.csv' with your CSV file path
    csv_file = 'network.csv'
    
    try:
        degree_matrix, nodes, matlab_str = create_degree_matrix(csv_file)
        
        print("Node labels:", nodes)
        print("\nDegree Matrix:")
        print(degree_matrix)
        print("\nMATLAB format:")
        print(matlab_str)
        
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")