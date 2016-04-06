
.. _API-struct-matrix-keymap-data:

=========================
struct matrix_keymap_data
=========================

*man struct matrix_keymap_data(9)*

*4.6.0-rc1*

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
    pointer to array of uint32 values encoded with ``KEY`` macro representing keymap

keymap_size
    number of entries (initialized) in this keymap


Description
===========

This structure is supposed to be used by platform code to supply keymaps to drivers that implement matrix-like keypads/keyboards.
