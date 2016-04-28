.. -*- coding: utf-8; mode: rst -*-

.. _API-pwm-can-sleep:

=============
pwm_can_sleep
=============

*man pwm_can_sleep(9)*

*4.6.0-rc5*

report whether PWM access will sleep


Synopsis
========

.. c:function:: bool pwm_can_sleep( struct pwm_device * pwm )

Arguments
=========

``pwm``
    PWM device


Returns
=======

True if accessing the PWM can sleep, false otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
