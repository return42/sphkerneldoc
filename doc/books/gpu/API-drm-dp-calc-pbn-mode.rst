.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-dp-calc-pbn-mode:

====================
drm_dp_calc_pbn_mode
====================

*man drm_dp_calc_pbn_mode(9)*

*4.6.0-rc5*

Calculate the PBN for a mode.


Synopsis
========

.. c:function:: int drm_dp_calc_pbn_mode( int clock, int bpp )

Arguments
=========

``clock``
    dot clock for the mode

``bpp``
    bpp for the mode.


Description
===========

This uses the formula in the spec to calculate the PBN value for a mode.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
