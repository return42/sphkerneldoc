.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-pwm-get:

============
devm_pwm_get
============

*man devm_pwm_get(9)*

*4.6.0-rc5*

resource managed ``pwm_get``


Synopsis
========

.. c:function:: struct pwm_device * devm_pwm_get( struct device * dev, const char * con_id )

Arguments
=========

``dev``
    device for PWM consumer

``con_id``
    consumer name


Description
===========

This function performs like ``pwm_get`` but the acquired PWM device will
automatically be released on driver detach.


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
