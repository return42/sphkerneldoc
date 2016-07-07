.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/mlx5/qp.c

.. _`mlx5_ib_read_user_wqe`:

mlx5_ib_read_user_wqe
=====================

.. c:function:: int mlx5_ib_read_user_wqe(struct mlx5_ib_qp *qp, int send, int wqe_index, void *buffer, u32 length, struct mlx5_ib_qp_base *base)

    Copy a user-space WQE to kernel space.

    :param struct mlx5_ib_qp \*qp:
        QP to copy from.

    :param int send:
        copy from the send queue when non-zero, use the receive queue
        otherwise.

    :param int wqe_index:
        index to start copying from. For send work queues, the
        wqe_index is in units of MLX5_SEND_WQE_BB.
        For receive work queue, it is the number of work queue
        element in the queue.

    :param void \*buffer:
        destination buffer.

    :param u32 length:
        maximum number of bytes to copy.

    :param struct mlx5_ib_qp_base \*base:
        *undescribed*

.. _`mlx5_ib_read_user_wqe.description`:

Description
-----------

Copies at least a single WQE, but may copy more data.

.. _`mlx5_ib_read_user_wqe.return`:

Return
------

the number of bytes copied, or an error code.

.. This file was automatic generated / don't edit.

