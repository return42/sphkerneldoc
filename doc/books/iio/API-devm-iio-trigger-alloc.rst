
.. _API-devm-iio-trigger-alloc:

======================
devm_iio_trigger_alloc
======================

*man devm_iio_trigger_alloc(9)*

*4.6.0-rc1*

Resource-managed ``iio_trigger_alloc``


Synopsis
========

.. c:function:: struct iio_trigger ⋆ devm_iio_trigger_alloc( struct device * dev, const char * fmt, ... )

Arguments
=========

``dev``
    Device to allocate iio_trigger for

``fmt``
    trigger name format. If it includes format specifiers, the additional arguments following format are formatted and inserted in the resulting string replacing their respective
    specifiers.

``...``
    variable arguments


Description
===========

Managed iio_trigger_alloc. iio_trigger allocated with this function is automatically freed on driver detach.

If an iio_trigger allocated with this function needs to be freed separately, ``devm_iio_trigger_free`` must be used.


RETURNS
=======

Pointer to allocated iio_trigger on success, NULL on failure.
