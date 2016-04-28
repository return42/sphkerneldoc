.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-input-handle:

===================
struct input_handle
===================

*man struct input_handle(9)*

*4.6.0-rc5*

links input device with an input handler


Synopsis
========

.. code-block:: c

    struct input_handle {
      void * private;
      int open;
      const char * name;
      struct input_dev * dev;
      struct input_handler * handler;
      struct list_head d_node;
      struct list_head h_node;
    };


Members
=======

private
    handler-specific data

open
    counter showing whether the handle is 'open', i.e. should deliver
    events from its device

name
    name given to the handle by handler that created it

dev
    input device the handle is attached to

handler
    handler that works with the device through this handle

d_node
    used to put the handle on device's list of attached handles

h_node
    used to put the handle on handler's list of handles from which it
    gets events


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
