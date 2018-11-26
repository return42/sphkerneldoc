.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iio/common/cros_ec_sensors_core.h

.. _`cros_ec_sensors_core_state`:

struct cros_ec_sensors_core_state
=================================

.. c:type:: struct cros_ec_sensors_core_state

    state data for EC sensors IIO driver

.. _`cros_ec_sensors_core_state.definition`:

Definition
----------

.. code-block:: c

    struct cros_ec_sensors_core_state {
        struct cros_ec_device *ec;
        struct mutex cmd_lock;
        struct cros_ec_command *msg;
        struct ec_params_motion_sense param;
        struct ec_response_motion_sense *resp;
        enum motionsensor_type type;
        enum motionsensor_location loc;
        s16 calib[CROS_EC_SENSOR_MAX_AXIS];
        u8 samples[CROS_EC_SAMPLE_SIZE];
        int (*read_ec_sensors_data)(struct iio_dev *indio_dev, unsigned long scan_mask, s16 *data);
        int curr_sampl_freq;
    }

.. _`cros_ec_sensors_core_state.members`:

Members
-------

ec
    cros EC device structure

cmd_lock
    lock used to prevent simultaneous access to the
    commands.

msg
    cros EC command structure

param
    motion sensor parameters structure

resp
    motion sensor response structure

type
    type of motion sensor

loc
    location where the motion sensor is placed

calib
    calibration parameters. Note that trigger
    captured data will always provide the calibrated
    data

samples
    static array to hold data from a single capture.
    For each channel we need 2 bytes, except for
    the timestamp. The timestamp is always last and
    is always 8-byte aligned.

read_ec_sensors_data
    function used for accessing sensors values

curr_sampl_freq
    *undescribed*

.. _`cros_ec_sensors_read_lpc`:

cros_ec_sensors_read_lpc
========================

.. c:function:: int cros_ec_sensors_read_lpc(struct iio_dev *indio_dev, unsigned long scan_mask, s16 *data)

    retrieve data from EC shared memory

    :param indio_dev:
        pointer to IIO device
    :type indio_dev: struct iio_dev \*

    :param scan_mask:
        bitmap of the sensor indices to scan
    :type scan_mask: unsigned long

    :param data:
        location to store data
    :type data: s16 \*

.. _`cros_ec_sensors_read_lpc.description`:

Description
-----------

This is the safe function for reading the EC data. It guarantees that the
data sampled was not modified by the EC while being read.

.. _`cros_ec_sensors_read_lpc.return`:

Return
------

0 on success, -errno on failure.

.. _`cros_ec_sensors_read_cmd`:

cros_ec_sensors_read_cmd
========================

.. c:function:: int cros_ec_sensors_read_cmd(struct iio_dev *indio_dev, unsigned long scan_mask, s16 *data)

    retrieve data using the EC command protocol

    :param indio_dev:
        pointer to IIO device
    :type indio_dev: struct iio_dev \*

    :param scan_mask:
        bitmap of the sensor indices to scan
    :type scan_mask: unsigned long

    :param data:
        location to store data
    :type data: s16 \*

.. _`cros_ec_sensors_read_cmd.return`:

Return
------

0 on success, -errno on failure.

.. _`cros_ec_sensors_core_init`:

cros_ec_sensors_core_init
=========================

.. c:function:: int cros_ec_sensors_core_init(struct platform_device *pdev, struct iio_dev *indio_dev, bool physical_device)

    basic initialization of the core structure

    :param pdev:
        platform device created for the sensors
    :type pdev: struct platform_device \*

    :param indio_dev:
        iio device structure of the device
    :type indio_dev: struct iio_dev \*

    :param physical_device:
        true if the device refers to a physical device
    :type physical_device: bool

.. _`cros_ec_sensors_core_init.return`:

Return
------

0 on success, -errno on failure.

.. _`cros_ec_sensors_capture`:

cros_ec_sensors_capture
=======================

.. c:function:: irqreturn_t cros_ec_sensors_capture(int irq, void *p)

    the trigger handler function

    :param irq:
        the interrupt number.
    :type irq: int

    :param p:
        a pointer to the poll function.
    :type p: void \*

.. _`cros_ec_sensors_capture.description`:

Description
-----------

On a trigger event occurring, if the pollfunc is attached then this
handler is called as a threaded interrupt (and hence may sleep). It
is responsible for grabbing data from the device and pushing it into
the associated buffer.

.. _`cros_ec_sensors_capture.return`:

Return
------

IRQ_HANDLED

.. _`cros_ec_motion_send_host_cmd`:

cros_ec_motion_send_host_cmd
============================

.. c:function:: int cros_ec_motion_send_host_cmd(struct cros_ec_sensors_core_state *st, u16 opt_length)

    send motion sense host command

    :param st:
        pointer to state information for device
    :type st: struct cros_ec_sensors_core_state \*

    :param opt_length:
        optional length to reduce the response size, useful on the data
        path. Otherwise, the maximal allowed response size is used
    :type opt_length: u16

.. _`cros_ec_motion_send_host_cmd.description`:

Description
-----------

When called, the sub-command is assumed to be set in param->cmd.

.. _`cros_ec_motion_send_host_cmd.return`:

Return
------

0 on success, -errno on failure.

.. _`cros_ec_sensors_core_read`:

cros_ec_sensors_core_read
=========================

.. c:function:: int cros_ec_sensors_core_read(struct cros_ec_sensors_core_state *st, struct iio_chan_spec const *chan, int *val, int *val2, long mask)

    function to request a value from the sensor

    :param st:
        pointer to state information for device
    :type st: struct cros_ec_sensors_core_state \*

    :param chan:
        channel specification structure table
    :type chan: struct iio_chan_spec const \*

    :param val:
        will contain one element making up the returned value
    :type val: int \*

    :param val2:
        will contain another element making up the returned value
    :type val2: int \*

    :param mask:
        specifies which values to be requested
    :type mask: long

.. _`cros_ec_sensors_core_read.return`:

Return
------

the type of value returned by the device

.. _`cros_ec_sensors_core_write`:

cros_ec_sensors_core_write
==========================

.. c:function:: int cros_ec_sensors_core_write(struct cros_ec_sensors_core_state *st, struct iio_chan_spec const *chan, int val, int val2, long mask)

    function to write a value to the sensor

    :param st:
        pointer to state information for device
    :type st: struct cros_ec_sensors_core_state \*

    :param chan:
        channel specification structure table
    :type chan: struct iio_chan_spec const \*

    :param val:
        first part of value to write
    :type val: int

    :param val2:
        second part of value to write
    :type val2: int

    :param mask:
        specifies which values to write
    :type mask: long

.. _`cros_ec_sensors_core_write.return`:

Return
------

the type of value returned by the device

.. This file was automatic generated / don't edit.

