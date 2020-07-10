import unreal

# texture_tga = "D:/Projects/PythonProject/Content/Assets/Vines_01.tga"
# sound_wav = "D:/Projects/PythonProject/Content/Assets/02_Run To You.wav"
# static_mesh_fbx = ("D:\Projects\MEW\Assets\Middle_School\Da Vinci Surgical Robot\DaVinci_Console.FBX")
# skeletal_mesh_fbx = ("D:\Projects\MEW\Assets\Background\Armor_6\Sci_Fi_Armors_6\Meshes\Armor6_UTpose.fbx")
animation_fbx = "D:\Projects\MEW\Assets\Middle_School\Male_SpaceSuit\Animation\Idle.FBX"


def importMyAssets():
    # texture_task = buildImportTask(texture_tga, "/Game/Textures")
    # sound_task = buildImportTask(sound_wav, "/Game/Sounds")
    # executeImportTasks([texture_task, sound_task])

    # static_mesh_task = buildImportTask(static_mesh_fbx, "/Game/StaticMeshes", buildStaticMeshImportOptions())
    # skeletal_mesh_task = buildImportTask(skeletal_mesh_fbx, "/Game/SkeletalMeshes", buildSkeletalMeshImportOptions())
    # executeImportTasks([static_mesh_task, skeletal_mesh_task])

    animation_task = buildImportTask(
        animation_fbx,
        "/Game/Animations",
        buildAnimationImportOptions(
            "/Game/SkeletalMeshes/Armor6_UTpose_Skeleton.Armor6_UTpose_Skeleton"
        ),
    )
    executeImportTasks([animation_task])


# unreal.AssetImportTask - https://api.unrealengine.com/INT/PythonAPI/class/AssetImportTask.html
def buildImportTask(filename, destination_path, options=None):
    task = unreal.AssetImportTask()
    task.set_editor_property("automated", True)
    task.set_editor_property("destination_name", "")
    task.set_editor_property("destination_path", destination_path)
    task.set_editor_property("filename", filename)
    task.set_editor_property("replace_existing", True)
    task.set_editor_property("save", True)
    task.set_editor_property("options", options)
    return task


# unreal.AssetTools - https://api.unrealengine.com/INT/PythonAPI/class/AssetTools.html
def executeImportTasks(tasks):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    for task in tasks:
        for path in task.get_editor_property("imported_object_paths"):
            print "Imported: %s" % path


# unreal.FbxImportUI
# https://api.unrealengine.com/INT/PythonAPI/class/FbxImportUI.html
# unreal.FbxMeshImportData
# https://api.unrealengine.com/INT/PythonAPI/class/FbxMeshImportData.html
# unreal.FbxStaticMeshImportData
# https://api.unrealengine.com/INT/PythonAPI/class/FbxStaticMeshImportData.html
def buildStaticMeshImportOptions():
    options = unreal.FbxImportUI()
    # unreal.FbxImportUI
    options.set_editor_property("import_mesh", True)
    options.set_editor_property("import_textures", False)
    options.set_editor_property("import_materials", False)
    options.set_editor_property("import_as_skeletal", False)  # Static Mesh
    # unreal.FbxMeshImportData
    options.static_mesh_import_data.set_editor_property(
        "import_translation", unreal.Vector(0.0, 0.0, 0.0)
    )
    options.static_mesh_import_data.set_editor_property(
        "import_rotation", unreal.Rotator(0.0, 0.0, 0.0)
    )
    options.static_mesh_import_data.set_editor_property("import_uniform_scale", 1.0)
    # unreal.FbxStaticMeshImportData
    options.static_mesh_import_data.set_editor_property("combine_meshes", True)
    options.static_mesh_import_data.set_editor_property("generate_lightmap_u_vs", True)
    options.static_mesh_import_data.set_editor_property("auto_generate_collision", True)
    return options


