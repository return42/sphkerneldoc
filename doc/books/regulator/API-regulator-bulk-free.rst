.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-bulk-free:

===================
regulator_bulk_free
===================

*man regulator_bulk_free(9)*

*4.6.0-rc5*

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

This convenience API allows consumers to free multiple regulator clients
in a single API call.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
