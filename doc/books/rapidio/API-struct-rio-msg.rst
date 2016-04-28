.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-rio-msg:

==============
struct rio_msg
==============

*man struct rio_msg(9)*

*4.6.0-rc5*

RIO message event


Synopsis
========

.. code-block:: c

    struct rio_msg {
      struct resource * res;
      void (* mcback) (struct rio_mport * mport, void *dev_id, int mbox, int slot);
    };


Members
=======

res
    Mailbox resource

mcback
    Message event callback


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