# unreal.FbxImportUI
# https://api.unrealengine.com/INT/PythonAPI/class/FbxImportUI.html
# unreal.FbxMeshImportData
# https://api.unrealengine.com/INT/PythonAPI/class/FbxMeshImportData.html
# unreal.FbxSkeletalMeshImportData
# https://api.unrealengine.com/INT/PythonAPI/class/FbxSkeletalMeshImportData.html
def buildSkeletalMeshImportOptions():
    options = unreal.FbxImportUI()
    # unreal.FbxImportUI
    options.set_editor_property("import_mesh", True)
    options.set_editor_property("import_textures", True)
    options.set_editor_property("import_materials", True)
    options.set_editor_property("import_as_skeletal", True)  # Skeletal Mesh
    # unreal.FbxMeshImportData
    options.skeletal_mesh_import_data.set_editor_property(
        "import_translation", unreal.Vector(0.0, 0.0, 0.0)
    )
    options.skeletal_mesh_import_data.set_editor_property(
        "import_rotation", unreal.Rotator(0.0, 0.0, 0.0)
    )
    options.skeletal_mesh_import_data.set_editor_property("import_uniform_scale", 1.0)
    # unreal.FbxSkeletalMeshImportData
    options.skeletal_mesh_import_data.set_editor_property("import_morph_targets", True)
    options.skeletal_mesh_import_data.set_editor_property(
        "update_skeleton_reference_pose", False
    )
    return options


# unreal.FbxImportUI
# https://api.unrealengine.com/INT/PythonAPI/class/FbxImportUI.html
# unreal.FbxAssetImportData
# https://api.unrealengine.com/INT/PythonAPI/class/FbxAssetImportData.html
# unreal.FbxAnimSequenceImportData
# https://api.unrealeninge.com/INT/PythonAPI/class/FbxAnimSequenceImportData.html
# unreal.FBXAnimationLengthImportType
# https://api.unrealengine.com/INT/PythonAPI/class/FbxAnimationLengthImportType.html
def buildAnimationImportOptions(skeleton_path):
    options = unreal.FbxImportUI()
    # unreal.FbxImportUI
    options.set_editor_property("import_animations", True)
    options.skeleton = unreal.load_asset(skeleton_path)
    # unreal.FbxMeshImportData
    options.anim_sequence_import_data.set_editor_property(
        "import_translation", unreal.Vector(0.0, 0.0, 0.0)
    )
    options.anim_sequence_import_data.set_editor_property(
        "import_rotation", unreal.Rotator(0.0, 0.0, 0.0)
    )
    options.anim_sequence_import_data.set_editor_property("import_uniform_scale", 1.0)
    # unreal.FbxAnimSequenceImportData
    options.anim_sequence_import_data.set_editor_property(
        "animation_length", unreal.FBXAnimationLengthImportType.FBXALIT_EXPORTED_TIME
    )
    options.anim_sequence_import_data.set_editor_property(
        "remove_redundant_keys", False
    )
    return options


# unreal.EditorAssetLibrary
# https://api.unrealengine.com/INT/PythonAPI/class/EditorAssetLibrary.html
def saveAsset():
    unreal.EditorAssetLibrary.save_asset(
        "/Game/Textures/Vines_01", only_if_is_dirty=False
    )


def saveDirectory():
    unreal.EditorAssetLibrary.save_asset(
        "/Game", only_if_is_dirty=False, recursive=True
    )


# unreal.Package
# https://api.unrealen gine.com/INT/PythonAPI/class/Package.html
def getPackageFromPath():
    return unreal.load_package("/Game/Textures/Vines_01")


# unreal.EditorLoadingAndSavingUtils
# https://api.unrealengien.com/INT/PythonAPI/class/EditorLoadingAndSavingUtils.html
def getAllDirtyPackages():  # AssetFunctions.getAllDirtyPackages()
    packages = unreal.Array(unreal.Package)
    for x in unreal.EditorLoadingAndSavingUtils.get_dirty_content_packages():
        packages.append(x)
    for x in unreal.EditorLoadingAndSavingUtils.get_dirty_map_packages():
        packages.append(x)
    return packages


def saveAllDirtyPackages(show_dialog=False):
    if show_dialog:
        unreal.EditorLoadingAndSavingUtils.save_dirty_packages_with_dialog(
            save_map_packages=True, save_content_packages=True
        )
    else:
        unreal.EditorLoadingAndSavingUtils.save_dirty_packages(
            save_map_packages=True, save_content_packages=True
        )


def savePackages(packages=[], show_dialog=False):
    if show_dialog:
        unreal.EditorLoadingAndSavingUtils.save_packages_with_dialog(
            packages, only_dirty=False
        )  # only_dirty=False :
    else:  # looks like that it's not
        unreal.EditorLoadingAndSavingUtils.save_packages(
            packages, only_dirty=False
        )  # working properly at the moment

