.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/edac/amd76x_edac.c

.. _`amd76x_get_error_info`:

amd76x_get_error_info
=====================

.. c:function:: void amd76x_get_error_info(struct mem_ctl_info *mci, struct amd76x_error_info *info)

    fetch error information

    :param mci:
        Memory controller
    :type mci: struct mem_ctl_info \*

    :param info:
        Info to fill in
    :type info: struct amd76x_error_info \*

.. _`amd76x_get_error_info.description`:

Description
-----------

Fetch and store the AMD76x ECC status. Clear pending status
on the chip so that further errors will be reported

.. _`amd76x_process_error_info`:

amd76x_process_error_info
=========================

.. c:function:: int amd76x_process_error_info(struct mem_ctl_info *mci, struct amd76x_error_info *info, int handle_errors)

    Error check

    :param mci:
        Memory controller
    :type mci: struct mem_ctl_info \*

    :param info:
        Previously fetched information from chip
    :type info: struct amd76x_error_info \*

    :param handle_errors:
        1 if we should do recovery
    :type handle_errors: int

.. _`amd76x_process_error_info.description`:

Description
-----------

Process the chip state and decide if an error has occurred.
A return of 1 indicates an error. Also if handle_errors is true
then attempt to handle and clean up after the error

.. _`amd76x_check`:

amd76x_check
============

.. c:function:: void amd76x_check(struct mem_ctl_info *mci)

    Poll the controller

    :param mci:
        Memory controller
    :type mci: struct mem_ctl_info \*

.. _`amd76x_check.description`:

Description
-----------

Called by the poll handlers this function reads the status
from the controller and checks for errors.

.. _`amd76x_probe1`:

amd76x_probe1
=============

.. c:function:: int amd76x_probe1(struct pci_dev *pdev, int dev_idx)

    Perform set up for detected device \ ``pdev``\ ; PCI device detected

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

    :param dev_idx:
        Device type index
    :type dev_idx: int

.. _`amd76x_probe1.description`:

Description
-----------

We have found an AMD76x and now need to set up the memory
controller status reporting. We configure and set up the
memory controller reporting and claim the device.

.. _`amd76x_remove_one`:

amd76x_remove_one
=================

.. c:function:: void amd76x_remove_one(struct pci_dev *pdev)

    driver shutdown

    :param pdev:
        PCI device being handed back
    :type pdev: struct pci_dev \*

.. _`amd76x_remove_one.description`:

Description
-----------

Called when the driver is unloaded. Find the matching mci
structure for the device then delete the mci and free the
resources.

.. This file was automatic generated / don't edit.

