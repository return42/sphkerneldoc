.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns/hns_dsaf_ppe.c

.. _`hns_ppe_common_get_cfg`:

hns_ppe_common_get_cfg
======================

.. c:function:: int hns_ppe_common_get_cfg(struct dsaf_device *dsaf_dev, int comm_index)

    get ppe common config

    :param dsaf_dev:
        dasf device
    :type dsaf_dev: struct dsaf_device \*

    :param comm_index:
        *undescribed*
    :type comm_index: int

.. _`hns_ppe_common_get_cfg.comm_index`:

comm_index
----------

common index
retuen 0 - success , negative --fail

.. _`hns_ppe_checksum_hw`:

hns_ppe_checksum_hw
===================

.. c:function:: void hns_ppe_checksum_hw(struct hns_ppe_cb *ppe_cb, u32 value)

    set ppe checksum caculate

    :param ppe_cb:
        *undescribed*
    :type ppe_cb: struct hns_ppe_cb \*

    :param value:
        value
    :type value: u32

.. _`hns_ppe_set_qid`:

hns_ppe_set_qid
===============

.. c:function:: void hns_ppe_set_qid(struct ppe_common_cb *ppe_common, u32 qid)

    set ppe qid

    :param ppe_common:
        ppe common device
    :type ppe_common: struct ppe_common_cb \*

    :param qid:
        queue id
    :type qid: u32

.. _`hns_ppe_set_port_mode`:

hns_ppe_set_port_mode
=====================

.. c:function:: void hns_ppe_set_port_mode(struct hns_ppe_cb *ppe_cb, enum ppe_port_mode mode)

    set port mode

    :param ppe_cb:
        *undescribed*
    :type ppe_cb: struct hns_ppe_cb \*

    :param mode:
        port mode
    :type mode: enum ppe_port_mode

.. _`hns_ppe_common_init_hw`:

hns_ppe_common_init_hw
======================

.. c:function:: int hns_ppe_common_init_hw(struct ppe_common_cb *ppe_common)

    init ppe common device

    :param ppe_common:
        ppe common device
    :type ppe_common: struct ppe_common_cb \*

.. _`hns_ppe_common_init_hw.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`hns_ppe_init_hw`:

hns_ppe_init_hw
===============

.. c:function:: void hns_ppe_init_hw(struct hns_ppe_cb *ppe_cb)

    init ppe

    :param ppe_cb:
        ppe device
    :type ppe_cb: struct hns_ppe_cb \*

.. _`hns_ppe_uninit_hw`:

hns_ppe_uninit_hw
=================

.. c:function:: void hns_ppe_uninit_hw(struct hns_ppe_cb *ppe_cb)

    uninit ppe

    :param ppe_cb:
        *undescribed*
    :type ppe_cb: struct hns_ppe_cb \*

.. _`hns_ppe_reset_common`:

hns_ppe_reset_common
====================

.. c:function:: void hns_ppe_reset_common(struct dsaf_device *dsaf_dev, u8 ppe_common_index)

    reinit ppe/rcb hw

    :param dsaf_dev:
        dasf device
        retuen void
    :type dsaf_dev: struct dsaf_device \*

    :param ppe_common_index:
        *undescribed*
    :type ppe_common_index: u8

.. _`hns_ppe_get_strings`:

hns_ppe_get_strings
===================

.. c:function:: void hns_ppe_get_strings(struct hns_ppe_cb *ppe_cb, int stringset, u8 *data)

    get ppe srting

    :param ppe_cb:
        *undescribed*
    :type ppe_cb: struct hns_ppe_cb \*

    :param stringset:
        string set type
    :type stringset: int

    :param data:
        output string
    :type data: u8 \*

.. _`hns_ppe_init`:

hns_ppe_init
============

.. c:function:: int hns_ppe_init(struct dsaf_device *dsaf_dev)

    init ppe device

    :param dsaf_dev:
        dasf device
        retuen 0 - success , negative --fail
    :type dsaf_dev: struct dsaf_device \*

.. This file was automatic generated / don't edit.

