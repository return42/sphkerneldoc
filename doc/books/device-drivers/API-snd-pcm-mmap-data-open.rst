
.. _API-snd-pcm-mmap-data-open:

======================
snd_pcm_mmap_data_open
======================

*man snd_pcm_mmap_data_open(9)*

*4.6.0-rc1*

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
