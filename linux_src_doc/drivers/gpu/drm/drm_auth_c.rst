.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_auth.c

.. _`master-and-authentication`:

master and authentication
=========================

\ :c:type:`struct drm_master <drm_master>`\  is used to track groups of clients with open
primary/legacy device nodes. For every \ :c:type:`struct drm_file <drm_file>`\  which has had at
least once successfully became the device master (either through the
SET_MASTER IOCTL, or implicitly through opening the primary device node when
no one else is the current master that time) there exists one \ :c:type:`struct drm_master <drm_master>`\ .
This is noted in \ :c:type:`drm_file.is_master <drm_file>`\ . All other clients have just a pointer
to the \ :c:type:`struct drm_master <drm_master>`\  they are associated with.

In addition only one \ :c:type:`struct drm_master <drm_master>`\  can be the current master for a \ :c:type:`struct drm_device <drm_device>`\ .
It can be switched through the DROP_MASTER and SET_MASTER IOCTL, or
implicitly through closing/openeing the primary device node. See also
\ :c:func:`drm_is_current_master`\ .

Clients can authenticate against the current master (if it matches their own)
using the GETMAGIC and AUTHMAGIC IOCTLs. Together with exchanging masters,
this allows controlled access to the device for an entire group of mutually
trusted clients.

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
        \ :c:type:`struct drm_master <drm_master>`\ 

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

