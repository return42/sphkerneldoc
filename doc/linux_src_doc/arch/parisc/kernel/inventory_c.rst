.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/parisc/kernel/inventory.c

.. _`snake_inventory`:

snake_inventory
===============

.. c:function:: void snake_inventory( void)

    :param  void:
        no arguments

.. _`snake_inventory.description`:

Description
-----------

Before PDC_SYSTEM_MAP was invented, the PDC_MEM_MAP call was used.
To use it, we initialise the mod_path.bc to 0xff and try all values of
mod to get the HPA for the top-level devices.  Bus adapters may have
sub-devices which are discovered by setting bc[5] to 0 and bc[4] to the
module, then trying all possible functions.

.. _`add_system_map_addresses`:

add_system_map_addresses
========================

.. c:function:: void add_system_map_addresses(struct parisc_device *dev, int num_addrs, int module_instance)

    Add additional addresses to the parisc device.

    :param struct parisc_device \*dev:
        The parisc device.

    :param int num_addrs:
        Then number of addresses to add;

    :param int module_instance:
        The system_map module instance.

.. _`add_system_map_addresses.description`:

Description
-----------

This function adds any additional addresses reported by the system_map
firmware to the parisc device.

.. _`system_map_inventory`:

system_map_inventory
====================

.. c:function:: void system_map_inventory( void)

    Retrieve firmware devices via SYSTEM_MAP.

    :param  void:
        no arguments

.. _`system_map_inventory.description`:

Description
-----------

This function attempts to retrieve and register all the devices firmware
knows about via the SYSTEM_MAP PDC call.

.. This file was automatic generated / don't edit.

