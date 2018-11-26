.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns/hns_dsaf_rcb.c

.. _`hns_rcb_wait_fbd_clean`:

hns_rcb_wait_fbd_clean
======================

.. c:function:: void hns_rcb_wait_fbd_clean(struct hnae_queue **qs, int q_num, u32 flag)

    clean fbd \ ``qs``\ : ring struct pointer array \ ``qnum``\ : num of array \ ``flag``\ : tx or rx flag

    :param qs:
        *undescribed*
    :type qs: struct hnae_queue \*\*

    :param q_num:
        *undescribed*
    :type q_num: int

    :param flag:
        *undescribed*
    :type flag: u32

.. _`hns_rcb_reset_ring_hw`:

hns_rcb_reset_ring_hw
=====================

.. c:function:: void hns_rcb_reset_ring_hw(struct hnae_queue *q)

    ring reset \ ``q``\ : ring struct pointer

    :param q:
        *undescribed*
    :type q: struct hnae_queue \*

.. _`hns_rcb_int_ctrl_hw`:

hns_rcb_int_ctrl_hw
===================

.. c:function:: void hns_rcb_int_ctrl_hw(struct hnae_queue *q, u32 flag, u32 mask)

    rcb irq enable control \ ``q``\ : hnae queue struct pointer \ ``flag``\ :ring flag tx or rx \ ``mask``\ :mask

    :param q:
        *undescribed*
    :type q: struct hnae_queue \*

    :param flag:
        *undescribed*
    :type flag: u32

    :param mask:
        *undescribed*
    :type mask: u32

.. _`hns_rcb_ring_enable_hw`:

hns_rcb_ring_enable_hw
======================

.. c:function:: void hns_rcb_ring_enable_hw(struct hnae_queue *q, u32 val)

    enable ring \ ``ring``\ : rcb ring

    :param q:
        *undescribed*
    :type q: struct hnae_queue \*

    :param val:
        *undescribed*
    :type val: u32

.. _`hns_rcb_common_init_commit_hw`:

hns_rcb_common_init_commit_hw
=============================

.. c:function:: void hns_rcb_common_init_commit_hw(struct rcb_common_cb *rcb_common)

    make rcb common init completed \ ``rcb_common``\ : rcb common device

    :param rcb_common:
        *undescribed*
    :type rcb_common: struct rcb_common_cb \*

.. _`hns_rcb_ring_init`:

hns_rcb_ring_init
=================

.. c:function:: void hns_rcb_ring_init(struct ring_pair_cb *ring_pair, int ring_type)

    init rcb ring \ ``ring_pair``\ : ring pair control block \ ``ring_type``\ : ring type, RX_RING or TX_RING

    :param ring_pair:
        *undescribed*
    :type ring_pair: struct ring_pair_cb \*

    :param ring_type:
        *undescribed*
    :type ring_type: int

.. _`hns_rcb_init_hw`:

hns_rcb_init_hw
===============

.. c:function:: void hns_rcb_init_hw(struct ring_pair_cb *ring)

    init rcb hardware \ ``ring``\ : rcb ring

    :param ring:
        *undescribed*
    :type ring: struct ring_pair_cb \*

.. _`hns_rcb_set_port_desc_cnt`:

hns_rcb_set_port_desc_cnt
=========================

.. c:function:: void hns_rcb_set_port_desc_cnt(struct rcb_common_cb *rcb_common, u32 port_idx, u32 desc_cnt)

    set rcb port description num \ ``rcb_common``\ : rcb_common device \ ``port_idx``\ :port index \ ``desc_cnt``\ :BD num

    :param rcb_common:
        *undescribed*
    :type rcb_common: struct rcb_common_cb \*

    :param port_idx:
        *undescribed*
    :type port_idx: u32

    :param desc_cnt:
        *undescribed*
    :type desc_cnt: u32

.. _`hns_rcb_common_init_hw`:

