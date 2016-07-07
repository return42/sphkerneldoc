.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_context.c

.. _`drm_legacy_ctxbitmap_free`:

drm_legacy_ctxbitmap_free
=========================

.. c:function:: void drm_legacy_ctxbitmap_free(struct drm_device *dev, int ctx_handle)

    :param struct drm_device \*dev:
        *undescribed*

    :param int ctx_handle:
        *undescribed*

.. _`drm_legacy_ctxbitmap_free.description`:

Description
-----------

\param dev DRM device.
\param ctx_handle context handle.

Clears the bit specified by \p ctx_handle in drm_device::ctx_bitmap and the entry
in drm_device::ctx_idr, while holding the drm_device::struct_mutex
lock.

.. _`drm_legacy_ctxbitmap_next`:

drm_legacy_ctxbitmap_next
=========================

.. c:function:: int drm_legacy_ctxbitmap_next(struct drm_device *dev)

    :param struct drm_device \*dev:
        *undescribed*

.. _`drm_legacy_ctxbitmap_next.description`:

Description
-----------

\param dev DRM device.
\return (non-negative) context handle on success or a negative number on failure.

Allocate a new idr from drm_device::ctx_idr while holding the
drm_device::struct_mutex lock.

.. _`drm_legacy_ctxbitmap_init`:

drm_legacy_ctxbitmap_init
=========================

.. c:function:: void drm_legacy_ctxbitmap_init(struct drm_device *dev)

    :param struct drm_device \*dev:
        *undescribed*

.. _`drm_legacy_ctxbitmap_init.description`:

Description
-----------

\param dev DRM device.

Initialise the drm_device::ctx_idr

.. _`drm_legacy_ctxbitmap_cleanup`:

drm_legacy_ctxbitmap_cleanup
============================

.. c:function:: void drm_legacy_ctxbitmap_cleanup(struct drm_device *dev)

    :param struct drm_device \*dev:
        *undescribed*

.. _`drm_legacy_ctxbitmap_cleanup.description`:

Description
-----------

\param dev DRM device.

Free all idr members using drm_ctx_sarea_free helper function
while holding the drm_device::struct_mutex lock.

.. _`drm_legacy_ctxbitmap_flush`:

drm_legacy_ctxbitmap_flush
==========================

.. c:function:: void drm_legacy_ctxbitmap_flush(struct drm_device *dev, struct drm_file *file)

    Flush all contexts owned by a file

    :param struct drm_device \*dev:
        DRM device to operate on

    :param struct drm_file \*file:
        Open file to flush contexts for

.. _`drm_legacy_ctxbitmap_flush.description`:

Description
-----------

This iterates over all contexts on \ ``dev``\  and drops them if they're owned by
\ ``file``\ . Note that after this call returns, new contexts might be added if
the file is still alive.

.. _`drm_legacy_getsareactx`:

drm_legacy_getsareactx
======================

.. c:function:: int drm_legacy_getsareactx(struct drm_device *dev, void *data, struct drm_file *file_priv)

    context SAREA.

    :param struct drm_device \*dev:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param struct drm_file \*file_priv:
        *undescribed*

.. _`drm_legacy_getsareactx.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg user argument pointing to a drm_ctx_priv_map structure.
\return zero on success or a negative number on failure.

Gets the map from drm_device::ctx_idr with the handle specified and
returns its handle.

.. _`drm_legacy_setsareactx`:

drm_legacy_setsareactx
======================

.. c:function:: int drm_legacy_setsareactx(struct drm_device *dev, void *data, struct drm_file *file_priv)

    context SAREA.

    :param struct drm_device \*dev:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param struct drm_file \*file_priv:
        *undescribed*

.. _`drm_legacy_setsareactx.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg user argument pointing to a drm_ctx_priv_map structure.
\return zero on success or a negative number on failure.

Searches the mapping specified in \p arg and update the entry in
drm_device::ctx_idr with it.

.. _`drm_context_switch`:

