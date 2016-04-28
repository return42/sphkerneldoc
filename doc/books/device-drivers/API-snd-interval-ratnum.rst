.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-interval-ratnum:

===================
snd_interval_ratnum
===================

*man snd_interval_ratnum(9)*

*4.6.0-rc5*

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

Positive if the value is changed, zero if it's not changed, or a
negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
