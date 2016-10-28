.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/tegra/cvb.c

.. _`tegra_cvb_add_opp_table`:

tegra_cvb_add_opp_table
=======================

.. c:function:: const struct cvb_table *tegra_cvb_add_opp_table(struct device *dev, const struct cvb_table *tables, size_t count, int process_id, int speedo_id, int speedo_value, unsigned long max_freq)

    build OPP table from Tegra CVB tables

    :param struct device \*dev:
        *undescribed*

    :param const struct cvb_table \*tables:
        *undescribed*

    :param size_t count:
        *undescribed*

    :param int process_id:
        process id of the HW module

    :param int speedo_id:
        speedo id of the HW module

    :param int speedo_value:
        speedo value of the HW module

    :param unsigned long max_freq:
        *undescribed*

.. _`tegra_cvb_add_opp_table.description`:

Description
-----------

On Tegra, a CVB table encodes the relationship between operating voltage
and safe maximal frequency for a given module (e.g. GPU or CPU). This
function calculates the optimal voltage-frequency operating points
for the given arguments and exports them via the OPP library for the
given \ ``opp_dev``\ . Returns a pointer to the struct cvb_table that matched
or an ERR_PTR on failure.

.. This file was automatic generated / don't edit.

