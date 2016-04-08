
.. _API-regulator-bulk-disable:

======================
regulator_bulk_disable
======================

*man regulator_bulk_disable(9)*

*4.6.0-rc1*

disable multiple regulator consumers


Synopsis
========

.. c:function:: int regulator_bulk_disable( int num_consumers, struct regulator_bulk_data * consumers )

Arguments
=========

``num_consumers``
    Number of consumers

``consumers``
    Consumer data; clients are stored here. ``return`` 0 on success, an errno on failure


Description
===========

This convenience API allows consumers to disable multiple regulator clients in a single API call. If any consumers cannot be disabled then any others that were disabled will be
enabled again prior to return.
