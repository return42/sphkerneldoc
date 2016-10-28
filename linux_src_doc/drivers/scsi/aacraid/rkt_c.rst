.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aacraid/rkt.c

.. _`aac_rkt_select_comm`:

aac_rkt_select_comm
===================

.. c:function:: int aac_rkt_select_comm(struct aac_dev *dev, int comm)

    Select communications method

    :param struct aac_dev \*dev:
        Adapter

    :param int comm:
        communications method

.. _`aac_rkt_ioremap`:

aac_rkt_ioremap
===============

.. c:function:: int aac_rkt_ioremap(struct aac_dev *dev, u32 size)

    :param struct aac_dev \*dev:
        *undescribed*

    :param u32 size:
        mapping resize request

.. _`aac_rkt_init`:

aac_rkt_init
============

.. c:function:: int aac_rkt_init(struct aac_dev *dev)

    initialize an i960 based AAC card

    :param struct aac_dev \*dev:
        device to configure

.. _`aac_rkt_init.description`:

Description
-----------

Allocate and set up resources for the i960 based AAC variants. The
device_interface in the commregion will be allocated and linked
to the comm region.

.. This file was automatic generated / don't edit.

