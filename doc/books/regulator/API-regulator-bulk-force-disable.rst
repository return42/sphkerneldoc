.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-bulk-force-disable:

============================
regulator_bulk_force_disable
============================

*man regulator_bulk_force_disable(9)*

*4.6.0-rc5*

force disable multiple regulator consumers


Synopsis
========

.. c:function:: int regulator_bulk_force_disable( int num_consumers, struct regulator_bulk_data * consumers )

Arguments
=========

``num_consumers``
    Number of consumers

``consumers``
    Consumer data; clients are stored here. ``return`` 0 on success, an
    errno on failure


Description
===========

This convenience API allows consumers to forcibly disable multiple
regulator clients in a single API call.


NOTE
====

This should be used for situations when device damage will likely occur
if the regulators are not disabled (e.g. over temp). Although
regulator_force_disable function call for some consumers can return
error numbers, the function is called for all consumers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
