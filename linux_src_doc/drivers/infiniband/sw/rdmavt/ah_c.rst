.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/sw/rdmavt/ah.c

.. _`rvt_check_ah`:

rvt_check_ah
============

.. c:function:: int rvt_check_ah(struct ib_device *ibdev, struct rdma_ah_attr *ah_attr)

    validate the attributes of AH

    :param struct ib_device \*ibdev:
        the ib device

    :param struct rdma_ah_attr \*ah_attr:
        the attributes of the AH

.. _`rvt_check_ah.description`:

Description
-----------

If driver supports a more detailed check_ah function call back to it
otherwise just check the basics.

.. _`rvt_check_ah.return`:

Return
------

0 on success

.. _`rvt_create_ah`:

rvt_create_ah
=============

.. c:function:: struct ib_ah *rvt_create_ah(struct ib_pd *pd, struct rdma_ah_attr *ah_attr)

    create an address handle

    :param struct ib_pd \*pd:
        the protection domain

    :param struct rdma_ah_attr \*ah_attr:
        the attributes of the AH

.. _`rvt_create_ah.description`:

Description
-----------

This may be called from interrupt context.

.. _`rvt_create_ah.return`:

Return
------

newly allocated ah

.. _`rvt_destroy_ah`:

rvt_destroy_ah
==============

.. c:function:: int rvt_destroy_ah(struct ib_ah *ibah)

    Destory an address handle

    :param struct ib_ah \*ibah:
        address handle

.. _`rvt_destroy_ah.return`:

Return
------

0 on success

.. _`rvt_modify_ah`:

rvt_modify_ah
=============

.. c:function:: int rvt_modify_ah(struct ib_ah *ibah, struct rdma_ah_attr *ah_attr)

    modify an ah with given attrs

    :param struct ib_ah \*ibah:
        address handle to modify

    :param struct rdma_ah_attr \*ah_attr:
        attrs to apply

.. _`rvt_modify_ah.return`:

Return
------

0 on success

.. _`rvt_query_ah`:

rvt_query_ah
============

.. c:function:: int rvt_query_ah(struct ib_ah *ibah, struct rdma_ah_attr *ah_attr)

    return attrs for ah

    :param struct ib_ah \*ibah:
        address handle to query

    :param struct rdma_ah_attr \*ah_attr:
        return info in this

.. _`rvt_query_ah.return`:

Return
------

always 0

.. This file was automatic generated / don't edit.

