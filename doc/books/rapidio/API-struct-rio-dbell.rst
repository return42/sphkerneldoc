.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-rio-dbell:

================
struct rio_dbell
================

*man struct rio_dbell(9)*

*4.6.0-rc5*

RIO doorbell event


Synopsis
========

.. code-block:: c

    struct rio_dbell {
      struct list_head node;
      struct resource * res;
      void (* dinb) (struct rio_mport *mport, void *dev_id, u16 src, u16 dst, u16 info);
      void * dev_id;
    };


Members
=======

node
    Node in list of doorbell events

res
    Doorbell resource

dinb
    Doorbell event callback

dev_id
    Device specific pointer to pass on event


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
