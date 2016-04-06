
.. _API-input-set-capability:

====================
input_set_capability
====================

*man input_set_capability(9)*

*4.6.0-rc1*

mark device as capable of a certain event


Synopsis
========

.. c:function:: void input_set_capability( struct input_dev * dev, unsigned int type, unsigned int code )

Arguments
=========

``dev``
    device that is capable of emitting or accepting event

``type``
    type of the event (EV_KEY, EV_REL, etc...)

``code``
    event code


Description
===========

In addition to setting up corresponding bit in appropriate capability bitmap the function also adjusts dev->evbit.
