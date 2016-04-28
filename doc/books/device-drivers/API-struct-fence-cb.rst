.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-fence-cb:

===============
struct fence_cb
===============

*man struct fence_cb(9)*

*4.6.0-rc5*

callback for fence_add_callback


Synopsis
========

.. code-block:: c

    struct fence_cb {
      struct list_head node;
      fence_func_t func;
    };


Members
=======

node
    used by fence_add_callback to append this struct to
    fence::cb_list

func
    fence_func_t to call


Description
===========

This struct will be initialized by fence_add_callback, additional data
can be passed along by embedding fence_cb in another struct.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
