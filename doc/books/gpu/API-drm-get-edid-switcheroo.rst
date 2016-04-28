.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-get-edid-switcheroo:

=======================
drm_get_edid_switcheroo
=======================

*man drm_get_edid_switcheroo(9)*

*4.6.0-rc5*

get EDID data for a vga_switcheroo output


Synopsis
========

.. c:function:: struct edid * drm_get_edid_switcheroo( struct drm_connector * connector, struct i2c_adapter * adapter )

Arguments
=========

``connector``
    connector we're probing

``adapter``
    I2C adapter to use for DDC


Description
===========

Wrapper around ``drm_get_edid`` for laptops with dual GPUs using one set
of outputs. The wrapper adds the requisite vga_switcheroo calls to
temporarily switch DDC to the GPU which is retrieving EDID.


Return
======

Pointer to valid EDID or ``NULL`` if we couldn't find any.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
