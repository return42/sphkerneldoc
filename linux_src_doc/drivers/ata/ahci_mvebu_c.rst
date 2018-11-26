.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/ahci_mvebu.c

.. _`ahci_mvebu_stop_engine`:

ahci_mvebu_stop_engine
======================

.. c:function:: int ahci_mvebu_stop_engine(struct ata_port *ap)

    :param ap:
        Target ata port
    :type ap: struct ata_port \*

.. _`ahci_mvebu_stop_engine.description`:

Description
-----------

Errata Ref#226 - SATA Disk HOT swap issue when connected through
Port Multiplier in FIS-based Switching mode.

To avoid the issue, according to design, the bits[11:8, 0] of
register PxFBS are cleared when Port Command and Status (0x18) bit[0]
changes its value from 1 to 0, i.e. falling edge of Port
Command and Status bit[0] sends PULSE that resets PxFBS
bits[11:8; 0].

This function is used to override function of "ahci_stop_engine"
from libahci.c by adding the mvebu work around(WA) to save PxFBS
value before the PxCMD ST write of 0, then restore PxFBS value.

.. _`ahci_mvebu_stop_engine.return`:

Return
------

0 on success; Error code otherwise.

.. This file was automatic generated / don't edit.

