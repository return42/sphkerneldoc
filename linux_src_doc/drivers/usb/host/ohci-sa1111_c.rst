.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/ohci-sa1111.c

.. _`ohci_hcd_sa1111_probe`:

ohci_hcd_sa1111_probe
=====================

.. c:function:: int ohci_hcd_sa1111_probe(struct sa1111_dev *dev)

    initialize SA-1111-based HCDs

    :param dev:
        *undescribed*
    :type dev: struct sa1111_dev \*

.. _`ohci_hcd_sa1111_probe.description`:

Description
-----------

Allocates basic resources for this USB host controller, and
then invokes the \ :c:func:`start`\  method for the HCD associated with it.

.. _`ohci_hcd_sa1111_remove`:

ohci_hcd_sa1111_remove
======================

.. c:function:: int ohci_hcd_sa1111_remove(struct sa1111_dev *dev)

    shutdown processing for SA-1111-based HCDs

    :param dev:
        USB Host Controller being removed
    :type dev: struct sa1111_dev \*

.. _`ohci_hcd_sa1111_remove.description`:

Description
-----------

Reverses the effect of \ :c:func:`ohci_hcd_sa1111_probe`\ , first invoking
the HCD's \ :c:func:`stop`\  method.

.. This file was automatic generated / don't edit.

