
.. _API-snd-interval-list:

=================
snd_interval_list
=================

*man snd_interval_list(9)*

*4.6.0-rc1*

refine the interval value from the list


Synopsis
========

.. c:function:: int snd_interval_list( struct snd_interval * i, unsigned int count, const unsigned int * list, unsigned int mask )

Arguments
=========

``i``
    the interval value to refine

``count``
    the number of elements in the list

``list``
    the value list

``mask``
    the bit-mask to evaluate


Description
===========

Refines the interval value from the list. When mask is non-zero, only the elements corresponding to bit 1 are evaluated.


Return
======

Positive if the value is changed, zero if it's not changed, or a negative error code.
