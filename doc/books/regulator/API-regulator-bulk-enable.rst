
.. _API-regulator-bulk-enable:

=====================
regulator_bulk_enable
=====================

*man regulator_bulk_enable(9)*

*4.6.0-rc1*

enable multiple regulator consumers


Synopsis
========

.. c:function:: int regulator_bulk_enable( int num_consumers, struct regulator_bulk_data * consumers )

Arguments
=========

``num_consumers``
    Number of consumers

``consumers``
    Consumer data; clients are stored here. ``return`` 0 on success, an errno on failure


Description
===========

This convenience API allows consumers to enable multiple regulator clients in a single API call. If any consumers cannot be enabled then any others that were enabled will be
disabled again prior to return.
