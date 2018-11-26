.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/prom.c

.. _`move_device_tree`:

move_device_tree
================

.. c:function:: void move_device_tree( void)

    move tree to an unused area, if needed.

    :param void:
        no arguments
    :type void: 

.. _`move_device_tree.description`:

Description
-----------

The device tree may be allocated beyond our memory limit, or inside the
crash kernel region for kdump, or within the page aligned range of initrd.
If so, move it out of the way.

.. _`of_get_ibm_chip_id`:

of_get_ibm_chip_id
==================

.. c:function:: int of_get_ibm_chip_id(struct device_node *np)

    Returns the IBM "chip-id" of a device

    :param np:
        device node of the device
    :type np: struct device_node \*

.. _`of_get_ibm_chip_id.description`:

Description
-----------

This looks for a property "ibm,chip-id" in the node or any
of its parents and returns its content, or -1 if it cannot
be found.

.. _`cpu_to_chip_id`:

cpu_to_chip_id
==============

.. c:function:: int cpu_to_chip_id(int cpu)

    Return the cpus chip-id

    :param cpu:
        The logical cpu number.
    :type cpu: int

.. _`cpu_to_chip_id.description`:

Description
-----------

Return the value of the ibm,chip-id property corresponding to the given
logical cpu number. If the chip-id can not be found, returns -1.

.. This file was automatic generated / don't edit.

