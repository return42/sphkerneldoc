
.. _API-input-enable-softrepeat:

=======================
input_enable_softrepeat
=======================

*man input_enable_softrepeat(9)*

*4.6.0-rc1*

enable software autorepeat


Synopsis
========

.. c:function:: void input_enable_softrepeat( struct input_dev * dev, int delay, int period )

Arguments
=========

``dev``
    input device

``delay``
    repeat delay

``period``
    repeat period


Description
===========

Enable software autorepeat on the input device.
