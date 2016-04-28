.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-mmap-data-open:

======================
snd_pcm_mmap_data_open
======================

*man snd_pcm_mmap_data_open(9)*

*4.6.0-rc5*

increase the mmap counter


Synopsis
========

.. c:function:: void snd_pcm_mmap_data_open( struct vm_area_struct * area )

Arguments
=========

``area``
    VMA


Description
===========

PCM mmap callback should handle this counter properly


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
