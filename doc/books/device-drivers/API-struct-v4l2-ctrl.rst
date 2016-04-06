
.. _API-struct-v4l2-ctrl:

================
struct v4l2_ctrl
================

*man struct v4l2_ctrl(9)*

*4.6.0-rc1*

The control structure.


Synopsis
========

.. code-block:: c

    struct v4l2_ctrl {
      struct list_head node;
      struct list_head ev_subs;
      struct v4l2_ctrl_handler * handler;
      struct v4l2_ctrl ** cluster;
      unsigned ncontrols;
      unsigned int done:1;
      unsigned int is_new:1;
      unsigned int has_changed:1;
      unsigned int is_private:1;
      unsigned int is_auto:1;
      unsigned int is_int:1;
      unsigned int is_string:1;
      unsigned int is_ptr:1;
      unsigned int is_array:1;
      unsigned int has_volatiles:1;
      unsigned int call_notify:1;
      unsigned int manual_mode_value:8;
      const struct v4l2_ctrl_ops * ops;
      const struct v4l2_ctrl_type_ops * type_ops;
      u32 id;
      const char * name;
      enum v4l2_ctrl_type type;
      s64 minimum;
      s64 maximum;
      s64 default_value;
      u32 elems;
      u32 elem_size;
      u32 dims[V4L2_CTRL_MAX_DIMS];
      u32 nr_of_dims;
      union cur;
      union v4l2_ctrl_ptr p_new;
      union v4l2_ctrl_ptr p_cur;
    };


Members
=======

node
    The list node.

ev_subs
    The list of control event subscriptions.

handler
    The handler that owns the control.

cluster
    Point to start of cluster array.

ncontrols
    Number of controls in cluster array.

done
    Internal flag: set for each processed control.

is_new
    Set when the user specified a new value for this control. It is also set when called from v4l2_ctrl_handler_setup. Drivers should never set this flag.

has_changed
    Set when the current value differs from the new value. Drivers should never use this flag.

is_private
    If set, then this control is private to its handler and it will not be added to any other handlers. Drivers can set this flag.

is_auto
    If set, then this control selects whether the other cluster members are in 'automatic' mode or 'manual' mode. This is used for autogain/gain type clusters. Drivers should never
    set this flag directly.

is_int
    If set, then this control has a simple integer value (i.e. it uses ctrl->val).

is_string
    If set, then this control has type V4L2_CTRL_TYPE_STRING.

is_ptr
    If set, then this control is an array and/or has type >= V4L2_CTRL_COMPOUND_TYPES and/or has type V4L2_CTRL_TYPE_STRING. In other words, struct v4l2_ext_control uses
    field p to point to the data.

is_array
    If set, then this control contains an N-dimensional array.

has_volatiles
    If set, then one or more members of the cluster are volatile. Drivers should never touch this flag.

call_notify
    If set, then call the handler's notify function whenever the control's value changes.

manual_mode_value
    If the is_auto flag is set, then this is the value of the auto control that determines if that control is in manual mode. So if the value of the auto control equals this
    value, then the whole cluster is in manual mode. Drivers should never set this flag directly.

ops
    The control ops.

type_ops
    The control type ops.

id
    The control ID.

name
    The control name.

type
    The control type.

minimum
    The control's minimum value.

maximum
    The control's maximum value.

default_value
    The control's default value.

elems
    The number of elements in the N-dimensional array.

elem_size
    The size in bytes of the control.

dims[V4L2_CTRL_MAX_DIMS]
    The size of each dimension.

nr_of_dims
    The number of dimensions in ``dims``.

cur
    The control's current value.

p_new
    The control's new value represented via an union with provides a standard way of accessing control types through a pointer.

p_cur
    The control's current value represented via an union with provides a standard way of accessing control types through a pointer.
