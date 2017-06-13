.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iio/common/ssp_sensors.h

.. _`ssp_sensor_type`:

enum ssp_sensor_type
====================

.. c:type:: enum ssp_sensor_type

    SSP sensor type

.. _`ssp_sensor_type.definition`:

Definition
----------

.. code-block:: c

    enum ssp_sensor_type {
        SSP_ACCELEROMETER_SENSOR,
        SSP_GYROSCOPE_SENSOR,
        SSP_GEOMAGNETIC_UNCALIB_SENSOR,
        SSP_GEOMAGNETIC_RAW,
        SSP_GEOMAGNETIC_SENSOR,
        SSP_PRESSURE_SENSOR,
        SSP_GESTURE_SENSOR,
        SSP_PROXIMITY_SENSOR,
        SSP_TEMPERATURE_HUMIDITY_SENSOR,
        SSP_LIGHT_SENSOR,
        SSP_PROXIMITY_RAW,
        SSP_ORIENTATION_SENSOR,
        SSP_STEP_DETECTOR,
        SSP_SIG_MOTION_SENSOR,
        SSP_GYRO_UNCALIB_SENSOR,
        SSP_GAME_ROTATION_VECTOR,
        SSP_ROTATION_VECTOR,
        SSP_STEP_COUNTER,
        SSP_BIO_HRM_RAW,
        SSP_BIO_HRM_RAW_FAC,
        SSP_BIO_HRM_LIB,
        SSP_SENSOR_MAX
    };

.. _`ssp_sensor_type.constants`:

Constants
---------

SSP_ACCELEROMETER_SENSOR
    *undescribed*

SSP_GYROSCOPE_SENSOR
    *undescribed*

SSP_GEOMAGNETIC_UNCALIB_SENSOR
    *undescribed*

SSP_GEOMAGNETIC_RAW
    *undescribed*

SSP_GEOMAGNETIC_SENSOR
    *undescribed*

SSP_PRESSURE_SENSOR
    *undescribed*

SSP_GESTURE_SENSOR
    *undescribed*

SSP_PROXIMITY_SENSOR
    *undescribed*

SSP_TEMPERATURE_HUMIDITY_SENSOR
    *undescribed*

SSP_LIGHT_SENSOR
    *undescribed*

SSP_PROXIMITY_RAW
    *undescribed*

SSP_ORIENTATION_SENSOR
    *undescribed*

SSP_STEP_DETECTOR
    *undescribed*

SSP_SIG_MOTION_SENSOR
    *undescribed*

SSP_GYRO_UNCALIB_SENSOR
    *undescribed*

SSP_GAME_ROTATION_VECTOR
    *undescribed*

SSP_ROTATION_VECTOR
    *undescribed*

SSP_STEP_COUNTER
    *undescribed*

SSP_BIO_HRM_RAW
    *undescribed*

SSP_BIO_HRM_RAW_FAC
    *undescribed*

SSP_BIO_HRM_LIB
    *undescribed*

SSP_SENSOR_MAX
    *undescribed*

.. _`ssp_sensor_data`:

struct ssp_sensor_data
======================

.. c:type:: struct ssp_sensor_data

    Sensor object

.. _`ssp_sensor_data.definition`:

Definition
----------

.. code-block:: c

    struct ssp_sensor_data {
        int (*process_data)(struct iio_dev *indio_dev, void *buf, int64_t timestamp);
        enum ssp_sensor_type type;
        u8 *buffer;
    }

.. _`ssp_sensor_data.members`:

Members
-------

process_data
    Callback to feed sensor data.

type
    Used sensor type.

buffer
    Received data buffer.

.. This file was automatic generated / don't edit.

