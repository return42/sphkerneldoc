.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/mlx5/odp.c

.. _`pagefault_data_segments`:

pagefault_data_segments
=======================

.. c:function:: int pagefault_data_segments(struct mlx5_ib_qp *qp, struct mlx5_ib_pfault *pfault, void *wqe, void *wqe_end, u32 *bytes_mapped, u32 *total_wqe_bytes, int receive_queue)

    :param struct mlx5_ib_qp \*qp:
        *undescribed*

    :param struct mlx5_ib_pfault \*pfault:
        *undescribed*

    :param void \*wqe:
        *undescribed*

    :param void \*wqe_end:
        *undescribed*

    :param u32 \*bytes_mapped:
        *undescribed*

    :param u32 \*total_wqe_bytes:
        *undescribed*

    :param int receive_queue:
        *undescribed*

.. _`pagefault_data_segments.description`:

Description
-----------

\ ``qp``\  the QP on which the fault occurred.
\ ``pfault``\  contains page fault information.
\ ``wqe``\  points at the first data segment in the WQE.
\ ``wqe_end``\  points after the end of the WQE.
\ ``bytes_mapped``\  receives the number of bytes that the function was able to
map. This allows the caller to decide intelligently whether
enough memory was mapped to resolve the page fault
successfully (e.g. enough for the next MTU, or the entire
WQE).
\ ``total_wqe_bytes``\  receives the total data size of this WQE in bytes (minus
the committed bytes).

Returns the number of pages loaded if positive, zero for an empty WQE, or a
negative error code.

.. This file was automatic generated / don't edit.

