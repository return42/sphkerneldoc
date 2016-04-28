.. -*- coding: utf-8; mode: rst -*-

.. _API-decode-rs16:

===========
decode_rs16
===========

*man decode_rs16(9)*

*4.6.0-rc5*

Decode codeword (16bit data width)


Synopsis
========

.. c:function:: int decode_rs16( struct rs_control * rs, uint16_t * data, uint16_t * par, int len, uint16_t * s, int no_eras, int * eras_pos, uint16_t invmsk, uint16_t * corr )

Arguments
=========

``rs``
    the rs control structure

``data``
    data field of a given type

``par``
    received parity data field

``len``
    data length

``s``
    syndrome data field (if NULL, syndrome is calculated)

``no_eras``
    number of erasures

``eras_pos``
    position of erasures, can be NULL

``invmsk``
    invert data mask (will be xored on data, not on parity!)

``corr``
    buffer to store correction bitmask on eras_pos


Description
===========

Each field in the data array contains up to symbol size bits of valid
data. Returns the number of corrected bits or -EBADMSG for uncorrectable
errors.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
