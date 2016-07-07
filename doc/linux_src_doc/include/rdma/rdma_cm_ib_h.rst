.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/rdma_cm_ib.h

.. _`rdma_set_ib_paths`:

rdma_set_ib_paths
=================

.. c:function:: int rdma_set_ib_paths(struct rdma_cm_id *id, struct ib_sa_path_rec *path_rec, int num_paths)

    Manually sets the path records used to establish a connection.

    :param struct rdma_cm_id \*id:
        Connection identifier associated with the request.

    :param struct ib_sa_path_rec \*path_rec:
        Reference to the path record

    :param int num_paths:
        *undescribed*

.. _`rdma_set_ib_paths.description`:

Description
-----------

This call permits a user to specify routing information for rdma_cm_id's
bound to Infiniband devices.  It is called on the client side of a
connection and replaces the call to rdma_resolve_route.

.. This file was automatic generated / don't edit.

