.. -*- coding: utf-8; mode: rst -*-

.. _API-pwm-request:

===========
pwm_request
===========

*man pwm_request(9)*

*4.6.0-rc5*

request a PWM device


Synopsis
========

.. c:function:: struct pwm_device * pwm_request( int pwm, const char * label )

Arguments
=========

``pwm``
    global PWM device index

``label``
    PWM device label


Description
===========

This function is deprecated, use ``pwm_get`` instead.


Returns
=======

A pointer to a PWM device or an ``ERR_PTR``-encoded error code on
failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
