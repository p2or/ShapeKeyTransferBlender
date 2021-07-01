# ----------------------------------------------------------
# File __init__.py
# ----------------------------------------------------------
#
# ShapeKeyTransfer - Copyright (C) 2018 Ajit Christopher D'Monte
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ----------------------------------------------------------

# Addon info
# ----------------------------------------------------------

bl_info = {
    "name": "Shape Key Transfer",
    "description": "Copies shape keys from one mesh to another.",
    "author": "Ajit D'Monte (fBlah), email: ajitdmonte@gmail.com",
    "version": (1, 0, 2),
    "blender": (2, 93, 0),
    "location": "View3D > Tools > Shape Key Transfer",    
    "warning": "This has not been tested rigorously.",
    "wiki_url": "",    
    "category": 'Mesh'}


# register
# ----------------------------------------------------------

import bpy
from bpy.props import (PointerProperty, CollectionProperty, StringProperty)
from . uisettings import *
from . shapekeytransfer import *

    
# Custom scene properties

bpy.types.Scene.customshapekeylist_index = IntProperty()
bpy.types.Scene.srcMeshShapeKey = StringProperty()
bpy.types.Scene.destMeshShapeKey = StringProperty()
def load_custom_properties():
    bpy.types.Scene.shapekeytransferSettings = PointerProperty(type=UISettings)
    bpy.types.Scene.customshapekeylist = CollectionProperty(type=ShapeKeyItem)
    bpy.types.Scene.shapekeytransferOperatorSettings = PointerProperty(type=TransferShapeKeysOperatorUI)

#bpy.app.handlers.load_post.append(load_custom_properties)

def register():
    bpy.utils.register_class(UISettings)
    bpy.utils.register_class(TransferShapeKeysOperatorUI)
    bpy.utils.register_class(ShapeKeyItem)
    load_custom_properties()
    
    bpy.utils.register_class(CopyKeyNamesOperator)
    bpy.utils.register_class(InsertKeyNamesOperator)
    bpy.utils.register_class(TransferShapeKeyOperator)
    bpy.utils.register_class(TransferExcludedShapeKeyOperator)
    bpy.utils.register_class(RemoveShapeKeyOperator)
    bpy.utils.register_class(CUSTOM_OT_actions)
    bpy.utils.register_class(CUSTOM_OT_clearList)
    bpy.utils.register_class(CUSTOM_OT_removeDuplicates)
    bpy.utils.register_class(CUSTOM_UL_items)

    

    bpy.utils.register_class(VIEW3D_PT_tools_ShapeKeyTransfer)
    

# unregister
# ----------------------------------------------------------

def unregister():    
    bpy.utils.unregister_class(UISettings)
    bpy.utils.unregister_class(TransferShapeKeysOperatorUI)
    bpy.utils.unregister_class(ShapeKeyItem)
    
    bpy.utils.unregister_class(CopyKeyNamesOperator)
    bpy.utils.unregister_class(InsertKeyNamesOperator)
    bpy.utils.unregister_class(TransferShapeKeyOperator)
    bpy.utils.unregister_class(TransferExcludedShapeKeyOperator)
    bpy.utils.unregister_class(RemoveShapeKeyOperator)
    bpy.utils.unregister_class(CUSTOM_OT_actions)
    bpy.utils.unregister_class(CUSTOM_OT_clearList)
    bpy.utils.unregister_class(CUSTOM_OT_removeDuplicates)
    bpy.utils.unregister_class(CUSTOM_UL_items)
    bpy.utils.unregister_class(VIEW3D_PT_tools_ShapeKeyTransfer)
    del bpy.types.Scene.shapekeytransferSettings
    del bpy.types.Scene.customshapekeylist
    del bpy.types.Scene.shapekeytransferOperatorSettings