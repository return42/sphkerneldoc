
.. _API-drm-dp-calc-pbn-mode:

====================
drm_dp_calc_pbn_mode
====================

*man drm_dp_calc_pbn_mode(9)*

*4.6.0-rc1*

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
