.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-media-intf-devnode:

=========================
struct media_intf_devnode
=========================

*man struct media_intf_devnode(9)*

*4.6.0-rc5*

A media interface via a device node.


Synopsis
========

.. code-block:: c

    struct media_intf_devnode {
      struct media_interface intf;
      u32 major;
      u32 minor;
    };


Members
=======

intf
    embedded interface object

major
    Major number of a device node

minor
    Minor number of a device node


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
