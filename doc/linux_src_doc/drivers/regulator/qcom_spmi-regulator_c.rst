.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/regulator/qcom_spmi-regulator.c

.. _`spmi_regulator_init_data`:

struct spmi_regulator_init_data
===============================

.. c:type:: struct spmi_regulator_init_data

    spmi-regulator initialization data

.. _`spmi_regulator_init_data.definition`:

Definition
----------

.. code-block:: c

    struct spmi_regulator_init_data {
        unsigned pin_ctrl_enable;
        unsigned pin_ctrl_hpm;
        enum spmi_vs_soft_start_str vs_soft_start_strength;
    }

.. _`spmi_regulator_init_data.members`:

Members
-------

pin_ctrl_enable
    Bit mask specifying which hardware pins should be
    used to enable the regulator, if any
    Value should be an ORing of
    SPMI_REGULATOR_PIN_CTRL_ENABLE\_\* constants.  If
    the bit specified by
    SPMI_REGULATOR_PIN_CTRL_ENABLE_HW_DEFAULT is
    set, then pin control enable hardware registers
    will not be modified.

pin_ctrl_hpm
    Bit mask specifying which hardware pins should be
    used to force the regulator into high power
    mode, if any
    Value should be an ORing of
    SPMI_REGULATOR_PIN_CTRL_HPM\_\* constants.  If
    the bit specified by
    SPMI_REGULATOR_PIN_CTRL_HPM_HW_DEFAULT is
    set, then pin control mode hardware registers
    will not be modified.

vs_soft_start_strength
    This parameter sets the soft start strength for
    voltage switch type regulators.  Its value
    should be one of SPMI_VS_SOFT_START_STR\_\*.  If
    its value is SPMI_VS_SOFT_START_STR_HW_DEFAULT,
    then the soft start strength will be left at its
    default hardware value.

.. _`spmi_voltage_range`:

struct spmi_voltage_range
=========================

.. c:type:: struct spmi_voltage_range

    regulator set point voltage mapping description

.. _`spmi_voltage_range.definition`:

Definition
----------

.. code-block:: c

    struct spmi_voltage_range {
        int min_uV;
        int max_uV;
        int step_uV;
        int set_point_min_uV;
        int set_point_max_uV;
        unsigned n_voltages;
        u8 range_sel;
    }

.. _`spmi_voltage_range.members`:

Members
-------

min_uV
    Minimum programmable output voltage resulting from
    set point register value 0x00

max_uV
    Maximum programmable output voltage

step_uV
    Output voltage increase resulting from the set point
    register value increasing by 1

set_point_min_uV
    Minimum allowed voltage

set_point_max_uV
    Maximum allowed voltage.  This may be tweaked in order
    to pick which range should be used in the case of
    overlapping set points.

n_voltages
    Number of preferred voltage set points present in this
    range

range_sel
    Voltage range register value corresponding to this range

.. _`spmi_voltage_range.the-following-relationships-must-be-true-for-the-values-used-in-this-struct`:

The following relationships must be true for the values used in this struct
---------------------------------------------------------------------------

(max_uV - min_uV) % step_uV == 0
(set_point_min_uV - min_uV) % step_uV == 0\*
(set_point_max_uV - min_uV) % step_uV == 0\*
n_voltages = (set_point_max_uV - set_point_min_uV) / step_uV + 1

\*Note, set_point_min_uV == set_point_max_uV == 0 is allowed in order to
specify that the voltage range has meaning, but is not preferred.

.. This file was automatic generated / don't edit.

