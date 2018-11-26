.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/pciehp_core.c

.. _`pciehp_check_presence`:

pciehp_check_presence
=====================

.. c:function:: void pciehp_check_presence(struct controller *ctrl)

    synthesize event if presence has changed

    :param ctrl:
        *undescribed*
    :type ctrl: struct controller \*

.. _`pciehp_check_presence.description`:

Description
-----------

On probe and resume, an explicit presence check is necessary to bring up an
occupied slot or bring down an unoccupied slot.  This can't be triggered by
events in the Slot Status register, they may be stale and are therefore
cleared.  Secondly, sending an interrupt for "events that occur while
interrupt generation is disabled [when] interrupt generation is subsequently
enabled" is optional per PCIe r4.0, sec 6.7.3.4.

.. This file was automatic generated / don't edit.

