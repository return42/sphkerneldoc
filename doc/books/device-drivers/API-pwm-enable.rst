.. -*- coding: utf-8; mode: rst -*-

.. _API-pwm-enable:

==========
pwm_enable
==========

*man pwm_enable(9)*

*4.6.0-rc5*

start a PWM output toggling


Synopsis
========

.. c:function:: int pwm_enable( struct pwm_device * pwm )

Arguments
=========

``pwm``
    PWM device


Returns
=======

0 on success or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
