.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_simple_resource.c

.. _`vmw_user_simple_resource`:

struct vmw_user_simple_resource
===============================

.. c:type:: struct vmw_user_simple_resource

    User-space simple resource struct

.. _`vmw_user_simple_resource.definition`:

Definition
----------

.. code-block:: c

    struct vmw_user_simple_resource {
        struct ttm_base_object base;
        size_t account_size;
        struct vmw_simple_resource simple;
    }

.. _`vmw_user_simple_resource.members`:

Members
-------

base
    The TTM base object implementing user-space visibility.

account_size
    How much memory was accounted for this object.

simple
    The embedded struct vmw_simple_resource.

.. _`vmw_simple_resource_init`:

vmw_simple_resource_init
========================

.. c:function:: int vmw_simple_resource_init(struct vmw_private *dev_priv, struct vmw_simple_resource *simple, void *data, void (*res_free)(struct vmw_resource *res))

    Initialize a simple resource object.

    :param dev_priv:
        Pointer to a struct device private.
    :type dev_priv: struct vmw_private \*

    :param simple:
        The struct vmw_simple_resource to initialize.
    :type simple: struct vmw_simple_resource \*

    :param data:
        Data passed to the information initialization function.
    :type data: void \*

    :param void (\*res_free)(struct vmw_resource \*res):
        Function pointer to destroy the simple resource.

.. _`vmw_simple_resource_init.return`:

Return
------

0 if succeeded.
Negative error value if error, in which case the resource will have been
freed.

.. _`vmw_simple_resource_free`:

vmw_simple_resource_free
========================

.. c:function:: void vmw_simple_resource_free(struct vmw_resource *res)

    Free a simple resource object.

    :param res:
        The struct vmw_resource member of the simple resource object.
    :type res: struct vmw_resource \*

.. _`vmw_simple_resource_free.description`:

Description
-----------

Frees memory and memory accounting for the object.

.. _`vmw_simple_resource_base_release`:

vmw_simple_resource_base_release
================================

.. c:function:: void vmw_simple_resource_base_release(struct ttm_base_object **p_base)

    TTM object release callback

    :param p_base:
        The struct ttm_base_object member of the simple resource object.
    :type p_base: struct ttm_base_object \*\*

.. _`vmw_simple_resource_base_release.description`:

Description
-----------

Called when the last reference to the embedded struct ttm_base_object is
gone. Typically results in an object free, unless there are other
references to the embedded struct vmw_resource.

.. _`vmw_simple_resource_create_ioctl`:

vmw_simple_resource_create_ioctl
================================

.. c:function:: int vmw_simple_resource_create_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv, const struct vmw_simple_resource_func *func)

    Helper to set up an ioctl function to create a struct vmw_simple_resource.

    :param dev:
        Pointer to a struct drm device.
    :type dev: struct drm_device \*

    :param data:
        Ioctl argument.
    :type data: void \*

    :param file_priv:
        Pointer to a struct drm_file identifying the caller.
    :type file_priv: struct drm_file \*

    :param func:
        Pointer to a struct vmw_simple_resource_func identifying the
        simple resource type.
    :type func: const struct vmw_simple_resource_func \*

.. _`vmw_simple_resource_create_ioctl.return`:

Return
------

0 if success,
Negative error value on error.

.. _`vmw_simple_resource_lookup`:

vmw_simple_resource_lookup
==========================

.. c:function:: struct vmw_resource *vmw_simple_resource_lookup(struct ttm_object_file *tfile, uint32_t handle, const struct vmw_simple_resource_func *func)

    Look up a simple resource from its user-space handle.

    :param tfile:
        struct ttm_object_file identifying the caller.
    :type tfile: struct ttm_object_file \*

    :param handle:
        The user-space handle.
    :type handle: uint32_t

    :param func:
        The struct vmw_simple_resource_func identifying the simple resource
        type.
    :type func: const struct vmw_simple_resource_func \*

.. _`vmw_simple_resource_lookup.return`:

Return
------

Refcounted pointer to the embedded struct vmw_resource if
successfule. Error pointer otherwise.

.. This file was automatic generated / don't edit.

