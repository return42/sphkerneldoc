.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_cmdbuf_res.c

.. _`vmw_cmdbuf_res`:

struct vmw_cmdbuf_res
=====================

.. c:type:: struct vmw_cmdbuf_res

    Command buffer managed resource entry.

.. _`vmw_cmdbuf_res.definition`:

Definition
----------

.. code-block:: c

    struct vmw_cmdbuf_res {
        struct vmw_resource *res;
        struct drm_hash_item hash;
        struct list_head head;
        enum vmw_cmdbuf_res_state state;
        struct vmw_cmdbuf_res_manager *man;
    }

.. _`vmw_cmdbuf_res.members`:

Members
-------

res
    Refcounted pointer to a struct vmw_resource.

hash
    Hash entry for the manager hash table.

head
    List head used either by the staging list or the manager list
    of commited resources.

state
    Staging state of this resource entry.

man
    Pointer to a resource manager for this entry.

.. _`vmw_cmdbuf_res_manager`:

struct vmw_cmdbuf_res_manager
=============================

.. c:type:: struct vmw_cmdbuf_res_manager

    Command buffer resource manager.

.. _`vmw_cmdbuf_res_manager.definition`:

Definition
----------

.. code-block:: c

    struct vmw_cmdbuf_res_manager {
        struct drm_open_hash resources;
        struct list_head list;
        struct vmw_private *dev_priv;
    }

.. _`vmw_cmdbuf_res_manager.members`:

Members
-------

resources
    Hash table containing staged and commited command buffer
    resources

list
    List of commited command buffer resources.

dev_priv
    Pointer to a device private structure.

.. _`vmw_cmdbuf_res_manager.description`:

Description
-----------

\ ``resources``\  and \ ``list``\  are protected by the cmdbuf mutex for now.

.. _`vmw_cmdbuf_res_lookup`:

vmw_cmdbuf_res_lookup
=====================

.. c:function:: struct vmw_resource *vmw_cmdbuf_res_lookup(struct vmw_cmdbuf_res_manager *man, enum vmw_cmdbuf_res_type res_type, u32 user_key)

    Look up a command buffer resource

    :param man:
        Pointer to the command buffer resource manager
    :type man: struct vmw_cmdbuf_res_manager \*

    :param res_type:
        *undescribed*
    :type res_type: enum vmw_cmdbuf_res_type

    :param user_key:
        The user key.
    :type user_key: u32

.. _`vmw_cmdbuf_res_lookup.description`:

Description
-----------

Returns a valid refcounted struct vmw_resource pointer on success,
an error pointer on failure.

.. _`vmw_cmdbuf_res_free`:

vmw_cmdbuf_res_free
===================

.. c:function:: void vmw_cmdbuf_res_free(struct vmw_cmdbuf_res_manager *man, struct vmw_cmdbuf_res *entry)

    Free a command buffer resource.

    :param man:
        Pointer to the command buffer resource manager
    :type man: struct vmw_cmdbuf_res_manager \*

    :param entry:
        Pointer to a struct vmw_cmdbuf_res.
    :type entry: struct vmw_cmdbuf_res \*

.. _`vmw_cmdbuf_res_free.description`:

Description
-----------

Frees a struct vmw_cmdbuf_res entry and drops its reference to the
struct vmw_resource.

.. _`vmw_cmdbuf_res_commit`:

vmw_cmdbuf_res_commit
=====================

.. c:function:: void vmw_cmdbuf_res_commit(struct list_head *list)

    Commit a list of command buffer resource actions

    :param list:
        Caller's list of command buffer resource actions.
    :type list: struct list_head \*

.. _`vmw_cmdbuf_res_commit.description`:

Description
-----------

This function commits a list of command buffer resource
additions or removals.
It is typically called when the execbuf ioctl call triggering these
actions has commited the fifo contents to the device.

.. _`vmw_cmdbuf_res_revert`:

vmw_cmdbuf_res_revert
=====================

