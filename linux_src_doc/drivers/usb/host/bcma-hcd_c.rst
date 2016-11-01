.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/bcma-hcd.c

.. _`bcma_hcd_usb20_old_arm_init`:

bcma_hcd_usb20_old_arm_init
===========================

.. c:function:: int bcma_hcd_usb20_old_arm_init(struct bcma_hcd_device *usb_dev)

    Initialize old USB 2.0 controller on ARM

    :param struct bcma_hcd_device \*usb_dev:
        *undescribed*

.. _`bcma_hcd_usb20_old_arm_init.description`:

Description
-----------

Old USB 2.0 core is identified as BCMA_CORE_USB20_HOST and was introduced
long before Northstar devices. It seems some cheaper chipsets like BCM53573
still use it.
Initialization of this old core differs between MIPS and ARM.

.. _`bcma_hcd_usb20_ns_init`:

bcma_hcd_usb20_ns_init
======================

.. c:function:: int bcma_hcd_usb20_ns_init(struct bcma_hcd_device *bcma_hcd)

    Initialize Northstar USB 2.0 controller

    :param struct bcma_hcd_device \*bcma_hcd:
        *undescribed*

.. This file was automatic generated / don't edit.

