.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hns/hns_roce_main.c

.. _`hns_get_gid_index`:

hns_get_gid_index
=================

.. c:function:: int hns_get_gid_index(struct hns_roce_dev *hr_dev, u8 port, int gid_index)

    Get gid index.

    :param struct hns_roce_dev \*hr_dev:
        pointer to structure hns_roce_dev.

    :param u8 port:
        port, value range: 0 ~ MAX

    :param int gid_index:
        gid_index, value range: 0 ~ MAX

.. _`hns_get_gid_index.description`:

Description
-----------

N ports shared gids, allocation method as follow:
GID[0][0], GID[1][0],.....GID[N - 1][0],
GID[0][0], GID[1][0],.....GID[N - 1][0],
And so on

.. _`hns_roce_setup_hca`:

hns_roce_setup_hca
==================

.. c:function:: int hns_roce_setup_hca(struct hns_roce_dev *hr_dev)

    setup host channel adapter

    :param struct hns_roce_dev \*hr_dev:
        pointer to hns roce device
        Return : int

.. _`hns_roce_probe`:

hns_roce_probe
==============

.. c:function:: int hns_roce_probe(struct platform_device *pdev)

    RoCE driver entrance

    :param struct platform_device \*pdev:
        pointer to platform device
        Return : int

.. _`hns_roce_remove`:

hns_roce_remove
===============

.. c:function:: int hns_roce_remove(struct platform_device *pdev)

    remove RoCE device

    :param struct platform_device \*pdev:
        pointer to platform device

.. This file was automatic generated / don't edit.

