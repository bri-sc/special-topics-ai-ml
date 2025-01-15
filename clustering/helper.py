import numpy as np

def dendrogram_convert(dendrogram):
    """
    Convert dendrogram to a format that can be used by scipy.cluster.hierarchy.dendrogram
    
    :param dendrogram: numpy array of shape (n-1, 4) from hierarchical clustering algorithm. 
    
    :return: dendrogram in the format that can be used by scipy.cluster.hierarchy.dendrogram
    """
    new_dendrogram = np.array(dendrogram) 
    for i in range(len(new_dendrogram)):
        if np.any(new_dendrogram[i, 0] == new_dendrogram[:i, :2]):
            new_dendrogram[i, 0] =  new_dendrogram[:i+1, :2].max() + 1
        if np.any(new_dendrogram[i, 1] == new_dendrogram[:i, :2]):
            new_dendrogram[i, 1] =  new_dendrogram[:i+1, :2].max() + 1
    return new_dendrogram