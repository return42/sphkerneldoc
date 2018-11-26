.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/umc-bus.c

.. _`umc_controller_reset`:

umc_controller_reset
====================

.. c:function:: int umc_controller_reset(struct umc_dev *umc)

    reset the whole UMC controller

    :param umc:
        the UMC device for the radio controller.
    :type umc: struct umc_dev \*

.. _`umc_controller_reset.description`:

Description
-----------

Drivers or all capabilities of the controller will have their
pre_reset methods called or be unbound from their device.  Then all
post_reset methods will be called or the drivers will be rebound.

Radio controllers must provide pre_reset and post_reset methods and
reset the hardware in their start method.

If this is called while a \ :c:func:`probe`\  or \ :c:func:`remove`\  is in progress it
will return -EAGAIN and not perform the reset.

.. _`umc_match_pci_id`:

umc_match_pci_id
================

.. c:function:: int umc_match_pci_id(struct umc_driver *umc_drv, struct umc_dev *umc)

    match a UMC driver to a UMC device's parent PCI device.

    :param umc_drv:
        umc driver with match_data pointing to a zero-terminated
        table of pci_device_id's.
    :type umc_drv: struct umc_driver \*

    :param umc:
        umc device whose parent is to be matched.
    :type umc: struct umc_dev \*

.. This file was automatic generated / don't edit.

