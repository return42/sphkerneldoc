.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/ulp/iser/iser_initiator.c

.. _`iser_send_command`:

iser_send_command
=================

.. c:function:: int iser_send_command(struct iscsi_conn *conn, struct iscsi_task *task)

    send command PDU

    :param conn:
        *undescribed*
    :type conn: struct iscsi_conn \*

    :param task:
        *undescribed*
    :type task: struct iscsi_task \*

.. _`iser_send_data_out`:

iser_send_data_out
==================

.. c:function:: int iser_send_data_out(struct iscsi_conn *conn, struct iscsi_task *task, struct iscsi_data *hdr)

    send data out PDU

    :param conn:
        *undescribed*
    :type conn: struct iscsi_conn \*

    :param task:
        *undescribed*
    :type task: struct iscsi_task \*

    :param hdr:
        *undescribed*
    :type hdr: struct iscsi_data \*

.. This file was automatic generated / don't edit.

