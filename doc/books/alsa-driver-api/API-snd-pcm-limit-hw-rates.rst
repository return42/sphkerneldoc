.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-limit-hw-rates:

======================
snd_pcm_limit_hw_rates
======================

*man snd_pcm_limit_hw_rates(9)*

*4.6.0-rc5*

determine rate_min/rate_max fields


Synopsis
========

.. c:function:: int snd_pcm_limit_hw_rates( struct snd_pcm_runtime * runtime )

Arguments
=========

``runtime``
    the runtime instance


Description
===========

Determines the rate_min and rate_max fields from the rates bits of the
given runtime->hw.


Return
======

Zero if successful.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
