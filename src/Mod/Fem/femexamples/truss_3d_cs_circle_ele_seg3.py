# ***************************************************************************
# *   Copyright (c) 2021 Bernd Hahnebach <bernd@bimstatik.org>              *
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

import FreeCAD
from FreeCAD import Vector as vec

from BOPTools import SplitFeatures
from Part import makeLine

import Fem
import ObjectsFem

from . import manager
from .manager import get_meshname
from .manager import init_doc


def get_information():
    return {
        "name": "Truss 3D circle cs, seg3 elements",
        "meshtype": "edge",
        "meshelement": "Seg3",
        "constraints": ["fixed", "force"],
        "solvers": ["calculix", "ccxtools"],
        "material": "solid",
        "equation": "mechanical"
    }


def get_explanation(header=""):
    return header + """

# To run the example from Python console use,
# (works even after an edit without restart of FreeCAD):
import importlib
import femexamples.truss_3d_cs_circle_ele_seg3 as example
importlib.reload(example)
example.setup()


See forum topic post:
https://forum.freecadweb.org/viewtopic.php?f=18&t=23318&start=20#p521050
https://forum.freecadweb.org/viewtopic.php?f=13&t=59239&start=100#p521220

Z88 official example 2, crane beam
- nonsway (on x deformation on both support)
- in pratical engineering one would let the truss breathe on one side
- max deflection CalxuliX: 8.22 mm  # but it needs four seg3 elements foreach bar
- max deflection Mystran : x.xx mm
- max deflection Z88 : 8.19 mm  # one seg2 truss element foreach bar
"""


