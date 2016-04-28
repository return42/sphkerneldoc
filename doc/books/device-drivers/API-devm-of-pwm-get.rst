.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-of-pwm-get:

===============
devm_of_pwm_get
===============

*man devm_of_pwm_get(9)*

*4.6.0-rc5*

resource managed ``of_pwm_get``


Synopsis
========

.. c:function:: struct pwm_device * devm_of_pwm_get( struct device * dev, struct device_node * np, const char * con_id )

Arguments
=========

``dev``
    device for PWM consumer

``np``
    device node to get the PWM from

``con_id``
    consumer name


Description
===========

This function performs like ``of_pwm_get`` but the acquired PWM device
will automatically be released on driver detach.


Returns
=======

A pointer to the requested PWM device or an ``ERR_PTR``-encoded error
code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
