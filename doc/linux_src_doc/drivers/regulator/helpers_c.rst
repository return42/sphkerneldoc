.. -*- coding: utf-8; mode: rst -*-

=========
helpers.c
=========


.. _`regulator_is_enabled_regmap`:

regulator_is_enabled_regmap
===========================

.. c:function:: int regulator_is_enabled_regmap (struct regulator_dev *rdev)

    standard is_enabled() for regmap users

    :param struct regulator_dev \*rdev:
        regulator to operate on



.. _`regulator_is_enabled_regmap.description`:

Description
-----------

Regulators that use regmap for their register I/O can set the
enable_reg and enable_mask fields in their descriptor and then use
this as their is_enabled operation, saving some code.



.. _`regulator_enable_regmap`:

regulator_enable_regmap
=======================

.. c:function:: int regulator_enable_regmap (struct regulator_dev *rdev)

    standard enable() for regmap users

    :param struct regulator_dev \*rdev:
        regulator to operate on



.. _`regulator_enable_regmap.description`:

Description
-----------

Regulators that use regmap for their register I/O can set the
enable_reg and enable_mask fields in their descriptor and then use
this as their :c:func:`enable` operation, saving some code.



.. _`regulator_disable_regmap`:

regulator_disable_regmap
========================

.. c:function:: int regulator_disable_regmap (struct regulator_dev *rdev)

    standard disable() for regmap users

    :param struct regulator_dev \*rdev:
        regulator to operate on



.. _`regulator_disable_regmap.description`:

Description
-----------

Regulators that use regmap for their register I/O can set the
enable_reg and enable_mask fields in their descriptor and then use
this as their :c:func:`disable` operation, saving some code.



.. _`regulator_get_voltage_sel_regmap`:

regulator_get_voltage_sel_regmap
================================

.. c:function:: int regulator_get_voltage_sel_regmap (struct regulator_dev *rdev)

    standard get_voltage_sel for regmap users

    :param struct regulator_dev \*rdev:
        regulator to operate on



.. _`regulator_get_voltage_sel_regmap.description`:

Description
-----------

Regulators that use regmap for their register I/O can set the
vsel_reg and vsel_mask fields in their descriptor and then use this
as their get_voltage_vsel operation, saving some code.



.. _`regulator_set_voltage_sel_regmap`:

regulator_set_voltage_sel_regmap
================================

.. c:function:: int regulator_set_voltage_sel_regmap (struct regulator_dev *rdev, unsigned sel)

    standard set_voltage_sel for regmap users

    :param struct regulator_dev \*rdev:
        regulator to operate on

    :param unsigned sel:
        Selector to set



.. _`regulator_set_voltage_sel_regmap.description`:

Description
-----------

Regulators that use regmap for their register I/O can set the
vsel_reg and vsel_mask fields in their descriptor and then use this
as their set_voltage_vsel operation, saving some code.



.. _`regulator_map_voltage_iterate`:

regulator_map_voltage_iterate
=============================

.. c:function:: int regulator_map_voltage_iterate (struct regulator_dev *rdev, int min_uV, int max_uV)

    map_voltage() based on list_voltage()

    :param struct regulator_dev \*rdev:
        Regulator to operate on

    :param int min_uV:
        Lower bound for voltage

    :param int max_uV:
        Upper bound for voltage



.. _`regulator_map_voltage_iterate.description`:

Description
-----------

Drivers implementing :c:func:`set_voltage_sel` and :c:func:`list_voltage` can use
this as their :c:func:`map_voltage` operation.  It will find a suitable
voltage by calling :c:func:`list_voltage` until it gets something in bounds
for the requested voltages.



.. _`regulator_map_voltage_ascend`:

regulator_map_voltage_ascend
============================

.. c:function:: int regulator_map_voltage_ascend (struct regulator_dev *rdev, int min_uV, int max_uV)

    map_voltage() for ascendant voltage list

    :param struct regulator_dev \*rdev:
        Regulator to operate on

    :param int min_uV:
        Lower bound for voltage

    :param int max_uV:
        Upper bound for voltage



.. _`regulator_map_voltage_ascend.description`:

Description
-----------

