
.. _API-regulator-bulk-get:

==================
regulator_bulk_get
==================

*man regulator_bulk_get(9)*

*4.6.0-rc1*

get multiple regulator consumers


Synopsis
========

.. c:function:: int regulator_bulk_get( struct device * dev, int num_consumers, struct regulator_bulk_data * consumers )

Arguments
=========

``dev``
    Device to supply

``num_consumers``
    Number of consumers to register

``consumers``
    Configuration of consumers; clients are stored here.


Description
===========

``return`` 0 on success, an errno on failure.

This helper function allows drivers to get several regulator consumers in one operation. If any of the regulators cannot be acquired then any regulators that were allocated will be
freed before returning to the caller.