drm_context_switch
==================

.. c:function:: int drm_context_switch(struct drm_device *dev, int old, int new)

    :param struct drm_device \*dev:
        *undescribed*

    :param int old:
        *undescribed*

    :param int new:
        *undescribed*

.. _`drm_context_switch.description`:

Description
-----------

\param dev DRM device.
\param old old context handle.
\param new new context handle.
\return zero on success or a negative number on failure.

Attempt to set drm_device::context_flag.

.. _`drm_context_switch_complete`:

drm_context_switch_complete
===========================

.. c:function:: int drm_context_switch_complete(struct drm_device *dev, struct drm_file *file_priv, int new)

    :param struct drm_device \*dev:
        *undescribed*

    :param struct drm_file \*file_priv:
        *undescribed*

    :param int new:
        *undescribed*

.. _`drm_context_switch_complete.description`:

Description
-----------

\param dev DRM device.
\param new new context handle.
\return zero on success or a negative number on failure.

Updates drm_device::last_context and drm_device::last_switch. Verifies the
hardware lock is held, clears the drm_device::context_flag and wakes up
drm_device::context_wait.

.. _`drm_legacy_resctx`:

drm_legacy_resctx
=================

.. c:function:: int drm_legacy_resctx(struct drm_device *dev, void *data, struct drm_file *file_priv)

    :param struct drm_device \*dev:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param struct drm_file \*file_priv:
        *undescribed*

.. _`drm_legacy_resctx.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg user argument pointing to a drm_ctx_res structure.
\return zero on success or a negative number on failure.

.. _`drm_legacy_addctx`:

drm_legacy_addctx
=================

.. c:function:: int drm_legacy_addctx(struct drm_device *dev, void *data, struct drm_file *file_priv)

    :param struct drm_device \*dev:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param struct drm_file \*file_priv:
        *undescribed*

.. _`drm_legacy_addctx.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg user argument pointing to a drm_ctx structure.
\return zero on success or a negative number on failure.

Get a new handle for the context and copy to userspace.

.. _`drm_legacy_getctx`:

drm_legacy_getctx
=================

.. c:function:: int drm_legacy_getctx(struct drm_device *dev, void *data, struct drm_file *file_priv)

    :param struct drm_device \*dev:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param struct drm_file \*file_priv:
        *undescribed*

.. _`drm_legacy_getctx.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg user argument pointing to a drm_ctx structure.
\return zero on success or a negative number on failure.

.. _`drm_legacy_switchctx`:

drm_legacy_switchctx
====================

.. c:function:: int drm_legacy_switchctx(struct drm_device *dev, void *data, struct drm_file *file_priv)

    :param struct drm_device \*dev:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param struct drm_file \*file_priv:
        *undescribed*

.. _`drm_legacy_switchctx.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg user argument pointing to a drm_ctx structure.
\return zero on success or a negative number on failure.

Calls \ :c:func:`context_switch`\ .

.. _`drm_legacy_newctx`:

drm_legacy_newctx
=================

.. c:function:: int drm_legacy_newctx(struct drm_device *dev, void *data, struct drm_file *file_priv)

    :param struct drm_device \*dev:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param struct drm_file \*file_priv:
        *undescribed*

.. _`drm_legacy_newctx.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg user argument pointing to a drm_ctx structure.
\return zero on success or a negative number on failure.

Calls \ :c:func:`context_switch_complete`\ .

.. _`drm_legacy_rmctx`:

drm_legacy_rmctx
================

.. c:function:: int drm_legacy_rmctx(struct drm_device *dev, void *data, struct drm_file *file_priv)

    :param struct drm_device \*dev:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param struct drm_file \*file_priv:
        *undescribed*

.. _`drm_legacy_rmctx.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg user argument pointing to a drm_ctx structure.
\return zero on success or a negative number on failure.

If not the special kernel context, calls \ :c:func:`ctxbitmap_free`\  to free the specified context.

.. This file was automatic generated / don't edit.

