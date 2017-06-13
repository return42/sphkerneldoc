.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_resource_priv.h

.. _`vmw_user_resource_conv`:

struct vmw_user_resource_conv
=============================

.. c:type:: struct vmw_user_resource_conv

    Identify a derived user-exported resource type and provide a function to convert its ttm_base_object pointer to a struct vmw_resource

.. _`vmw_user_resource_conv.definition`:

Definition
----------

.. code-block:: c

    struct vmw_user_resource_conv {
        enum ttm_object_type object_type;
        struct vmw_resource *(*base_obj_to_res)(struct ttm_base_object *base);
        void (*res_free)(struct vmw_resource *res);
    }

.. _`vmw_user_resource_conv.members`:

Members
-------

object_type
    *undescribed*

base_obj_to_res
    *undescribed*

res_free
    *undescribed*

.. _`vmw_res_func`:

struct vmw_res_func
===================

.. c:type:: struct vmw_res_func

    members and functions common for a resource type

.. _`vmw_res_func.definition`:

Definition
----------

.. code-block:: c

    struct vmw_res_func {
        enum vmw_res_type res_type;
        bool needs_backup;
        const char *type_name;
        struct ttm_placement *backup_placement;
        bool may_evict;
        int (*create)(struct vmw_resource *res);
        int (*destroy)(struct vmw_resource *res);
        int (*bind)(struct vmw_resource *res,struct ttm_validate_buffer *val_buf);
        int (*unbind)(struct vmw_resource *res,bool readback,struct ttm_validate_buffer *val_buf);
        void (*commit_notify)(struct vmw_resource *res,enum vmw_cmdbuf_res_state state);
    }

.. _`vmw_res_func.members`:

Members
-------

res_type
    Enum that identifies the lru list to use for eviction.

needs_backup
    Whether the resource is guest-backed and needs
    persistent buffer storage.

type_name
    String that identifies the resource type.

backup_placement
    TTM placement for backup buffers.
    \ ``may_evict``\           Whether the resource may be evicted.

may_evict
    *undescribed*

create
    Create a hardware resource.

destroy
    Destroy a hardware resource.

bind
    Bind a hardware resource to persistent buffer storage.

unbind
    Unbind a hardware resource from persistent
    buffer storage.

commit_notify
    If the resource is a command buffer managed resource,
    callback to notify that a define or remove command
    has been committed to the device.

.. _`vmw_simple_resource_func`:

struct vmw_simple_resource_func
===============================

.. c:type:: struct vmw_simple_resource_func

    members and functions common for the simple resource helpers.

.. _`vmw_simple_resource_func.definition`:

Definition
----------

.. code-block:: c

    struct vmw_simple_resource_func {
        const struct vmw_res_func res_func;
        int ttm_res_type;
        size_t size;
        int (*init)(struct vmw_resource *res, void *data);
        void (*hw_destroy)(struct vmw_resource *res);
        void (*set_arg_handle)(void *data, u32 handle);
    }

.. _`vmw_simple_resource_func.members`:

Members
-------

res_func
    struct vmw_res_func as described above.

ttm_res_type
    TTM resource type used for handle recognition.

size
    Size of the simple resource information struct.

init
    Initialize the simple resource information.

hw_destroy
    A resource hw_destroy function.

set_arg_handle
    Set the handle output argument of the ioctl create struct.

.. _`vmw_simple_resource`:

struct vmw_simple_resource
==========================

.. c:type:: struct vmw_simple_resource

    Kernel only side simple resource

.. _`vmw_simple_resource.definition`:

Definition
----------

.. code-block:: c

    struct vmw_simple_resource {
        struct vmw_resource res;
        const struct vmw_simple_resource_func *func;
    }

.. _`vmw_simple_resource.members`:

Members
-------

res
    The resource we derive from.

func
    The method and member virtual table.

.. This file was automatic generated / don't edit.

