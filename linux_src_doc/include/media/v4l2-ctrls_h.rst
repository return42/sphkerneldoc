.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-ctrls.h

.. _`v4l2_ctrl_ptr`:

union v4l2_ctrl_ptr
===================

.. c:type:: struct v4l2_ctrl_ptr

    A pointer to a control value.

.. _`v4l2_ctrl_ptr.definition`:

Definition
----------

.. code-block:: c

    union v4l2_ctrl_ptr {
        s32 *p_s32;
        s64 *p_s64;
        u8 *p_u8;
        u16 *p_u16;
        u32 *p_u32;
        char *p_char;
        struct v4l2_ctrl_mpeg2_slice_params *p_mpeg2_slice_params;
        struct v4l2_ctrl_mpeg2_quantization *p_mpeg2_quantization;
        void *p;
    }

.. _`v4l2_ctrl_ptr.members`:

Members
-------

p_s32
    Pointer to a 32-bit signed value.

p_s64
    Pointer to a 64-bit signed value.

p_u8
    Pointer to a 8-bit unsigned value.

p_u16
    Pointer to a 16-bit unsigned value.

p_u32
    Pointer to a 32-bit unsigned value.

p_char
    Pointer to a string.

p_mpeg2_slice_params
    Pointer to a MPEG2 slice parameters structure.

p_mpeg2_quantization
    Pointer to a MPEG2 quantization data structure.

p
    Pointer to a compound value.

.. _`v4l2_ctrl_ops`:

struct v4l2_ctrl_ops
====================

.. c:type:: struct v4l2_ctrl_ops

    The control operations that the driver has to provide.

.. _`v4l2_ctrl_ops.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_ctrl_ops {
        int (*g_volatile_ctrl)(struct v4l2_ctrl *ctrl);
        int (*try_ctrl)(struct v4l2_ctrl *ctrl);
        int (*s_ctrl)(struct v4l2_ctrl *ctrl);
    }

.. _`v4l2_ctrl_ops.members`:

Members
-------

g_volatile_ctrl
    Get a new value for this control. Generally only relevant
    for volatile (and usually read-only) controls such as a control
    that returns the current signal strength which changes
    continuously.
    If not set, then the currently cached value will be returned.

try_ctrl
    Test whether the control's value is valid. Only relevant when
    the usual min/max/step checks are not sufficient.

s_ctrl
    Actually set the new control value. s_ctrl is compulsory. The
    ctrl->handler->lock is held when these ops are called, so no
    one else can access controls owned by that handler.

.. _`v4l2_ctrl_type_ops`:

struct v4l2_ctrl_type_ops
=========================

.. c:type:: struct v4l2_ctrl_type_ops

    The control type operations that the driver has to provide.

.. _`v4l2_ctrl_type_ops.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_ctrl_type_ops {
        bool (*equal)(const struct v4l2_ctrl *ctrl, u32 idx,union v4l2_ctrl_ptr ptr1, union v4l2_ctrl_ptr ptr2);
        void (*init)(const struct v4l2_ctrl *ctrl, u32 idx, union v4l2_ctrl_ptr ptr);
        void (*log)(const struct v4l2_ctrl *ctrl);
        int (*validate)(const struct v4l2_ctrl *ctrl, u32 idx, union v4l2_ctrl_ptr ptr);
    }

.. _`v4l2_ctrl_type_ops.members`:

Members
-------

equal
    return true if both values are equal.

init
    initialize the value.

log
    log the value.

validate
    validate the value. Return 0 on success and a negative value
    otherwise.

.. _`v4l2_ctrl_notify_fnc`:

v4l2_ctrl_notify_fnc
====================

.. c:function:: void v4l2_ctrl_notify_fnc(struct v4l2_ctrl *ctrl, void *priv)

    typedef for a notify argument with a function that should be called when a control value has changed.

    :param ctrl:
        pointer to struct \ :c:type:`struct v4l2_ctrl <v4l2_ctrl>`\ 
    :type ctrl: struct v4l2_ctrl \*

    :param priv:
        control private data
    :type priv: void \*

.. _`v4l2_ctrl_notify_fnc.description`:

Description
-----------

This typedef definition is used as an argument to \ :c:func:`v4l2_ctrl_notify`\ 
and as an argument at struct \ :c:type:`struct v4l2_ctrl_handler <v4l2_ctrl_handler>`\ .

.. _`v4l2_ctrl`:

struct v4l2_ctrl
================

.. c:type:: struct v4l2_ctrl

    The control structure.

.. _`v4l2_ctrl.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_ctrl {
        struct list_head node;
        struct list_head ev_subs;
        struct v4l2_ctrl_handler *handler;
        struct v4l2_ctrl **cluster;
        unsigned int ncontrols;
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
        const struct v4l2_ctrl_ops *ops;
        const struct v4l2_ctrl_type_ops *type_ops;
        u32 id;
        const char *name;
        enum v4l2_ctrl_type type;
        s64 minimum, maximum, default_value;
        u32 elems;
        u32 elem_size;
        u32 dims[V4L2_CTRL_MAX_DIMS];
        u32 nr_of_dims;
        union {
            u64 step;
            u64 menu_skip_mask;
        } ;
        union {
            const char * const *qmenu;
            const s64 *qmenu_int;
        } ;
        unsigned long flags;
        void *priv;
        s32 val;
        struct {
            s32 val;
        } cur;
        union v4l2_ctrl_ptr p_new;
        union v4l2_ctrl_ptr p_cur;
    }

.. _`v4l2_ctrl.members`:

Members
-------

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
    Set when the user specified a new value for this control. It
    is also set when called from \ :c:func:`v4l2_ctrl_handler_setup`\ . Drivers
    should never set this flag.

has_changed
    Set when the current value differs from the new value. Drivers
    should never use this flag.

is_private
    If set, then this control is private to its handler and it
    will not be added to any other handlers. Drivers can set
    this flag.

is_auto
    If set, then this control selects whether the other cluster
    members are in 'automatic' mode or 'manual' mode. This is
    used for autogain/gain type clusters. Drivers should never
    set this flag directly.

is_int
    If set, then this control has a simple integer value (i.e. it
    uses ctrl->val).

is_string
    If set, then this control has type \ ``V4L2_CTRL_TYPE_STRING``\ .

is_ptr
    If set, then this control is an array and/or has type >=
    \ ``V4L2_CTRL_COMPOUND_TYPES``\ 
    and/or has type \ ``V4L2_CTRL_TYPE_STRING``\ . In other words, \ :c:type:`struct struct <struct>`\ 
    v4l2_ext_control uses field p to point to the data.

is_array
    If set, then this control contains an N-dimensional array.

has_volatiles
    If set, then one or more members of the cluster are volatile.
    Drivers should never touch this flag.

call_notify
    If set, then call the handler's notify function whenever the
    control's value changes.

manual_mode_value
    If the is_auto flag is set, then this is the value
    of the auto control that determines if that control is in
    manual mode. So if the value of the auto control equals this
    value, then the whole cluster is in manual mode. Drivers should
    never set this flag directly.

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

dims
    The size of each dimension.

nr_of_dims
    The number of dimensions in \ ``dims``\ .

{unnamed_union}
    anonymous

step
    The control's step value for non-menu controls.

menu_skip_mask
    The control's skip mask for menu controls. This makes it
    easy to skip menu items that are not valid. If bit X is set,
    then menu item X is skipped. Of course, this only works for
    menus with <= 32 menu items. There are no menus that come
    close to that number, so this is OK. Should we ever need more,
    then this will have to be extended to a u64 or a bit array.

{unnamed_union}
    anonymous

qmenu
    A const char * array for all menu items. Array entries that are
    empty strings ("") correspond to non-existing menu items (this
    is in addition to the menu_skip_mask above). The last entry
    must be NULL.
    Used only if the \ ``type``\  is \ ``V4L2_CTRL_TYPE_MENU``\ .

qmenu_int
    A 64-bit integer array for with integer menu items.
    The size of array must be equal to the menu size, e. g.:
    :math:`ceil(\frac{maximum - minimum}{step}) + 1`.
    Used only if the \ ``type``\  is \ ``V4L2_CTRL_TYPE_INTEGER_MENU``\ .

flags
    The control's flags.

priv
    The control's private pointer. For use by the driver. It is
    untouched by the control framework. Note that this pointer is
    not freed when the control is deleted. Should this be needed
    then a new internal bitfield can be added to tell the framework
    to free this pointer.

val
    The control's new s32 value.

cur
    Structure to store the current value.

cur.val
    The control's current value, if the \ ``type``\  is represented via
    a u32 integer (see \ :c:type:`enum v4l2_ctrl_type <v4l2_ctrl_type>`\ ).

p_new
    The control's new value represented via a union which provides
    a standard way of accessing control types
    through a pointer.

p_cur
    The control's current value represented via a union which
    provides a standard way of accessing control types
    through a pointer.

.. _`v4l2_ctrl_ref`:

struct v4l2_ctrl_ref
====================

.. c:type:: struct v4l2_ctrl_ref

    The control reference.

.. _`v4l2_ctrl_ref.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_ctrl_ref {
        struct list_head node;
        struct v4l2_ctrl_ref *next;
        struct v4l2_ctrl *ctrl;
        struct v4l2_ctrl_helper *helper;
        bool from_other_dev;
        bool req_done;
        struct v4l2_ctrl_ref *req;
        union v4l2_ctrl_ptr p_req;
    }

