.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/pmic/intel_pmic_xpower.c

.. _`intel_xpower_pmic_get_raw_temp`:

intel_xpower_pmic_get_raw_temp
==============================

.. c:function:: int intel_xpower_pmic_get_raw_temp(struct regmap *regmap, int reg)

    Get raw temperature reading from the PMIC

    :param regmap:
        regmap of the PMIC device
    :type regmap: struct regmap \*

    :param reg:
        register to get the reading
    :type reg: int

.. _`intel_xpower_pmic_get_raw_temp.description`:

Description
-----------

Return a positive value on success, errno on failure.

.. This file was automatic generated / don't edit.