def setup(doc=None, solvertype="ccxtools"):

    # init FreeCAD document
    if doc is None:
        doc = init_doc()

    # explanation object
    # just keep the following line and change text string in get_explanation method
    manager.add_explanation_obj(doc, get_explanation(manager.get_header(get_information())))

    # geometric object
    # load line
    load_line = doc.addObject("Part::Line", "LoadLine")
    load_line.X1 = 0
    load_line.Y1 = 0
    load_line.Z1 = 1000
    load_line.X2 = 0
    load_line.Y2 = 0
    load_line.Z2 = 0
    if FreeCAD.GuiUp:
        load_line.ViewObject.hide()

    # commands where generated by Pyhon out of the original Z88 Mesh obj data
    v1 = vec(0.0, 2000.0, 0.0)
    v2 = vec(0.0, 0.0, 0.0)
    v3 = vec(1000.0, 1000.0, 2000.0)
    v4 = vec(2000.0, 2000.0, 0.0)
    v5 = vec(2000.0, 0.0, 0.0)
    v6 = vec(3000.0, 1000.0, 2000.0)
    v7 = vec(4000.0, 2000.0, 0.0)
    v8 = vec(4000.0, 0.0, 0.0)
    v9 = vec(5000.0, 1000.0, 2000.0)
    v10 = vec(6000.0, 2000.0, 0.0)
    v11 = vec(6000.0, 0.0, 0.0)
    v12 = vec(7000.0, 1000.0, 2000.0)
    v13 = vec(8000.0, 2000.0, 0.0)
    v14 = vec(8000.0, 0.0, 0.0)
    v15 = vec(9000.0, 1000.0, 2000.0)
    v16 = vec(10000.0, 2000.0, 0.0)
    v17 = vec(10000.0, 0.0, 0.0)
    v18 = vec(11000.0, 1000.0, 2000.0)
    v19 = vec(12000.0, 2000.0, 0.0)
    v20 = vec(12000.0, 0.0, 0.0)
    line1 = makeLine(v1, v2)
    line2 = makeLine(v4, v5)
    line3 = makeLine(v7, v8)
    line4 = makeLine(v10, v11)
    line5 = makeLine(v13, v14)
    line6 = makeLine(v16, v17)
    line7 = makeLine(v19, v20)
    line8 = makeLine(v1, v4)
    line9 = makeLine(v2, v5)
    line10 = makeLine(v4, v7)
    line11 = makeLine(v5, v8)
    line12 = makeLine(v7, v10)
    line13 = makeLine(v8, v11)
    line14 = makeLine(v10, v13)
    line15 = makeLine(v11, v14)
    line16 = makeLine(v13, v16)
    line17 = makeLine(v14, v17)
    line18 = makeLine(v16, v19)
    line19 = makeLine(v17, v20)
    line20 = makeLine(v1, v3)
    line21 = makeLine(v4, v6)
    line22 = makeLine(v7, v9)
    line23 = makeLine(v10, v12)
    line24 = makeLine(v13, v15)
    line25 = makeLine(v16, v18)
    line26 = makeLine(v2, v3)
    line27 = makeLine(v5, v6)
    line28 = makeLine(v8, v9)
    line29 = makeLine(v11, v12)
    line30 = makeLine(v14, v15)
    line31 = makeLine(v17, v18)
    line32 = makeLine(v3, v4)
    line33 = makeLine(v6, v7)
    line34 = makeLine(v9, v10)
    line35 = makeLine(v12, v13)
    line36 = makeLine(v15, v16)
    line37 = makeLine(v18, v19)
    line38 = makeLine(v3, v5)
    line39 = makeLine(v6, v8)
    line40 = makeLine(v9, v11)
    line41 = makeLine(v12, v14)
    line42 = makeLine(v15, v17)
    line43 = makeLine(v18, v20)
    line44 = makeLine(v3, v6)
    line45 = makeLine(v6, v9)
    line46 = makeLine(v9, v12)
    line47 = makeLine(v12, v15)
    line48 = makeLine(v15, v18)
    line49 = makeLine(v2, v4)
    line50 = makeLine(v5, v7)
    line51 = makeLine(v8, v10)
    line52 = makeLine(v11, v13)
    line53 = makeLine(v14, v16)
    line54 = makeLine(v17, v19)
    obj_line1 = doc.addObject("Part::Feature", "Line1")
    obj_line1.Shape = line1
    obj_line2 = doc.addObject("Part::Feature", "Line2")
    obj_line2.Shape = line2
    obj_line3 = doc.addObject("Part::Feature", "Line3")
    obj_line3.Shape = line3
    obj_line4 = doc.addObject("Part::Feature", "Line4")
    obj_line4.Shape = line4
    obj_line5 = doc.addObject("Part::Feature", "Line5")
    obj_line5.Shape = line5
    obj_line6 = doc.addObject("Part::Feature", "Line6")
    obj_line6.Shape = line6
    obj_line7 = doc.addObject("Part::Feature", "Line7")
    obj_line7.Shape = line7
    obj_line8 = doc.addObject("Part::Feature", "Line8")
    obj_line8.Shape = line8
    obj_line9 = doc.addObject("Part::Feature", "Line9")
    obj_line9.Shape = line9
    obj_line10 = doc.addObject("Part::Feature", "Line10")
    obj_line10.Shape = line10
    obj_line11 = doc.addObject("Part::Feature", "Line11")
    obj_line11.Shape = line11
    obj_line12 = doc.addObject("Part::Feature", "Line12")
    obj_line12.Shape = line12
    obj_line13 = doc.addObject("Part::Feature", "Line13")
    obj_line13.Shape = line13
    obj_line14 = doc.addObject("Part::Feature", "Line14")
    obj_line14.Shape = line14
    obj_line15 = doc.addObject("Part::Feature", "Line15")
    obj_line15.Shape = line15
    obj_line16 = doc.addObject("Part::Feature", "Line16")
    obj_line16.Shape = line16
    obj_line17 = doc.addObject("Part::Feature", "Line17")
    obj_line17.Shape = line17
    obj_line18 = doc.addObject("Part::Feature", "Line18")
    obj_line18.Shape = line18
    obj_line19 = doc.addObject("Part::Feature", "Line19")
    obj_line19.Shape = line19
    obj_line20 = doc.addObject("Part::Feature", "Line20")
    obj_line20.Shape = line20
    obj_line21 = doc.addObject("Part::Feature", "Line21")
    obj_line21.Shape = line21
    obj_line22 = doc.addObject("Part::Feature", "Line22")
    obj_line22.Shape = line22
    obj_line23 = doc.addObject("Part::Feature", "Line23")
    obj_line23.Shape = line23
    obj_line24 = doc.addObject("Part::Feature", "Line24")
    obj_line24.Shape = line24
    obj_line25 = doc.addObject("Part::Feature", "Line25")
    obj_line25.Shape = line25
    obj_line26 = doc.addObject("Part::Feature", "Line26")
    obj_line26.Shape = line26
    obj_line27 = doc.addObject("Part::Feature", "Line27")
    obj_line27.Shape = line27
    obj_line28 = doc.addObject("Part::Feature", "Line28")
    obj_line28.Shape = line28
    obj_line29 = doc.addObject("Part::Feature", "Line29")
    obj_line29.Shape = line29
    obj_line30 = doc.addObject("Part::Feature", "Line30")
    obj_line30.Shape = line30
    obj_line31 = doc.addObject("Part::Feature", "Line31")
    obj_line31.Shape = line31
    obj_line32 = doc.addObject("Part::Feature", "Line32")
    obj_line32.Shape = line32
    obj_line33 = doc.addObject("Part::Feature", "Line33")
    obj_line33.Shape = line33
    obj_line34 = doc.addObject("Part::Feature", "Line34")
    obj_line34.Shape = line34
    obj_line35 = doc.addObject("Part::Feature", "Line35")
    obj_line35.Shape = line35
    obj_line36 = doc.addObject("Part::Feature", "Line36")
    obj_line36.Shape = line36
    obj_line37 = doc.addObject("Part::Feature", "Line37")
    obj_line37.Shape = line37
    obj_line38 = doc.addObject("Part::Feature", "Line38")
    obj_line38.Shape = line38
    obj_line39 = doc.addObject("Part::Feature", "Line39")
    obj_line39.Shape = line39
    obj_line40 = doc.addObject("Part::Feature", "Line40")
    obj_line40.Shape = line40
    obj_line41 = doc.addObject("Part::Feature", "Line41")
    obj_line41.Shape = line41
    obj_line42 = doc.addObject("Part::Feature", "Line42")
    obj_line42.Shape = line42
    obj_line43 = doc.addObject("Part::Feature", "Line43")
    obj_line43.Shape = line43
    obj_line44 = doc.addObject("Part::Feature", "Line44")
    obj_line44.Shape = line44
    obj_line45 = doc.addObject("Part::Feature", "Line45")
    obj_line45.Shape = line45
    obj_line46 = doc.addObject("Part::Feature", "Line46")
    obj_line46.Shape = line46
    obj_line47 = doc.addObject("Part::Feature", "Line47")
    obj_line47.Shape = line47
    obj_line48 = doc.addObject("Part::Feature", "Line48")
    obj_line48.Shape = line48
    obj_line49 = doc.addObject("Part::Feature", "Line49")
    obj_line49.Shape = line49
    obj_line50 = doc.addObject("Part::Feature", "Line50")
    obj_line50.Shape = line50
    obj_line51 = doc.addObject("Part::Feature", "Line51")
    obj_line51.Shape = line51
    obj_line52 = doc.addObject("Part::Feature", "Line52")
    obj_line52.Shape = line52
    obj_line53 = doc.addObject("Part::Feature", "Line53")
    obj_line53.Shape = line53
    obj_line54 = doc.addObject("Part::Feature", "Line54")
    obj_line54.Shape = line54
    doc.recompute()
    geom_obj = SplitFeatures.makeBooleanFragments(name="CraneTruss")
    geom_obj.Objects = [
        obj_line1,
        obj_line2,
        obj_line3,
        obj_line4,
        obj_line5,
        obj_line6,
        obj_line7,
        obj_line8,
        obj_line9,
        obj_line10,
        obj_line11,
        obj_line12,
        obj_line13,
        obj_line14,
        obj_line15,
        obj_line16,
        obj_line17,
        obj_line18,
        obj_line19,
        obj_line20,
        obj_line21,
        obj_line22,
        obj_line23,
        obj_line24,
        obj_line25,
        obj_line26,
        obj_line27,
        obj_line28,
        obj_line29,
        obj_line30,
        obj_line31,
        obj_line32,
        obj_line33,
        obj_line34,
        obj_line35,
        obj_line36,
        obj_line37,
        obj_line38,
        obj_line39,
        obj_line40,
        obj_line41,
        obj_line42,
        obj_line43,
        obj_line44,
        obj_line45,
        obj_line46,
        obj_line47,
        obj_line48,
        obj_line49,
        obj_line50,
        obj_line51,
        obj_line52,
        obj_line53,
        obj_line54,
    ]
    if FreeCAD.GuiUp:
        obj_line1.ViewObject.hide()
        obj_line2.ViewObject.hide()
        obj_line3.ViewObject.hide()
        obj_line4.ViewObject.hide()
        obj_line5.ViewObject.hide()
        obj_line6.ViewObject.hide()
        obj_line7.ViewObject.hide()
        obj_line8.ViewObject.hide()
        obj_line9.ViewObject.hide()
        obj_line10.ViewObject.hide()
        obj_line11.ViewObject.hide()
        obj_line12.ViewObject.hide()
        obj_line13.ViewObject.hide()
        obj_line14.ViewObject.hide()
        obj_line15.ViewObject.hide()
        obj_line16.ViewObject.hide()
        obj_line17.ViewObject.hide()
        obj_line18.ViewObject.hide()
        obj_line19.ViewObject.hide()
        obj_line20.ViewObject.hide()
        obj_line21.ViewObject.hide()
        obj_line22.ViewObject.hide()
        obj_line23.ViewObject.hide()
        obj_line24.ViewObject.hide()
        obj_line25.ViewObject.hide()
        obj_line26.ViewObject.hide()
        obj_line27.ViewObject.hide()
        obj_line28.ViewObject.hide()
        obj_line29.ViewObject.hide()
        obj_line30.ViewObject.hide()
        obj_line31.ViewObject.hide()
        obj_line32.ViewObject.hide()
        obj_line33.ViewObject.hide()
        obj_line34.ViewObject.hide()
        obj_line35.ViewObject.hide()
        obj_line36.ViewObject.hide()
        obj_line37.ViewObject.hide()
        obj_line38.ViewObject.hide()
        obj_line39.ViewObject.hide()
        obj_line40.ViewObject.hide()
        obj_line41.ViewObject.hide()
        obj_line42.ViewObject.hide()
        obj_line43.ViewObject.hide()
        obj_line44.ViewObject.hide()
        obj_line45.ViewObject.hide()
        obj_line46.ViewObject.hide()
        obj_line47.ViewObject.hide()
        obj_line48.ViewObject.hide()
        obj_line49.ViewObject.hide()
        obj_line50.ViewObject.hide()
        obj_line51.ViewObject.hide()
        obj_line52.ViewObject.hide()
        obj_line53.ViewObject.hide()
        obj_line54.ViewObject.hide()

    doc.recompute()
    if FreeCAD.GuiUp:
        geom_obj.ViewObject.Document.activeView().viewAxonometric()
        geom_obj.ViewObject.Document.activeView().fitAll()

    # analysis
    analysis = ObjectsFem.makeAnalysis(doc, "Analysis")

    # solver
    if solvertype == "calculix":
        solver_obj = ObjectsFem.makeSolverCalculix(doc, "SolverCalculiX")
    elif solvertype == "ccxtools":
        solver_obj = ObjectsFem.makeSolverCalculixCcxTools(doc, "CalculiXccxTools")
        solver_obj.WorkingDir = u""
    elif solvertype == "z88":
        solver_obj = ObjectsFem.makeSolverZ88(doc, "SolverZ88")
    else:
        FreeCAD.Console.PrintWarning(
            "Not known or not supported solver type: {}. "
            "No solver object was created.\n".format(solvertype)
        )
    if solvertype == "calculix" or solvertype == "ccxtools":
        solver_obj.SplitInputWriter = False
        solver_obj.AnalysisType = "static"
        solver_obj.GeometricalNonlinearity = "linear"
        solver_obj.ThermoMechSteadyState = False
        solver_obj.MatrixSolverType = "default"
        solver_obj.IterationsControlParameterTimeUse = False
    analysis.addObject(solver_obj)

    # beam section
    beamsection_obj = ObjectsFem.makeElementGeometry1D(
        doc,
        sectiontype="Circular",
        height=25.0,
        name="CrossSectionCircular"
    )
    analysis.addObject(beamsection_obj)

    # material
    material_obj = ObjectsFem.makeMaterialSolid(doc, "MechanicalMaterial")
    mat = material_obj.Material
    mat["Name"] = "Steel"
    mat["YoungsModulus"] = "200000 MPa"
    mat["PoissonRatio"] = "0.30"
    material_obj.Material = mat
    analysis.addObject(material_obj)

    # constraint fixed
    con_fixed = ObjectsFem.makeConstraintFixed(doc, "ConstraintFixed")
    con_fixed.References = [(geom_obj, ("Vertex1", "Vertex2", "Vertex13", "Vertex14"))]
    analysis.addObject(con_fixed)

    # constraint force
    con_force = ObjectsFem.makeConstraintForce(doc, "ConstraintForce")
    con_force.References = [(geom_obj, ("Vertex5", "Vertex6"))]
    con_force.Force = 60000.0  # 30 kN on each Node
    con_force.Direction = (load_line, ["Edge1"])
    con_force.Reversed = False
    analysis.addObject(con_force)

    # mesh
    from .meshes.mesh_truss_crane_seg3 import create_nodes, create_elements
    fem_mesh = Fem.FemMesh()
    control = create_nodes(fem_mesh)
    if not control:
        FreeCAD.Console.PrintError("Error on creating nodes.\n")
    control = create_elements(fem_mesh)
    if not control:
        FreeCAD.Console.PrintError("Error on creating elements.\n")
    femmesh_obj = analysis.addObject(ObjectsFem.makeMeshGmsh(doc, get_meshname()))[0]
    femmesh_obj.FemMesh = fem_mesh
    femmesh_obj.Part = geom_obj
    femmesh_obj.SecondOrderLinear = False
    femmesh_obj.ElementDimension = "1D"
    # four elements for each bar
    femmesh_obj.CharacteristicLengthMax = "1500.0 mm"
    femmesh_obj.CharacteristicLengthMin = "1500.0 mm"
    if FreeCAD.GuiUp:
        femmesh_obj.ViewObject.DisplayMode = "Faces, Wireframe & Nodes"
        femmesh_obj.ViewObject.PointColor = (1.0, 0.0, 0.5, 0.0)

    doc.recompute()
    return doc
