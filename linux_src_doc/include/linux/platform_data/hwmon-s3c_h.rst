.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/hwmon-s3c.h

.. _`s3c_hwmon_set_platdata`:

s3c_hwmon_set_platdata
======================

.. c:function:: void s3c_hwmon_set_platdata(struct s3c_hwmon_pdata *pd)

    Set platform data for S3C HWMON device

    :param struct s3c_hwmon_pdata \*pd:
        Platform data to register to device.

.. _`s3c_hwmon_set_platdata.description`:

Description
-----------

Register the given platform data for use with the S3C HWMON device.
The call will copy the platform data, so the board definitions can
make the structure itself \__initdata.

.. This file was automatic generated / don't edit.

