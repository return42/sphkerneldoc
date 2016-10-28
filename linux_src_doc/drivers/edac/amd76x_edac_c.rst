.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/edac/amd76x_edac.c

.. _`amd76x_get_error_info`:

amd76x_get_error_info
=====================

.. c:function:: void amd76x_get_error_info(struct mem_ctl_info *mci, struct amd76x_error_info *info)

    fetch error information

    :param struct mem_ctl_info \*mci:
        Memory controller

    :param struct amd76x_error_info \*info:
        Info to fill in

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

    :param struct mem_ctl_info \*mci:
        Memory controller

    :param struct amd76x_error_info \*info:
        Previously fetched information from chip

    :param int handle_errors:
        1 if we should do recovery

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

    :param struct mem_ctl_info \*mci:
        Memory controller

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

    :param struct pci_dev \*pdev:
        *undescribed*

    :param int dev_idx:
        Device type index

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

    :param struct pci_dev \*pdev:
        PCI device being handed back

.. _`amd76x_remove_one.description`:

Description
-----------

Called when the driver is unloaded. Find the matching mci
structure for the device then delete the mci and free the
resources.

.. This file was automatic generated / don't edit.