hns_rcb_common_init_hw
======================

.. c:function:: int hns_rcb_common_init_hw(struct rcb_common_cb *rcb_common)

    init rcb common hardware \ ``rcb_common``\ : rcb_common device retuen 0 - success , negative --fail

    :param rcb_common:
        *undescribed*
    :type rcb_common: struct rcb_common_cb \*

.. _`hns_rcb_get_cfg`:

hns_rcb_get_cfg
===============

.. c:function:: int hns_rcb_get_cfg(struct rcb_common_cb *rcb_common)

    get rcb config \ ``rcb_common``\ : rcb common device

    :param rcb_common:
        *undescribed*
    :type rcb_common: struct rcb_common_cb \*

.. _`hns_rcb_get_rx_coalesced_frames`:

hns_rcb_get_rx_coalesced_frames
===============================

.. c:function:: u32 hns_rcb_get_rx_coalesced_frames(struct rcb_common_cb *rcb_common, u32 port_idx)

    get rcb port rx coalesced frames \ ``rcb_common``\ : rcb_common device \ ``port_idx``\ :port id in comm

    :param rcb_common:
        *undescribed*
    :type rcb_common: struct rcb_common_cb \*

    :param port_idx:
        *undescribed*
    :type port_idx: u32

.. _`hns_rcb_get_rx_coalesced_frames.description`:

Description
-----------

Returns: coalesced_frames

.. _`hns_rcb_get_tx_coalesced_frames`:

hns_rcb_get_tx_coalesced_frames
===============================

.. c:function:: u32 hns_rcb_get_tx_coalesced_frames(struct rcb_common_cb *rcb_common, u32 port_idx)

    get rcb port tx coalesced frames \ ``rcb_common``\ : rcb_common device \ ``port_idx``\ :port id in comm

    :param rcb_common:
        *undescribed*
    :type rcb_common: struct rcb_common_cb \*

    :param port_idx:
        *undescribed*
    :type port_idx: u32

.. _`hns_rcb_get_tx_coalesced_frames.description`:

Description
-----------

Returns: coalesced_frames

.. _`hns_rcb_get_coalesce_usecs`:

hns_rcb_get_coalesce_usecs
==========================

.. c:function:: u32 hns_rcb_get_coalesce_usecs(struct rcb_common_cb *rcb_common, u32 port_idx)

    get rcb port coalesced time_out \ ``rcb_common``\ : rcb_common device \ ``port_idx``\ :port id in comm

    :param rcb_common:
        *undescribed*
    :type rcb_common: struct rcb_common_cb \*

    :param port_idx:
        *undescribed*
    :type port_idx: u32

.. _`hns_rcb_get_coalesce_usecs.description`:

Description
-----------

Returns: time_out

.. _`hns_rcb_set_coalesce_usecs`:

hns_rcb_set_coalesce_usecs
==========================

.. c:function:: int hns_rcb_set_coalesce_usecs(struct rcb_common_cb *rcb_common, u32 port_idx, u32 timeout)

    set rcb port coalesced time_out \ ``rcb_common``\ : rcb_common device \ ``port_idx``\ :port id in comm \ ``timeout``\ :tx/rx time for coalesced time_out

    :param rcb_common:
        *undescribed*
    :type rcb_common: struct rcb_common_cb \*

    :param port_idx:
        *undescribed*
    :type port_idx: u32

    :param timeout:
        *undescribed*
    :type timeout: u32

.. _`hns_rcb_set_coalesce_usecs.return`:

Return
------

Zero for success, or an error code in case of failure

.. _`hns_rcb_set_tx_coalesced_frames`:

hns_rcb_set_tx_coalesced_frames
===============================

