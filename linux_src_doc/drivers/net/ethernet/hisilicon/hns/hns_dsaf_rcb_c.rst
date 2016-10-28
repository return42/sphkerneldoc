.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns/hns_dsaf_rcb.c

.. _`hns_rcb_wait_fbd_clean`:

hns_rcb_wait_fbd_clean
======================

.. c:function:: void hns_rcb_wait_fbd_clean(struct hnae_queue **qs, int q_num, u32 flag)

    clean fbd \ ``qs``\ : ring struct pointer array \ ``qnum``\ : num of array \ ``flag``\ : tx or rx flag

    :param struct hnae_queue \*\*qs:
        *undescribed*

    :param int q_num:
        *undescribed*

    :param u32 flag:
        *undescribed*

.. _`hns_rcb_reset_ring_hw`:

hns_rcb_reset_ring_hw
=====================

.. c:function:: void hns_rcb_reset_ring_hw(struct hnae_queue *q)

    ring reset \ ``q``\ : ring struct pointer

    :param struct hnae_queue \*q:
        *undescribed*

.. _`hns_rcb_int_ctrl_hw`:

hns_rcb_int_ctrl_hw
===================

.. c:function:: void hns_rcb_int_ctrl_hw(struct hnae_queue *q, u32 flag, u32 mask)

    rcb irq enable control \ ``q``\ : hnae queue struct pointer \ ``flag``\ :ring flag tx or rx \ ``mask``\ :mask

    :param struct hnae_queue \*q:
        *undescribed*

    :param u32 flag:
        *undescribed*

    :param u32 mask:
        *undescribed*

.. _`hns_rcb_ring_enable_hw`:

hns_rcb_ring_enable_hw
======================

.. c:function:: void hns_rcb_ring_enable_hw(struct hnae_queue *q, u32 val)

    enable ring \ ``ring``\ : rcb ring

    :param struct hnae_queue \*q:
        *undescribed*

    :param u32 val:
        *undescribed*

.. _`hns_rcb_common_init_commit_hw`:

hns_rcb_common_init_commit_hw
=============================

.. c:function:: void hns_rcb_common_init_commit_hw(struct rcb_common_cb *rcb_common)

    make rcb common init completed \ ``rcb_common``\ : rcb common device

    :param struct rcb_common_cb \*rcb_common:
        *undescribed*

.. _`hns_rcb_ring_init`:

hns_rcb_ring_init
=================

.. c:function:: void hns_rcb_ring_init(struct ring_pair_cb *ring_pair, int ring_type)

    init rcb ring \ ``ring_pair``\ : ring pair control block \ ``ring_type``\ : ring type, RX_RING or TX_RING

    :param struct ring_pair_cb \*ring_pair:
        *undescribed*

    :param int ring_type:
        *undescribed*

.. _`hns_rcb_init_hw`:

hns_rcb_init_hw
===============

.. c:function:: void hns_rcb_init_hw(struct ring_pair_cb *ring)

    init rcb hardware \ ``ring``\ : rcb ring

    :param struct ring_pair_cb \*ring:
        *undescribed*

.. _`hns_rcb_set_port_desc_cnt`:

hns_rcb_set_port_desc_cnt
=========================

.. c:function:: void hns_rcb_set_port_desc_cnt(struct rcb_common_cb *rcb_common, u32 port_idx, u32 desc_cnt)

    set rcb port description num \ ``rcb_common``\ : rcb_common device \ ``port_idx``\ :port index \ ``desc_cnt``\ :BD num

    :param struct rcb_common_cb \*rcb_common:
        *undescribed*

    :param u32 port_idx:
        *undescribed*

    :param u32 desc_cnt:
        *undescribed*

.. _`hns_rcb_common_init_hw`:

hns_rcb_common_init_hw
======================

.. c:function:: int hns_rcb_common_init_hw(struct rcb_common_cb *rcb_common)

    init rcb common hardware \ ``rcb_common``\ : rcb_common device retuen 0 - success , negative --fail

    :param struct rcb_common_cb \*rcb_common:
        *undescribed*

.. _`hns_rcb_get_cfg`:

hns_rcb_get_cfg
===============

.. c:function:: void hns_rcb_get_cfg(struct rcb_common_cb *rcb_common)

    get rcb config \ ``rcb_common``\ : rcb common device

    :param struct rcb_common_cb \*rcb_common:
        *undescribed*

.. _`hns_rcb_get_coalesced_frames`:

hns_rcb_get_coalesced_frames
============================

.. c:function:: u32 hns_rcb_get_coalesced_frames(struct rcb_common_cb *rcb_common, u32 port_idx)

    get rcb port coalesced frames \ ``rcb_common``\ : rcb_common device \ ``port_idx``\ :port id in comm

    :param struct rcb_common_cb \*rcb_common:
        *undescribed*

    :param u32 port_idx:
        *undescribed*

