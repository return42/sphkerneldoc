.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_hw_io.c

.. _`write_qp_ctxts`:

write_qp_ctxts
==============

.. c:function:: int write_qp_ctxts(struct hinic_func_to_io *func_to_io, u16 base_qpn, u16 num_qps)

    write the qp ctxt to HW

    :param func_to_io:
        func to io channel that holds the IO components
    :type func_to_io: struct hinic_func_to_io \*

    :param base_qpn:
        first qp number
    :type base_qpn: u16

    :param num_qps:
        number of qps to write
    :type num_qps: u16

.. _`write_qp_ctxts.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`init_qp`:

init_qp
=======

.. c:function:: int init_qp(struct hinic_func_to_io *func_to_io, struct hinic_qp *qp, int q_id, struct msix_entry *sq_msix_entry, struct msix_entry *rq_msix_entry)

    Initialize a Queue Pair

    :param func_to_io:
        func to io channel that holds the IO components
    :type func_to_io: struct hinic_func_to_io \*

    :param qp:
        pointer to the qp to initialize
    :type qp: struct hinic_qp \*

    :param q_id:
        the id of the qp
    :type q_id: int

    :param sq_msix_entry:
        msix entry for sq
    :type sq_msix_entry: struct msix_entry \*

    :param rq_msix_entry:
        msix entry for rq
    :type rq_msix_entry: struct msix_entry \*

.. _`init_qp.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`destroy_qp`:

destroy_qp
==========

.. c:function:: void destroy_qp(struct hinic_func_to_io *func_to_io, struct hinic_qp *qp)

    Clean the resources of a Queue Pair

    :param func_to_io:
        func to io channel that holds the IO components
    :type func_to_io: struct hinic_func_to_io \*

    :param qp:
        pointer to the qp to clean
    :type qp: struct hinic_qp \*

.. _`hinic_io_create_qps`:

hinic_io_create_qps
===================

.. c:function:: int hinic_io_create_qps(struct hinic_func_to_io *func_to_io, u16 base_qpn, int num_qps, struct msix_entry *sq_msix_entries, struct msix_entry *rq_msix_entries)

    Create Queue Pairs

    :param func_to_io:
        func to io channel that holds the IO components
    :type func_to_io: struct hinic_func_to_io \*

    :param base_qpn:
        base qp number
    :type base_qpn: u16

    :param num_qps:
        number queue pairs to create
    :type num_qps: int

    :param sq_msix_entries:
        *undescribed*
    :type sq_msix_entries: struct msix_entry \*

    :param rq_msix_entries:
        *undescribed*
    :type rq_msix_entries: struct msix_entry \*

.. _`hinic_io_create_qps.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_io_destroy_qps`:

hinic_io_destroy_qps
====================

.. c:function:: void hinic_io_destroy_qps(struct hinic_func_to_io *func_to_io, int num_qps)

    Destroy the IO Queue Pairs

    :param func_to_io:
        func to io channel that holds the IO components
    :type func_to_io: struct hinic_func_to_io \*

    :param num_qps:
        number queue pairs to destroy
    :type num_qps: int

.. _`hinic_io_init`:

hinic_io_init
=============

.. c:function:: int hinic_io_init(struct hinic_func_to_io *func_to_io, struct hinic_hwif *hwif, u16 max_qps, int num_ceqs, struct msix_entry *ceq_msix_entries)

    Initialize the IO components

    :param func_to_io:
        func to io channel that holds the IO components
    :type func_to_io: struct hinic_func_to_io \*

    :param hwif:
        HW interface for accessing IO
    :type hwif: struct hinic_hwif \*

    :param max_qps:
        maximum QPs in HW
    :type max_qps: u16

    :param num_ceqs:
        number completion event queues
    :type num_ceqs: int

    :param ceq_msix_entries:
        msix entries for ceqs
    :type ceq_msix_entries: struct msix_entry \*

.. _`hinic_io_init.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_io_free`:

hinic_io_free
=============

.. c:function:: void hinic_io_free(struct hinic_func_to_io *func_to_io)

    Free the IO components

    :param func_to_io:
        func to io channel that holds the IO components
    :type func_to_io: struct hinic_func_to_io \*

.. This file was automatic generated / don't edit.