.. c:function:: int hns_rcb_set_tx_coalesced_frames(struct rcb_common_cb *rcb_common, u32 port_idx, u32 coalesced_frames)

    set rcb coalesced frames \ ``rcb_common``\ : rcb_common device \ ``port_idx``\ :port id in comm \ ``coalesced_frames``\ :tx/rx BD num for coalesced frames

    :param rcb_common:
        *undescribed*
    :type rcb_common: struct rcb_common_cb \*

    :param port_idx:
        *undescribed*
    :type port_idx: u32

    :param coalesced_frames:
        *undescribed*
    :type coalesced_frames: u32

.. _`hns_rcb_set_tx_coalesced_frames.return`:

Return
------

Zero for success, or an error code in case of failure

.. _`hns_rcb_set_rx_coalesced_frames`:

hns_rcb_set_rx_coalesced_frames
===============================

.. c:function:: int hns_rcb_set_rx_coalesced_frames(struct rcb_common_cb *rcb_common, u32 port_idx, u32 coalesced_frames)

    set rcb rx coalesced frames \ ``rcb_common``\ : rcb_common device \ ``port_idx``\ :port id in comm \ ``coalesced_frames``\ :tx/rx BD num for coalesced frames

    :param rcb_common:
        *undescribed*
    :type rcb_common: struct rcb_common_cb \*

    :param port_idx:
        *undescribed*
    :type port_idx: u32

    :param coalesced_frames:
        *undescribed*
    :type coalesced_frames: u32

.. _`hns_rcb_set_rx_coalesced_frames.return`:

Return
------

Zero for success, or an error code in case of failure

.. _`hns_rcb_get_queue_mode`:

hns_rcb_get_queue_mode
======================

.. c:function:: void hns_rcb_get_queue_mode(enum dsaf_mode dsaf_mode, u16 *max_vfn, u16 *max_q_per_vf)

    get max VM number and max ring number per VM accordding to dsaf mode \ ``dsaf_mode``\ : dsaf mode \ ``max_vfn``\  : max vfn number \ ``max_q_per_vf``\ :max ring number per vm

    :param dsaf_mode:
        *undescribed*
    :type dsaf_mode: enum dsaf_mode

    :param max_vfn:
        *undescribed*
    :type max_vfn: u16 \*

    :param max_q_per_vf:
        *undescribed*
    :type max_q_per_vf: u16 \*

.. _`hns_rcb_get_stats`:

hns_rcb_get_stats
=================

.. c:function:: void hns_rcb_get_stats(struct hnae_queue *queue, u64 *data)

    get rcb statistic \ ``ring``\ : rcb ring \ ``data``\ :statistic value

    :param queue:
        *undescribed*
    :type queue: struct hnae_queue \*

    :param data:
        *undescribed*
    :type data: u64 \*

.. _`hns_rcb_get_ring_sset_count`:

hns_rcb_get_ring_sset_count
===========================

.. c:function:: int hns_rcb_get_ring_sset_count(int stringset)

    rcb string set count \ ``stringset``\ :ethtool cmd return rcb ring string set count

    :param stringset:
        *undescribed*
    :type stringset: int

.. _`hns_rcb_get_common_regs_count`:

hns_rcb_get_common_regs_count
=============================

.. c:function:: int hns_rcb_get_common_regs_count( void)

    rcb common regs count return regs count

    :param void:
        no arguments
    :type void: 

.. _`hns_rcb_get_ring_regs_count`:

hns_rcb_get_ring_regs_count
===========================

.. c:function:: int hns_rcb_get_ring_regs_count( void)

    rcb ring regs count return regs count

    :param void:
        no arguments
    :type void: 

.. _`hns_rcb_get_strings`:

hns_rcb_get_strings
===================

.. c:function:: void hns_rcb_get_strings(int stringset, u8 *data, int index)

    get rcb string set \ ``stringset``\ :string set index \ ``data``\ :strings name value \ ``index``\ :queue index

    :param stringset:
        *undescribed*
    :type stringset: int

    :param data:
        *undescribed*
    :type data: u8 \*

    :param index:
        *undescribed*
    :type index: int

.. This file was automatic generated / don't edit.

