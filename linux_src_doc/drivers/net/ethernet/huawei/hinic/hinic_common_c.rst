.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_common.c

.. _`hinic_cpu_to_be32`:

hinic_cpu_to_be32
=================

.. c:function:: void hinic_cpu_to_be32(void *data, int len)

    convert data to big endian 32 bit format

    :param data:
        the data to convert
    :type data: void \*

    :param len:
        length of data to convert
    :type len: int

.. _`hinic_be32_to_cpu`:

hinic_be32_to_cpu
=================

.. c:function:: void hinic_be32_to_cpu(void *data, int len)

    convert data from big endian 32 bit format

    :param data:
        the data to convert
    :type data: void \*

    :param len:
        length of data to convert
    :type len: int

.. _`hinic_set_sge`:

hinic_set_sge
=============

.. c:function:: void hinic_set_sge(struct hinic_sge *sge, dma_addr_t addr, int len)

    set dma area in scatter gather entry

    :param sge:
        scatter gather entry
    :type sge: struct hinic_sge \*

    :param addr:
        dma address
    :type addr: dma_addr_t

    :param len:
        length of relevant data in the dma address
    :type len: int

.. _`hinic_sge_to_dma`:

hinic_sge_to_dma
================

.. c:function:: dma_addr_t hinic_sge_to_dma(struct hinic_sge *sge)

    get dma address from scatter gather entry

    :param sge:
        scatter gather entry
    :type sge: struct hinic_sge \*

.. _`hinic_sge_to_dma.description`:

Description
-----------

Return dma address of sg entry

.. This file was automatic generated / don't edit.

