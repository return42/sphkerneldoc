.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/pmic/intel_pmic_xpower.c

.. _`intel_xpower_pmic_get_raw_temp`:

intel_xpower_pmic_get_raw_temp
==============================

.. c:function:: int intel_xpower_pmic_get_raw_temp(struct regmap *regmap, int reg)

    Get raw temperature reading from the PMIC

    :param struct regmap \*regmap:
        regmap of the PMIC device

    :param int reg:
        register to get the reading

.. _`intel_xpower_pmic_get_raw_temp.description`:

Description
-----------

We could get the sensor value by manipulating the HW regs here, but since
the axp288 IIO driver may also access the same regs at the same time, the
APIs provided by IIO subsystem are used here instead to avoid problems. As
a result, the two passed in params are of no actual use.

Return a positive value on success, errno on failure.

.. This file was automatic generated / don't edit.

