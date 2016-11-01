.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/rpadlpar_core.c

.. _`find_php_slot`:

find_php_slot
=============

.. c:function:: struct slot *find_php_slot(struct device_node *dn)

    return hotplug slot structure for device node

    :param struct device_node \*dn:
        target \ :c:type:`struct device_node <device_node>`\ 

.. _`find_php_slot.description`:

Description
-----------

This routine will return the hotplug slot structure
for a given device node. Note that built-in PCI slots
may be dlpar-able, but not hot-pluggable, so this routine
will return NULL for built-in PCI slots.

.. _`dlpar_add_slot`:

dlpar_add_slot
==============

.. c:function:: int dlpar_add_slot(char *drc_name)

    DLPAR add an I/O Slot

    :param char \*drc_name:
        drc-name of newly added slot

.. _`dlpar_add_slot.description`:

Description
-----------

Make the hotplug module and the kernel aware of a newly added I/O Slot.

.. _`dlpar_add_slot.return-codes`:

Return Codes
------------

0                    Success
-ENODEV              Not a valid drc_name
-EINVAL              Slot already added
-ERESTARTSYS         Signalled before obtaining lock
-EIO                 Internal PCI Error

.. _`dlpar_remove_vio_slot`:

dlpar_remove_vio_slot
=====================

.. c:function:: int dlpar_remove_vio_slot(char *drc_name, struct device_node *dn)

    DLPAR remove a virtual I/O Slot

    :param char \*drc_name:
        drc-name of newly added slot

    :param struct device_node \*dn:
        &device_node

.. _`dlpar_remove_vio_slot.description`:

Description
-----------

Remove the kernel and hotplug representations of an I/O Slot.

.. _`dlpar_remove_vio_slot.return-codes`:

Return Codes
------------

0                    Success
-EINVAL              Vio dev doesn't exist

.. _`dlpar_remove_pci_slot`:

dlpar_remove_pci_slot
=====================

.. c:function:: int dlpar_remove_pci_slot(char *drc_name, struct device_node *dn)

    DLPAR remove a PCI I/O Slot

    :param char \*drc_name:
        drc-name of newly added slot

    :param struct device_node \*dn:
        &device_node

.. _`dlpar_remove_pci_slot.description`:

Description
-----------

Remove the kernel and hotplug representations of a PCI I/O Slot.

.. _`dlpar_remove_pci_slot.return-codes`:

Return Codes
------------

0                    Success
-ENODEV              Not a valid drc_name
-EIO                 Internal PCI Error

.. _`dlpar_remove_slot`:

dlpar_remove_slot
=================

.. c:function:: int dlpar_remove_slot(char *drc_name)

    DLPAR remove an I/O Slot

    :param char \*drc_name:
        drc-name of newly added slot

.. _`dlpar_remove_slot.description`:

Description
-----------

Remove the kernel and hotplug representations of an I/O Slot.

.. _`dlpar_remove_slot.return-codes`:

Return Codes
------------

0                    Success
-ENODEV              Not a valid drc_name
-EINVAL              Slot already removed
-ERESTARTSYS         Signalled before obtaining lock
-EIO                 Internal Error

.. This file was automatic generated / don't edit.

