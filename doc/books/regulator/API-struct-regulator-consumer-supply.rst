.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-regulator-consumer-supply:

================================
struct regulator_consumer_supply
================================

*man struct regulator_consumer_supply(9)*

*4.6.0-rc5*

supply -> device mapping


Synopsis
========

.. code-block:: c

    struct regulator_consumer_supply {
      const char * dev_name;
      const char * supply;
    };


Members
=======

dev_name
    Result of ``dev_name`` for the consumer.

supply
    Name for the supply.


Description
===========

This maps a supply name to a device. Use of dev_name allows support for
buses which make struct device available late such as I2C.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
