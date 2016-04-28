.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-w1-family:

================
struct w1_family
================

*man struct w1_family(9)*

*4.6.0-rc5*

reference counted family structure.


Synopsis
========

.. code-block:: c

    struct w1_family {
      struct list_head family_entry;
      u8 fid;
      struct w1_family_ops * fops;
      atomic_t refcnt;
    };


Members
=======

family_entry
    family linked list

fid
    8 bit family identifier

fops
    operations for this family

refcnt
    reference counter


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
