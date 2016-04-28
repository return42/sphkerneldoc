.. -*- coding: utf-8; mode: rst -*-

.. _API-decode-rs8:

==========
decode_rs8
==========

*man decode_rs8(9)*

*4.6.0-rc5*

Decode codeword (8bit data width)


Synopsis
========

.. c:function:: int decode_rs8( struct rs_control * rs, uint8_t * data, uint16_t * par, int len, uint16_t * s, int no_eras, int * eras_pos, uint16_t invmsk, uint16_t * corr )

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

The syndrome and parity uses a uint16_t data type to enable symbol size
> 8. The calling code must take care of decoding of the syndrome result
and the received parity before calling this code. Returns the number of
corrected bits or -EBADMSG for uncorrectable errors.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
