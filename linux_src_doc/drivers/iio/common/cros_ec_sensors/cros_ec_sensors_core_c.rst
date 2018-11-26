.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/common/cros_ec_sensors/cros_ec_sensors_core.c

.. _`cros_ec_sensors_idx_to_reg`:

cros_ec_sensors_idx_to_reg
==========================

.. c:function:: unsigned int cros_ec_sensors_idx_to_reg(struct cros_ec_sensors_core_state *st, unsigned int idx)

    convert index into offset in shared memory

    :param st:
        pointer to state information for device
    :type st: struct cros_ec_sensors_core_state \*

    :param idx:
        sensor index (should be element of enum sensor_index)
    :type idx: unsigned int

.. _`cros_ec_sensors_idx_to_reg.return`:

Return
------

address to read at

.. _`cros_ec_sensors_read_until_not_busy`:

cros_ec_sensors_read_until_not_busy
===================================

.. c:function:: int cros_ec_sensors_read_until_not_busy(struct cros_ec_sensors_core_state *st)

    read until is not busy

    :param st:
        pointer to state information for device
    :type st: struct cros_ec_sensors_core_state \*

.. _`cros_ec_sensors_read_until_not_busy.description`:

Description
-----------

Read from EC status byte until it reads not busy.

.. _`cros_ec_sensors_read_until_not_busy.return`:

Return
------

8-bit status if ok, -errno on failure.

.. _`cros_ec_sensors_read_data_unsafe`:

cros_ec_sensors_read_data_unsafe
================================

.. c:function:: int cros_ec_sensors_read_data_unsafe(struct iio_dev *indio_dev, unsigned long scan_mask, s16 *data)

    read acceleration data from EC shared memory

    :param indio_dev:
        pointer to IIO device
    :type indio_dev: struct iio_dev \*

    :param scan_mask:
        bitmap of the sensor indices to scan
    :type scan_mask: unsigned long

    :param data:
        location to store data
    :type data: s16 \*

.. _`cros_ec_sensors_read_data_unsafe.description`:

Description
-----------

This is the unsafe function for reading the EC data. It does not guarantee
that the EC will not modify the data as it is being read in.

.. _`cros_ec_sensors_read_data_unsafe.return`:

Return
------

0 on success, -errno on failure.

.. This file was automatic generated / don't edit.