.. _`v4l2_ctrl_ref.members`:

Members
-------

node
    List node for the sorted list.

next
    Single-link list node for the hash.

ctrl
    The actual control information.

helper
    Pointer to helper struct. Used internally in
    ``prepare_ext_ctrls`` function at ``v4l2-ctrl.c``.

from_other_dev
    If true, then \ ``ctrl``\  was defined in another
    device than the \ :c:type:`struct v4l2_ctrl_handler <v4l2_ctrl_handler>`\ .

req_done
    Internal flag: if the control handler containing this control
    reference is bound to a media request, then this is set when
    the control has been applied. This prevents applying controls
    from a cluster with multiple controls twice (when the first
    control of a cluster is applied, they all are).

req
    If set, this refers to another request that sets this control.

p_req
    If the control handler containing this control reference
    is bound to a media request, then this points to the
    value of the control that should be applied when the request
    is executed, or to the value of the control at the time
    that the request was completed.

.. _`v4l2_ctrl_ref.description`:

Description
-----------

Each control handler has a list of these refs. The list_head is used to
keep a sorted-by-control-ID list of all controls, while the next pointer
is used to link the control in the hash's bucket.

.. _`v4l2_ctrl_handler`:

struct v4l2_ctrl_handler
========================

.. c:type:: struct v4l2_ctrl_handler

    The control handler keeps track of all the controls: both the controls owned by the handler and those inherited from other handlers.

.. _`v4l2_ctrl_handler.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_ctrl_handler {
        struct mutex _lock;
        struct mutex *lock;
        struct list_head ctrls;
        struct list_head ctrl_refs;
        struct v4l2_ctrl_ref *cached;
        struct v4l2_ctrl_ref **buckets;
        v4l2_ctrl_notify_fnc notify;
        void *notify_priv;
        u16 nr_of_buckets;
        int error;
        bool request_is_queued;
        struct list_head requests;
        struct list_head requests_queued;
        struct media_request_object req_obj;
    }

.. _`v4l2_ctrl_handler.members`:

Members
-------

_lock
    Default for "lock".

lock
    Lock to control access to this handler and its controls.
    May be replaced by the user right after init.

ctrls
    The list of controls owned by this handler.

ctrl_refs
    The list of control references.

cached
    The last found control reference. It is common that the same
    control is needed multiple times, so this is a simple
    optimization.

buckets
    Buckets for the hashing. Allows for quick control lookup.

notify
    A notify callback that is called whenever the control changes
    value.
    Note that the handler's lock is held when the notify function
    is called!

notify_priv
    Passed as argument to the v4l2_ctrl notify callback.

nr_of_buckets
    Total number of buckets in the array.

error
    The error code of the first failed control addition.

request_is_queued
    True if the request was queued.

requests
    List to keep track of open control handler request objects.
    For the parent control handler (@req_obj.req == NULL) this
    is the list header. When the parent control handler is
    removed, it has to unbind and put all these requests since
    they refer to the parent.

requests_queued
    List of the queued requests. This determines the order
    in which these controls are applied. Once the request is
    completed it is removed from this list.

req_obj
    The \ :c:type:`struct media_request_object <media_request_object>`\ , used to link into a
    \ :c:type:`struct media_request <media_request>`\ . This request object has a refcount.

.. _`v4l2_ctrl_config`:

struct v4l2_ctrl_config
=======================

.. c:type:: struct v4l2_ctrl_config

    Control configuration structure.

.. _`v4l2_ctrl_config.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_ctrl_config {
        const struct v4l2_ctrl_ops *ops;
        const struct v4l2_ctrl_type_ops *type_ops;
        u32 id;
        const char *name;
        enum v4l2_ctrl_type type;
        s64 min;
        s64 max;
        u64 step;
        s64 def;
        u32 dims[V4L2_CTRL_MAX_DIMS];
        u32 elem_size;
        u32 flags;
        u64 menu_skip_mask;
        const char * const *qmenu;
        const s64 *qmenu_int;
        unsigned int is_private:1;
    }

.. _`v4l2_ctrl_config.members`:

Members
-------

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

dims
    The size of each dimension.

elem_size
    The size in bytes of the control.

flags
    The control's flags.

menu_skip_mask
    The control's skip mask for menu controls. This makes it
    easy to skip menu items that are not valid. If bit X is set,
    then menu item X is skipped. Of course, this only works for
    menus with <= 64 menu items. There are no menus that come
    close to that number, so this is OK. Should we ever need more,
    then this will have to be extended to a bit array.

qmenu
    A const char * array for all menu items. Array entries that are
    empty strings ("") correspond to non-existing menu items (this
    is in addition to the menu_skip_mask above). The last entry
    must be NULL.

qmenu_int
    A const s64 integer array for all menu items of the type
    V4L2_CTRL_TYPE_INTEGER_MENU.

is_private
    If set, then this control is private to its handler and it
    will not be added to any other handlers.

.. _`v4l2_ctrl_fill`:

v4l2_ctrl_fill
==============

.. c:function:: void v4l2_ctrl_fill(u32 id, const char **name, enum v4l2_ctrl_type *type, s64 *min, s64 *max, u64 *step, s64 *def, u32 *flags)

    Fill in the control fields based on the control ID.

    :param id:
        ID of the control
    :type id: u32

    :param name:
        pointer to be filled with a string with the name of the control
    :type name: const char \*\*

    :param type:
        pointer for storing the type of the control
    :type type: enum v4l2_ctrl_type \*

    :param min:
        pointer for storing the minimum value for the control
    :type min: s64 \*

    :param max:
        pointer for storing the maximum value for the control
    :type max: s64 \*

    :param step:
        pointer for storing the control step
    :type step: u64 \*

    :param def:
        pointer for storing the default value for the control
    :type def: s64 \*

    :param flags:
        pointer for storing the flags to be used on the control
    :type flags: u32 \*

.. _`v4l2_ctrl_fill.description`:

Description
-----------

This works for all standard V4L2 controls.
For non-standard controls it will only fill in the given arguments
and \ ``name``\  content will be set to \ ``NULL``\ .

