.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/rdma_cm_ib.h

.. _`rdma_set_ib_path`:

rdma_set_ib_path
================

.. c:function:: int rdma_set_ib_path(struct rdma_cm_id *id, struct sa_path_rec *path_rec)

    Manually sets the path record used to establish a connection.

    :param struct rdma_cm_id \*id:
        Connection identifier associated with the request.

    :param struct sa_path_rec \*path_rec:
        Reference to the path record

.. _`rdma_set_ib_path.description`:

Description
-----------

This call permits a user to specify routing information for rdma_cm_id's
bound to InfiniBand devices. It is called on the client side of a
connection and replaces the call to rdma_resolve_route.

.. This file was automatic generated / don't edit.

