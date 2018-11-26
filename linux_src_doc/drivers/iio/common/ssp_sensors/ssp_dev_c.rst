.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/common/ssp_sensors/ssp_dev.c

.. _`ssp_get_sensor_delay`:

ssp_get_sensor_delay
====================

.. c:function:: u32 ssp_get_sensor_delay(struct ssp_data *data, enum ssp_sensor_type type)

    gets sensor data acquisition period

    :param data:
        sensorhub structure
    :type data: struct ssp_data \*

    :param type:
        SSP sensor type
    :type type: enum ssp_sensor_type

.. _`ssp_get_sensor_delay.description`:

Description
-----------

Returns acquisition period in ms

.. _`ssp_enable_sensor`:

ssp_enable_sensor
=================

.. c:function:: int ssp_enable_sensor(struct ssp_data *data, enum ssp_sensor_type type, u32 delay)

    enables data acquisition for sensor

    :param data:
        sensorhub structure
    :type data: struct ssp_data \*

    :param type:
        SSP sensor type
    :type type: enum ssp_sensor_type

    :param delay:
        delay in ms
    :type delay: u32

.. _`ssp_enable_sensor.description`:

Description
-----------

Returns 0 or negative value in case of error

.. _`ssp_change_delay`:

ssp_change_delay
================

.. c:function:: int ssp_change_delay(struct ssp_data *data, enum ssp_sensor_type type, u32 delay)

    changes data acquisition for sensor

    :param data:
        sensorhub structure
    :type data: struct ssp_data \*

    :param type:
        SSP sensor type
    :type type: enum ssp_sensor_type

    :param delay:
        delay in ms
    :type delay: u32

.. _`ssp_change_delay.description`:

Description
-----------

Returns 0 or negative value in case of error

.. _`ssp_disable_sensor`:

ssp_disable_sensor
==================

.. c:function:: int ssp_disable_sensor(struct ssp_data *data, enum ssp_sensor_type type)

    disables sensor

    :param data:
        sensorhub structure
    :type data: struct ssp_data \*

    :param type:
        SSP sensor type
    :type type: enum ssp_sensor_type

.. _`ssp_disable_sensor.description`:

Description
-----------

Returns 0 or negative value in case of error

.. _`ssp_register_consumer`:

ssp_register_consumer
=====================

.. c:function:: void ssp_register_consumer(struct iio_dev *indio_dev, enum ssp_sensor_type type)

    registers iio consumer in ssp framework

    :param indio_dev:
        consumer iio device
    :type indio_dev: struct iio_dev \*

    :param type:
        ssp sensor type
    :type type: enum ssp_sensor_type

.. This file was automatic generated / don't edit.