.. c:function:: void vmw_cmdbuf_res_revert(struct list_head *list)

    Revert a list of command buffer resource actions

    :param list:
        Caller's list of command buffer resource action
    :type list: struct list_head \*

.. _`vmw_cmdbuf_res_revert.description`:

Description
-----------

This function reverts a list of command buffer resource
additions or removals.
It is typically called when the execbuf ioctl call triggering these
actions failed for some reason, and the command stream was never
submitted.

.. _`vmw_cmdbuf_res_add`:

vmw_cmdbuf_res_add
==================

.. c:function:: int vmw_cmdbuf_res_add(struct vmw_cmdbuf_res_manager *man, enum vmw_cmdbuf_res_type res_type, u32 user_key, struct vmw_resource *res, struct list_head *list)

    Stage a command buffer managed resource for addition.

    :param man:
        Pointer to the command buffer resource manager.
    :type man: struct vmw_cmdbuf_res_manager \*

    :param res_type:
        The resource type.
    :type res_type: enum vmw_cmdbuf_res_type

    :param user_key:
        The user-space id of the resource.
    :type user_key: u32

    :param res:
        Valid (refcount != 0) pointer to a struct vmw_resource.
    :type res: struct vmw_resource \*

    :param list:
        The staging list.
    :type list: struct list_head \*

.. _`vmw_cmdbuf_res_add.description`:

Description
-----------

This function allocates a struct vmw_cmdbuf_res entry and adds the
resource to the hash table of the manager identified by \ ``man``\ . The
entry is then put on the staging list identified by \ ``list``\ .

.. _`vmw_cmdbuf_res_remove`:

vmw_cmdbuf_res_remove
=====================

.. c:function:: int vmw_cmdbuf_res_remove(struct vmw_cmdbuf_res_manager *man, enum vmw_cmdbuf_res_type res_type, u32 user_key, struct list_head *list, struct vmw_resource **res_p)

    Stage a command buffer managed resource for removal.

    :param man:
        Pointer to the command buffer resource manager.
    :type man: struct vmw_cmdbuf_res_manager \*

    :param res_type:
        The resource type.
    :type res_type: enum vmw_cmdbuf_res_type

    :param user_key:
        The user-space id of the resource.
    :type user_key: u32

    :param list:
        The staging list.
    :type list: struct list_head \*

    :param res_p:
        If the resource is in an already committed state, points to the
        struct vmw_resource on successful return. The pointer will be
        non ref-counted.
    :type res_p: struct vmw_resource \*\*

.. _`vmw_cmdbuf_res_remove.description`:

Description
-----------

This function looks up the struct vmw_cmdbuf_res entry from the manager
hash table and, if it exists, removes it. Depending on its current staging
state it then either removes the entry from the staging list or adds it
to it with a staging state of removal.

.. _`vmw_cmdbuf_res_man_create`:

vmw_cmdbuf_res_man_create
=========================

.. c:function:: struct vmw_cmdbuf_res_manager *vmw_cmdbuf_res_man_create(struct vmw_private *dev_priv)

    Allocate a command buffer managed resource manager.

    :param dev_priv:
        Pointer to a struct vmw_private
    :type dev_priv: struct vmw_private \*

.. _`vmw_cmdbuf_res_man_create.description`:

Description
-----------

Allocates and initializes a command buffer managed resource manager. Returns
an error pointer on failure.

.. _`vmw_cmdbuf_res_man_destroy`:

vmw_cmdbuf_res_man_destroy
==========================

.. c:function:: void vmw_cmdbuf_res_man_destroy(struct vmw_cmdbuf_res_manager *man)

    Destroy a command buffer managed resource manager.

    :param man:
        Pointer to the  manager to destroy.
    :type man: struct vmw_cmdbuf_res_manager \*

.. _`vmw_cmdbuf_res_man_destroy.description`:

Description
-----------

This function destroys a command buffer managed resource manager and
unreferences / frees all command buffer managed resources and -entries
associated with it.

.. This file was automatic generated / don't edit.

