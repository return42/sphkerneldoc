.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-vb2-io-modes:

=================
enum vb2_io_modes
=================

*man enum vb2_io_modes(9)*

*4.6.0-rc5*

queue access methods


Synopsis
========

.. code-block:: c

    enum vb2_io_modes {
      VB2_MMAP,
      VB2_USERPTR,
      VB2_READ,
      VB2_WRITE,
      VB2_DMABUF
    };


Constants
=========

VB2_MMAP
    driver supports MMAP with streaming API

VB2_USERPTR
    driver supports USERPTR with streaming API

VB2_READ
    driver supports ``read`` style access

VB2_WRITE
    driver supports ``write`` style access

VB2_DMABUF
    driver supports DMABUF with streaming API


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
