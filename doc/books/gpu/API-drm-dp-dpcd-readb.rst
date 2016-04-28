.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-dp-dpcd-readb:

=================
drm_dp_dpcd_readb
=================

*man drm_dp_dpcd_readb(9)*

*4.6.0-rc5*

read a single byte from the DPCD


Synopsis
========

.. c:function:: ssize_t drm_dp_dpcd_readb( struct drm_dp_aux * aux, unsigned int offset, u8 * valuep )

Arguments
=========

``aux``
    DisplayPort AUX channel

``offset``
    address of the register to read

``valuep``
    location where the value of the register will be stored


Description
===========

Returns the number of bytes transferred (1) on success, or a negative
error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
