
.. _API-regulator-bulk-free:

===================
regulator_bulk_free
===================

*man regulator_bulk_free(9)*

*4.6.0-rc1*

free multiple regulator consumers


Synopsis
========

.. c:function:: void regulator_bulk_free( int num_consumers, struct regulator_bulk_data * consumers )

Arguments
=========

``num_consumers``
    Number of consumers

``consumers``
    Consumer data; clients are stored here.


Description
===========

This convenience API allows consumers to free multiple regulator clients in a single API call.
