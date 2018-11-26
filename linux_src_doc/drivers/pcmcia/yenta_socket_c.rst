.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pcmcia/yenta_socket.c

.. _`yenta_fixup_parent_bridge`:

yenta_fixup_parent_bridge
=========================

.. c:function:: void yenta_fixup_parent_bridge(struct pci_bus *cardbus_bridge)

    Fix subordinate bus# of the parent bridge

    :param cardbus_bridge:
        The PCI bus which the CardBus bridge bridges to
    :type cardbus_bridge: struct pci_bus \*

.. _`yenta_fixup_parent_bridge.description`:

Description
-----------

Checks if devices on the bus which the CardBus bridge bridges to would be
invisible during PCI scans because of a misconfigured subordinate number
of the parent brige - some BIOSes seem to be too lazy to set it right.
Does the fixup carefully by checking how far it can go without conflicts.
See http://bugzilla.kernel.org/show_bug.cgi?id=2944 for more information.

.. This file was automatic generated / don't edit.

