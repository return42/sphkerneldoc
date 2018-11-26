.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/regulator/helpers.c

.. _`regulator_is_enabled_regmap`:

regulator_is_enabled_regmap
===========================

.. c:function:: int regulator_is_enabled_regmap(struct regulator_dev *rdev)

    standard \ :c:func:`is_enabled`\  for regmap users

    :param rdev:
        regulator to operate on
    :type rdev: struct regulator_dev \*

.. _`regulator_is_enabled_regmap.description`:

Description
-----------

Regulators that use regmap for their register I/O can set the
enable_reg and enable_mask fields in their descriptor and then use
this as their is_enabled operation, saving some code.

.. _`regulator_enable_regmap`:

regulator_enable_regmap
=======================

.. c:function:: int regulator_enable_regmap(struct regulator_dev *rdev)

    standard \ :c:func:`enable`\  for regmap users

    :param rdev:
        regulator to operate on
    :type rdev: struct regulator_dev \*

.. _`regulator_enable_regmap.description`:

Description
-----------

Regulators that use regmap for their register I/O can set the
enable_reg and enable_mask fields in their descriptor and then use
this as their \ :c:func:`enable`\  operation, saving some code.

.. _`regulator_disable_regmap`:

regulator_disable_regmap
========================

.. c:function:: int regulator_disable_regmap(struct regulator_dev *rdev)

    standard \ :c:func:`disable`\  for regmap users

    :param rdev:
        regulator to operate on
    :type rdev: struct regulator_dev \*

.. _`regulator_disable_regmap.description`:

Description
-----------

Regulators that use regmap for their register I/O can set the
enable_reg and enable_mask fields in their descriptor and then use
this as their \ :c:func:`disable`\  operation, saving some code.

.. _`regulator_get_voltage_sel_pickable_regmap`:

regulator_get_voltage_sel_pickable_regmap
=========================================

.. c:function:: int regulator_get_voltage_sel_pickable_regmap(struct regulator_dev *rdev)

    pickable range get_voltage_sel

    :param rdev:
        regulator to operate on
    :type rdev: struct regulator_dev \*

.. _`regulator_get_voltage_sel_pickable_regmap.description`:

Description
-----------

Regulators that use regmap for their register I/O and use pickable
ranges can set the vsel_reg, vsel_mask, vsel_range_reg and vsel_range_mask
fields in their descriptor and then use this as their get_voltage_vsel
operation, saving some code.

.. _`regulator_set_voltage_sel_pickable_regmap`:

regulator_set_voltage_sel_pickable_regmap
=========================================

.. c:function:: int regulator_set_voltage_sel_pickable_regmap(struct regulator_dev *rdev, unsigned int sel)

    pickable range set_voltage_sel

    :param rdev:
        regulator to operate on
    :type rdev: struct regulator_dev \*

    :param sel:
        Selector to set
    :type sel: unsigned int

.. _`regulator_set_voltage_sel_pickable_regmap.description`:

Description
-----------

Regulators that use regmap for their register I/O and use pickable
ranges can set the vsel_reg, vsel_mask, vsel_range_reg and vsel_range_mask
fields in their descriptor and then use this as their set_voltage_vsel
operation, saving some code.

.. _`regulator_get_voltage_sel_regmap`:

regulator_get_voltage_sel_regmap
================================

.. c:function:: int regulator_get_voltage_sel_regmap(struct regulator_dev *rdev)

    standard get_voltage_sel for regmap users

    :param rdev:
        regulator to operate on
    :type rdev: struct regulator_dev \*

.. _`regulator_get_voltage_sel_regmap.description`:

Description
-----------

Regulators that use regmap for their register I/O can set the
vsel_reg and vsel_mask fields in their descriptor and then use this
as their get_voltage_vsel operation, saving some code.

.. _`regulator_set_voltage_sel_regmap`:

regulator_set_voltage_sel_regmap
================================

.. c:function:: int regulator_set_voltage_sel_regmap(struct regulator_dev *rdev, unsigned sel)

    standard set_voltage_sel for regmap users

    :param rdev:
        regulator to operate on
    :type rdev: struct regulator_dev \*

    :param sel:
        Selector to set
    :type sel: unsigned

.. _`regulator_set_voltage_sel_regmap.description`:

