.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libsas/sas_ata.c

.. _`sas_discover_sata`:

sas_discover_sata
=================

.. c:function:: int sas_discover_sata(struct domain_device *dev)

    discover an STP/SATA domain device

    :param dev:
        pointer to struct domain_device of interest
    :type dev: struct domain_device \*

.. _`sas_discover_sata.description`:

Description
-----------

Devices directly attached to a HA port, have no parents.  All other
devices do, and should have their "parent" pointer set appropriately
before calling this function.

.. This file was automatic generated / don't edit.

