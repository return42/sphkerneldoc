.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-pre-voltage-change-data:

==============================
struct pre_voltage_change_data
==============================

*man struct pre_voltage_change_data(9)*

*4.6.0-rc5*

Data sent with PRE_VOLTAGE_CHANGE event


Synopsis
========

.. code-block:: c

    struct pre_voltage_change_data {
      unsigned long old_uV;
      unsigned long min_uV;
      unsigned long max_uV;
    };


Members
=======

old_uV
    Current voltage before change.

min_uV
    Min voltage we'll change to.

max_uV
    Max voltage we'll change to.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
