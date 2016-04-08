
.. _API-encode-rs8:

==========
encode_rs8
==========

*man encode_rs8(9)*

*4.6.0-rc1*

Calculate the parity for data values (8bit data width)


Synopsis
========

.. c:function:: int encode_rs8( struct rs_control * rs, uint8_t * data, int len, uint16_t * par, uint16_t invmsk )

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
    invert data mask (will be xored on data)


Description
===========

The parity uses a uint16_t data type to enable symbol size > 8. The calling code must take care of encoding of the syndrome result for storage itself.
