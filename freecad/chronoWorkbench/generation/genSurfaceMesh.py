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

import FreeCAD as App
import ObjectsFem
import numpy as np
from femmesh.gmshtools import GmshTools as gmsh



def genSurfMesh(analysisName,geoName,meshName,minPar,maxPar):


    # Set up Gmsh
    femmesh_obj = ObjectsFem.makeMeshGmsh(App.ActiveDocument, meshName)
    App.ActiveDocument.getObject(meshName).CharacteristicLengthMin = minPar
    App.ActiveDocument.getObject(meshName).CharacteristicLengthMax = 2*minPar
    App.ActiveDocument.getObject(meshName).MeshSizeFromCurvature = 0
    App.ActiveDocument.getObject(meshName).ElementOrder = u"1st"
    App.ActiveDocument.getObject(meshName).Algorithm2D = u"Delaunay"
    App.ActiveDocument.getObject(meshName).Algorithm3D = u"Delaunay"
    App.ActiveDocument.getObject(meshName).ElementDimension = u"3D"
    App.ActiveDocument.getObject(meshName).CoherenceMesh = True
    App.ActiveDocument.ActiveObject.Part = App.getDocument(App.ActiveDocument.Name).getObjectsByLabel(geoName)[0]
    App.ActiveDocument.recompute()
    App.ActiveDocument.getObject(meshName).adjustRelativeLinks(App.ActiveDocument.getObject(analysisName))
    App.ActiveDocument.getObject(analysisName).addObject(App.ActiveDocument.getObject(meshName))

    # Run Gmsh
    gmsh_mesh = gmsh(femmesh_obj)
    error = gmsh_mesh.create_mesh()
    print(error)
    App.ActiveDocument.recompute()

    femmesh = App.ActiveDocument.getObject(meshName).FemMesh


    vertices = []
    edges = []
    faces = []
    tets = []


    for v in femmesh.Nodes:
        vertices.append(femmesh.Nodes[v])
    vertices = np.asarray(vertices)

    for v in femmesh.Edges:
        edges.append(femmesh.getElementNodes(v))
    edges = np.asarray(edges)

    for v in femmesh.Faces:
        faces.append(femmesh.getElementNodes(v))
    faces = np.asarray(faces)

    for v in femmesh.Volumes:
        tets.append(femmesh.getElementNodes(v))
    tets = np.asarray(tets)
    tets = (tets).astype(int)

    return vertices,edges,faces,tets
