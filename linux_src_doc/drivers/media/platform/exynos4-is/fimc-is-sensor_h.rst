.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/exynos4-is/fimc-is-sensor.h

.. _`fimc_is_sensor`:

struct fimc_is_sensor
=====================

.. c:type:: struct fimc_is_sensor

    fimc-is sensor data structure

.. _`fimc_is_sensor.definition`:

Definition
----------

.. code-block:: c

    struct fimc_is_sensor {
        const struct sensor_drv_data *drvdata;
        unsigned int i2c_bus;
        u8 test_pattern;
    }

.. _`fimc_is_sensor.members`:

Members
-------

drvdata
    a pointer to the sensor's parameters data structure

i2c_bus
    ISP I2C bus index (0...1)

test_pattern
    true to enable video test pattern

.. This file was automatic generated / don't edit.

