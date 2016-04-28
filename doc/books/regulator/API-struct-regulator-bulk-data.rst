.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-regulator-bulk-data:

==========================
struct regulator_bulk_data
==========================

*man struct regulator_bulk_data(9)*

*4.6.0-rc5*

Data used for bulk regulator operations.


Synopsis
========

.. code-block:: c

    struct regulator_bulk_data {
      const char * supply;
      bool optional;
      struct regulator * consumer;
    };


Members
=======

supply
    The name of the supply. Initialised by the user before using the
    bulk regulator APIs.

optional
    The supply should be considered optional. Initialised by the user
    before using the bulk regulator APIs.

consumer
    The regulator consumer for the supply. This will be managed by the
    bulk API.


Description
===========

The regulator APIs provide a series of ``regulator_bulk_`` API calls as
a convenience to consumers which require multiple supplies. This
structure is used to manage data for these calls.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
