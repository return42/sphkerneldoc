.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-check-dv-timings-fnc:

=========================
v4l2_check_dv_timings_fnc
=========================

*man v4l2_check_dv_timings_fnc(9)*

*4.6.0-rc5*

timings check callback


Synopsis
========

.. c:function:: typedef bool v4l2_check_dv_timings_fnc( const struct v4l2_dv_timings * t, void * handle )

Arguments
=========

``t``
    the v4l2_dv_timings struct.

``handle``
    a handle from the driver.


Description
===========

Returns true if the given timings are valid.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
