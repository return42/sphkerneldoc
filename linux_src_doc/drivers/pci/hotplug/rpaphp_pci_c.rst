.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/rpaphp_pci.c

.. _`rpaphp_enable_slot`:

rpaphp_enable_slot
==================

.. c:function:: int rpaphp_enable_slot(struct slot *slot)

    record slot state, config pci device

    :param slot:
        target \ :c:type:`struct slot <slot>`\ 
    :type slot: struct slot \*

.. _`rpaphp_enable_slot.description`:

Description
-----------

Initialize values in the slot structure to indicate if there is a pci card
plugged into the slot. If the slot is not empty, run the pcibios routine
to get pcibios stuff correctly set up.

.. This file was automatic generated / don't edit.

