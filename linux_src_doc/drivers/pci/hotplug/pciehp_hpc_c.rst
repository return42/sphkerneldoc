.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/pciehp_hpc.c

.. _`pcie_write_cmd`:

pcie_write_cmd
==============

.. c:function:: void pcie_write_cmd(struct controller *ctrl, u16 cmd, u16 mask)

    Issue controller command

    :param ctrl:
        controller to which the command is issued
    :type ctrl: struct controller \*

    :param cmd:
        command value written to slot control register
    :type cmd: u16

    :param mask:
        bitmask of slot control register to be modified
    :type mask: u16

.. _`pciehp_card_present_or_link_active`:

pciehp_card_present_or_link_active
==================================

.. c:function:: bool pciehp_card_present_or_link_active(struct controller *ctrl)

    whether given slot is occupied

    :param ctrl:
        PCIe hotplug controller
    :type ctrl: struct controller \*

.. _`pciehp_card_present_or_link_active.description`:

Description
-----------

Unlike \ :c:func:`pciehp_card_present`\ , which determines presence solely from the
Presence Detect State bit, this helper also returns true if the Link Active
bit is set.  This is a concession to broken hotplug ports which hardwire
Presence Detect State to zero, such as Wilocity's [1ae9:0200].

.. This file was automatic generated / don't edit.

