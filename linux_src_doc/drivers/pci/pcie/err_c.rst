.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pcie/err.c

.. _`default_reset_link`:

default_reset_link
==================

.. c:function:: pci_ers_result_t default_reset_link(struct pci_dev *dev)

    default reset function

    :param struct pci_dev \*dev:
        pointer to pci_dev data structure

.. _`default_reset_link.description`:

Description
-----------

Invoked when performing link reset on a Downstream Port or a
Root Port with no aer driver.

.. _`broadcast_error_message`:

broadcast_error_message
=======================

.. c:function:: pci_ers_result_t broadcast_error_message(struct pci_dev *dev, enum pci_channel_state state, char *error_mesg, int (*cb)(struct pci_dev *, void *))

    handle message broadcast to downstream drivers

    :param struct pci_dev \*dev:
        pointer to from where in a hierarchy message is broadcasted down

    :param enum pci_channel_state state:
        error state

    :param char \*error_mesg:
        message to print

    :param int (\*cb)(struct pci_dev \*, void \*):
        callback to be broadcasted

.. _`broadcast_error_message.description`:

Description
-----------

Invoked during error recovery process. Once being invoked, the content
of error severity will be broadcasted to all downstream drivers in a
hierarchy in question.

.. _`pcie_do_fatal_recovery`:

pcie_do_fatal_recovery
======================

.. c:function:: void pcie_do_fatal_recovery(struct pci_dev *dev, u32 service)

    handle fatal error recovery process

    :param struct pci_dev \*dev:
        pointer to a pci_dev data structure of agent detecting an error

    :param u32 service:
        *undescribed*

.. _`pcie_do_fatal_recovery.description`:

Description
-----------

Invoked when an error is fatal. Once being invoked, removes the devices
beneath this AER agent, followed by reset link e.g. secondary bus reset
followed by re-enumeration of devices.

.. _`pcie_do_nonfatal_recovery`:

pcie_do_nonfatal_recovery
=========================

.. c:function:: void pcie_do_nonfatal_recovery(struct pci_dev *dev)

    handle nonfatal error recovery process

    :param struct pci_dev \*dev:
        pointer to a pci_dev data structure of agent detecting an error

.. _`pcie_do_nonfatal_recovery.description`:

Description
-----------

Invoked when an error is nonfatal/fatal. Once being invoked, broadcast
error detected message to all downstream drivers within a hierarchy in
question and return the returned code.

.. This file was automatic generated / don't edit.

