.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-sgbuf-ops-page:

======================
snd_pcm_sgbuf_ops_page
======================

*man snd_pcm_sgbuf_ops_page(9)*

*4.6.0-rc5*

get the page struct at the given offset


Synopsis
========

.. c:function:: struct page * snd_pcm_sgbuf_ops_page( struct snd_pcm_substream * substream, unsigned long offset )

Arguments
=========

``substream``
    the pcm substream instance

``offset``
    the buffer offset


Description
===========

Used as the page callback of PCM ops.


Return
======

The page struct at the given buffer offset. ``NULL`` on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
