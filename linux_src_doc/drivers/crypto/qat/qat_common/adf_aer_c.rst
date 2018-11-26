.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/qat/qat_common/adf_aer.c

.. _`adf_enable_aer`:

adf_enable_aer
==============

.. c:function:: int adf_enable_aer(struct adf_accel_dev *accel_dev, struct pci_driver *adf)

    Enable Advance Error Reporting for acceleration device

    :param accel_dev:
        Pointer to acceleration device.
    :type accel_dev: struct adf_accel_dev \*

    :param adf:
        PCI device driver owning the given acceleration device.
    :type adf: struct pci_driver \*

.. _`adf_enable_aer.description`:

Description
-----------

Function enables PCI Advance Error Reporting for the
QAT acceleration device accel_dev.
To be used by QAT device specific drivers.

.. _`adf_enable_aer.return`:

Return
------

0 on success, error code otherwise.

.. _`adf_disable_aer`:

adf_disable_aer
===============

.. c:function:: void adf_disable_aer(struct adf_accel_dev *accel_dev)

    Enable Advance Error Reporting for acceleration device

    :param accel_dev:
        Pointer to acceleration device.
    :type accel_dev: struct adf_accel_dev \*

.. _`adf_disable_aer.description`:

Description
-----------

Function disables PCI Advance Error Reporting for the
QAT acceleration device accel_dev.
To be used by QAT device specific drivers.

.. _`adf_disable_aer.return`:

Return
------

void

.. This file was automatic generated / don't edit.