This function will overwrite the contents of \ ``name``\ , \ ``type``\  and \ ``flags``\ .
The contents of \ ``min``\ , \ ``max``\ , \ ``step``\  and \ ``def``\  may be modified depending on
the type.

.. note::

   Do not use in drivers! It is used internally for backwards compatibility
   control handling only. Once all drivers are converted to use the new
   control framework this function will no longer be exported.

.. _`v4l2_ctrl_handler_init_class`:

v4l2_ctrl_handler_init_class
============================

.. c:function:: int v4l2_ctrl_handler_init_class(struct v4l2_ctrl_handler *hdl, unsigned int nr_of_controls_hint, struct lock_class_key *key, const char *name)

    Initialize the control handler.

    :param hdl:
        The control handler.
    :type hdl: struct v4l2_ctrl_handler \*

    :param nr_of_controls_hint:
        A hint of how many controls this handler is
        expected to refer to. This is the total number, so including
        any inherited controls. It doesn't have to be precise, but if
        it is way off, then you either waste memory (too many buckets
        are allocated) or the control lookup becomes slower (not enough
        buckets are allocated, so there are more slow list lookups).
        It will always work, though.
    :type nr_of_controls_hint: unsigned int

    :param key:
        Used by the lock validator if CONFIG_LOCKDEP is set.
    :type key: struct lock_class_key \*

    :param name:
        Used by the lock validator if CONFIG_LOCKDEP is set.
    :type name: const char \*

.. _`v4l2_ctrl_handler_init_class.description`:

Description
-----------

.. attention::

   Never use this call directly, always use the v4l2_ctrl_handler_init()
   macro that hides the @key and @name arguments.

.. _`v4l2_ctrl_handler_init_class.return`:

Return
------

returns an error if the buckets could not be allocated. This
error will also be stored in \ ``hdl->error``\ .

.. _`v4l2_ctrl_handler_init`:

v4l2_ctrl_handler_init
======================

.. c:function::  v4l2_ctrl_handler_init( hdl,  nr_of_controls_hint)

    helper function to create a static struct \ :c:type:`struct lock_class_key <lock_class_key>`\  and calls \ :c:func:`v4l2_ctrl_handler_init_class`\ 

    :param hdl:
        The control handler.
    :type hdl: 

    :param nr_of_controls_hint:
        A hint of how many controls this handler is
        expected to refer to. This is the total number, so including
        any inherited controls. It doesn't have to be precise, but if
        it is way off, then you either waste memory (too many buckets
        are allocated) or the control lookup becomes slower (not enough
        buckets are allocated, so there are more slow list lookups).
        It will always work, though.
    :type nr_of_controls_hint: 

.. _`v4l2_ctrl_handler_init.description`:

Description
-----------

This helper function creates a static struct \ :c:type:`struct lock_class_key <lock_class_key>`\  and
calls \ :c:func:`v4l2_ctrl_handler_init_class`\ , providing a proper name for the lock
validador.

Use this helper function to initialize a control handler.

.. _`v4l2_ctrl_handler_free`:

v4l2_ctrl_handler_free
======================

.. c:function:: void v4l2_ctrl_handler_free(struct v4l2_ctrl_handler *hdl)

    Free all controls owned by the handler and free the control list.

    :param hdl:
        The control handler.
    :type hdl: struct v4l2_ctrl_handler \*

.. _`v4l2_ctrl_handler_free.description`:

Description
-----------

Does nothing if \ ``hdl``\  == NULL.

.. _`v4l2_ctrl_lock`:

v4l2_ctrl_lock
==============

.. c:function:: void v4l2_ctrl_lock(struct v4l2_ctrl *ctrl)

    Helper function to lock the handler associated with the control.

    :param ctrl:
        The control to lock.
    :type ctrl: struct v4l2_ctrl \*

.. _`v4l2_ctrl_unlock`:

v4l2_ctrl_unlock
================

.. c:function:: void v4l2_ctrl_unlock(struct v4l2_ctrl *ctrl)

    Helper function to unlock the handler associated with the control.

    :param ctrl:
        The control to unlock.
    :type ctrl: struct v4l2_ctrl \*

.. _`__v4l2_ctrl_handler_setup`:

__v4l2_ctrl_handler_setup
=========================

.. c:function:: int __v4l2_ctrl_handler_setup(struct v4l2_ctrl_handler *hdl)

    Call the s_ctrl op for all controls belonging to the handler to initialize the hardware to the current control values. The caller is responsible for acquiring the control handler mutex on behalf of \ :c:func:`__v4l2_ctrl_handler_setup`\ .

    :param hdl:
        The control handler.
    :type hdl: struct v4l2_ctrl_handler \*

.. _`__v4l2_ctrl_handler_setup.description`:

Description
-----------

Button controls will be skipped, as are read-only controls.

If \ ``hdl``\  == NULL, then this just returns 0.

.. _`v4l2_ctrl_handler_setup`:

v4l2_ctrl_handler_setup
=======================

.. c:function:: int v4l2_ctrl_handler_setup(struct v4l2_ctrl_handler *hdl)

    Call the s_ctrl op for all controls belonging to the handler to initialize the hardware to the current control values.

    :param hdl:
        The control handler.
    :type hdl: struct v4l2_ctrl_handler \*

.. _`v4l2_ctrl_handler_setup.description`:

Description
-----------

Button controls will be skipped, as are read-only controls.

If \ ``hdl``\  == NULL, then this just returns 0.

.. _`v4l2_ctrl_handler_log_status`:

v4l2_ctrl_handler_log_status
============================

.. c:function:: void v4l2_ctrl_handler_log_status(struct v4l2_ctrl_handler *hdl, const char *prefix)

    Log all controls owned by the handler.

    :param hdl:
        The control handler.
    :type hdl: struct v4l2_ctrl_handler \*

    :param prefix:
        The prefix to use when logging the control values. If the
        prefix does not end with a space, then ": " will be added
        after the prefix. If \ ``prefix``\  == NULL, then no prefix will be
        used.
    :type prefix: const char \*

.. _`v4l2_ctrl_handler_log_status.description`:

Description
-----------

For use with VIDIOC_LOG_STATUS.

Does nothing if \ ``hdl``\  == NULL.

.. _`v4l2_ctrl_new_custom`:

v4l2_ctrl_new_custom
====================

.. c:function:: struct v4l2_ctrl *v4l2_ctrl_new_custom(struct v4l2_ctrl_handler *hdl, const struct v4l2_ctrl_config *cfg, void *priv)

    Allocate and initialize a new custom V4L2 control.

    :param hdl:
        The control handler.
    :type hdl: struct v4l2_ctrl_handler \*

    :param cfg:
        The control's configuration data.
    :type cfg: const struct v4l2_ctrl_config \*

    :param priv:
        The control's driver-specific private data.
    :type priv: void \*

.. _`v4l2_ctrl_new_custom.description`:

Description
-----------

