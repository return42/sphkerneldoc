.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/devices/powernv_flash.c

.. _`powernv_flash_set_driver_info`:

powernv_flash_set_driver_info
=============================

.. c:function:: int powernv_flash_set_driver_info(struct device *dev, struct mtd_info *mtd)

    Fill the mtd_info structure and docg3 structure \ ``pdev``\ : The platform device

    :param struct device \*dev:
        *undescribed*

    :param struct mtd_info \*mtd:
        The structure to fill

.. _`powernv_flash_probe`:

powernv_flash_probe
===================

.. c:function:: int powernv_flash_probe(struct platform_device *pdev)

    :param struct platform_device \*pdev:
        platform device

.. _`powernv_flash_probe.description`:

Description
-----------

Returns 0 on success, -ENOMEM, -ENXIO on error

.. _`powernv_flash_release`:

powernv_flash_release
=====================

.. c:function:: int powernv_flash_release(struct platform_device *pdev)

    Release the driver

    :param struct platform_device \*pdev:
        the platform device

.. _`powernv_flash_release.description`:

Description
-----------

Returns 0

.. This file was automatic generated / don't edit.

