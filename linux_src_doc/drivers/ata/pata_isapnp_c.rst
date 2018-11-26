.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_isapnp.c

.. _`isapnp_init_one`:

isapnp_init_one
===============

.. c:function:: int isapnp_init_one(struct pnp_dev *idev, const struct pnp_device_id *dev_id)

    attach an isapnp interface

    :param idev:
        PnP device
    :type idev: struct pnp_dev \*

    :param dev_id:
        matching detect line
    :type dev_id: const struct pnp_device_id \*

.. _`isapnp_init_one.description`:

Description
-----------

Register an ISA bus IDE interface. Such interfaces are PIO 0 and
non shared IRQ.

.. _`isapnp_remove_one`:

isapnp_remove_one
=================

.. c:function:: void isapnp_remove_one(struct pnp_dev *idev)

    unplug an isapnp interface

    :param idev:
        PnP device
    :type idev: struct pnp_dev \*

.. _`isapnp_remove_one.description`:

Description
-----------

Remove a previously configured PnP ATA port. Called only on module
unload events as the core does not currently deal with ISAPnP docking.

.. This file was automatic generated / don't edit.

