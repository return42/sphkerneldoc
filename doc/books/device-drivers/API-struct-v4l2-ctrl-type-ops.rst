
.. _API-struct-v4l2-ctrl-type-ops:

=========================
struct v4l2_ctrl_type_ops
=========================

*man struct v4l2_ctrl_type_ops(9)*

*4.6.0-rc1*

The control type operations that the driver has to provide.


Synopsis
========

.. code-block:: c

    struct v4l2_ctrl_type_ops {
      bool (* equal) (const struct v4l2_ctrl *ctrl, u32 idx,union v4l2_ctrl_ptr ptr1,union v4l2_ctrl_ptr ptr2);
      void (* init) (const struct v4l2_ctrl *ctrl, u32 idx,union v4l2_ctrl_ptr ptr);
      void (* log) (const struct v4l2_ctrl *ctrl);
      int (* validate) (const struct v4l2_ctrl *ctrl, u32 idx,union v4l2_ctrl_ptr ptr);
    };


Members
=======

equal
    return true if both values are equal.

init
    initialize the value.

log
    log the value.

validate
    validate the value. Return 0 on success and a negative value otherwise.