If the \ :c:type:`struct v4l2_ctrl <v4l2_ctrl>`\  struct could not be allocated then NULL is returned
and \ ``hdl->error``\  is set to the error code (if it wasn't set already).

.. _`v4l2_ctrl_new_std`:

v4l2_ctrl_new_std
=================

.. c:function:: struct v4l2_ctrl *v4l2_ctrl_new_std(struct v4l2_ctrl_handler *hdl, const struct v4l2_ctrl_ops *ops, u32 id, s64 min, s64 max, u64 step, s64 def)

    Allocate and initialize a new standard V4L2 non-menu control.

    :param hdl:
        The control handler.
    :type hdl: struct v4l2_ctrl_handler \*

    :param ops:
        The control ops.
    :type ops: const struct v4l2_ctrl_ops \*

    :param id:
        The control ID.
    :type id: u32

    :param min:
        The control's minimum value.
    :type min: s64

    :param max:
        The control's maximum value.
    :type max: s64

    :param step:
        The control's step value
    :type step: u64

    :param def:
        The control's default value.
    :type def: s64

.. _`v4l2_ctrl_new_std.description`:

Description
-----------

If the \ :c:type:`struct v4l2_ctrl <v4l2_ctrl>`\  struct could not be allocated, or the control
ID is not known, then NULL is returned and \ ``hdl->error``\  is set to the
appropriate error code (if it wasn't set already).

If \ ``id``\  refers to a menu control, then this function will return NULL.

Use \ :c:func:`v4l2_ctrl_new_std_menu`\  when adding menu controls.

.. _`v4l2_ctrl_new_std_menu`:

v4l2_ctrl_new_std_menu
======================

.. c:function:: struct v4l2_ctrl *v4l2_ctrl_new_std_menu(struct v4l2_ctrl_handler *hdl, const struct v4l2_ctrl_ops *ops, u32 id, u8 max, u64 mask, u8 def)

    Allocate and initialize a new standard V4L2 menu control.

    :param hdl:
        The control handler.
    :type hdl: struct v4l2_ctrl_handler \*

    :param ops:
        The control ops.
    :type ops: const struct v4l2_ctrl_ops \*

    :param id:
        The control ID.
    :type id: u32

    :param max:
        The control's maximum value.
    :type max: u8

    :param mask:
        The control's skip mask for menu controls. This makes it
        easy to skip menu items that are not valid. If bit X is set,
        then menu item X is skipped. Of course, this only works for
        menus with <= 64 menu items. There are no menus that come
        close to that number, so this is OK. Should we ever need more,
        then this will have to be extended to a bit array.
    :type mask: u64

    :param def:
        The control's default value.
    :type def: u8

.. _`v4l2_ctrl_new_std_menu.description`:

Description
-----------

Same as \ :c:func:`v4l2_ctrl_new_std`\ , but \ ``min``\  is set to 0 and the \ ``mask``\  value
determines which menu items are to be skipped.

If \ ``id``\  refers to a non-menu control, then this function will return NULL.

.. _`v4l2_ctrl_new_std_menu_items`:

v4l2_ctrl_new_std_menu_items
============================

.. c:function:: struct v4l2_ctrl *v4l2_ctrl_new_std_menu_items(struct v4l2_ctrl_handler *hdl, const struct v4l2_ctrl_ops *ops, u32 id, u8 max, u64 mask, u8 def, const char * const *qmenu)

    Create a new standard V4L2 menu control with driver specific menu.

    :param hdl:
        The control handler.
    :type hdl: struct v4l2_ctrl_handler \*

    :param ops:
        The control ops.
    :type ops: const struct v4l2_ctrl_ops \*

    :param id:
        The control ID.
    :type id: u32

    :param max:
        The control's maximum value.
    :type max: u8

    :param mask:
        The control's skip mask for menu controls. This makes it
        easy to skip menu items that are not valid. If bit X is set,
        then menu item X is skipped. Of course, this only works for
        menus with <= 64 menu items. There are no menus that come
        close to that number, so this is OK. Should we ever need more,
        then this will have to be extended to a bit array.
    :type mask: u64

    :param def:
        The control's default value.
    :type def: u8

    :param qmenu:
        The new menu.
    :type qmenu: const char \* const \*

.. _`v4l2_ctrl_new_std_menu_items.description`:

Description
-----------

Same as \ :c:func:`v4l2_ctrl_new_std_menu`\ , but \ ``qmenu``\  will be the driver specific
menu of this control.

.. _`v4l2_ctrl_new_int_menu`:

v4l2_ctrl_new_int_menu
======================

.. c:function:: struct v4l2_ctrl *v4l2_ctrl_new_int_menu(struct v4l2_ctrl_handler *hdl, const struct v4l2_ctrl_ops *ops, u32 id, u8 max, u8 def, const s64 *qmenu_int)

    Create a new standard V4L2 integer menu control.

    :param hdl:
        The control handler.
    :type hdl: struct v4l2_ctrl_handler \*

    :param ops:
        The control ops.
    :type ops: const struct v4l2_ctrl_ops \*

    :param id:
        The control ID.
    :type id: u32

    :param max:
        The control's maximum value.
    :type max: u8

    :param def:
        The control's default value.
    :type def: u8

    :param qmenu_int:
        The control's menu entries.
    :type qmenu_int: const s64 \*

.. _`v4l2_ctrl_new_int_menu.description`:

Description
-----------

Same as \ :c:func:`v4l2_ctrl_new_std_menu`\ , but \ ``mask``\  is set to 0 and it additionaly
takes as an argument an array of integers determining the menu items.

If \ ``id``\  refers to a non-integer-menu control, then this function will
return \ ``NULL``\ .

.. _`v4l2_ctrl_filter`:

v4l2_ctrl_filter
================

.. c:function:: bool v4l2_ctrl_filter(const struct v4l2_ctrl *ctrl)

    Typedef to define the filter function to be used when adding a control handler.

    :param ctrl:
        pointer to struct \ :c:type:`struct v4l2_ctrl <v4l2_ctrl>`\ .
    :type ctrl: const struct v4l2_ctrl \*

.. _`v4l2_ctrl_add_handler`:

v4l2_ctrl_add_handler
=====================

.. c:function:: int v4l2_ctrl_add_handler(struct v4l2_ctrl_handler *hdl, struct v4l2_ctrl_handler *add, v4l2_ctrl_filter filter, bool from_other_dev)

    Add all controls from handler \ ``add``\  to handler \ ``hdl``\ .

    :param hdl:
        The control handler.
    :type hdl: struct v4l2_ctrl_handler \*

    :param add:
        The control handler whose controls you want to add to
        the \ ``hdl``\  control handler.
    :type add: struct v4l2_ctrl_handler \*

    :param filter:
        This function will filter which controls should be added.
    :type filter: v4l2_ctrl_filter

    :param from_other_dev:
        If true, then the controls in \ ``add``\  were defined in another
        device than \ ``hdl``\ .
    :type from_other_dev: bool

.. _`v4l2_ctrl_add_handler.description`:

Description
-----------

Does nothing if either of the two handlers is a NULL pointer.
If \ ``filter``\  is NULL, then all controls are added. Otherwise only those
controls for which \ ``filter``\  returns true will be added.
In case of an error \ ``hdl->error``\  will be set to the error code (if it
wasn't set already).

.. _`v4l2_ctrl_radio_filter`:

v4l2_ctrl_radio_filter
======================

.. c:function:: bool v4l2_ctrl_radio_filter(const struct v4l2_ctrl *ctrl)

    Standard filter for radio controls.

    :param ctrl:
        The control that is filtered.
    :type ctrl: const struct v4l2_ctrl \*

.. _`v4l2_ctrl_radio_filter.description`:

Description
-----------

This will return true for any controls that are valid for radio device
nodes. Those are all of the V4L2_CID_AUDIO_* user controls and all FM
transmitter class controls.

This function is to be used with \ :c:func:`v4l2_ctrl_add_handler`\ .

.. _`v4l2_ctrl_cluster`:

v4l2_ctrl_cluster
=================

.. c:function:: void v4l2_ctrl_cluster(unsigned int ncontrols, struct v4l2_ctrl **controls)

    Mark all controls in the cluster as belonging to that cluster.

    :param ncontrols:
        The number of controls in this cluster.
    :type ncontrols: unsigned int

    :param controls:
        The cluster control array of size \ ``ncontrols``\ .
    :type controls: struct v4l2_ctrl \*\*

.. _`v4l2_ctrl_auto_cluster`:

v4l2_ctrl_auto_cluster
======================

.. c:function:: void v4l2_ctrl_auto_cluster(unsigned int ncontrols, struct v4l2_ctrl **controls, u8 manual_val, bool set_volatile)

    Mark all controls in the cluster as belonging to that cluster and set it up for autofoo/foo-type handling.

    :param ncontrols:
        The number of controls in this cluster.
    :type ncontrols: unsigned int

    :param controls:
        The cluster control array of size \ ``ncontrols``\ . The first control
        must be the 'auto' control (e.g. autogain, autoexposure, etc.)
    :type controls: struct v4l2_ctrl \*\*

    :param manual_val:
        The value for the first control in the cluster that equals the
        manual setting.
    :type manual_val: u8

    :param set_volatile:
        If true, then all controls except the first auto control will
        be volatile.
    :type set_volatile: bool

.. _`v4l2_ctrl_auto_cluster.description`:

Description
-----------

Use for control groups where one control selects some automatic feature and
the other controls are only active whenever the automatic feature is turned
off (manual mode). Typical examples: autogain vs gain, auto-whitebalance vs
red and blue balance, etc.

.. _`v4l2_ctrl_auto_cluster.the-behavior-of-such-controls-is-as-follows`:

The behavior of such controls is as follows
-------------------------------------------


When the autofoo control is set to automatic, then any manual controls
are set to inactive and any reads will call g_volatile_ctrl (if the control
was marked volatile).

When the autofoo control is set to manual, then any manual controls will
be marked active, and any reads will just return the current value without
going through g_volatile_ctrl.

In addition, this function will set the \ ``V4L2_CTRL_FLAG_UPDATE``\  flag
on the autofoo control and \ ``V4L2_CTRL_FLAG_INACTIVE``\  on the foo control(s)
if autofoo is in auto mode.

.. _`v4l2_ctrl_find`:

v4l2_ctrl_find
==============

.. c:function:: struct v4l2_ctrl *v4l2_ctrl_find(struct v4l2_ctrl_handler *hdl, u32 id)

    Find a control with the given ID.

    :param hdl:
        The control handler.
    :type hdl: struct v4l2_ctrl_handler \*

    :param id:
        The control ID to find.
    :type id: u32

.. _`v4l2_ctrl_find.description`:

Description
-----------

If \ ``hdl``\  == NULL this will return NULL as well. Will lock the handler so
do not use from inside \ :c:type:`struct v4l2_ctrl_ops <v4l2_ctrl_ops>`\ .

.. _`v4l2_ctrl_activate`:

v4l2_ctrl_activate
==================

.. c:function:: void v4l2_ctrl_activate(struct v4l2_ctrl *ctrl, bool active)

    Make the control active or inactive.

    :param ctrl:
        The control to (de)activate.
    :type ctrl: struct v4l2_ctrl \*

    :param active:
        True if the control should become active.
    :type active: bool

.. _`v4l2_ctrl_activate.description`:

Description
-----------

This sets or clears the V4L2_CTRL_FLAG_INACTIVE flag atomically.
Does nothing if \ ``ctrl``\  == NULL.
This will usually be called from within the s_ctrl op.
The V4L2_EVENT_CTRL event will be generated afterwards.

This function assumes that the control handler is locked.

.. _`__v4l2_ctrl_grab`:

__v4l2_ctrl_grab
================

.. c:function:: void __v4l2_ctrl_grab(struct v4l2_ctrl *ctrl, bool grabbed)

    Unlocked variant of v4l2_ctrl_grab.

    :param ctrl:
        The control to (de)activate.
    :type ctrl: struct v4l2_ctrl \*

    :param grabbed:
        True if the control should become grabbed.
    :type grabbed: bool

.. _`__v4l2_ctrl_grab.description`:

Description
-----------

This sets or clears the V4L2_CTRL_FLAG_GRABBED flag atomically.
Does nothing if \ ``ctrl``\  == NULL.
The V4L2_EVENT_CTRL event will be generated afterwards.
This will usually be called when starting or stopping streaming in the
driver.

This function assumes that the control handler is locked by the caller.

.. _`v4l2_ctrl_grab`:

v4l2_ctrl_grab
==============

.. c:function:: void v4l2_ctrl_grab(struct v4l2_ctrl *ctrl, bool grabbed)

    Mark the control as grabbed or not grabbed.

    :param ctrl:
        The control to (de)activate.
    :type ctrl: struct v4l2_ctrl \*

    :param grabbed:
        True if the control should become grabbed.
    :type grabbed: bool

.. _`v4l2_ctrl_grab.description`:

Description
-----------

This sets or clears the V4L2_CTRL_FLAG_GRABBED flag atomically.
Does nothing if \ ``ctrl``\  == NULL.
The V4L2_EVENT_CTRL event will be generated afterwards.
This will usually be called when starting or stopping streaming in the
driver.

This function assumes that the control handler is not locked and will
take the lock itself.

.. _`__v4l2_ctrl_modify_range`:

__v4l2_ctrl_modify_range
========================

.. c:function:: int __v4l2_ctrl_modify_range(struct v4l2_ctrl *ctrl, s64 min, s64 max, u64 step, s64 def)

    Unlocked variant of \ :c:func:`v4l2_ctrl_modify_range`\ 

    :param ctrl:
        The control to update.
    :type ctrl: struct v4l2_ctrl \*

    :param min:
        The control's minimum value.
    :type min: s64

    :param max:
        The control's maximum value.
    :type max: s64

    :param step:
        The control's step value
    :type step: u64

    :param def:
        The control's default value.
    :type def: s64

.. _`__v4l2_ctrl_modify_range.description`:

Description
-----------

Update the range of a control on the fly. This works for control types
INTEGER, BOOLEAN, MENU, INTEGER MENU and BITMASK. For menu controls the
\ ``step``\  value is interpreted as a menu_skip_mask.

An error is returned if one of the range arguments is invalid for this
control type.

The caller is responsible for acquiring the control handler mutex on behalf
of \ :c:func:`__v4l2_ctrl_modify_range`\ .

.. _`v4l2_ctrl_modify_range`:

v4l2_ctrl_modify_range
======================

.. c:function:: int v4l2_ctrl_modify_range(struct v4l2_ctrl *ctrl, s64 min, s64 max, u64 step, s64 def)

    Update the range of a control.

    :param ctrl:
        The control to update.
    :type ctrl: struct v4l2_ctrl \*

    :param min:
        The control's minimum value.
    :type min: s64

    :param max:
        The control's maximum value.
    :type max: s64

    :param step:
        The control's step value
    :type step: u64

    :param def:
        The control's default value.
    :type def: s64

.. _`v4l2_ctrl_modify_range.description`:

Description
-----------

Update the range of a control on the fly. This works for control types
INTEGER, BOOLEAN, MENU, INTEGER MENU and BITMASK. For menu controls the
\ ``step``\  value is interpreted as a menu_skip_mask.

An error is returned if one of the range arguments is invalid for this
control type.

This function assumes that the control handler is not locked and will
take the lock itself.

.. _`v4l2_ctrl_notify`:

v4l2_ctrl_notify
================

.. c:function:: void v4l2_ctrl_notify(struct v4l2_ctrl *ctrl, v4l2_ctrl_notify_fnc notify, void *priv)

    Function to set a notify callback for a control.

    :param ctrl:
        The control.
    :type ctrl: struct v4l2_ctrl \*

    :param notify:
        The callback function.
    :type notify: v4l2_ctrl_notify_fnc

    :param priv:
        The callback private handle, passed as argument to the callback.
    :type priv: void \*

.. _`v4l2_ctrl_notify.description`:

Description
-----------

This function sets a callback function for the control. If \ ``ctrl``\  is NULL,
then it will do nothing. If \ ``notify``\  is NULL, then the notify callback will
be removed.

There can be only one notify. If another already exists, then a WARN_ON
will be issued and the function will do nothing.

.. _`v4l2_ctrl_get_name`:

v4l2_ctrl_get_name
==================

.. c:function:: const char *v4l2_ctrl_get_name(u32 id)

    Get the name of the control

    :param id:
        The control ID.
    :type id: u32

.. _`v4l2_ctrl_get_name.description`:

Description
-----------

This function returns the name of the given control ID or NULL if it isn't
a known control.

.. _`v4l2_ctrl_get_menu`:

v4l2_ctrl_get_menu
==================

.. c:function:: const char * const *v4l2_ctrl_get_menu(u32 id)

    Get the menu string array of the control

    :param id:
        The control ID.
    :type id: u32

.. _`v4l2_ctrl_get_menu.description`:

Description
-----------

This function returns the NULL-terminated menu string array name of the
given control ID or NULL if it isn't a known menu control.

.. _`v4l2_ctrl_get_int_menu`:

v4l2_ctrl_get_int_menu
======================

.. c:function:: const s64 *v4l2_ctrl_get_int_menu(u32 id, u32 *len)

    Get the integer menu array of the control

    :param id:
        The control ID.
    :type id: u32

    :param len:
        The size of the integer array.
    :type len: u32 \*

.. _`v4l2_ctrl_get_int_menu.description`:

Description
-----------

This function returns the integer array of the given control ID or NULL if it
if it isn't a known integer menu control.

.. _`v4l2_ctrl_g_ctrl`:

v4l2_ctrl_g_ctrl
================

.. c:function:: s32 v4l2_ctrl_g_ctrl(struct v4l2_ctrl *ctrl)

    Helper function to get the control's value from within a driver.

    :param ctrl:
        The control.
    :type ctrl: struct v4l2_ctrl \*

.. _`v4l2_ctrl_g_ctrl.description`:

Description
-----------

This returns the control's value safely by going through the control
framework. This function will lock the control's handler, so it cannot be
used from within the \ :c:type:`struct v4l2_ctrl_ops <v4l2_ctrl_ops>`\  functions.

This function is for integer type controls only.

.. _`__v4l2_ctrl_s_ctrl`:

__v4l2_ctrl_s_ctrl
==================

.. c:function:: int __v4l2_ctrl_s_ctrl(struct v4l2_ctrl *ctrl, s32 val)

    Unlocked variant of \ :c:func:`v4l2_ctrl_s_ctrl`\ .

    :param ctrl:
        The control.
    :type ctrl: struct v4l2_ctrl \*

    :param val:
        TheControls name new value.
    :type val: s32

.. _`__v4l2_ctrl_s_ctrl.description`:

Description
-----------

This sets the control's new value safely by going through the control
framework. This function assumes the control's handler is already locked,
allowing it to be used from within the \ :c:type:`struct v4l2_ctrl_ops <v4l2_ctrl_ops>`\  functions.

This function is for integer type controls only.

.. _`v4l2_ctrl_s_ctrl`:

v4l2_ctrl_s_ctrl
================

.. c:function:: int v4l2_ctrl_s_ctrl(struct v4l2_ctrl *ctrl, s32 val)

    Helper function to set the control's value from within a driver.

    :param ctrl:
        The control.
    :type ctrl: struct v4l2_ctrl \*

    :param val:
        The new value.
    :type val: s32

.. _`v4l2_ctrl_s_ctrl.description`:

Description
-----------

This sets the control's new value safely by going through the control
framework. This function will lock the control's handler, so it cannot be
used from within the \ :c:type:`struct v4l2_ctrl_ops <v4l2_ctrl_ops>`\  functions.

This function is for integer type controls only.

.. _`v4l2_ctrl_g_ctrl_int64`:

v4l2_ctrl_g_ctrl_int64
======================

.. c:function:: s64 v4l2_ctrl_g_ctrl_int64(struct v4l2_ctrl *ctrl)

    Helper function to get a 64-bit control's value from within a driver.

    :param ctrl:
        The control.
    :type ctrl: struct v4l2_ctrl \*

.. _`v4l2_ctrl_g_ctrl_int64.description`:

Description
-----------

This returns the control's value safely by going through the control
framework. This function will lock the control's handler, so it cannot be
used from within the \ :c:type:`struct v4l2_ctrl_ops <v4l2_ctrl_ops>`\  functions.

This function is for 64-bit integer type controls only.

.. _`__v4l2_ctrl_s_ctrl_int64`:

__v4l2_ctrl_s_ctrl_int64
========================

.. c:function:: int __v4l2_ctrl_s_ctrl_int64(struct v4l2_ctrl *ctrl, s64 val)

    Unlocked variant of \ :c:func:`v4l2_ctrl_s_ctrl_int64`\ .

    :param ctrl:
        The control.
    :type ctrl: struct v4l2_ctrl \*

    :param val:
        The new value.
    :type val: s64

.. _`__v4l2_ctrl_s_ctrl_int64.description`:

Description
-----------

This sets the control's new value safely by going through the control
framework. This function assumes the control's handler is already locked,
allowing it to be used from within the \ :c:type:`struct v4l2_ctrl_ops <v4l2_ctrl_ops>`\  functions.

This function is for 64-bit integer type controls only.

.. _`v4l2_ctrl_s_ctrl_int64`:

v4l2_ctrl_s_ctrl_int64
======================

.. c:function:: int v4l2_ctrl_s_ctrl_int64(struct v4l2_ctrl *ctrl, s64 val)

    Helper function to set a 64-bit control's value from within a driver.

    :param ctrl:
        The control.
    :type ctrl: struct v4l2_ctrl \*

    :param val:
        The new value.
    :type val: s64

.. _`v4l2_ctrl_s_ctrl_int64.description`:

Description
-----------

This sets the control's new value safely by going through the control
framework. This function will lock the control's handler, so it cannot be
used from within the \ :c:type:`struct v4l2_ctrl_ops <v4l2_ctrl_ops>`\  functions.

This function is for 64-bit integer type controls only.

.. _`__v4l2_ctrl_s_ctrl_string`:

__v4l2_ctrl_s_ctrl_string
=========================

.. c:function:: int __v4l2_ctrl_s_ctrl_string(struct v4l2_ctrl *ctrl, const char *s)

    Unlocked variant of \ :c:func:`v4l2_ctrl_s_ctrl_string`\ .

    :param ctrl:
        The control.
    :type ctrl: struct v4l2_ctrl \*

    :param s:
        The new string.
    :type s: const char \*

.. _`__v4l2_ctrl_s_ctrl_string.description`:

Description
-----------

This sets the control's new string safely by going through the control
framework. This function assumes the control's handler is already locked,
allowing it to be used from within the \ :c:type:`struct v4l2_ctrl_ops <v4l2_ctrl_ops>`\  functions.

This function is for string type controls only.

.. _`v4l2_ctrl_s_ctrl_string`:

v4l2_ctrl_s_ctrl_string
=======================

.. c:function:: int v4l2_ctrl_s_ctrl_string(struct v4l2_ctrl *ctrl, const char *s)

    Helper function to set a control's string value from within a driver.

    :param ctrl:
        The control.
    :type ctrl: struct v4l2_ctrl \*

    :param s:
        The new string.
        Controls name
        This sets the control's new string safely by going through the control
        framework. This function will lock the control's handler, so it cannot be
        used from within the \ :c:type:`struct v4l2_ctrl_ops <v4l2_ctrl_ops>`\  functions.
    :type s: const char \*

.. _`v4l2_ctrl_s_ctrl_string.description`:

Description
-----------

This function is for string type controls only.

.. _`v4l2_ctrl_replace`:

v4l2_ctrl_replace
=================

.. c:function:: void v4l2_ctrl_replace(struct v4l2_event *old, const struct v4l2_event *new)

    Function to be used as a callback to \ :c:type:`struct v4l2_subscribed_event_ops <v4l2_subscribed_event_ops>`\  replace(\)

    :param old:
        pointer to struct \ :c:type:`struct v4l2_event <v4l2_event>`\  with the reported
        event;
    :type old: struct v4l2_event \*

    :param new:
        pointer to struct \ :c:type:`struct v4l2_event <v4l2_event>`\  with the modified
        event;
    :type new: const struct v4l2_event \*

.. _`v4l2_ctrl_merge`:

v4l2_ctrl_merge
===============

.. c:function:: void v4l2_ctrl_merge(const struct v4l2_event *old, struct v4l2_event *new)

    Function to be used as a callback to \ :c:type:`struct v4l2_subscribed_event_ops <v4l2_subscribed_event_ops>`\  merge(\)

    :param old:
        pointer to struct \ :c:type:`struct v4l2_event <v4l2_event>`\  with the reported
        event;
    :type old: const struct v4l2_event \*

    :param new:
        pointer to struct \ :c:type:`struct v4l2_event <v4l2_event>`\  with the merged
        event;
    :type new: struct v4l2_event \*

.. _`v4l2_ctrl_log_status`:

v4l2_ctrl_log_status
====================

.. c:function:: int v4l2_ctrl_log_status(struct file *file, void *fh)

    helper function to implement \ ``VIDIOC_LOG_STATUS``\  ioctl

    :param file:
        pointer to struct file
    :type file: struct file \*

    :param fh:
        unused. Kept just to be compatible to the arguments expected by
        \ :c:type:`struct v4l2_ioctl_ops <v4l2_ioctl_ops>`\ .vidioc_log_status.
    :type fh: void \*

.. _`v4l2_ctrl_log_status.description`:

Description
-----------

Can be used as a vidioc_log_status function that just dumps all controls
associated with the filehandle.

.. _`v4l2_ctrl_subscribe_event`:

v4l2_ctrl_subscribe_event
=========================

.. c:function:: int v4l2_ctrl_subscribe_event(struct v4l2_fh *fh, const struct v4l2_event_subscription *sub)

    Subscribes to an event

    :param fh:
        pointer to struct v4l2_fh
    :type fh: struct v4l2_fh \*

    :param sub:
        pointer to \ :c:type:`struct v4l2_event_subscription <v4l2_event_subscription>`\ 
    :type sub: const struct v4l2_event_subscription \*

.. _`v4l2_ctrl_subscribe_event.description`:

Description
-----------

Can be used as a vidioc_subscribe_event function that just subscribes
control events.

.. _`v4l2_ctrl_poll`:

v4l2_ctrl_poll
==============

.. c:function:: __poll_t v4l2_ctrl_poll(struct file *file, struct poll_table_struct *wait)

    function to be used as a callback to the \ :c:func:`poll`\  That just polls for control events.

    :param file:
        pointer to struct file
    :type file: struct file \*

    :param wait:
        pointer to struct poll_table_struct
    :type wait: struct poll_table_struct \*

.. _`v4l2_ctrl_request_setup`:

v4l2_ctrl_request_setup
=======================

.. c:function:: void v4l2_ctrl_request_setup(struct media_request *req, struct v4l2_ctrl_handler *parent)

    helper function to apply control values in a request

    :param req:
        The request
    :type req: struct media_request \*

    :param parent:
        The parent control handler ('priv' in \ :c:func:`media_request_object_find`\ )
    :type parent: struct v4l2_ctrl_handler \*

.. _`v4l2_ctrl_request_setup.description`:

Description
-----------

This is a helper function to call the control handler's s_ctrl callback with
the control values contained in the request. Do note that this approach of
applying control values in a request is only applicable to memory-to-memory
devices.

.. _`v4l2_ctrl_request_complete`:

v4l2_ctrl_request_complete
==========================

.. c:function:: void v4l2_ctrl_request_complete(struct media_request *req, struct v4l2_ctrl_handler *parent)

    Complete a control handler request object

    :param req:
        The request
    :type req: struct media_request \*

    :param parent:
        The parent control handler ('priv' in \ :c:func:`media_request_object_find`\ )
    :type parent: struct v4l2_ctrl_handler \*

.. _`v4l2_ctrl_request_complete.description`:

Description
-----------

This function is to be called on each control handler that may have had a
request object associated with it, i.e. control handlers of a driver that
supports requests.

The function first obtains the values of any volatile controls in the control
handler and attach them to the request. Then, the function completes the
request object.

.. _`v4l2_ctrl_request_hdl_find`:

v4l2_ctrl_request_hdl_find
==========================

.. c:function:: struct v4l2_ctrl_handler *v4l2_ctrl_request_hdl_find(struct media_request *req, struct v4l2_ctrl_handler *parent)

    Find the control handler in the request

    :param req:
        The request
    :type req: struct media_request \*

    :param parent:
        The parent control handler ('priv' in \ :c:func:`media_request_object_find`\ )
    :type parent: struct v4l2_ctrl_handler \*

.. _`v4l2_ctrl_request_hdl_find.description`:

Description
-----------

This function finds the control handler in the request. It may return
NULL if not found. When done, you must call \ :c:func:`v4l2_ctrl_request_put_hdl`\ 
with the returned handler pointer.

If the request is not in state VALIDATING or QUEUED, then this function
will always return NULL.

Note that in state VALIDATING the req_queue_mutex is held, so
no objects can be added or deleted from the request.

In state QUEUED it is the driver that will have to ensure this.

.. _`v4l2_ctrl_request_hdl_put`:

v4l2_ctrl_request_hdl_put
=========================

.. c:function:: void v4l2_ctrl_request_hdl_put(struct v4l2_ctrl_handler *hdl)

    Put the control handler

    :param hdl:
        Put this control handler
    :type hdl: struct v4l2_ctrl_handler \*

.. _`v4l2_ctrl_request_hdl_put.description`:

Description
-----------

This function released the control handler previously obtained from'
\ :c:func:`v4l2_ctrl_request_hdl_find`\ .

.. _`v4l2_ctrl_request_hdl_ctrl_find`:

v4l2_ctrl_request_hdl_ctrl_find
===============================

.. c:function:: struct v4l2_ctrl *v4l2_ctrl_request_hdl_ctrl_find(struct v4l2_ctrl_handler *hdl, u32 id)

    Find a control with the given ID.

    :param hdl:
        The control handler from the request.
    :type hdl: struct v4l2_ctrl_handler \*

    :param id:
        The ID of the control to find.
    :type id: u32

.. _`v4l2_ctrl_request_hdl_ctrl_find.description`:

Description
-----------

This function returns a pointer to the control if this control is
part of the request or NULL otherwise.

.. _`v4l2_queryctrl`:

v4l2_queryctrl
==============

.. c:function:: int v4l2_queryctrl(struct v4l2_ctrl_handler *hdl, struct v4l2_queryctrl *qc)

    Helper function to implement :ref:`VIDIOC_QUERYCTRL <vidioc_queryctrl>` ioctl

    :param hdl:
        pointer to \ :c:type:`struct v4l2_ctrl_handler <v4l2_ctrl_handler>`\ 
    :type hdl: struct v4l2_ctrl_handler \*

    :param qc:
        pointer to \ :c:type:`struct v4l2_queryctrl <v4l2_queryctrl>`\ 
    :type qc: struct v4l2_queryctrl \*

.. _`v4l2_queryctrl.description`:

Description
-----------

If hdl == NULL then they will all return -EINVAL.

.. _`v4l2_query_ext_ctrl`:

v4l2_query_ext_ctrl
===================

.. c:function:: int v4l2_query_ext_ctrl(struct v4l2_ctrl_handler *hdl, struct v4l2_query_ext_ctrl *qc)

    Helper function to implement :ref:`VIDIOC_QUERY_EXT_CTRL <vidioc_queryctrl>` ioctl

    :param hdl:
        pointer to \ :c:type:`struct v4l2_ctrl_handler <v4l2_ctrl_handler>`\ 
    :type hdl: struct v4l2_ctrl_handler \*

    :param qc:
        pointer to \ :c:type:`struct v4l2_query_ext_ctrl <v4l2_query_ext_ctrl>`\ 
    :type qc: struct v4l2_query_ext_ctrl \*

.. _`v4l2_query_ext_ctrl.description`:

Description
-----------

If hdl == NULL then they will all return -EINVAL.

.. _`v4l2_querymenu`:

v4l2_querymenu
==============

.. c:function:: int v4l2_querymenu(struct v4l2_ctrl_handler *hdl, struct v4l2_querymenu *qm)

    Helper function to implement :ref:`VIDIOC_QUERYMENU <vidioc_queryctrl>` ioctl

    :param hdl:
        pointer to \ :c:type:`struct v4l2_ctrl_handler <v4l2_ctrl_handler>`\ 
    :type hdl: struct v4l2_ctrl_handler \*

    :param qm:
        pointer to \ :c:type:`struct v4l2_querymenu <v4l2_querymenu>`\ 
    :type qm: struct v4l2_querymenu \*

.. _`v4l2_querymenu.description`:

Description
-----------

If hdl == NULL then they will all return -EINVAL.

.. _`v4l2_g_ctrl`:

v4l2_g_ctrl
===========

.. c:function:: int v4l2_g_ctrl(struct v4l2_ctrl_handler *hdl, struct v4l2_control *ctrl)

    Helper function to implement :ref:`VIDIOC_G_CTRL <vidioc_g_ctrl>` ioctl

    :param hdl:
        pointer to \ :c:type:`struct v4l2_ctrl_handler <v4l2_ctrl_handler>`\ 
    :type hdl: struct v4l2_ctrl_handler \*

    :param ctrl:
        pointer to \ :c:type:`struct v4l2_control <v4l2_control>`\ 
    :type ctrl: struct v4l2_control \*

.. _`v4l2_g_ctrl.description`:

Description
-----------

If hdl == NULL then they will all return -EINVAL.

.. _`v4l2_s_ctrl`:

v4l2_s_ctrl
===========

.. c:function:: int v4l2_s_ctrl(struct v4l2_fh *fh, struct v4l2_ctrl_handler *hdl, struct v4l2_control *ctrl)

    Helper function to implement :ref:`VIDIOC_S_CTRL <vidioc_g_ctrl>` ioctl

    :param fh:
        pointer to \ :c:type:`struct v4l2_fh <v4l2_fh>`\ 
    :type fh: struct v4l2_fh \*

    :param hdl:
        pointer to \ :c:type:`struct v4l2_ctrl_handler <v4l2_ctrl_handler>`\ 
    :type hdl: struct v4l2_ctrl_handler \*

    :param ctrl:
        pointer to \ :c:type:`struct v4l2_control <v4l2_control>`\ 
    :type ctrl: struct v4l2_control \*

.. _`v4l2_s_ctrl.description`:

Description
-----------

If hdl == NULL then they will all return -EINVAL.

.. _`v4l2_g_ext_ctrls`:

v4l2_g_ext_ctrls
================

.. c:function:: int v4l2_g_ext_ctrls(struct v4l2_ctrl_handler *hdl, struct media_device *mdev, struct v4l2_ext_controls *c)

    Helper function to implement :ref:`VIDIOC_G_EXT_CTRLS <vidioc_g_ext_ctrls>` ioctl

    :param hdl:
        pointer to \ :c:type:`struct v4l2_ctrl_handler <v4l2_ctrl_handler>`\ 
    :type hdl: struct v4l2_ctrl_handler \*

    :param mdev:
        pointer to \ :c:type:`struct media_device <media_device>`\ 
    :type mdev: struct media_device \*

    :param c:
        pointer to \ :c:type:`struct v4l2_ext_controls <v4l2_ext_controls>`\ 
    :type c: struct v4l2_ext_controls \*

.. _`v4l2_g_ext_ctrls.description`:

Description
-----------

If hdl == NULL then they will all return -EINVAL.

.. _`v4l2_try_ext_ctrls`:

v4l2_try_ext_ctrls
==================

.. c:function:: int v4l2_try_ext_ctrls(struct v4l2_ctrl_handler *hdl, struct media_device *mdev, struct v4l2_ext_controls *c)

    Helper function to implement :ref:`VIDIOC_TRY_EXT_CTRLS <vidioc_g_ext_ctrls>` ioctl

    :param hdl:
        pointer to \ :c:type:`struct v4l2_ctrl_handler <v4l2_ctrl_handler>`\ 
    :type hdl: struct v4l2_ctrl_handler \*

    :param mdev:
        pointer to \ :c:type:`struct media_device <media_device>`\ 
    :type mdev: struct media_device \*

    :param c:
        pointer to \ :c:type:`struct v4l2_ext_controls <v4l2_ext_controls>`\ 
    :type c: struct v4l2_ext_controls \*

.. _`v4l2_try_ext_ctrls.description`:

Description
-----------

If hdl == NULL then they will all return -EINVAL.

.. _`v4l2_s_ext_ctrls`:

v4l2_s_ext_ctrls
================

.. c:function:: int v4l2_s_ext_ctrls(struct v4l2_fh *fh, struct v4l2_ctrl_handler *hdl, struct media_device *mdev, struct v4l2_ext_controls *c)

    Helper function to implement :ref:`VIDIOC_S_EXT_CTRLS <vidioc_g_ext_ctrls>` ioctl

    :param fh:
        pointer to \ :c:type:`struct v4l2_fh <v4l2_fh>`\ 
    :type fh: struct v4l2_fh \*

    :param hdl:
        pointer to \ :c:type:`struct v4l2_ctrl_handler <v4l2_ctrl_handler>`\ 
    :type hdl: struct v4l2_ctrl_handler \*

    :param mdev:
        pointer to \ :c:type:`struct media_device <media_device>`\ 
    :type mdev: struct media_device \*

    :param c:
        pointer to \ :c:type:`struct v4l2_ext_controls <v4l2_ext_controls>`\ 
    :type c: struct v4l2_ext_controls \*

.. _`v4l2_s_ext_ctrls.description`:

Description
-----------

If hdl == NULL then they will all return -EINVAL.

.. _`v4l2_ctrl_subdev_subscribe_event`:

v4l2_ctrl_subdev_subscribe_event
================================

.. c:function:: int v4l2_ctrl_subdev_subscribe_event(struct v4l2_subdev *sd, struct v4l2_fh *fh, struct v4l2_event_subscription *sub)

    Helper function to implement as a \ :c:type:`struct v4l2_subdev_core_ops <v4l2_subdev_core_ops>`\  subscribe_event function that just subscribes control events.

    :param sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 
    :type sd: struct v4l2_subdev \*

    :param fh:
        pointer to \ :c:type:`struct v4l2_fh <v4l2_fh>`\ 
    :type fh: struct v4l2_fh \*

    :param sub:
        pointer to \ :c:type:`struct v4l2_event_subscription <v4l2_event_subscription>`\ 
    :type sub: struct v4l2_event_subscription \*

.. _`v4l2_ctrl_subdev_log_status`:

v4l2_ctrl_subdev_log_status
===========================

.. c:function:: int v4l2_ctrl_subdev_log_status(struct v4l2_subdev *sd)

    Log all controls owned by subdev's control handler.

    :param sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 
    :type sd: struct v4l2_subdev \*

.. This file was automatic generated / don't edit.

