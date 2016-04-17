.. -*- coding: utf-8; mode: rst -*-

=============
adis_buffer.c
=============


.. _`adis_setup_buffer_and_trigger`:

adis_setup_buffer_and_trigger
=============================

.. c:function:: int adis_setup_buffer_and_trigger (struct adis *adis, struct iio_dev *indio_dev, irqreturn_t (*trigger_handler) (int, void *)

    Sets up buffer and trigger for the adis device

    :param struct adis \*adis:
        The adis device.

    :param struct iio_dev \*indio_dev:
        The IIO device.

    :param irqreturn_t (\*trigger_handler) (int, void \*):
        Optional trigger handler, may be NULL.



.. _`adis_setup_buffer_and_trigger.description`:

Description
-----------

Returns 0 on success, a negative error code otherwise.

This function sets up the buffer and trigger for a adis devices.  If
'trigger_handler' is NULL the default trigger handler will be used. The
default trigger handler will simply read the registers assigned to the
currently active channels.

:c:func:`adis_cleanup_buffer_and_trigger` should be called to free the resources
allocated by this function.



.. _`adis_cleanup_buffer_and_trigger`:

adis_cleanup_buffer_and_trigger
===============================

.. c:function:: void adis_cleanup_buffer_and_trigger (struct adis *adis, struct iio_dev *indio_dev)

    Free buffer and trigger resources

    :param struct adis \*adis:
        The adis device.

    :param struct iio_dev \*indio_dev:
        The IIO device.



.. _`adis_cleanup_buffer_and_trigger.description`:

Description
-----------

Frees resources allocated by :c:func:`adis_setup_buffer_and_trigger`

