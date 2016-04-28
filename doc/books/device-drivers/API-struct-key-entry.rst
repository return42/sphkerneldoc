.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-key-entry:

================
struct key_entry
================

*man struct key_entry(9)*

*4.6.0-rc5*

keymap entry for use in sparse keymap


Synopsis
========

.. code-block:: c

    struct key_entry {
      int type;
      u32 code;
      union {unnamed_union};
    };


Members
=======

type
    Type of the key entry (KE_KEY, KE_SW, KE_VSW, KE_END); drivers
    are allowed to extend the list with their own private definitions.

code
    Device-specific data identifying the button/switch

{unnamed_union}
    anonymous


Description
===========

This structure defines an entry in a sparse keymap used by some input
devices for which traditional table-based approach is not suitable.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
