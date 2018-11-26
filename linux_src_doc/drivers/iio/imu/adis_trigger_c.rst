.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/imu/adis_trigger.c

.. _`adis_probe_trigger`:

adis_probe_trigger
==================

.. c:function:: int adis_probe_trigger(struct adis *adis, struct iio_dev *indio_dev)

    Sets up trigger for a adis device

    :param adis:
        The adis device
    :type adis: struct adis \*

    :param indio_dev:
        The IIO device
    :type indio_dev: struct iio_dev \*

.. _`adis_probe_trigger.description`:

Description
-----------

Returns 0 on success or a negative error code

\ :c:func:`adis_remove_trigger`\  should be used to free the trigger.

.. _`adis_remove_trigger`:

adis_remove_trigger
===================

.. c:function:: void adis_remove_trigger(struct adis *adis)

    Remove trigger for a adis devices

    :param adis:
        The adis device
    :type adis: struct adis \*

.. _`adis_remove_trigger.description`:

Description
-----------

Removes the trigger previously registered with \ :c:func:`adis_probe_trigger`\ .

.. This file was automatic generated / don't edit.

