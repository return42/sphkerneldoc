.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_global.c

.. _`drm_global_item_ref`:

drm_global_item_ref
===================

.. c:function:: int drm_global_item_ref(struct drm_global_reference *ref)

    Initialize and acquire reference to memory object

    :param struct drm_global_reference \*ref:
        Object for initialization

.. _`drm_global_item_ref.description`:

Description
-----------

This initializes a memory object, allocating memory and calling the
.init() hook. Further calls will increase the reference count for
that item.

.. _`drm_global_item_ref.return`:

Return
------

Zero on success, non-zero otherwise.

.. _`drm_global_item_unref`:

drm_global_item_unref
=====================

.. c:function:: void drm_global_item_unref(struct drm_global_reference *ref)

    Drop reference to memory object

    :param struct drm_global_reference \*ref:
        Object being removed

.. _`drm_global_item_unref.description`:

Description
-----------

Drop a reference to the memory object and eventually call the
\ :c:func:`release`\  hook.  The allocated object should be dropped in the
\ :c:func:`release`\  hook or before calling this function

.. This file was automatic generated / don't edit.