Description
-----------

Regulators that use regmap for their register I/O can set the
vsel_reg and vsel_mask fields in their descriptor and then use this
as their set_voltage_vsel operation, saving some code.

.. _`regulator_map_voltage_iterate`:

regulator_map_voltage_iterate
=============================

.. c:function:: int regulator_map_voltage_iterate(struct regulator_dev *rdev, int min_uV, int max_uV)

    \ :c:func:`map_voltage`\  based on \ :c:func:`list_voltage`\ 

    :param rdev:
        Regulator to operate on
    :type rdev: struct regulator_dev \*

    :param min_uV:
        Lower bound for voltage
    :type min_uV: int

    :param max_uV:
        Upper bound for voltage
    :type max_uV: int

.. _`regulator_map_voltage_iterate.description`:

Description
-----------

Drivers implementing \ :c:func:`set_voltage_sel`\  and \ :c:func:`list_voltage`\  can use
this as their \ :c:func:`map_voltage`\  operation.  It will find a suitable
voltage by calling \ :c:func:`list_voltage`\  until it gets something in bounds
for the requested voltages.

.. _`regulator_map_voltage_ascend`:

regulator_map_voltage_ascend
============================

.. c:function:: int regulator_map_voltage_ascend(struct regulator_dev *rdev, int min_uV, int max_uV)

    \ :c:func:`map_voltage`\  for ascendant voltage list

    :param rdev:
        Regulator to operate on
    :type rdev: struct regulator_dev \*

    :param min_uV:
        Lower bound for voltage
    :type min_uV: int

    :param max_uV:
        Upper bound for voltage
    :type max_uV: int

.. _`regulator_map_voltage_ascend.description`:

Description
-----------

Drivers that have ascendant voltage list can use this as their
\ :c:func:`map_voltage`\  operation.

.. _`regulator_map_voltage_linear`:

regulator_map_voltage_linear
============================

.. c:function:: int regulator_map_voltage_linear(struct regulator_dev *rdev, int min_uV, int max_uV)

    \ :c:func:`map_voltage`\  for simple linear mappings

    :param rdev:
        Regulator to operate on
    :type rdev: struct regulator_dev \*

    :param min_uV:
        Lower bound for voltage
    :type min_uV: int

    :param max_uV:
        Upper bound for voltage
    :type max_uV: int

.. _`regulator_map_voltage_linear.description`:

Description
-----------

Drivers providing min_uV and uV_step in their regulator_desc can
use this as their \ :c:func:`map_voltage`\  operation.

.. _`regulator_map_voltage_linear_range`:

regulator_map_voltage_linear_range
==================================

.. c:function:: int regulator_map_voltage_linear_range(struct regulator_dev *rdev, int min_uV, int max_uV)

    \ :c:func:`map_voltage`\  for multiple linear ranges

    :param rdev:
        Regulator to operate on
    :type rdev: struct regulator_dev \*

    :param min_uV:
        Lower bound for voltage
    :type min_uV: int

    :param max_uV:
        Upper bound for voltage
    :type max_uV: int

.. _`regulator_map_voltage_linear_range.description`:

Description
-----------

Drivers providing linear_ranges in their descriptor can use this as
their \ :c:func:`map_voltage`\  callback.

.. _`regulator_map_voltage_pickable_linear_range`:

regulator_map_voltage_pickable_linear_range
===========================================

.. c:function:: int regulator_map_voltage_pickable_linear_range(struct regulator_dev *rdev, int min_uV, int max_uV)

    map_voltage, pickable ranges

    :param rdev:
        Regulator to operate on
    :type rdev: struct regulator_dev \*

    :param min_uV:
        Lower bound for voltage
    :type min_uV: int

    :param max_uV:
        Upper bound for voltage
    :type max_uV: int

.. _`regulator_map_voltage_pickable_linear_range.description`:

Description
-----------

Drivers providing pickable linear_ranges in their descriptor can use
this as their \ :c:func:`map_voltage`\  callback.

.. _`regulator_list_voltage_linear`:

regulator_list_voltage_linear
=============================

.. c:function:: int regulator_list_voltage_linear(struct regulator_dev *rdev, unsigned int selector)

    List voltages with simple calculation

    :param rdev:
        Regulator device
    :type rdev: struct regulator_dev \*

    :param selector:
        Selector to convert into a voltage
    :type selector: unsigned int

