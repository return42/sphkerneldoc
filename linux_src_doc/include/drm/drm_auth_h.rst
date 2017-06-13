.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_auth.h

.. _`drm_master`:

struct drm_master
=================

.. c:type:: struct drm_master

    drm master structure

.. _`drm_master.definition`:

Definition
----------

.. code-block:: c

    struct drm_master {
        struct kref refcount;
        struct drm_device *dev;
        char *unique;
        int unique_len;
        struct idr magic_map;
        struct drm_lock_data lock;
        void *driver_priv;
    }

.. _`drm_master.members`:

Members
-------

refcount
    Refcount for this master object.

dev
    Link back to the DRM device

unique
    Unique identifier: e.g. busid. Protected by&drm_device.master_mutex.

unique_len
    Length of unique field. Protected by&drm_device.master_mutex.

magic_map
    Map of used authentication tokens. Protected by&drm_device.master_mutex.

lock
    DRI1 lock information.

driver_priv
    Pointer to driver-private information.

.. _`drm_master.description`:

Description
-----------

Note that master structures are only relevant for the legacy/primary device
nodes, hence there can only be one per device, not one per drm_minor.

.. This file was automatic generated / don't edit.

