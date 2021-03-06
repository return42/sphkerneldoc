.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_so.c

.. _`vmw_view`:

struct vmw_view
===============

.. c:type:: struct vmw_view

    view metadata

.. _`vmw_view.definition`:

Definition
----------

.. code-block:: c

    struct vmw_view {
        struct rcu_head rcu;
        struct vmw_resource res;
        struct vmw_resource *ctx;
        struct vmw_resource *srf;
        struct vmw_resource *cotable;
        struct list_head srf_head;
        struct list_head cotable_head;
        unsigned view_type;
        unsigned view_id;
        u32 cmd_size;
        bool committed;
        u32 cmd[1];
    }

.. _`vmw_view.members`:

Members
-------

rcu
    *undescribed*

res
    The struct vmw_resource we derive from

ctx
    Non-refcounted pointer to the context this view belongs to.

srf
    Refcounted pointer to the surface pointed to by this view.

cotable
    Refcounted pointer to the cotable holding this view.

srf_head
    List head for the surface-to-view list.

cotable_head
    List head for the cotable-to_view list.

view_type
    View type.

view_id
    User-space per context view id. Currently used also as per
    context device view id.

cmd_size
    Size of the SVGA3D define view command that we've copied from the
    command stream.

committed
    Whether the view is actually created or pending creation at the
    device level.

cmd
    The SVGA3D define view command copied from the command stream.

.. _`vmw_view_define`:

struct vmw_view_define
======================

.. c:type:: struct vmw_view_define

    view define command body stub

.. _`vmw_view_define.definition`:

Definition
----------

.. code-block:: c

    struct vmw_view_define {
        uint32 view_id;
        uint32 sid;
    }

.. _`vmw_view_define.members`:

Members
-------

view_id
    The device id of the view being defined

sid
    The surface id of the view being defined

.. _`vmw_view_define.description`:

Description
-----------

This generic struct is used by the code to change \ ``view_id``\  and \ ``sid``\  of a
saved view define command.

.. _`vmw_view`:

vmw_view
========

.. c:function:: struct vmw_view *vmw_view(struct vmw_resource *res)

    Convert a struct vmw_resource to a struct vmw_view

    :param res:
        Pointer to the resource to convert.
    :type res: struct vmw_resource \*

.. _`vmw_view.description`:

Description
-----------

Returns a pointer to a struct vmw_view.

.. _`vmw_view_commit_notify`:

vmw_view_commit_notify
======================

.. c:function:: void vmw_view_commit_notify(struct vmw_resource *res, enum vmw_cmdbuf_res_state state)

    Notify that a view operation has been committed to hardware from a user-supplied command stream.

    :param res:
        Pointer to the view resource.
    :type res: struct vmw_resource \*

    :param state:
        Indicating whether a creation or removal has been committed.
    :type state: enum vmw_cmdbuf_res_state

.. _`vmw_view_create`:

vmw_view_create
===============

.. c:function:: int vmw_view_create(struct vmw_resource *res)

    Create a hardware view.

    :param res:
        Pointer to the view resource.
    :type res: struct vmw_resource \*

.. _`vmw_view_create.description`:

Description
-----------

Create a hardware view. Typically used if that view has previously been
destroyed by an eviction operation.

.. _`vmw_view_destroy`:

vmw_view_destroy
================

.. c:function:: int vmw_view_destroy(struct vmw_resource *res)

    Destroy a hardware view.

    :param res:
        Pointer to the view resource.
    :type res: struct vmw_resource \*

.. _`vmw_view_destroy.description`:

Description
-----------

Destroy a hardware view. Typically used on unexpected termination of the
owning process or if the surface the view is pointing to is destroyed.

.. _`vmw_hw_view_destroy`:

vmw_hw_view_destroy
===================

.. c:function:: void vmw_hw_view_destroy(struct vmw_resource *res)

    Destroy a hardware view as part of resource cleanup.

    :param res:
        Pointer to the view resource.
    :type res: struct vmw_resource \*

.. _`vmw_hw_view_destroy.description`:

Description
-----------

Destroy a hardware view if it's still present.

.. _`vmw_view_key`:

vmw_view_key
============

.. c:function:: u32 vmw_view_key(u32 user_key, enum vmw_view_type view_type)

    Compute a view key suitable for the cmdbuf resource manager

    :param user_key:
        The user-space id used for the view.
    :type user_key: u32

    :param view_type:
        The view type.
    :type view_type: enum vmw_view_type

.. _`vmw_view_key.description`:

Description
-----------

Destroy a hardware view if it's still present.

.. _`vmw_view_id_ok`:

vmw_view_id_ok
==============

.. c:function:: bool vmw_view_id_ok(u32 user_key, enum vmw_view_type view_type)

    Basic view id and type range checks.

    :param user_key:
        The user-space id used for the view.
    :type user_key: u32

    :param view_type:
        The view type.
    :type view_type: enum vmw_view_type

.. _`vmw_view_id_ok.description`:

Description
-----------

Checks that the view id and type (typically provided by user-space) is
valid.

.. _`vmw_view_res_free`:

