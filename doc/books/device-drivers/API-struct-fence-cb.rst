
.. _API-struct-fence-cb:

===============
struct fence_cb
===============

*man struct fence_cb(9)*

*4.6.0-rc1*

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
    used by fence_add_callback to append this struct to fence::cb_list

func
    fence_func_t to call


Description
===========

This struct will be initialized by fence_add_callback, additional data can be passed along by embedding fence_cb in another struct.
