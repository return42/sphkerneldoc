.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/sw/rdmavt/ah.c

.. _`rvt_check_ah`:

rvt_check_ah
============

.. c:function:: int rvt_check_ah(struct ib_device *ibdev, struct rdma_ah_attr *ah_attr)

    validate the attributes of AH

    :param ibdev:
        the ib device
    :type ibdev: struct ib_device \*

    :param ah_attr:
        the attributes of the AH
    :type ah_attr: struct rdma_ah_attr \*

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

    :param pd:
        the protection domain
    :type pd: struct ib_pd \*

    :param ah_attr:
        the attributes of the AH
    :type ah_attr: struct rdma_ah_attr \*

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

    :param ibah:
        address handle
    :type ibah: struct ib_ah \*

.. _`rvt_destroy_ah.return`:

Return
------

0 on success

.. _`rvt_modify_ah`:

rvt_modify_ah
=============

.. c:function:: int rvt_modify_ah(struct ib_ah *ibah, struct rdma_ah_attr *ah_attr)

    modify an ah with given attrs

    :param ibah:
        address handle to modify
    :type ibah: struct ib_ah \*

    :param ah_attr:
        attrs to apply
    :type ah_attr: struct rdma_ah_attr \*

.. _`rvt_modify_ah.return`:

Return
------

0 on success

.. _`rvt_query_ah`:

rvt_query_ah
============

.. c:function:: int rvt_query_ah(struct ib_ah *ibah, struct rdma_ah_attr *ah_attr)

    return attrs for ah

    :param ibah:
        address handle to query
    :type ibah: struct ib_ah \*

    :param ah_attr:
        return info in this
    :type ah_attr: struct rdma_ah_attr \*

.. _`rvt_query_ah.return`:

Return
------

always 0

.. This file was automatic generated / don't edit.

