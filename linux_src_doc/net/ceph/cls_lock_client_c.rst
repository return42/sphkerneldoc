.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ceph/cls_lock_client.c

.. _`ceph_cls_lock`:

ceph_cls_lock
=============

.. c:function:: int ceph_cls_lock(struct ceph_osd_client *osdc, struct ceph_object_id *oid, struct ceph_object_locator *oloc, char *lock_name, u8 type, char *cookie, char *tag, char *desc, u8 flags)

    grab rados lock for object

    :param osdc:
        *undescribed*
    :type osdc: struct ceph_osd_client \*

    :param oid:
        object to lock
    :type oid: struct ceph_object_id \*

    :param oloc:
        *undescribed*
    :type oloc: struct ceph_object_locator \*

    :param lock_name:
        the name of the lock
    :type lock_name: char \*

    :param type:
        lock type (CEPH_CLS_LOCK_EXCLUSIVE or CEPH_CLS_LOCK_SHARED)
    :type type: u8

    :param cookie:
        user-defined identifier for this instance of the lock
    :type cookie: char \*

    :param tag:
        user-defined tag
    :type tag: char \*

    :param desc:
        user-defined lock description
    :type desc: char \*

    :param flags:
        lock flags
    :type flags: u8

.. _`ceph_cls_lock.description`:

Description
-----------

All operations on the same lock should use the same tag.

.. _`ceph_cls_unlock`:

ceph_cls_unlock
===============

.. c:function:: int ceph_cls_unlock(struct ceph_osd_client *osdc, struct ceph_object_id *oid, struct ceph_object_locator *oloc, char *lock_name, char *cookie)

    release rados lock for object

    :param osdc:
        *undescribed*
    :type osdc: struct ceph_osd_client \*

    :param oid:
        object to lock
    :type oid: struct ceph_object_id \*

    :param oloc:
        *undescribed*
    :type oloc: struct ceph_object_locator \*

    :param lock_name:
        the name of the lock
    :type lock_name: char \*

    :param cookie:
        user-defined identifier for this instance of the lock
    :type cookie: char \*

.. _`ceph_cls_break_lock`:

ceph_cls_break_lock
===================

.. c:function:: int ceph_cls_break_lock(struct ceph_osd_client *osdc, struct ceph_object_id *oid, struct ceph_object_locator *oloc, char *lock_name, char *cookie, struct ceph_entity_name *locker)

    release rados lock for object for specified client

    :param osdc:
        *undescribed*
    :type osdc: struct ceph_osd_client \*

    :param oid:
        object to lock
    :type oid: struct ceph_object_id \*

    :param oloc:
        *undescribed*
    :type oloc: struct ceph_object_locator \*

    :param lock_name:
        the name of the lock
    :type lock_name: char \*

    :param cookie:
        user-defined identifier for this instance of the lock
    :type cookie: char \*

    :param locker:
        current lock owner
    :type locker: struct ceph_entity_name \*

.. This file was automatic generated / don't edit.

