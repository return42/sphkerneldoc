.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/ulp/isert/ib_isert.c

.. _`isert_conn_terminate`:

isert_conn_terminate
====================

.. c:function:: void isert_conn_terminate(struct isert_conn *isert_conn)

    Initiate connection termination

    :param isert_conn:
        isert connection struct
    :type isert_conn: struct isert_conn \*

.. _`isert_conn_terminate.notes`:

Notes
-----

In case the connection state is BOUND, move state
to TEMINATING and start teardown sequence (rdma_disconnect).
In case the connection state is UP, complete flush as well.

This routine must be called with mutex held. Thus it is
safe to call multiple times.

.. _`isert_put_unsol_pending_cmds`:

isert_put_unsol_pending_cmds
============================

.. c:function:: void isert_put_unsol_pending_cmds(struct iscsi_conn *conn)

    Drop commands waiting for unsolicitate dataout

    :param conn:
        iscsi connection
    :type conn: struct iscsi_conn \*

.. _`isert_put_unsol_pending_cmds.description`:

Description
-----------

We might still have commands that are waiting for unsolicited
dataouts messages. We must put the extra reference on those
before blocking on the target_wait_for_session_cmds

.. This file was automatic generated / don't edit.

