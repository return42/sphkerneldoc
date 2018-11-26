.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/memory/of_memory.c

.. _`of_get_min_tck`:

of_get_min_tck
==============

.. c:function:: const struct lpddr2_min_tck *of_get_min_tck(struct device_node *np, struct device *dev)

    extract min timing values for ddr

    :param np:
        pointer to ddr device tree node
    :type np: struct device_node \*

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`of_get_min_tck.description`:

Description
-----------

Populates the lpddr2_min_tck structure by extracting data
from device tree node. Returns a pointer to the populated
structure. If any error in populating the structure, returns
default min timings provided by JEDEC.

.. _`of_get_ddr_timings`:

of_get_ddr_timings
==================

.. c:function:: const struct lpddr2_timings *of_get_ddr_timings(struct device_node *np_ddr, struct device *dev, u32 device_type, u32 *nr_frequencies)

    extracts the ddr timings and updates no of frequencies available.

    :param np_ddr:
        Pointer to ddr device tree node
    :type np_ddr: struct device_node \*

    :param dev:
        Device requesting for ddr timings
    :type dev: struct device \*

    :param device_type:
        Type of ddr(LPDDR2 S2/S4)
    :type device_type: u32

    :param nr_frequencies:
        No of frequencies available for ddr
        (updated by this function)
    :type nr_frequencies: u32 \*

.. _`of_get_ddr_timings.description`:

Description
-----------

Populates lpddr2_timings structure by extracting data from device
tree node. Returns pointer to populated structure. If any error
while populating, returns default timings provided by JEDEC.

.. This file was automatic generated / don't edit.

