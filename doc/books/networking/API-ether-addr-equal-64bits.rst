
.. _API-ether-addr-equal-64bits:

=======================
ether_addr_equal_64bits
=======================

*man ether_addr_equal_64bits(9)*

*4.6.0-rc1*

Compare two Ethernet addresses


Synopsis
========

.. c:function:: bool ether_addr_equal_64bits( const u8 addr1[6+2], const u8 addr2[6+2] )

Arguments
=========

``addr1[6+2]``
    Pointer to an array of 8 bytes

``addr2[6+2]``
    Pointer to an other array of 8 bytes


Description
===========

Compare two Ethernet addresses, returns true if equal, false otherwise.

The function doesn't need any conditional branches and possibly uses word memory accesses on CPU allowing cheap unaligned memory reads. arrays = { byte1, byte2, byte3, byte4,
byte5, byte6, pad1, pad2 }

Please note that alignment of addr1 & addr2 are only guaranteed to be 16 bits.