.. _`hns_rcb_get_coalesced_frames.description`:

Description
-----------

Returns: coalesced_frames

.. _`hns_rcb_get_coalesce_usecs`:

hns_rcb_get_coalesce_usecs
==========================

.. c:function:: u32 hns_rcb_get_coalesce_usecs(struct rcb_common_cb *rcb_common, u32 port_idx)

    get rcb port coalesced time_out \ ``rcb_common``\ : rcb_common device \ ``port_idx``\ :port id in comm

    :param struct rcb_common_cb \*rcb_common:
        *undescribed*

    :param u32 port_idx:
        *undescribed*

.. _`hns_rcb_get_coalesce_usecs.description`:

Description
-----------

Returns: time_out

.. _`hns_rcb_set_coalesce_usecs`:

hns_rcb_set_coalesce_usecs
==========================

.. c:function:: int hns_rcb_set_coalesce_usecs(struct rcb_common_cb *rcb_common, u32 port_idx, u32 timeout)

    set rcb port coalesced time_out \ ``rcb_common``\ : rcb_common device \ ``port_idx``\ :port id in comm \ ``timeout``\ :tx/rx time for coalesced time_out

    :param struct rcb_common_cb \*rcb_common:
        *undescribed*

    :param u32 port_idx:
        *undescribed*

    :param u32 timeout:
        *undescribed*

.. _`hns_rcb_set_coalesce_usecs.return`:

Return
------

Zero for success, or an error code in case of failure

.. _`hns_rcb_set_coalesced_frames`:

hns_rcb_set_coalesced_frames
============================

.. c:function:: int hns_rcb_set_coalesced_frames(struct rcb_common_cb *rcb_common, u32 port_idx, u32 coalesced_frames)

    set rcb coalesced frames \ ``rcb_common``\ : rcb_common device \ ``port_idx``\ :port id in comm \ ``coalesced_frames``\ :tx/rx BD num for coalesced frames

    :param struct rcb_common_cb \*rcb_common:
        *undescribed*

    :param u32 port_idx:
        *undescribed*

    :param u32 coalesced_frames:
        *undescribed*

.. _`hns_rcb_set_coalesced_frames.return`:

Return
------

Zero for success, or an error code in case of failure

.. _`hns_rcb_get_queue_mode`:

hns_rcb_get_queue_mode
======================

.. c:function:: void hns_rcb_get_queue_mode(enum dsaf_mode dsaf_mode, u16 *max_vfn, u16 *max_q_per_vf)

    get max VM number and max ring number per VM accordding to dsaf mode \ ``dsaf_mode``\ : dsaf mode \ ``max_vfn``\  : max vfn number \ ``max_q_per_vf``\ :max ring number per vm

    :param enum dsaf_mode dsaf_mode:
        *undescribed*

    :param u16 \*max_vfn:
        *undescribed*

    :param u16 \*max_q_per_vf:
        *undescribed*

.. _`hns_rcb_get_stats`:

hns_rcb_get_stats
=================

.. c:function:: void hns_rcb_get_stats(struct hnae_queue *queue, u64 *data)

    get rcb statistic \ ``ring``\ : rcb ring \ ``data``\ :statistic value

    :param struct hnae_queue \*queue:
        *undescribed*

    :param u64 \*data:
        *undescribed*

.. _`hns_rcb_get_ring_sset_count`:

hns_rcb_get_ring_sset_count
===========================

.. c:function:: int hns_rcb_get_ring_sset_count(int stringset)

    rcb string set count \ ``stringset``\ :ethtool cmd return rcb ring string set count

    :param int stringset:
        *undescribed*

.. _`hns_rcb_get_common_regs_count`:

hns_rcb_get_common_regs_count
=============================

.. c:function:: int hns_rcb_get_common_regs_count( void)

    rcb common regs count return regs count

    :param  void:
        no arguments

.. _`hns_rcb_get_ring_regs_count`:

hns_rcb_get_ring_regs_count
===========================

.. c:function:: int hns_rcb_get_ring_regs_count( void)

    rcb ring regs count return regs count

    :param  void:
        no arguments

.. _`hns_rcb_get_strings`:

hns_rcb_get_strings
===================

.. c:function:: void hns_rcb_get_strings(int stringset, u8 *data, int index)

    get rcb string set \ ``stringset``\ :string set index \ ``data``\ :strings name value \ ``index``\ :queue index

    :param int stringset:
        *undescribed*

    :param u8 \*data:
        *undescribed*

    :param int index:
        *undescribed*

.. This file was automatic generated / don't edit.

