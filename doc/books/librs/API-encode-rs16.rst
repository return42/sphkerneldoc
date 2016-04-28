.. -*- coding: utf-8; mode: rst -*-

.. _API-encode-rs16:

===========
encode_rs16
===========

*man encode_rs16(9)*

*4.6.0-rc5*

Calculate the parity for data values (16bit data width)


Synopsis
========

.. c:function:: int encode_rs16( struct rs_control * rs, uint16_t * data, int len, uint16_t * par, uint16_t invmsk )

Arguments
=========

``rs``
    the rs control structure

``data``
    data field of a given type

``len``
    data length

``par``
    parity data, must be initialized by caller (usually all 0)

``invmsk``
    invert data mask (will be xored on data, not on parity!)


Description
===========

Each field in the data array contains up to symbol size bits of valid
data.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
