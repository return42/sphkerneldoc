.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-new-compress:

====================
snd_soc_new_compress
====================

*man snd_soc_new_compress(9)*

*4.6.0-rc5*

create a new compress.


Synopsis
========

.. c:function:: int snd_soc_new_compress( struct snd_soc_pcm_runtime * rtd, int num )

Arguments
=========

``rtd``
    The runtime for which we will create compress

``num``
    the device index number (zero based - shared with normal PCMs)


Return
======

0 for success, else error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
