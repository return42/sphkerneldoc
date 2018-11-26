.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aacraid/rkt.c

.. _`aac_rkt_select_comm`:

aac_rkt_select_comm
===================

.. c:function:: int aac_rkt_select_comm(struct aac_dev *dev, int comm)

    Select communications method

    :param dev:
        Adapter
    :type dev: struct aac_dev \*

    :param comm:
        communications method
    :type comm: int

.. _`aac_rkt_ioremap`:

aac_rkt_ioremap
===============

.. c:function:: int aac_rkt_ioremap(struct aac_dev *dev, u32 size)

    :param dev:
        *undescribed*
    :type dev: struct aac_dev \*

    :param size:
        mapping resize request
    :type size: u32

.. _`aac_rkt_init`:

aac_rkt_init
============

.. c:function:: int aac_rkt_init(struct aac_dev *dev)

    initialize an i960 based AAC card

    :param dev:
        device to configure
    :type dev: struct aac_dev \*

.. _`aac_rkt_init.description`:

Description
-----------

Allocate and set up resources for the i960 based AAC variants. The
device_interface in the commregion will be allocated and linked
to the comm region.

.. This file was automatic generated / don't edit.

