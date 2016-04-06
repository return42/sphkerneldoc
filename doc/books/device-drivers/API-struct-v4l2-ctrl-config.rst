
.. _API-struct-v4l2-ctrl-config:

=======================
struct v4l2_ctrl_config
=======================

*man struct v4l2_ctrl_config(9)*

*4.6.0-rc1*

Control configuration structure.


Synopsis
========

.. code-block:: c

    struct v4l2_ctrl_config {
      const struct v4l2_ctrl_ops * ops;
      const struct v4l2_ctrl_type_ops * type_ops;
      u32 id;
      const char * name;
      enum v4l2_ctrl_type type;
      s64 min;
      s64 max;
      u64 step;
      s64 def;
      u32 dims[V4L2_CTRL_MAX_DIMS];
      u32 elem_size;
      u32 flags;
      u64 menu_skip_mask;
      const char *const * qmenu;
      const s64 * qmenu_int;
      unsigned int is_private:1;
    };


Members
=======

ops
    The control ops.

type_ops
    The control type ops. Only needed for compound controls.

id
    The control ID.

name
    The control name.

type
    The control type.

min
    The control's minimum value.

max
    The control's maximum value.

step
    The control's step value for non-menu controls.

def
    The control's default value.

dims[V4L2_CTRL_MAX_DIMS]
    The size of each dimension.

elem_size
    The size in bytes of the control.

flags
    The control's flags.

menu_skip_mask
    The control's skip mask for menu controls. This makes it easy to skip menu items that are not valid. If bit X is set, then menu item X is skipped. Of course, this only works
    for menus with <= 64 menu items. There are no menus that come close to that number, so this is OK. Should we ever need more, then this will have to be extended to a bit array.

qmenu
    A const char ⋆ array for all menu items. Array entries that are empty strings ("") correspond to non-existing menu items (this is in addition to the menu_skip_mask above).
    The last entry must be NULL.

qmenu_int
    A const s64 integer array for all menu items of the type V4L2_CTRL_TYPE_INTEGER_MENU.

is_private
    If set, then this control is private to its handler and it will not be added to any other handlers.
