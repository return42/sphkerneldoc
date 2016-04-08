
.. _API-snd-pcm-mmap-data-close:

=======================
snd_pcm_mmap_data_close
=======================

*man snd_pcm_mmap_data_close(9)*

*4.6.0-rc1*

decrease the mmap counter


Synopsis
========

.. c:function:: void snd_pcm_mmap_data_close( struct vm_area_struct * area )

Arguments
=========

``area``
    VMA


Description
===========

PCM mmap callback should handle this counter properly
