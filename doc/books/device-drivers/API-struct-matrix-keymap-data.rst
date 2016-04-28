.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-matrix-keymap-data:

=========================
struct matrix_keymap_data
=========================

*man struct matrix_keymap_data(9)*

*4.6.0-rc5*

keymap for matrix keyboards


Synopsis
========

.. code-block:: c

    struct matrix_keymap_data {
      const uint32_t * keymap;
      unsigned int keymap_size;
    };


Members
=======

keymap
    pointer to array of uint32 values encoded with ``KEY`` macro
    representing keymap

keymap_size
    number of entries (initialized) in this keymap


Description
===========

This structure is supposed to be used by platform code to supply keymaps
to drivers that implement matrix-like keypads/keyboards.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
