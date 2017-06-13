.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/invensense_mpu6050.h

.. _`inv_mpu6050_platform_data`:

struct inv_mpu6050_platform_data
================================

.. c:type:: struct inv_mpu6050_platform_data

    Platform data for the mpu driver

.. _`inv_mpu6050_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct inv_mpu6050_platform_data {
        __s8 orientation;
    }

.. _`inv_mpu6050_platform_data.members`:

Members
-------

orientation
    Orientation matrix of the chip (deprecated in favor of
    mounting matrix retrieved from device-tree)

.. _`inv_mpu6050_platform_data.description`:

Description
-----------

Contains platform specific information on how to configure the MPU6050 to
work on this platform.  The orientation matricies are 3x3 rotation matricies
that are applied to the data to rotate from the mounting orientation to the
platform orientation.  The values must be one of 0, 1, or -1 and each row and
column should have exactly 1 non-zero value.

Deprecated in favor of mounting matrix retrieved from device-tree.

.. This file was automatic generated / don't edit.

