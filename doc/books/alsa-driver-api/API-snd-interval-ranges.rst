
.. _API-snd-interval-ranges:

===================
snd_interval_ranges
===================

*man snd_interval_ranges(9)*

*4.6.0-rc1*

refine the interval value from the list of ranges


Synopsis
========

.. c:function:: int snd_interval_ranges( struct snd_interval * i, unsigned int count, const struct snd_interval * ranges, unsigned int mask )

Arguments
=========

``i``
    the interval value to refine

``count``
    the number of elements in the list of ranges

``ranges``
    the ranges list

``mask``
    the bit-mask to evaluate


Description
===========

Refines the interval value from the list of ranges. When mask is non-zero, only the elements corresponding to bit 1 are evaluated.


Return
======

Positive if the value is changed, zero if it's not changed, or a negative error code.
