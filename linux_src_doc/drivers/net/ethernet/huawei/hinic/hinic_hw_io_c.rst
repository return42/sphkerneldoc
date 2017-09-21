.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_hw_io.c

.. _`write_qp_ctxts`:

write_qp_ctxts
==============

.. c:function:: int write_qp_ctxts(struct hinic_func_to_io *func_to_io, u16 base_qpn, u16 num_qps)

    write the qp ctxt to HW

    :param struct hinic_func_to_io \*func_to_io:
        func to io channel that holds the IO components

    :param u16 base_qpn:
        first qp number

    :param u16 num_qps:
        number of qps to write

.. _`write_qp_ctxts.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`init_qp`:

init_qp
=======

.. c:function:: int init_qp(struct hinic_func_to_io *func_to_io, struct hinic_qp *qp, int q_id, struct msix_entry *sq_msix_entry, struct msix_entry *rq_msix_entry)

    Initialize a Queue Pair

    :param struct hinic_func_to_io \*func_to_io:
        func to io channel that holds the IO components

    :param struct hinic_qp \*qp:
        pointer to the qp to initialize

    :param int q_id:
        the id of the qp

    :param struct msix_entry \*sq_msix_entry:
        msix entry for sq

    :param struct msix_entry \*rq_msix_entry:
        msix entry for rq

.. _`init_qp.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`destroy_qp`:

destroy_qp
==========

.. c:function:: void destroy_qp(struct hinic_func_to_io *func_to_io, struct hinic_qp *qp)

    Clean the resources of a Queue Pair

    :param struct hinic_func_to_io \*func_to_io:
        func to io channel that holds the IO components

    :param struct hinic_qp \*qp:
        pointer to the qp to clean

.. _`hinic_io_create_qps`:

hinic_io_create_qps
===================

.. c:function:: int hinic_io_create_qps(struct hinic_func_to_io *func_to_io, u16 base_qpn, int num_qps, struct msix_entry *sq_msix_entries, struct msix_entry *rq_msix_entries)

    Create Queue Pairs

    :param struct hinic_func_to_io \*func_to_io:
        func to io channel that holds the IO components

    :param u16 base_qpn:
        base qp number

    :param int num_qps:
        number queue pairs to create

    :param struct msix_entry \*sq_msix_entries:
        *undescribed*

    :param struct msix_entry \*rq_msix_entries:
        *undescribed*

.. _`hinic_io_create_qps.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_io_destroy_qps`:

hinic_io_destroy_qps
====================

.. c:function:: void hinic_io_destroy_qps(struct hinic_func_to_io *func_to_io, int num_qps)

    Destroy the IO Queue Pairs

    :param struct hinic_func_to_io \*func_to_io:
        func to io channel that holds the IO components

    :param int num_qps:
        number queue pairs to destroy

.. _`hinic_io_init`:

hinic_io_init
=============

.. c:function:: int hinic_io_init(struct hinic_func_to_io *func_to_io, struct hinic_hwif *hwif, u16 max_qps, int num_ceqs, struct msix_entry *ceq_msix_entries)

    Initialize the IO components

    :param struct hinic_func_to_io \*func_to_io:
        func to io channel that holds the IO components

    :param struct hinic_hwif \*hwif:
        HW interface for accessing IO

    :param u16 max_qps:
        maximum QPs in HW

    :param int num_ceqs:
        number completion event queues

    :param struct msix_entry \*ceq_msix_entries:
        msix entries for ceqs

.. _`hinic_io_init.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_io_free`:

hinic_io_free
=============

.. c:function:: void hinic_io_free(struct hinic_func_to_io *func_to_io)

    Free the IO components

    :param struct hinic_func_to_io \*func_to_io:
        func to io channel that holds the IO components

.. This file was automatic generated / don't edit.

