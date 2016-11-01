.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/ehci-fsl.c

.. _`fsl_ehci_drv_remove`:

fsl_ehci_drv_remove
===================

.. c:function:: int fsl_ehci_drv_remove(struct platform_device *pdev)

    shutdown processing for FSL-based HCDs

    :param struct platform_device \*pdev:
        *undescribed*

.. _`fsl_ehci_drv_remove.context`:

Context
-------

!in_interrupt()

.. _`fsl_ehci_drv_remove.description`:

Description
-----------

Reverses the effect of \ :c:func:`usb_hcd_fsl_probe`\ .

.. This file was automatic generated / don't edit.

