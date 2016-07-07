.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/power/opp/of.c

.. _`dev_pm_opp_of_remove_table`:

dev_pm_opp_of_remove_table
==========================

.. c:function:: void dev_pm_opp_of_remove_table(struct device *dev)

    Free OPP table entries created from static DT entries

    :param struct device \*dev:
        device pointer used to lookup OPP table.

.. _`dev_pm_opp_of_remove_table.description`:

Description
-----------

Free OPPs created using static entries present in DT.

.. _`dev_pm_opp_of_remove_table.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function indirectly uses RCU updater strategy with mutex locks
to keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex cannot be locked.

.. _`_opp_add_static_v2`:

_opp_add_static_v2
==================

.. c:function:: int _opp_add_static_v2(struct device *dev, struct device_node *np)

    Allocate static OPPs (As per 'v2' DT bindings)

    :param struct device \*dev:
        device for which we do this operation

    :param struct device_node \*np:
        device node

.. _`_opp_add_static_v2.description`:

Description
-----------

This function adds an opp definition to the opp table and returns status. The
opp can be controlled using dev_pm_opp_enable/disable functions and may be
removed by dev_pm_opp_remove.

.. _`_opp_add_static_v2.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function internally uses RCU updater strategy with mutex locks
to keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex cannot be locked.

.. _`_opp_add_static_v2.return`:

Return
------

0            On success OR
Duplicate OPPs (both freq and volt are same) and opp->available
-EEXIST      Freq are same and volt are different OR
Duplicate OPPs (both freq and volt are same) and !opp->available
-ENOMEM      Memory allocation failure
-EINVAL      Failed parsing the OPP node

.. _`dev_pm_opp_of_add_table`:

dev_pm_opp_of_add_table
=======================

.. c:function:: int dev_pm_opp_of_add_table(struct device *dev)

    Initialize opp table from device tree

    :param struct device \*dev:
        device pointer used to lookup OPP table.

.. _`dev_pm_opp_of_add_table.description`:

Description
-----------

Register the initial OPP table with the OPP library for given device.

.. _`dev_pm_opp_of_add_table.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function indirectly uses RCU updater strategy with mutex locks
to keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex cannot be locked.

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

.. _`dev_pm_opp_of_cpumask_remove_table`:

dev_pm_opp_of_cpumask_remove_table
==================================

.. c:function:: void dev_pm_opp_of_cpumask_remove_table(const struct cpumask *cpumask)

    Removes OPP table for \ ``cpumask``\ 

    :param const struct cpumask \*cpumask:
        cpumask for which OPP table needs to be removed

.. _`dev_pm_opp_of_cpumask_remove_table.description`:

Description
-----------

This removes the OPP tables for CPUs present in the \ ``cpumask``\ .
This should be used only to remove static entries created from DT.

.. _`dev_pm_opp_of_cpumask_remove_table.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function internally uses RCU updater strategy with mutex locks
to keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex cannot be locked.

.. _`dev_pm_opp_of_cpumask_add_table`:

dev_pm_opp_of_cpumask_add_table
===============================

.. c:function:: int dev_pm_opp_of_cpumask_add_table(const struct cpumask *cpumask)

    Adds OPP table for \ ``cpumask``\ 

    :param const struct cpumask \*cpumask:
        cpumask for which OPP table needs to be added.

.. _`dev_pm_opp_of_cpumask_add_table.description`:

Description
-----------

This adds the OPP tables for CPUs present in the \ ``cpumask``\ .

.. _`dev_pm_opp_of_cpumask_add_table.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function internally uses RCU updater strategy with mutex locks
to keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex cannot be locked.

.. _`dev_pm_opp_of_get_sharing_cpus`:

dev_pm_opp_of_get_sharing_cpus
==============================

.. c:function:: int dev_pm_opp_of_get_sharing_cpus(struct device *cpu_dev, struct cpumask *cpumask)

    Get cpumask of CPUs sharing OPPs with \ ``cpu_dev``\  using operating-points-v2 bindings.

    :param struct device \*cpu_dev:
        CPU device for which we do this operation

    :param struct cpumask \*cpumask:
        cpumask to update with information of sharing CPUs

.. _`dev_pm_opp_of_get_sharing_cpus.description`:

Description
-----------

This updates the \ ``cpumask``\  with CPUs that are sharing OPPs with \ ``cpu_dev``\ .

Returns -ENOENT if operating-points-v2 isn't present for \ ``cpu_dev``\ .

.. _`dev_pm_opp_of_get_sharing_cpus.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function internally uses RCU updater strategy with mutex locks
to keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex cannot be locked.

.. This file was automatic generated / don't edit.

