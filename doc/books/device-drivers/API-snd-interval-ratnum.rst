
.. _API-snd-interval-ratnum:

===================
snd_interval_ratnum
===================

*man snd_interval_ratnum(9)*

*4.6.0-rc1*

refine the interval value


Synopsis
========

.. c:function:: int snd_interval_ratnum( struct snd_interval * i, unsigned int rats_count, const struct snd_ratnum * rats, unsigned int * nump, unsigned int * denp )

Arguments
=========

``i``
    interval to refine

``rats_count``
    number of ratnum_t

``rats``
    ratnum_t array

``nump``
    pointer to store the resultant numerator

``denp``
    pointer to store the resultant denominator


Return
======

Positive if the value is changed, zero if it's not changed, or a negative error code.