vmw_view_res_free
=================

.. c:function:: void vmw_view_res_free(struct vmw_resource *res)

    resource res_free callback for view resources

    :param res:
        Pointer to a struct vmw_resource
    :type res: struct vmw_resource \*

.. _`vmw_view_res_free.description`:

Description
-----------

Frees memory and memory accounting held by a struct vmw_view.

.. _`vmw_view_add`:

vmw_view_add
============

.. c:function:: int vmw_view_add(struct vmw_cmdbuf_res_manager *man, struct vmw_resource *ctx, struct vmw_resource *srf, enum vmw_view_type view_type, u32 user_key, const void *cmd, size_t cmd_size, struct list_head *list)

    Create a view resource and stage it for addition as a command buffer managed resource.

    :param man:
        Pointer to the compat shader manager identifying the shader namespace.
    :type man: struct vmw_cmdbuf_res_manager \*

    :param ctx:
        Pointer to a struct vmw_resource identifying the active context.
    :type ctx: struct vmw_resource \*

    :param srf:
        Pointer to a struct vmw_resource identifying the surface the view
        points to.
    :type srf: struct vmw_resource \*

    :param view_type:
        The view type deduced from the view create command.
    :type view_type: enum vmw_view_type

    :param user_key:
        The key that is used to identify the shader. The key is
        unique to the view type and to the context.
    :type user_key: u32

    :param cmd:
        Pointer to the view create command in the command stream.
    :type cmd: const void \*

    :param cmd_size:
        Size of the view create command in the command stream.
    :type cmd_size: size_t

    :param list:
        Caller's list of staged command buffer resource actions.
    :type list: struct list_head \*

.. _`vmw_view_remove`:

vmw_view_remove
===============

.. c:function:: int vmw_view_remove(struct vmw_cmdbuf_res_manager *man, u32 user_key, enum vmw_view_type view_type, struct list_head *list, struct vmw_resource **res_p)

    Stage a view for removal.

    :param man:
        Pointer to the view manager identifying the shader namespace.
    :type man: struct vmw_cmdbuf_res_manager \*

    :param user_key:
        The key that is used to identify the view. The key is
        unique to the view type.
    :type user_key: u32

    :param view_type:
        View type
    :type view_type: enum vmw_view_type

    :param list:
        Caller's list of staged command buffer resource actions.
    :type list: struct list_head \*

    :param res_p:
        If the resource is in an already committed state, points to the
        struct vmw_resource on successful return. The pointer will be
        non ref-counted.
    :type res_p: struct vmw_resource \*\*

.. _`vmw_view_cotable_list_destroy`:

vmw_view_cotable_list_destroy
=============================

.. c:function:: void vmw_view_cotable_list_destroy(struct vmw_private *dev_priv, struct list_head *list, bool readback)

    Evict all views belonging to a cotable.

    :param dev_priv:
        Pointer to a device private struct.
    :type dev_priv: struct vmw_private \*

    :param list:
        List of views belonging to a cotable.
    :type list: struct list_head \*

    :param readback:
        Unused. Needed for function interface only.
    :type readback: bool

.. _`vmw_view_cotable_list_destroy.description`:

Description
-----------

This function evicts all views belonging to a cotable.
It must be called with the binding_mutex held, and the caller must hold
a reference to the view resource. This is typically called before the
cotable is paged out.

.. _`vmw_view_surface_list_destroy`:

vmw_view_surface_list_destroy
=============================

.. c:function:: void vmw_view_surface_list_destroy(struct vmw_private *dev_priv, struct list_head *list)

    Evict all views pointing to a surface

    :param dev_priv:
        Pointer to a device private struct.
    :type dev_priv: struct vmw_private \*

    :param list:
        List of views pointing to a surface.
    :type list: struct list_head \*

.. _`vmw_view_surface_list_destroy.description`:

Description
-----------

This function evicts all views pointing to a surface. This is typically
called before the surface is evicted.

.. _`vmw_view_srf`:

vmw_view_srf
============

.. c:function:: struct vmw_resource *vmw_view_srf(struct vmw_resource *res)

    Return a non-refcounted pointer to the surface a view is pointing to.

    :param res:
        pointer to a view resource.
    :type res: struct vmw_resource \*

.. _`vmw_view_srf.description`:

Description
-----------

Note that the view itself is holding a reference, so as long
the view resource is alive, the surface resource will be.

.. _`vmw_view_lookup`:

vmw_view_lookup
===============

.. c:function:: struct vmw_resource *vmw_view_lookup(struct vmw_cmdbuf_res_manager *man, enum vmw_view_type view_type, u32 user_key)

    Look up a view.

    :param man:
        The context's cmdbuf ref manager.
    :type man: struct vmw_cmdbuf_res_manager \*

    :param view_type:
        The view type.
    :type view_type: enum vmw_view_type

    :param user_key:
        The view user id.
    :type user_key: u32

.. _`vmw_view_lookup.description`:

Description
-----------

returns a refcounted pointer to a view or an error pointer if not found.

.. This file was automatic generated / don't edit.