Drivers that have ascendant voltage list can use this as their
:c:func:`map_voltage` operation.



.. _`regulator_map_voltage_linear`:

regulator_map_voltage_linear
============================

.. c:function:: int regulator_map_voltage_linear (struct regulator_dev *rdev, int min_uV, int max_uV)

    map_voltage() for simple linear mappings

    :param struct regulator_dev \*rdev:
        Regulator to operate on

    :param int min_uV:
        Lower bound for voltage

    :param int max_uV:
        Upper bound for voltage



.. _`regulator_map_voltage_linear.description`:

Description
-----------

Drivers providing min_uV and uV_step in their regulator_desc can
use this as their :c:func:`map_voltage` operation.



.. _`regulator_map_voltage_linear_range`:

regulator_map_voltage_linear_range
==================================

.. c:function:: int regulator_map_voltage_linear_range (struct regulator_dev *rdev, int min_uV, int max_uV)

    map_voltage() for multiple linear ranges

    :param struct regulator_dev \*rdev:
        Regulator to operate on

    :param int min_uV:
        Lower bound for voltage

    :param int max_uV:
        Upper bound for voltage



.. _`regulator_map_voltage_linear_range.description`:

Description
-----------

Drivers providing linear_ranges in their descriptor can use this as
their :c:func:`map_voltage` callback.



.. _`regulator_list_voltage_linear`:

regulator_list_voltage_linear
=============================

.. c:function:: int regulator_list_voltage_linear (struct regulator_dev *rdev, unsigned int selector)

    List voltages with simple calculation

    :param struct regulator_dev \*rdev:
        Regulator device

    :param unsigned int selector:
        Selector to convert into a voltage



.. _`regulator_list_voltage_linear.description`:

Description
-----------

Regulators with a simple linear mapping between voltages and
selectors can set min_uV and uV_step in the regulator descriptor
and then use this function as their :c:func:`list_voltage` operation,



.. _`regulator_list_voltage_linear_range`:

regulator_list_voltage_linear_range
===================================

.. c:function:: int regulator_list_voltage_linear_range (struct regulator_dev *rdev, unsigned int selector)

    List voltages for linear ranges

    :param struct regulator_dev \*rdev:
        Regulator device

    :param unsigned int selector:
        Selector to convert into a voltage



.. _`regulator_list_voltage_linear_range.description`:

Description
-----------

Regulators with a series of simple linear mappings between voltages
and selectors can set linear_ranges in the regulator descriptor and
then use this function as their :c:func:`list_voltage` operation,



.. _`regulator_list_voltage_table`:

regulator_list_voltage_table
============================

.. c:function:: int regulator_list_voltage_table (struct regulator_dev *rdev, unsigned int selector)

    List voltages with table based mapping

    :param struct regulator_dev \*rdev:
        Regulator device

    :param unsigned int selector:
        Selector to convert into a voltage



.. _`regulator_list_voltage_table.description`:

Description
-----------

Regulators with table based mapping between voltages and
selectors can set volt_table in the regulator descriptor
and then use this function as their :c:func:`list_voltage` operation.



.. _`regulator_set_bypass_regmap`:

regulator_set_bypass_regmap
===========================

.. c:function:: int regulator_set_bypass_regmap (struct regulator_dev *rdev, bool enable)

    Default set_bypass() using regmap

    :param struct regulator_dev \*rdev:
        device to operate on.

    :param bool enable:
        state to set.



.. _`regulator_get_bypass_regmap`:

regulator_get_bypass_regmap
===========================

.. c:function:: int regulator_get_bypass_regmap (struct regulator_dev *rdev, bool *enable)

    Default get_bypass() using regmap

    :param struct regulator_dev \*rdev:
        device to operate on.

    :param bool \*enable:
        current state.



.. _`regulator_set_active_discharge_regmap`:

regulator_set_active_discharge_regmap
=====================================

.. c:function:: int regulator_set_active_discharge_regmap (struct regulator_dev *rdev, bool enable)

    Default set_active_discharge() using regmap

    :param struct regulator_dev \*rdev:
        device to operate on.

    :param bool enable:
        state to set, 0 to disable and 1 to enable.

