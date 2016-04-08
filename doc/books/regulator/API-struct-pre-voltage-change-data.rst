
.. _API-struct-pre-voltage-change-data:

==============================
struct pre_voltage_change_data
==============================

*man struct pre_voltage_change_data(9)*

*4.6.0-rc1*

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
