
.. _API-snd-interval-refine:

===================
snd_interval_refine
===================

*man snd_interval_refine(9)*

*4.6.0-rc1*

refine the interval value of configurator


Synopsis
========

.. c:function:: int snd_interval_refine( struct snd_interval * i, const struct snd_interval * v )

Arguments
=========

``i``
    the interval value to refine

``v``
    the interval value to refer to


Description
===========

Refines the interval value with the reference value. The interval is changed to the range satisfying both intervals. The interval status (min, max, integer, etc.) are evaluated.


Return
======

Positive if the value is changed, zero if it's not changed, or a negative error code.