.. _`regulator_list_voltage_linear.description`:

Description
-----------

Regulators with a simple linear mapping between voltages and
selectors can set min_uV and uV_step in the regulator descriptor
and then use this function as their \ :c:func:`list_voltage`\  operation,

.. _`regulator_list_voltage_pickable_linear_range`:

regulator_list_voltage_pickable_linear_range
============================================

.. c:function:: int regulator_list_voltage_pickable_linear_range(struct regulator_dev *rdev, unsigned int selector)

    pickable range list voltages

    :param rdev:
        Regulator device
    :type rdev: struct regulator_dev \*

    :param selector:
        Selector to convert into a voltage
    :type selector: unsigned int

.. _`regulator_list_voltage_pickable_linear_range.description`:

Description
-----------

\ :c:func:`list_voltage`\  operation, intended to be used by drivers utilizing pickable
ranges helpers.

.. _`regulator_list_voltage_linear_range`:

regulator_list_voltage_linear_range
===================================

.. c:function:: int regulator_list_voltage_linear_range(struct regulator_dev *rdev, unsigned int selector)

    List voltages for linear ranges

    :param rdev:
        Regulator device
    :type rdev: struct regulator_dev \*

    :param selector:
        Selector to convert into a voltage
    :type selector: unsigned int

.. _`regulator_list_voltage_linear_range.description`:

Description
-----------

Regulators with a series of simple linear mappings between voltages
and selectors can set linear_ranges in the regulator descriptor and
then use this function as their \ :c:func:`list_voltage`\  operation,

.. _`regulator_list_voltage_table`:

regulator_list_voltage_table
============================

.. c:function:: int regulator_list_voltage_table(struct regulator_dev *rdev, unsigned int selector)

    List voltages with table based mapping

    :param rdev:
        Regulator device
    :type rdev: struct regulator_dev \*

    :param selector:
        Selector to convert into a voltage
    :type selector: unsigned int

.. _`regulator_list_voltage_table.description`:

Description
-----------

Regulators with table based mapping between voltages and
selectors can set volt_table in the regulator descriptor
and then use this function as their \ :c:func:`list_voltage`\  operation.

.. _`regulator_set_bypass_regmap`:

regulator_set_bypass_regmap
===========================

.. c:function:: int regulator_set_bypass_regmap(struct regulator_dev *rdev, bool enable)

    Default \ :c:func:`set_bypass`\  using regmap

    :param rdev:
        device to operate on.
    :type rdev: struct regulator_dev \*

    :param enable:
        state to set.
    :type enable: bool

.. _`regulator_set_soft_start_regmap`:

regulator_set_soft_start_regmap
===============================

.. c:function:: int regulator_set_soft_start_regmap(struct regulator_dev *rdev)

    Default \ :c:func:`set_soft_start`\  using regmap

    :param rdev:
        device to operate on.
    :type rdev: struct regulator_dev \*

.. _`regulator_set_pull_down_regmap`:

regulator_set_pull_down_regmap
==============================

.. c:function:: int regulator_set_pull_down_regmap(struct regulator_dev *rdev)

    Default \ :c:func:`set_pull_down`\  using regmap

    :param rdev:
        device to operate on.
    :type rdev: struct regulator_dev \*

.. _`regulator_get_bypass_regmap`:

regulator_get_bypass_regmap
===========================

.. c:function:: int regulator_get_bypass_regmap(struct regulator_dev *rdev, bool *enable)

    Default \ :c:func:`get_bypass`\  using regmap

    :param rdev:
        device to operate on.
    :type rdev: struct regulator_dev \*

    :param enable:
        current state.
    :type enable: bool \*

.. _`regulator_set_active_discharge_regmap`:

regulator_set_active_discharge_regmap
=====================================

.. c:function:: int regulator_set_active_discharge_regmap(struct regulator_dev *rdev, bool enable)

    Default \ :c:func:`set_active_discharge`\  using regmap

    :param rdev:
        device to operate on.
    :type rdev: struct regulator_dev \*

    :param enable:
        state to set, 0 to disable and 1 to enable.
    :type enable: bool

.. This file was automatic generated / don't edit.

