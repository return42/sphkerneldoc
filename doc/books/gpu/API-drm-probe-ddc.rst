.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-probe-ddc:

=============
drm_probe_ddc
=============

*man drm_probe_ddc(9)*

*4.6.0-rc5*

probe DDC presence


Synopsis
========

.. c:function:: bool drm_probe_ddc( struct i2c_adapter * adapter )

Arguments
=========

``adapter``
    I2C adapter to probe


Return
======

True on success, false on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
