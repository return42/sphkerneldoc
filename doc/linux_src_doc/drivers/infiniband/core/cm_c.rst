.. -*- coding: utf-8; mode: rst -*-

====
cm.c
====


.. _`__ib_cm_listen`:

__ib_cm_listen
==============

.. c:function:: int __ib_cm_listen (struct ib_cm_id *cm_id, __be64 service_id, __be64 service_mask)

    Initiates listening on the specified service ID for connection and service ID resolution requests.

    :param struct ib_cm_id \*cm_id:
        Connection identifier associated with the listen request.

    :param __be64 service_id:
        Service identifier matched against incoming connection
        and service ID resolution requests.  The service ID should be specified
        network-byte order.  If set to IB_CM_ASSIGN_SERVICE_ID, the CM will
        assign a service ID to the caller.

    :param __be64 service_mask:
        Mask applied to service ID used to listen across a
        range of service IDs.  If set to 0, the service ID is matched
        exactly.  This parameter is ignored if ``service_id`` is set to
        IB_CM_ASSIGN_SERVICE_ID.



.. _`ib_cm_insert_listen`:

ib_cm_insert_listen
===================

.. c:function:: struct ib_cm_id *ib_cm_insert_listen (struct ib_device *device, ib_cm_handler cm_handler, __be64 service_id)

    :param struct ib_device \*device:
        Device associated with the cm_id.  All related communication will
        be associated with the specified device.

    :param ib_cm_handler cm_handler:
        Callback invoked to notify the user of CM events.

    :param __be64 service_id:
        Service identifier matched against incoming connection
        and service ID resolution requests.  The service ID should be specified
        network-byte order.  If set to IB_CM_ASSIGN_SERVICE_ID, the CM will
        assign a service ID to the caller.



.. _`ib_cm_insert_listen.description`:

Description
-----------

Callers should call ib_destroy_cm_id when done with the listener ID.



.. _`ib_cm_insert_listen.description`:

Description
-----------

Callers should call ib_destroy_cm_id when done with the listener ID.

