
.. _API-iio-triggered-buffer-setup:

==========================
iio_triggered_buffer_setup
==========================

*man iio_triggered_buffer_setup(9)*

*4.6.0-rc1*

Setup triggered buffer and pollfunc


Synopsis
========

.. c:function:: int iio_triggered_buffer_setup( struct iio_dev * indio_dev, irqreturn_t (*h) int irq, void *p, irqreturn_t (*thread) int irq, void *p, const struct iio_buffer_setup_ops * setup_ops )

Arguments
=========

``indio_dev``
    IIO device structure

``h``
    Function which will be used as pollfunc top half

``thread``
    Function which will be used as pollfunc bottom half

``setup_ops``
    Buffer setup functions to use for this device. If NULL the default setup functions for triggered buffers will be used.


Description
===========

This function combines some common tasks which will normally be performed when setting up a triggered buffer. It will allocate the buffer and the pollfunc.

Before calling this function the indio_dev structure should already be completely initialized, but not yet registered. In practice this means that this function should be called
right before ``iio_device_register``.

To free the resources allocated by this function call ``iio_triggered_buffer_cleanup``.
