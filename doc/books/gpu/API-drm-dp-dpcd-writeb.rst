.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-dp-dpcd-writeb:

==================
drm_dp_dpcd_writeb
==================

*man drm_dp_dpcd_writeb(9)*

*4.6.0-rc5*

write a single byte to the DPCD


Synopsis
========

.. c:function:: ssize_t drm_dp_dpcd_writeb( struct drm_dp_aux * aux, unsigned int offset, u8 value )

Arguments
=========

``aux``
    DisplayPort AUX channel

``offset``
    address of the register to write

``value``
    value to write to the register


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
