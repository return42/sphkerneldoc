.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/cm.c

.. _`__ib_cm_listen`:

\__ib_cm_listen
===============

.. c:function:: int __ib_cm_listen(struct ib_cm_id *cm_id, __be64 service_id, __be64 service_mask)

    Initiates listening on the specified service ID for connection and service ID resolution requests.

    :param cm_id:
        Connection identifier associated with the listen request.
    :type cm_id: struct ib_cm_id \*

    :param service_id:
        Service identifier matched against incoming connection
        and service ID resolution requests.  The service ID should be specified
        network-byte order.  If set to IB_CM_ASSIGN_SERVICE_ID, the CM will
        assign a service ID to the caller.
    :type service_id: __be64

    :param service_mask:
        Mask applied to service ID used to listen across a
        range of service IDs.  If set to 0, the service ID is matched
        exactly.  This parameter is ignored if \ ``service_id``\  is set to
        IB_CM_ASSIGN_SERVICE_ID.
    :type service_mask: __be64

.. _`ib_cm_insert_listen`:

ib_cm_insert_listen
===================

.. c:function:: struct ib_cm_id *ib_cm_insert_listen(struct ib_device *device, ib_cm_handler cm_handler, __be64 service_id)

    :param device:
        Device associated with the cm_id.  All related communication will
        be associated with the specified device.
    :type device: struct ib_device \*

    :param cm_handler:
        Callback invoked to notify the user of CM events.
    :type cm_handler: ib_cm_handler

    :param service_id:
        Service identifier matched against incoming connection
        and service ID resolution requests.  The service ID should be specified
        network-byte order.  If set to IB_CM_ASSIGN_SERVICE_ID, the CM will
        assign a service ID to the caller.
    :type service_id: __be64

.. _`ib_cm_insert_listen.description`:

Description
-----------

If there's an existing ID listening on that same device and service ID,
return it.

Callers should call ib_destroy_cm_id when done with the listener ID.

.. _`cm_opa_to_ib_sgid`:

cm_opa_to_ib_sgid
=================

.. c:function:: void cm_opa_to_ib_sgid(struct cm_work *work, struct sa_path_rec *path)

    ULPs (such as IPoIB) do not understand OPA GIDs and will reject them as the local_gid will not match the sgid. Therefore, change the pathrec's SGID to an IB SGID.

    :param work:
        Work completion
    :type work: struct cm_work \*

    :param path:
        Path record
    :type path: struct sa_path_rec \*

.. This file was automatic generated / don't edit.

