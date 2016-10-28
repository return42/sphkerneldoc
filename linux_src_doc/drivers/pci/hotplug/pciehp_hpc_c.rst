.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/pciehp_hpc.c

.. _`pcie_write_cmd`:

pcie_write_cmd
==============

.. c:function:: void pcie_write_cmd(struct controller *ctrl, u16 cmd, u16 mask)

    Issue controller command

    :param struct controller \*ctrl:
        controller to which the command is issued

    :param u16 cmd:
        command value written to slot control register

    :param u16 mask:
        bitmask of slot control register to be modified

.. This file was automatic generated / don't edit.

