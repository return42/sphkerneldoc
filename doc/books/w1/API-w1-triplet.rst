
.. _API-w1-triplet:

==========
w1_triplet
==========

*man w1_triplet(9)*

*4.6.0-rc1*

⋆ Does a triplet - used for searching ROM addresses.


Synopsis
========

.. c:function:: u8 w1_triplet( struct w1_master * dev, int bdir )

Arguments
=========

``dev``
    the master device

``bdir``
    the bit to write if both id_bit and comp_bit are 0


Return bits
===========

bit 0 = id_bit bit 1 = comp_bit bit 2 = dir_taken If both bits 0 & 1 are set, the search should be restarted.


Return
======

bit fields - see above
