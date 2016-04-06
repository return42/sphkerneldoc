
.. _API-input-mt-destroy-slots:

======================
input_mt_destroy_slots
======================

*man input_mt_destroy_slots(9)*

*4.6.0-rc1*

frees the MT slots of the input device


Synopsis
========

.. c:function:: void input_mt_destroy_slots( struct input_dev * dev )

Arguments
=========

``dev``
    input device with allocated MT slots


Description
===========

This function is only needed in error path as the input core will automatically free the MT slots when the device is destroyed.
