.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ceph/cls_lock_client.c

.. _`ceph_cls_lock`:

ceph_cls_lock
=============

.. c:function:: int ceph_cls_lock(struct ceph_osd_client *osdc, struct ceph_object_id *oid, struct ceph_object_locator *oloc, char *lock_name, u8 type, char *cookie, char *tag, char *desc, u8 flags)

    grab rados lock for object

    :param struct ceph_osd_client \*osdc:
        *undescribed*

    :param struct ceph_object_id \*oid:
        object to lock

    :param struct ceph_object_locator \*oloc:
        *undescribed*

    :param char \*lock_name:
        the name of the lock

    :param u8 type:
        lock type (CEPH_CLS_LOCK_EXCLUSIVE or CEPH_CLS_LOCK_SHARED)

    :param char \*cookie:
        user-defined identifier for this instance of the lock

    :param char \*tag:
        user-defined tag

    :param char \*desc:
        user-defined lock description

    :param u8 flags:
        lock flags

.. _`ceph_cls_lock.description`:

Description
-----------

All operations on the same lock should use the same tag.

.. _`ceph_cls_unlock`:

ceph_cls_unlock
===============

.. c:function:: int ceph_cls_unlock(struct ceph_osd_client *osdc, struct ceph_object_id *oid, struct ceph_object_locator *oloc, char *lock_name, char *cookie)

    release rados lock for object

    :param struct ceph_osd_client \*osdc:
        *undescribed*

    :param struct ceph_object_id \*oid:
        object to lock

    :param struct ceph_object_locator \*oloc:
        *undescribed*

    :param char \*lock_name:
        the name of the lock

    :param char \*cookie:
        user-defined identifier for this instance of the lock

.. _`ceph_cls_break_lock`:

ceph_cls_break_lock
===================

.. c:function:: int ceph_cls_break_lock(struct ceph_osd_client *osdc, struct ceph_object_id *oid, struct ceph_object_locator *oloc, char *lock_name, char *cookie, struct ceph_entity_name *locker)

    release rados lock for object for specified client

    :param struct ceph_osd_client \*osdc:
        *undescribed*

    :param struct ceph_object_id \*oid:
        object to lock

    :param struct ceph_object_locator \*oloc:
        *undescribed*

    :param char \*lock_name:
        the name of the lock

    :param char \*cookie:
        user-defined identifier for this instance of the lock

    :param struct ceph_entity_name \*locker:
        current lock owner

.. This file was automatic generated / don't edit.

