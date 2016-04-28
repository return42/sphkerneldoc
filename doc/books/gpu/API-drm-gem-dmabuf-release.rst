.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-dmabuf-release:

======================
drm_gem_dmabuf_release
======================

*man drm_gem_dmabuf_release(9)*

*4.6.0-rc5*

dma_buf release implementation for GEM


Synopsis
========

.. c:function:: void drm_gem_dmabuf_release( struct dma_buf * dma_buf )

Arguments
=========

``dma_buf``
    buffer to be released


Description
===========

Generic release function for dma_bufs exported as PRIME buffers. GEM
drivers must use this in their dma_buf ops structure as the release
callback.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
