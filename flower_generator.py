import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Qt
from shiboken2 import wrapInstance


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
        print(get_maya_main_win())
        self.raise_()
        self.flower_gen = Flower()
        self._set_win()
        self._define_widgets()
        self._layout_win()
        self._connect_buttons()

    def _set_win(self):
        self.setWindowTitle("Generate Flower")
        self.resize(500, 300)

    def _define_widgets(self):
        self._define_buttons()
        self._define_checkbox_widgets()
        self._define_flower_base_widgets()
        self._define_flower_petal_widgets()

    def _define_buttons(self):
        self.create_btn = QtWidgets.QPushButton("Create")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")

    def _define_checkbox_widgets(self):
        self.custom_petal_cb = QtWidgets.QCheckBox()
        self.custom_petal_le = QtWidgets.QLineEdit()
        self.grp_name_cb = QtWidgets.QCheckBox()
        self.grp_name_le = QtWidgets.QLineEdit()

    def _define_flower_base_widgets(self):
        self.center_rad_lay = QtWidgets.QHBoxLayout()
        self.center_rad_dspnbx = QtWidgets.QDoubleSpinBox()
        self.center_rad_dspnbx.setFixedWidth(75)
        self.center_rad_dspnbx.setRange(1.0, 9999)
        self.center_rad_dspnbx.setValue(3.00)
        self.center_rad_dspnbx.setSingleStep(1.0)
        self.center_rad_sldr = QtWidgets.QSlider(
            Qt.Orientation.Horizontal)
        self.center_rad_sldr.setRange(0, 100)
        self.center_rad_sldr.setValue(3.00)
        self.center_rad_lay.addWidget(self.center_rad_dspnbx)
        self.center_rad_lay.addWidget(self.center_rad_sldr)
        self.center_rad_sldr.valueChanged.connect(
            self._update_center_rad_dspnbx)
        self.center_rad_dspnbx.textChanged.connect(
            self._update_center_rad_sldr)

        self.center_thickness_lay = QtWidgets.QHBoxLayout()
        self.center_ratio_dspnbx = QtWidgets.QDoubleSpinBox()
        self.center_ratio_dspnbx.setFixedWidth(75)
        self.center_ratio_dspnbx.setRange(0.0, 1.0)
        self.center_ratio_dspnbx.setValue(0.25)
        self.center_ratio_dspnbx.setSingleStep(0.01)
        self.center_ratio_sldr = QtWidgets.QSlider(
            Qt.Orientation.Horizontal)
        self.center_ratio_sldr.setRange(0, 100)
        self.center_ratio_sldr.setValue(0.25)
        self.center_thickness_lay.addWidget(self.center_ratio_dspnbx)
        self.center_thickness_lay.addWidget(self.center_ratio_sldr)
        self.center_ratio_sldr.valueChanged.connect(
            self._update_center_ratio_dspnbx)
        self.center_ratio_dspnbx.textChanged.connect(
            self._update_center_ratio_sldr)

        self.num_rings_lay = QtWidgets.QHBoxLayout()
        self.num_rings_dspnbx = QtWidgets.QDoubleSpinBox()
        self.num_rings_dspnbx.setFixedWidth(75)
        self.num_rings_dspnbx.setRange(1.0, 9999)
        self.num_rings_dspnbx.setValue(1.00)
        self.num_rings_dspnbx.setSingleStep(1.0)
        self.num_rings_sldr = QtWidgets.QSlider(
            Qt.Orientation.Horizontal)
        self.num_rings_sldr.setRange(0, 100)
        self.num_rings_sldr.setValue(1.00)
        self.num_rings_lay.addWidget(self.num_rings_dspnbx)
        self.num_rings_lay.addWidget(self.num_rings_sldr)
        self.num_rings_sldr.valueChanged.connect(
            self._update_num_rings_dspnbx)
        self.num_rings_dspnbx.textChanged.connect(
            self._update_num_rings_sldr)

    def _define_flower_petal_widgets(self):
        self.petals_per_ring_lay = QtWidgets.QHBoxLayout()
        self.petals_per_ring_dspnbx = QtWidgets.QDoubleSpinBox()
        self.petals_per_ring_dspnbx.setFixedWidth(75)
        self.petals_per_ring_dspnbx.setRange(1.0, 9999)
        self.petals_per_ring_dspnbx.setValue(10.00)
        self.petals_per_ring_dspnbx.setSingleStep(1.0)
        self.petals_per_ring_sldr = QtWidgets.QSlider(
            Qt.Orientation.Horizontal)
        self.petals_per_ring_sldr.setRange(0, 100)
        self.petals_per_ring_sldr.setValue(10.00)
        self.petals_per_ring_lay.addWidget(self.petals_per_ring_dspnbx)
        self.petals_per_ring_lay.addWidget(self.petals_per_ring_sldr)
        self.petals_per_ring_sldr.valueChanged.connect(
            self._update_petals_per_ring_dspnbx)
        self.petals_per_ring_dspnbx.textChanged.connect(
            self._update_petals_per_ring_sldr)

        self.min_petal_size_lay = QtWidgets.QHBoxLayout()
        self.min_petal_size_dspnbx = QtWidgets.QDoubleSpinBox()
        self.min_petal_size_dspnbx.setFixedWidth(75)
        self.min_petal_size_dspnbx.setRange(1.0, 9999)
        self.min_petal_size_dspnbx.setValue(1.00)
        self.min_petal_size_dspnbx.setSingleStep(1.0)
        self.min_petal_size_sldr = QtWidgets.QSlider(
            Qt.Orientation.Horizontal)
        self.min_petal_size_sldr.setRange(0, 100)
        self.min_petal_size_sldr.setValue(1.00)
        self.min_petal_size_lay.addWidget(self.min_petal_size_dspnbx)
        self.min_petal_size_lay.addWidget(self.min_petal_size_sldr)
        self.min_petal_size_sldr.valueChanged.connect(
            self._update_min_petal_size_dspnbx)
        self.min_petal_size_dspnbx.textChanged.connect(
            self._update_min_petal_size_sldr)

        self.max_petal_size_lay = QtWidgets.QHBoxLayout()
        self.max_petal_size_dspnbx = QtWidgets.QDoubleSpinBox()
        self.max_petal_size_dspnbx.setFixedWidth(75)
        self.max_petal_size_dspnbx.setRange(1.0, 9999)
        self.max_petal_size_dspnbx.setValue(1.00)
        self.max_petal_size_dspnbx.setSingleStep(1.0)
        self.max_petal_size_sldr = QtWidgets.QSlider(
            Qt.Orientation.Horizontal)
        self.max_petal_size_sldr.setRange(0, 100)
        self.max_petal_size_sldr.setValue(1.00)
        self.max_petal_size_lay.addWidget(self.max_petal_size_dspnbx)
        self.max_petal_size_lay.addWidget(self.max_petal_size_sldr)
        self.max_petal_size_sldr.valueChanged.connect(
            self._update_max_petal_size_dspnbx)
        self.max_petal_size_dspnbx.textChanged.connect(
            self._update_max_petal_size_sldr)

        self.petal_shape_dbx = QtWidgets.QComboBox()
        self.petal_shape_dbx.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.Preferred)
        self.petal_shape_dbx.setMinimumWidth(75)
        self.petal_shape_dbx.addItems(["Default", "Pointed", "Square",
                                      "Round", "Heart"])

    def _add_params_form(self):
        self.param_lay = QtWidgets.QFormLayout()
        self.param_lay.addRow(self.tr("Center Radius"),
                              self.center_rad_lay)
        self.param_lay.addRow(self.tr("Center Thickness Ratio"),
                              self.center_thickness_lay)
        self.param_lay.addRow(self.tr("Number of Rings"),
                              self.num_rings_lay)
        self.param_lay.addRow(self.tr("Petals per Ring"),
                              self.petals_per_ring_lay)
        self.param_lay.addRow(self.tr("Min Petal Size"),
                              self.min_petal_size_lay)
        self.param_lay.addRow(self.tr("Max Petal Size"),
                              self.max_petal_size_lay)
        self.param_lay.addRow(self.tr("Petal Shape"),
                              self.petal_shape_dbx)

        self._add_custom_group_name()
        self._add_custom_petal()

        self.main_layout.addLayout(self.param_lay)

    def _add_custom_petal(self):
        self.custom_petal_lay = QtWidgets.QHBoxLayout()
        self.custom_petal_lay.addWidget(self.custom_petal_cb)
        self.custom_petal_lay.addWidget(self.custom_petal_le)

        self.custom_petal_le.setDisabled(True)
        self.custom_petal_cb.toggled.connect(self._toggle_petal_le)

        self.param_lay.addRow(self.tr("Custom Petal Object: "),
                              self.custom_petal_lay)

    def _add_custom_group_name(self):
        self.custom_grp_lay = QtWidgets.QHBoxLayout()
        self.custom_grp_lay.addWidget(self.grp_name_cb)
        self.custom_grp_lay.addWidget(self.grp_name_le)

        self.grp_name_le.setDisabled(True)
        self.grp_name_cb.toggled.connect(self._toggle_grp_name_le)

        self.param_lay.addRow(self.tr("Custom Group Name: "),
                              self.custom_grp_lay)

    def _add_buttons(self):
        self.btns_lay = QtWidgets.QHBoxLayout()
        self.main_layout.addWidget(self.create_btn)
        self.main_layout.addWidget(self.cancel_btn)
        self.main_layout.addLayout(self.btns_lay)

    def _layout_win(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self._add_params_form()
        self._add_buttons()
        self.setLayout(self.main_layout)

    def _connect_buttons(self):
        self.create_btn.clicked.connect(self.create)
        self.cancel_btn.clicked.connect(self.close_window)

    @QtCore.Slot()
    def close_window(self):
        self.close()

    @QtCore.Slot()
    def create(self):
        print("creating flower...")
        self.set_params()
        self.flower_gen._make_flower()

    @QtCore.Slot()
    def _update_center_rad_dspnbx(self):
        float_value = self.center_rad_sldr.value()
        self.center_rad_dspnbx.setValue(float_value)

    @QtCore.Slot()
    def _update_center_rad_sldr(self):
        int_value = int(self.center_rad_dspnbx.value())
        self.center_rad_sldr.setValue(int_value)

        if int_value > self.center_rad_sldr.maximum():
            self.center_rad_sldr.setMaximum(int_value)

    @QtCore.Slot()
    def _update_center_ratio_dspnbx(self):
        float_value = self.center_ratio_sldr.value() / 100
        self.center_ratio_dspnbx.setValue(float_value)

    @QtCore.Slot()
    def _update_center_ratio_sldr(self):
        int_value = int(self.center_ratio_dspnbx.value() * 100)
        self.center_ratio_sldr.setValue(int_value)

        if int_value > self.center_ratio_sldr.maximum():
            self.center_ratio_sldr.setMaximum(int_value)

    @QtCore.Slot()
    def _update_petals_per_ring_dspnbx(self):
        float_value = self.petals_per_ring_sldr.value()
        self.petals_per_ring_dspnbx.setValue(float_value)

    @QtCore.Slot()
    def _update_petals_per_ring_sldr(self):
        int_value = int(self.petals_per_ring_dspnbx.value())
        self.petals_per_ring_sldr.setValue(int_value)

        if int_value > self.petals_per_ring_sldr.maximum():
            self.petals_per_ring_sldr.setMaximum(int_value)

    @QtCore.Slot()
    def _update_num_rings_dspnbx(self):
        float_value = self.num_rings_sldr.value()
        self.num_rings_dspnbx.setValue(float_value)

    @QtCore.Slot()
    def _update_num_rings_sldr(self):
        int_value = int(self.num_rings_dspnbx.value())
        self.num_rings_sldr.setValue(int_value)

        if int_value > self.num_rings_sldr.maximum():
            self.num_rings_sldr.setMaximum(int_value)

    @QtCore.Slot()
    def _update_min_petal_size_dspnbx(self):
        float_value = self.min_petal_size_sldr.value()
        self.min_petal_size_dspnbx.setValue(float_value)

    @QtCore.Slot()
    def _update_min_petal_size_sldr(self):
        int_value = int(self.min_petal_size_dspnbx.value())
        self.min_petal_size_sldr.setValue(int_value)

        if int_value > self.min_petal_size_sldr.maximum():
            self.min_petal_size_sldr.setMaximum(int_value)

    @QtCore.Slot()
    def _update_max_petal_size_dspnbx(self):
        float_value = self.max_petal_size_sldr.value()
        self.max_petal_size_dspnbx.setValue(float_value)

    @QtCore.Slot()
    def _update_max_petal_size_sldr(self):
        float_value = self.max_petal_size_dspnbx.value()
        self.max_petal_size_sldr.setValue(float_value)

    @QtCore.Slot()
    def _toggle_grp_name_le(self):
        self.grp_name_le.setDisabled(not self.grp_name_cb.isChecked())

    @QtCore.Slot()
    def _toggle_petal_le(self):
        self.custom_petal_le.setDisabled(not self.custom_petal_cb.isChecked())

    @QtCore.Slot()
    def set_params(self):
        self.flower_gen.center_radius = self.center_rad_dspnbx.value()
        self.flower_gen.center_thickness = self.center_ratio_dspnbx.value()
        self.flower_gen.num_rings = int(
            self.num_rings_dspnbx.value())
        self.flower_gen.petals_per_ring = int(
            self.petals_per_ring_dspnbx.value())
        self.flower_gen.min_petal_size = self.min_petal_size_dspnbx.value()
        self.flower_gen.max_petal_size = self.max_petal_size_dspnbx.value()

        if self.custom_petal_cb.isChecked() is True:
            self.flower_gen.petal_type = self.custom_petal_le.text()
        else:
            self.flower_gen.petal_type = self.petal_shape_dbx.currentText()

        if self.grp_name_cb.isChecked() is True:
            self.flower_gen.group_name = self.grp_name_le.text()


class Flower(object):

    center_radius = 3
    center_thickness = 0.25
    min_petal_size = 1
    max_petal_size = 5
    num_rings = 1
    petals_per_ring = 10
    petal_type = "Default"

    group_name = "Flower_GRP"

    petal_size = max_petal_size
    layer_offset = 360 / (petals_per_ring * 2)
    og_layer_offset = layer_offset
    x_rotation = -10

    def __init__(self):
        super(Flower, self).__init__()
        print("initializing...")
        self.center = ""
        self.petals = []

    def _make_center(self):
        self.flower_center = cmds.polySphere(radius=self.center_radius,
                                             name="flower_center")[0]
        cmds.setAttr(f"{self.flower_center}.scaleY", self.center_thickness)
        self.center = self.flower_center

    def _make_petals(self):
        petal_shape = self._choose_petal_shape()
        for self.center_count in range(self.num_rings, 0, -1):
            cmds.select(petal_shape)
            self.first_petal = cmds.instance(petal_shape)[0]
            self.petals.append(self.first_petal)
            self._position_first_petal()

            for petal_count in range(1, self.petals_per_ring):
                active_petal = cmds.instance(f"{self.first_petal}")[0]
                cmds.setAttr(f"{active_petal}.rotateY",
                             ((360 / self.petals_per_ring)
                              * petal_count + self.layer_offset))
                self.petals.append(active_petal)

            self.petal_size -= ((self.max_petal_size - self.min_petal_size)
                                / self.num_rings)
            self.layer_offset += self.og_layer_offset

    def _choose_petal_shape(self):
        if self.petal_type == "Default":
            return "petal_000"
        if self.petal_type == "Round":
            return "petal_round_000"
        if self.petal_type == "Pointed":
            return "petal_pointed_000"
        if self.petal_type == "Square":
            return "petal_square_000"
        if self.petal_type == "Heart":
            return "petal_heart_000"
        # if petal_type holds the custom obj name rather than a dropbox option
        return self.petal_type

    def _position_first_petal(self):
        cmds.setAttr(f"{self.first_petal}.visibility", 1)
        cmds.setAttr(f"{self.first_petal}.translateZ", self.center_radius)
        cmds.setAttr(f"{self.first_petal}.scaleX", self.petal_size)
        cmds.setAttr(f"{self.first_petal}.scaleY", self.petal_size)
        cmds.setAttr(f"{self.first_petal}.scaleZ", self.petal_size)
        cmds.setAttr(f"{self.first_petal}.rotateX",
                     self.x_rotation * (self.num_rings - self.center_count))
        cmds.move(0, 0, 0, f"{self.first_petal}.scalePivot",
                  f"{self.first_petal}.rotatePivot", absolute=True)
        cmds.setAttr(f"{self.first_petal}.rotateY", self.layer_offset)

    def _create_petal_ring(self):
        self.active_petal = cmds.instance(f"{self.first_petal}")[0]
        cmds.setAttr(f"{self.active_petal}.rotateY",
                     (360 / self.petals_per_ring) *
                     self.petal_count + self.layer_offset)

    def _grp_objects(self):
        petals_grp = cmds.group(self.petals, name="petals_GRP")
        cmds.group(petals_grp, self.center, name=self.group_name)

    def _make_flower(self):
        self._make_center()
        self._make_petals()
        self._grp_objects()
