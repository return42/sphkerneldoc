
.. _API-struct-regulator-bulk-data:

==========================
struct regulator_bulk_data
==========================

*man struct regulator_bulk_data(9)*

*4.6.0-rc1*

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
    The name of the supply. Initialised by the user before using the bulk regulator APIs.

optional
    The supply should be considered optional. Initialised by the user before using the bulk regulator APIs.

consumer
    The regulator consumer for the supply. This will be managed by the bulk API.


Description
===========

The regulator APIs provide a series of ``regulator_bulk_`` API calls as a convenience to consumers which require multiple supplies. This structure is used to manage data for these
calls.
