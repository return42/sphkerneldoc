
.. _API-snd-soc-new-compress:

====================
snd_soc_new_compress
====================

*man snd_soc_new_compress(9)*

*4.6.0-rc1*

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
