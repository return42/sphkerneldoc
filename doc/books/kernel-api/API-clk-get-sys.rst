
.. _API-clk-get-sys:

===========
clk_get_sys
===========

*man clk_get_sys(9)*

*4.6.0-rc1*

get a clock based upon the device name


Synopsis
========

.. c:function:: struct clk ⋆ clk_get_sys( const char * dev_id, const char * con_id )

Arguments
=========

``dev_id``
    device name

``con_id``
    connection ID


Description
===========

Returns a struct clk corresponding to the clock producer, or valid ``IS_ERR`` condition containing errno. The implementation uses ``dev_id`` and ``con_id`` to determine the clock
consumer, and thereby the clock producer. In contrast to ``clk_get`` this function takes the device name instead of the device itself for identification.

Drivers must assume that the clock source is not enabled.

clk_get_sys should not be called from within interrupt context.
