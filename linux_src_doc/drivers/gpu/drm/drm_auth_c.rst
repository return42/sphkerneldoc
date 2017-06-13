.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_auth.c

.. _`drm_is_current_master`:

drm_is_current_master
=====================

.. c:function:: bool drm_is_current_master(struct drm_file *fpriv)

    checks whether \ ``priv``\  is the current master

    :param struct drm_file \*fpriv:
        DRM file private

.. _`drm_is_current_master.description`:

Description
-----------

Checks whether \ ``fpriv``\  is current master on its device. This decides whether a
client is allowed to run DRM_MASTER IOCTLs.

Most of the modern IOCTL which require DRM_MASTER are for kernel modesetting
- the current master is assumed to own the non-shareable display hardware.

.. _`drm_master_get`:

drm_master_get
==============

.. c:function:: struct drm_master *drm_master_get(struct drm_master *master)

    reference a master pointer

    :param struct drm_master \*master:
        &struct drm_master

.. _`drm_master_get.description`:

Description
-----------

Increments the reference count of \ ``master``\  and returns a pointer to \ ``master``\ .

.. _`drm_master_put`:

drm_master_put
==============

.. c:function:: void drm_master_put(struct drm_master **master)

    unreference and clear a master pointer

    :param struct drm_master \*\*master:
        pointer to a pointer of \ :c:type:`struct drm_master <drm_master>`\ 

.. _`drm_master_put.description`:

Description
-----------

This decrements the \ :c:type:`struct drm_master <drm_master>`\  behind \ ``master``\  and sets it to NULL.

.. This file was automatic generated / don't edit.

