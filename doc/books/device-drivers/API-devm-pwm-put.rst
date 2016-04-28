.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-pwm-put:

============
devm_pwm_put
============

*man devm_pwm_put(9)*

*4.6.0-rc5*

resource managed ``pwm_put``


Synopsis
========

.. c:function:: void devm_pwm_put( struct device * dev, struct pwm_device * pwm )

Arguments
=========

``dev``
    device for PWM consumer

``pwm``
    PWM device


Description
===========

Release a PWM previously allocated using ``devm_pwm_get``. Calling this
function is usually not needed because devm-allocated resources are
automatically released on driver detach.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
