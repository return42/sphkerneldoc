.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-debug-obj:

================
struct debug_obj
================

*man struct debug_obj(9)*

*4.6.0-rc5*

representaion of an tracked object


Synopsis
========

.. code-block:: c

    struct debug_obj {
      struct hlist_node node;
      enum debug_obj_state state;
      unsigned int astate;
      void * object;
      struct debug_obj_descr * descr;
    };


Members
=======

node
    hlist node to link the object into the tracker list

state
    tracked object state

astate
    current active state

object
    pointer to the real object

descr
    pointer to an object type specific debug description structure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
