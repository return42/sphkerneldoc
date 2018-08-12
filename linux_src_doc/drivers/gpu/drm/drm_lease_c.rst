.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_lease.c

.. _`drm_lease_owner`:

drm_lease_owner
===============

.. c:function:: struct drm_master *drm_lease_owner(struct drm_master *master)

    return ancestor owner drm_master

    :param struct drm_master \*master:
        drm_master somewhere within tree of lessees and lessors

.. _`drm_lease_owner.return`:

Return
------


drm_master at the top of the tree (i.e, with lessor NULL

.. _`_drm_find_lessee`:

\_drm_find_lessee
=================

.. c:function:: struct drm_master*_drm_find_lessee(struct drm_master *master, int lessee_id)

    find lessee by id (idr_mutex held)

    :param struct drm_master \*master:
        drm_master of lessor

    :param int lessee_id:
        id

.. _`_drm_find_lessee.return`:

Return
------


drm_master of the lessee if valid, NULL otherwise

.. _`_drm_lease_held_master`:

\_drm_lease_held_master
=======================

.. c:function:: int _drm_lease_held_master(struct drm_master *master, int id)

    check to see if an object is leased (or owned) by master (idr_mutex held)

    :param struct drm_master \*master:
        the master to check the lease status of

    :param int id:
        the id to check

.. _`_drm_lease_held_master.description`:

Description
-----------

Checks if the specified master holds a lease on the object. Return

.. _`_drm_lease_held_master.value`:

value
-----


true            'master' holds a lease on (or owns) the object
false           'master' does not hold a lease.

.. _`_drm_has_leased`:

\_drm_has_leased
================

.. c:function:: bool _drm_has_leased(struct drm_master *master, int id)

    check to see if an object has been leased (idr_mutex held)

    :param struct drm_master \*master:
        the master to check the lease status of

    :param int id:
        the id to check

.. _`_drm_has_leased.description`:

Description
-----------

Checks if any lessee of 'master' holds a lease on 'id'. Return

.. _`_drm_has_leased.value`:

value
-----


true            Some lessee holds a lease on the object.
false           No lessee has a lease on the object.

.. _`_drm_lease_held`:

\_drm_lease_held
================

.. c:function:: bool _drm_lease_held(struct drm_file *file_priv, int id)

    check drm_mode_object lease status (idr_mutex held)

    :param struct drm_file \*file_priv:
        the master drm_file

    :param int id:
        the object id

.. _`_drm_lease_held.description`:

Description
-----------

Checks if the specified master holds a lease on the object. Return

.. _`_drm_lease_held.value`:

value
-----


true            'master' holds a lease on (or owns) the object
false           'master' does not hold a lease.

.. _`drm_lease_held`:

drm_lease_held
==============

.. c:function:: bool drm_lease_held(struct drm_file *file_priv, int id)

    check drm_mode_object lease status (idr_mutex not held)

    :param struct drm_file \*file_priv:
        the master drm_file

    :param int id:
        the object id

.. _`drm_lease_held.description`:

Description
-----------

Checks if the specified master holds a lease on the object. Return

.. _`drm_lease_held.value`:

value
-----


true            'master' holds a lease on (or owns) the object
false           'master' does not hold a lease.

.. _`drm_lease_filter_crtcs`:

drm_lease_filter_crtcs
======================

.. c:function:: uint32_t drm_lease_filter_crtcs(struct drm_file *file_priv, uint32_t crtcs_in)

    restricted crtc set to leased values (idr_mutex not held)

    :param struct drm_file \*file_priv:
        requestor file

    :param uint32_t crtcs_in:
        bitmask of crtcs to check

.. _`drm_lease_filter_crtcs.description`:

Description
-----------

Reconstructs a crtc mask based on the crtcs which are visible
through the specified file.

.. _`drm_lease_destroy`:

drm_lease_destroy
=================

.. c:function:: void drm_lease_destroy(struct drm_master *master)

    a master is going away (idr_mutex not held)

    :param struct drm_master \*master:
        the drm_master being destroyed

.. _`drm_lease_destroy.description`:

Description
-----------

All lessees will have been destroyed as they
hold a reference on their lessor. Notify any
lessor for this master so that it can check
the list of lessees.

.. _`_drm_lease_revoke`:

\_drm_lease_revoke
==================

.. c:function:: void _drm_lease_revoke(struct drm_master *top)

    revoke access to all leased objects (idr_mutex held)

    :param struct drm_master \*top:
        the master losing its lease

.. _`drm_lease_revoke`:

drm_lease_revoke
================

.. c:function:: void drm_lease_revoke(struct drm_master *top)

    revoke access to all leased objects (idr_mutex not held)

    :param struct drm_master \*top:
        the master losing its lease

.. _`drm_mode_create_lease_ioctl`:

drm_mode_create_lease_ioctl
===========================

.. c:function:: int drm_mode_create_lease_ioctl(struct drm_device *dev, void *data, struct drm_file *lessor_priv)

    create a new lease

    :param struct drm_device \*dev:
        the drm device

    :param void \*data:
        pointer to struct drm_mode_create_lease

    :param struct drm_file \*lessor_priv:
        the file being manipulated

.. _`drm_mode_create_lease_ioctl.description`:

Description
-----------

The master associated with the specified file will have a lease
created containing the objects specified in the ioctl structure.
A file descriptor will be allocated for that and returned to the
application.

.. _`drm_mode_list_lessees_ioctl`:

drm_mode_list_lessees_ioctl
===========================

.. c:function:: int drm_mode_list_lessees_ioctl(struct drm_device *dev, void *data, struct drm_file *lessor_priv)

    list lessee ids

    :param struct drm_device \*dev:
        the drm device

    :param void \*data:
        pointer to struct drm_mode_list_lessees

    :param struct drm_file \*lessor_priv:
        the file being manipulated

.. _`drm_mode_list_lessees_ioctl.description`:

Description
-----------

Starting from the master associated with the specified file,
the master with the provided lessee_id is found, and then
an array of lessee ids associated with leases from that master
are returned.

.. _`drm_mode_get_lease_ioctl`:

drm_mode_get_lease_ioctl
========================

.. c:function:: int drm_mode_get_lease_ioctl(struct drm_device *dev, void *data, struct drm_file *lessee_priv)

    list leased objects

    :param struct drm_device \*dev:
        the drm device

    :param void \*data:
        pointer to struct drm_mode_get_lease

    :param struct drm_file \*lessee_priv:
        the file being manipulated

.. _`drm_mode_get_lease_ioctl.description`:

Description
-----------

Return the list of leased objects for the specified lessee

.. _`drm_mode_revoke_lease_ioctl`:

drm_mode_revoke_lease_ioctl
===========================

.. c:function:: int drm_mode_revoke_lease_ioctl(struct drm_device *dev, void *data, struct drm_file *lessor_priv)

    revoke lease

    :param struct drm_device \*dev:
        the drm device

    :param void \*data:
        pointer to struct drm_mode_revoke_lease

    :param struct drm_file \*lessor_priv:
        the file being manipulated

.. _`drm_mode_revoke_lease_ioctl.description`:

Description
-----------

This removes all of the objects from the lease without
actually getting rid of the lease itself; that way all
references to it still work correctly

.. This file was automatic generated / don't edit.

