.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-rio-scan:

===============
struct rio_scan
===============

*man struct rio_scan(9)*

*4.6.0-rc5*

RIO enumeration and discovery operations


Synopsis
========

.. code-block:: c

    struct rio_scan {
      struct module * owner;
      int (* enumerate) (struct rio_mport *mport, u32 flags);
      int (* discover) (struct rio_mport *mport, u32 flags);
    };


Members
=======

owner
    The module owner of this structure

enumerate
    Callback to perform RapidIO fabric enumeration.

discover
    Callback to perform RapidIO fabric discovery.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
