
.. _API-struct-v4l2-ctrl-ref:

====================
struct v4l2_ctrl_ref
====================

*man struct v4l2_ctrl_ref(9)*

*4.6.0-rc1*

The control reference.


Synopsis
========

.. code-block:: c

    struct v4l2_ctrl_ref {
      struct list_head node;
      struct v4l2_ctrl_ref * next;
      struct v4l2_ctrl * ctrl;
      struct v4l2_ctrl_helper * helper;
    };


Members
=======

node
    List node for the sorted list.

next
    Single-link list node for the hash.

ctrl
    The actual control information.

helper
    Pointer to helper struct. Used internally in ``prepare_ext_ctrls``.


Description
===========

Each control handler has a list of these refs. The list_head is used to keep a sorted-by-control-ID list of all controls, while the next pointer is used to link the control in the
hash's bucket.
