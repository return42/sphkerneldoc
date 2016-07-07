.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/plat-samsung/include/plat/devs.h

.. _`s3c_set_platdata`:

s3c_set_platdata
================

.. c:function:: void *s3c_set_platdata(void *pd, size_t pdsize, struct platform_device *pdev)

    helper for setting platform data

    :param void \*pd:
        The default platform data for this device.

    :param size_t pdsize:
        The size of the platform data.

    :param struct platform_device \*pdev:
        Pointer to the device to fill in.

.. _`s3c_set_platdata.description`:

Description
-----------

This helper replaces a number of calls that copy and then set the
platform data of the device.

.. This file was automatic generated / don't edit.

