.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/multicast.c

.. _`ib_init_ah_from_mcmember`:

ib_init_ah_from_mcmember
========================

.. c:function:: int ib_init_ah_from_mcmember(struct ib_device *device, u8 port_num, struct ib_sa_mcmember_rec *rec, struct net_device *ndev, enum ib_gid_type gid_type, struct rdma_ah_attr *ah_attr)

    Initialize AH attribute from multicast member record and gid of the device.

    :param device:
        RDMA device
    :type device: struct ib_device \*

    :param port_num:
        Port of the rdma device to consider
    :type port_num: u8

    :param rec:
        *undescribed*
    :type rec: struct ib_sa_mcmember_rec \*

    :param ndev:
        Optional netdevice, applicable only for RoCE
    :type ndev: struct net_device \*

    :param gid_type:
        GID type to consider
    :type gid_type: enum ib_gid_type

    :param ah_attr:
        AH attribute to fillup on successful completion
    :type ah_attr: struct rdma_ah_attr \*

.. _`ib_init_ah_from_mcmember.description`:

Description
-----------

\ :c:func:`ib_init_ah_from_mcmember`\  initializes AH attribute based on multicast
member record and other device properties. On success the caller is
responsible to call rdma_destroy_ah_attr on the ah_attr. Returns 0 on
success or appropriate error code.

.. This file was automatic generated / don't edit.

