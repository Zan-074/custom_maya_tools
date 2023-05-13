import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance
import random


def get_maya_main_win():
    """Return the Maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window), QtWidgets.QWidget)


class Window(QtWidgets.QDialog):
    """Dialog Box"""

    def __init__(self):
        """Constructor"""
        super(Window, self).__init__(parent=get_maya_main_win())
        self.setParent(get_maya_main_win())
        self.raise_()
        self.copier = PointCopy()
        self._set_win()
        self._layout_win()

    def _set_win(self):
        self.setWindowTitle("Copy to Points")
        self.resize(500, 150)

    def _layout_win(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self._add_about_dialog()
        self._enter_tocopy_target_objects()
        self._enter_copy_type()
        self._add_aim_vector()
        self._add_rotation_scale_jitter()
        self._add_custom_group_name()
        self._define_buttons()
        self.setLayout(self.main_layout)

    def _add_about_dialog(self):
        self.about_btn = QtWidgets.QPushButton("About(?)")
        self.about_btn.setFixedWidth(100)
        self.main_layout.addWidget(self.about_btn)
        self.about_btn.clicked.connect(self._show_about_dialog)

    def _enter_tocopy_target_objects(self):
        self.obj_to_copy_le = QtWidgets.QLineEdit()
        self.target_obj_le = QtWidgets.QLineEdit()

        self.objects_lay = QtWidgets.QFormLayout()
        self.objects_lay.addRow(self.tr("Object to Copy: "),
                                self.obj_to_copy_le)
        self.objects_lay.addRow(self.tr("Target Object: "),
                                self.target_obj_le)

        self.main_layout.addLayout(self.objects_lay)

    def _enter_copy_type(self):
        self.instance_cb = QtWidgets.QCheckBox()
        self.instance_cb.setChecked(False)

        self.objects_lay.addRow(self.tr("Create Instances? "),
                                self.instance_cb)

    def _add_aim_vector(self):
        self.aim_x_input = QtWidgets.QDoubleSpinBox()
        self.aim_x_input.setDecimals(4)
        self.aim_x_input.setRange(-1.0000, 1.0000)
        self.aim_x_input.setValue(1.0000)
        self.aim_x_input.setFixedWidth(100)

        self.aim_y_input = QtWidgets.QDoubleSpinBox()
        self.aim_y_input.setDecimals(4)
        self.aim_y_input.setRange(-1.0000, 1.0000)
        self.aim_y_input.setValue(0.0000)
        self.aim_y_input.setFixedWidth(100)

        self.aim_z_input = QtWidgets.QDoubleSpinBox()
        self.aim_z_input.setDecimals(4)
        self.aim_z_input.setRange(-1.0000, 1.0000)
        self.aim_z_input.setValue(0.0000)
        self.aim_z_input.setFixedWidth(100)

        self.aim_vector_lay = QtWidgets.QHBoxLayout()
        self.aim_vector_lay.addWidget(self.aim_x_input)
        self.aim_vector_lay.addWidget(self.aim_y_input)
        self.aim_vector_lay.addWidget(self.aim_z_input)

        self.objects_lay.addRow(self.tr("Rotational Aim Vector: "),
                                self.aim_vector_lay)

    def _add_rotation_scale_jitter(self):
        self.rot_jitter_x_dspnbx = QtWidgets.QDoubleSpinBox()
        self.rot_jitter_x_dspnbx.setDecimals(2)
        self.rot_jitter_x_dspnbx.setRange(0, 180)
        self.rot_jitter_x_dspnbx.setValue(0)
        self.rot_jitter_x_dspnbx.setSingleStep(1)
        self.rot_jitter_x_dspnbx.setFixedWidth(75)

        self.rot_jitter_y_dspnbx = QtWidgets.QDoubleSpinBox()
        self.rot_jitter_y_dspnbx.setDecimals(2)
        self.rot_jitter_y_dspnbx.setRange(0, 180)
        self.rot_jitter_y_dspnbx.setValue(0)
        self.rot_jitter_y_dspnbx.setSingleStep(1)
        self.rot_jitter_y_dspnbx.setFixedWidth(75)

        self.rot_jitter_z_dspnbx = QtWidgets.QDoubleSpinBox()
        self.rot_jitter_z_dspnbx.setDecimals(2)
        self.rot_jitter_z_dspnbx.setRange(0, 180)
        self.rot_jitter_z_dspnbx.setValue(0)
        self.rot_jitter_z_dspnbx.setSingleStep(1)
        self.rot_jitter_z_dspnbx.setFixedWidth(75)

        self.rot_jitter_lay = QtWidgets.QHBoxLayout()
        self.rot_jitter_lay.addWidget(self.rot_jitter_x_dspnbx)
        self.rot_jitter_lay.addWidget(self.rot_jitter_y_dspnbx)
        self.rot_jitter_lay.addWidget(self.rot_jitter_z_dspnbx)

        self.scale_jitter_x_dspnbx = QtWidgets.QDoubleSpinBox()
        self.scale_jitter_x_dspnbx.setDecimals(2)
        self.scale_jitter_x_dspnbx.setMinimum(1)
        self.scale_jitter_x_dspnbx.setValue(1)
        self.scale_jitter_x_dspnbx.setSingleStep(0.1)
        self.scale_jitter_x_dspnbx.setFixedWidth(75)

        self.scale_jitter_y_dspnbx = QtWidgets.QDoubleSpinBox()
        self.scale_jitter_y_dspnbx.setDecimals(2)
        self.scale_jitter_y_dspnbx.setMinimum(1)
        self.scale_jitter_y_dspnbx.setValue(1)
        self.scale_jitter_y_dspnbx.setSingleStep(0.1)
        self.scale_jitter_y_dspnbx.setFixedWidth(75)

        self.scale_jitter_z_dspnbx = QtWidgets.QDoubleSpinBox()
        self.scale_jitter_z_dspnbx.setDecimals(2)
        self.scale_jitter_z_dspnbx.setMinimum(1)
        self.scale_jitter_z_dspnbx.setValue(1)
        self.scale_jitter_z_dspnbx.setSingleStep(0.1)
        self.scale_jitter_z_dspnbx.setFixedWidth(75)

        self.scale_jitter_lay = QtWidgets.QHBoxLayout()
        self.scale_jitter_lay.addWidget(self.scale_jitter_x_dspnbx)
        self.scale_jitter_lay.addWidget(self.scale_jitter_y_dspnbx)
        self.scale_jitter_lay.addWidget(self.scale_jitter_z_dspnbx)

        self.objects_lay.addRow(self.tr("Rotation Jitter: "),
                                self.rot_jitter_lay)
        self.objects_lay.addRow(self.tr("Scale Jitter: "),
                                self.scale_jitter_lay)

    def _add_custom_group_name(self):
        self.grp_name_cb = QtWidgets.QCheckBox()
        self.grp_name_le = QtWidgets.QLineEdit()

        self.custom_grp_lay = QtWidgets.QHBoxLayout()
        self.custom_grp_lay.addWidget(self.grp_name_cb)
        self.custom_grp_lay.addWidget(self.grp_name_le)

        self.grp_name_le.setDisabled(True)
        self.grp_name_cb.toggled.connect(self._toggle_grp_name_le)

        self.objects_lay.addRow(self.tr("Custom Group Name: "),
                                self.custom_grp_lay)

    def _define_buttons(self):
        self.apply_btn = QtWidgets.QPushButton("Apply")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")

        self.btns_lay = QtWidgets.QHBoxLayout()
        self.btns_lay.addWidget(self.apply_btn)
        self.btns_lay.addWidget(self.cancel_btn)

        self._connect_buttons()
        self.main_layout.addLayout(self.btns_lay)

    def _connect_buttons(self):
        self.apply_btn.clicked.connect(self.apply)
        self.cancel_btn.clicked.connect(self.close_window)

    @QtCore.Slot()
    def _show_about_dialog(self):
        self.info_box = QtWidgets.QMessageBox()
        self.info_box.setWindowTitle("About Copy to Points")

        text = ("Copies an object along the vertices of the target object\n"
                "Parameters:\n"
                "Object to Copy and Target Object - The object to copy will"
                " be duplicated and parented to target object's verticles\n"
                "Copy type is defaulted to duplicates, but can be instanced"
                "Aim Vector - Axis which will aimed towards the target\n"
                "Rotation and Scale Jitters - makes additional transformations"
                " to the rotation and scale of the copy. Transformations are"
                " random within the given range")

        self.info_box.setText(text)
        self.info_box.exec_()

    @QtCore.Slot()
    def _toggle_grp_name_le(self):
        self.grp_name_le.setDisabled(not self.grp_name_cb.isChecked())

    @QtCore.Slot()
    def apply(self):
        print("copying...")
        self.set_params()
        self.copier._copy_to_points()

    @QtCore.Slot()
    def close_window(self):
        self.close()

    @QtCore.Slot()
    def set_params(self):
        if self.obj_to_copy_le.text() == "" or self.target_obj_le.text() == "":
            self._give_empty_field_error()
        else:
            self.copier.object_to_copy = self.obj_to_copy_le.text()
            self.copier.target_object = self.target_obj_le.text()

        if self.instance_cb.isChecked():
            self.copier.copy_type = 1
        else:
            self.copier.copy_type = 0

        if self.grp_name_cb.isChecked() is True:
            self.copier.group_name = self.grp_name_le.text()

        self.copier.aim_vector = [float(self.aim_x_input.text()),
                                  float(self.aim_y_input.text()),
                                  float(self.aim_z_input.text())]

        self.copier.rot_jitter = [float(self.rot_jitter_x_dspnbx.text()),
                                  float(self.rot_jitter_y_dspnbx.text()),
                                  float(self.rot_jitter_z_dspnbx.text())]

        self.copier.scale_jitter = [float(self.scale_jitter_x_dspnbx.text()),
                                    float(self.scale_jitter_y_dspnbx.text()),
                                    float(self.scale_jitter_z_dspnbx.text())]

    def _give_empty_field_error(self):
        text = "Error. The following required fields are empty:  \n"
        if self.obj_to_copy_le.text() == "":
            text = text + "- Object to Copy \n"
        if self.target_obj_le.text() == "":
            text = text + "- Target Object \n"

        self.error_dialog = QtWidgets.QErrorMessage()
        self.error_dialog.resize(1000, 50)
        self.error_dialog.showMessage(text)


class PointCopy(object):
    """Class for copied objects"""

    object_to_copy = ""
    target_object = ""
    copy_type = 0  # integer flag for duplicate(0) or instance(1)
    aim_vector = [1.0, 0.0, 0.0]
    group_name = "Copied_Objects"
    rot_jitter = [0.0, 0.0, 0.0]
    scale_jitter = [1.0, 1.0, 1.0]

    def __init__(self):
        super(PointCopy, self).__init__()
        print("initializing...")
        self.copies_list = []

    def _copy_to_points(self):
        self._get_target_vert_positions()
        self._create_copies()
        self._group_objects()

    def _get_target_vert_positions(self):
        self.target_vert_x = []
        self.target_vert_y = []
        self.target_vert_z = []

        self.num_points = cmds.polyEvaluate(f"{self.target_object}", v=True)

        # Maya verts are counted from 0 to num - 1
        for vert_counter in range(0, self.num_points):
            self.coords = cmds.pointPosition(
                f"{self.target_object}.vtx[{vert_counter}]")
            self.target_vert_x.append(self.coords[0])
            self.target_vert_y.append(self.coords[1])
            self.target_vert_z.append(self.coords[2])

    def _create_copies(self):
        for self.copy_counter in range(1, self.num_points+1):

            if self.copy_type == 0:
                self.obj_copy = cmds.duplicate(self.object_to_copy)[0]
            else:
                self.obj_copy = cmds.instance(self.object_to_copy)[0]

            self._jitter_rotation_scale()
            self._create_transform_group()
            self._positon_copied_obj()
            self._constrain_copied_obj_to_normal()

            # ungrouping transform group will maintain additional transforms
            # while keeping outliner tidy
            cmds.ungroup(f"{self.transfom_grp}")

            self.copies_list.append(self.obj_copy)

    def _jitter_rotation_scale(self):

        rot = [random.uniform(-self.rot_jitter[0], self.rot_jitter[0]),
               random.uniform(-self.rot_jitter[1], self.rot_jitter[1]),
               random.uniform(-self.rot_jitter[2], self.rot_jitter[2])]
        scale = [random.uniform(1, self.scale_jitter[0]),
                 random.uniform(1, self.scale_jitter[1]),
                 random.uniform(1, self.scale_jitter[2])]
        # checking if the jitter values are not default
        if self.rot_jitter != [0.0, 0.0, 0.0]:
            cmds.xform(f"{self.obj_copy}", ro=(rot[0], rot[1], rot[2]))
        if self.scale_jitter != [1.0, 1.0, 1.0]:
            cmds.xform(f"{self.obj_copy}", s=(scale[0], scale[1], scale[2]))

    def _create_transform_group(self):
        """Creating a group on which the jitter transforms can be applied
        allows us to add onto the object tranforms rather than
        overriding them"""
        # starting with 0 translation
        cmds.move(0, 0, 0, f"{self.obj_copy}", rpr=True)
        self.transfom_grp = cmds.group(self.obj_copy)

    def _positon_copied_obj(self):
        cmds.xform(f"{self.transfom_grp}", t=(
            self.target_vert_x[self.copy_counter - 1],
            self.target_vert_y[self.copy_counter - 1],
            self.target_vert_z[self.copy_counter - 1]))

    def _constrain_copied_obj_to_normal(self):
        cmds.normalConstraint(f"{self.target_object}", f"{self.transfom_grp}",
                              aim=self.aim_vector)
        # deleting constraint will still retain the rotational transform
        cmds.normalConstraint(f"{self.target_object}", f"{self.transfom_grp}",
                              rm=True)

    def _group_objects(self):
        self.obj_group = cmds.group(self.copies_list, name=self.group_name)
        cmds.parent(f"{self.obj_group}", f"{self.target_object}")
