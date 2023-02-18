## ================================================================================
## CHRONO WORKBENCH - github.com/Concrete-Chrono-Development/chrono-preprocessor
##
## Copyright (c) 2023 
## All rights reserved. 
##
## Use of this source code is governed by a BSD-style license that can be found
## in the LICENSE file at the top level of the distribution and at
## github.com/Concrete-Chrono-Development/chrono-preprocessor/blob/main/LICENSE
##
## ================================================================================
## Author: Matthew Troemner
## ================================================================================
##
## Description coming soon...
##
##
## ================================================================================

import numpy as np

def surfMeshSize(vertices, faces):
    # Calculate the edge lengths for all faces
    edge_lengths_1 = np.linalg.norm(vertices[faces[:,1].astype(int) - 1, 0:3] - vertices[faces[:,0].astype(int) - 1, 0:3], axis=1)
    edge_lengths_2 = np.linalg.norm(vertices[faces[:,2].astype(int) - 1, 0:3] - vertices[faces[:,1].astype(int) - 1, 0:3], axis=1)
    edge_lengths_3 = np.linalg.norm(vertices[faces[:,2].astype(int) - 1, 0:3] - vertices[faces[:,0].astype(int) - 1, 0:3], axis=1)

    # Combine the edge lengths and find the maximum
    edge_lengths = np.concatenate((edge_lengths_1, edge_lengths_2, edge_lengths_3))
    max_edge_length = np.amax(edge_lengths)

    return max_edge_length
