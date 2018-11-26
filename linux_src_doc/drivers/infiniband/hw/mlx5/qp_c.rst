.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/mlx5/qp.c

.. _`mlx5_ib_read_user_wqe`:

mlx5_ib_read_user_wqe
=====================

.. c:function:: int mlx5_ib_read_user_wqe(struct mlx5_ib_qp *qp, int send, int wqe_index, void *buffer, u32 length, struct mlx5_ib_qp_base *base)

    Copy a user-space WQE to kernel space.

    :param qp:
        QP to copy from.
    :type qp: struct mlx5_ib_qp \*

    :param send:
        copy from the send queue when non-zero, use the receive queue
        otherwise.
    :type send: int

    :param wqe_index:
        index to start copying from. For send work queues, the
        wqe_index is in units of MLX5_SEND_WQE_BB.
        For receive work queue, it is the number of work queue
        element in the queue.
    :type wqe_index: int

    :param buffer:
        destination buffer.
    :type buffer: void \*

    :param length:
        maximum number of bytes to copy.
    :type length: u32

    :param base:
        *undescribed*
    :type base: struct mlx5_ib_qp_base \*

.. _`mlx5_ib_read_user_wqe.description`:

Description
-----------

Copies at least a single WQE, but may copy more data.

.. _`mlx5_ib_read_user_wqe.return`:

Return
------

the number of bytes copied, or an error code.

.. This file was automatic generated / don't edit.

