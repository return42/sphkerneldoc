.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/opp/of.c

.. _`dev_pm_opp_of_remove_table`:

dev_pm_opp_of_remove_table
==========================

.. c:function:: void dev_pm_opp_of_remove_table(struct device *dev)

    Free OPP table entries created from static DT entries

    :param dev:
        device pointer used to lookup OPP table.
    :type dev: struct device \*

.. _`dev_pm_opp_of_remove_table.description`:

Description
-----------

Free OPPs created using static entries present in DT.

.. _`_opp_add_static_v2`:

\_opp_add_static_v2
===================

.. c:function:: struct dev_pm_opp *_opp_add_static_v2(struct opp_table *opp_table, struct device *dev, struct device_node *np)

    Allocate static OPPs (As per 'v2' DT bindings)

    :param opp_table:
        OPP table
    :type opp_table: struct opp_table \*

    :param dev:
        device for which we do this operation
    :type dev: struct device \*

    :param np:
        device node
    :type np: struct device_node \*

.. _`_opp_add_static_v2.description`:

Description
-----------

This function adds an opp definition to the opp table and returns status. The
opp can be controlled using dev_pm_opp_enable/disable functions and may be
removed by dev_pm_opp_remove.

.. _`_opp_add_static_v2.valid-opp-pointer`:

Valid OPP pointer
-----------------

On success

.. _`_opp_add_static_v2.null`:

NULL
----

Duplicate OPPs (both freq and volt are same) and opp->available
OR if the OPP is not supported by hardware.
ERR_PTR(-EEXIST):
Freq are same and volt are different OR
Duplicate OPPs (both freq and volt are same) and !opp->available
ERR_PTR(-ENOMEM):
Memory allocation failure
ERR_PTR(-EINVAL):
Failed parsing the OPP node

.. _`dev_pm_opp_of_add_table`:

dev_pm_opp_of_add_table
=======================

.. c:function:: int dev_pm_opp_of_add_table(struct device *dev)

    Initialize opp table from device tree

    :param dev:
        device pointer used to lookup OPP table.
    :type dev: struct device \*

.. _`dev_pm_opp_of_add_table.description`:

Description
-----------

Register the initial OPP table with the OPP library for given device.

.. _`dev_pm_opp_of_add_table.return`:

Return
------

0            On success OR
Duplicate OPPs (both freq and volt are same) and opp->available
-EEXIST      Freq are same and volt are different OR
Duplicate OPPs (both freq and volt are same) and !opp->available
-ENOMEM      Memory allocation failure
-ENODEV      when 'operating-points' property is not found or is invalid data
in device node.
-ENODATA     when empty 'operating-points' property is found
-EINVAL      when invalid entries are found in opp-v2 table

.. _`dev_pm_opp_of_add_table_indexed`:

dev_pm_opp_of_add_table_indexed
===============================

.. c:function:: int dev_pm_opp_of_add_table_indexed(struct device *dev, int index)

    Initialize indexed opp table from device tree

    :param dev:
        device pointer used to lookup OPP table.
    :type dev: struct device \*

    :param index:
        Index number.
    :type index: int

.. _`dev_pm_opp_of_add_table_indexed.description`:

Description
-----------

Register the initial OPP table with the OPP library for given device only
using the "operating-points-v2" property.

.. _`dev_pm_opp_of_add_table_indexed.return`:

Return
------

0            On success OR
Duplicate OPPs (both freq and volt are same) and opp->available
-EEXIST      Freq are same and volt are different OR
Duplicate OPPs (both freq and volt are same) and !opp->available
-ENOMEM      Memory allocation failure
-ENODEV      when 'operating-points' property is not found or is invalid data
in device node.
-ENODATA     when empty 'operating-points' property is found
-EINVAL      when invalid entries are found in opp-v2 table

.. _`dev_pm_opp_of_cpumask_remove_table`:

dev_pm_opp_of_cpumask_remove_table
==================================

.. c:function:: void dev_pm_opp_of_cpumask_remove_table(const struct cpumask *cpumask)

    Removes OPP table for \ ``cpumask``\ 

    :param cpumask:
        cpumask for which OPP table needs to be removed
    :type cpumask: const struct cpumask \*

.. _`dev_pm_opp_of_cpumask_remove_table.description`:

Description
-----------

This removes the OPP tables for CPUs present in the \ ``cpumask``\ .
This should be used only to remove static entries created from DT.

.. _`dev_pm_opp_of_cpumask_add_table`:

dev_pm_opp_of_cpumask_add_table
===============================

.. c:function:: int dev_pm_opp_of_cpumask_add_table(const struct cpumask *cpumask)

    Adds OPP table for \ ``cpumask``\ 

    :param cpumask:
        cpumask for which OPP table needs to be added.
    :type cpumask: const struct cpumask \*

.. _`dev_pm_opp_of_cpumask_add_table.description`:

Description
-----------

This adds the OPP tables for CPUs present in the \ ``cpumask``\ .

.. _`dev_pm_opp_of_get_sharing_cpus`:

dev_pm_opp_of_get_sharing_cpus
==============================

.. c:function:: int dev_pm_opp_of_get_sharing_cpus(struct device *cpu_dev, struct cpumask *cpumask)

    Get cpumask of CPUs sharing OPPs with \ ``cpu_dev``\  using operating-points-v2 bindings.

    :param cpu_dev:
        CPU device for which we do this operation
    :type cpu_dev: struct device \*

    :param cpumask:
        cpumask to update with information of sharing CPUs
    :type cpumask: struct cpumask \*

.. _`dev_pm_opp_of_get_sharing_cpus.description`:

Description
-----------

This updates the \ ``cpumask``\  with CPUs that are sharing OPPs with \ ``cpu_dev``\ .

Returns -ENOENT if operating-points-v2 isn't present for \ ``cpu_dev``\ .

.. _`of_dev_pm_opp_find_required_opp`:

of_dev_pm_opp_find_required_opp
===============================

.. c:function:: struct dev_pm_opp *of_dev_pm_opp_find_required_opp(struct device *dev, struct device_node *np)

    Search for required OPP.

    :param dev:
        The device whose OPP node is referenced by the 'np' DT node.
    :type dev: struct device \*

    :param np:
        Node that contains the "required-opps" property.
    :type np: struct device_node \*

.. _`of_dev_pm_opp_find_required_opp.description`:

Description
-----------

Returns the OPP of the device 'dev', whose phandle is present in the "np"
node. Although the "required-opps" property supports having multiple
phandles, this helper routine only parses the very first phandle in the list.

.. _`of_dev_pm_opp_find_required_opp.return`:

Return
------

Matching opp, else returns ERR_PTR in case of error and should be
handled using IS_ERR.

The callers are required to call \ :c:func:`dev_pm_opp_put`\  for the returned OPP after
use.

.. _`dev_pm_opp_get_of_node`:

dev_pm_opp_get_of_node
======================

.. c:function:: struct device_node *dev_pm_opp_get_of_node(struct dev_pm_opp *opp)

    Gets the DT node corresponding to an opp

    :param opp:
        opp for which DT node has to be returned for
    :type opp: struct dev_pm_opp \*

.. _`dev_pm_opp_get_of_node.return`:

Return
------

DT node corresponding to the opp, else 0 on success.

The caller needs to put the node with \ :c:func:`of_node_put`\  after using it.

.. This file was automatic generated / don't edit.

