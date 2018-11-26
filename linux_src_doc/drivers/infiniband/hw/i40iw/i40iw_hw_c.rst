.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_hw.c

.. _`i40iw_initialize_hw_resources`:

i40iw_initialize_hw_resources
=============================

.. c:function:: u32 i40iw_initialize_hw_resources(struct i40iw_device *iwdev)

    initialize hw resource during open

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_cqp_ce_handler`:

i40iw_cqp_ce_handler
====================

.. c:function:: void i40iw_cqp_ce_handler(struct i40iw_device *iwdev, struct i40iw_sc_cq *cq, bool arm)

    handle cqp completions

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param cq:
        cq for cqp completions
    :type cq: struct i40iw_sc_cq \*

    :param arm:
        flag to arm after completions
    :type arm: bool

.. _`i40iw_iwarp_ce_handler`:

i40iw_iwarp_ce_handler
======================

.. c:function:: void i40iw_iwarp_ce_handler(struct i40iw_device *iwdev, struct i40iw_sc_cq *iwcq)

    handle iwarp completions

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param iwcq:
        *undescribed*
    :type iwcq: struct i40iw_sc_cq \*

.. _`i40iw_puda_ce_handler`:

i40iw_puda_ce_handler
=====================

.. c:function:: void i40iw_puda_ce_handler(struct i40iw_device *iwdev, struct i40iw_sc_cq *cq)

    handle puda completion events

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param cq:
        puda completion q for event
    :type cq: struct i40iw_sc_cq \*

.. _`i40iw_process_ceq`:

i40iw_process_ceq
=================

.. c:function:: void i40iw_process_ceq(struct i40iw_device *iwdev, struct i40iw_ceq *ceq)

    handle ceq for completions

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param ceq:
        ceq having cq for completion
    :type ceq: struct i40iw_ceq \*

.. _`i40iw_next_iw_state`:

i40iw_next_iw_state
===================

.. c:function:: void i40iw_next_iw_state(struct i40iw_qp *iwqp, u8 state, u8 del_hash, u8 term, u8 termlen)

    modify qp state

    :param iwqp:
        iwarp qp to modify
    :type iwqp: struct i40iw_qp \*

    :param state:
        next state for qp
    :type state: u8

    :param del_hash:
        del hash
    :type del_hash: u8

    :param term:
        term message
    :type term: u8

    :param termlen:
        length of term message
    :type termlen: u8

.. _`i40iw_process_aeq`:

i40iw_process_aeq
=================

.. c:function:: void i40iw_process_aeq(struct i40iw_device *iwdev)

    handle aeq events

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_cqp_manage_abvpt_cmd`:

i40iw_cqp_manage_abvpt_cmd
==========================

.. c:function:: enum i40iw_status_code i40iw_cqp_manage_abvpt_cmd(struct i40iw_device *iwdev, u16 accel_local_port, bool add_port)

    send cqp command manage abpvt

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param accel_local_port:
        port for apbvt
    :type accel_local_port: u16

    :param add_port:
        add or delete port
    :type add_port: bool

.. _`i40iw_manage_apbvt`:

i40iw_manage_apbvt
==================

.. c:function:: enum i40iw_status_code i40iw_manage_apbvt(struct i40iw_device *iwdev, u16 accel_local_port, bool add_port)

    add or delete tcp port

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param accel_local_port:
        port for apbvt
    :type accel_local_port: u16

    :param add_port:
        add or delete port
    :type add_port: bool

.. _`i40iw_manage_arp_cache`:

i40iw_manage_arp_cache
======================

.. c:function:: void i40iw_manage_arp_cache(struct i40iw_device *iwdev, unsigned char *mac_addr, u32 *ip_addr, bool ipv4, u32 action)

    manage hw arp cache

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param mac_addr:
        mac address ptr
    :type mac_addr: unsigned char \*

    :param ip_addr:
        ip addr for arp cache
    :type ip_addr: u32 \*

    :param ipv4:
        *undescribed*
    :type ipv4: bool

    :param action:
        add, delete or modify
    :type action: u32

.. _`i40iw_send_syn_cqp_callback`:

i40iw_send_syn_cqp_callback
===========================

.. c:function:: void i40iw_send_syn_cqp_callback(struct i40iw_cqp_request *cqp_request, u32 send_ack)

    do syn/ack after qhash

    :param cqp_request:
        qhash cqp completion
    :type cqp_request: struct i40iw_cqp_request \*

    :param send_ack:
        flag send ack
    :type send_ack: u32

.. _`i40iw_manage_qhash`:

i40iw_manage_qhash
==================

.. c:function:: enum i40iw_status_code i40iw_manage_qhash(struct i40iw_device *iwdev, struct i40iw_cm_info *cminfo, enum i40iw_quad_entry_type etype, enum i40iw_quad_hash_manage_type mtype, void *cmnode, bool wait)

    add or modify qhash

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param cminfo:
        cm info for qhash
    :type cminfo: struct i40iw_cm_info \*

    :param etype:
        type (syn or quad)
    :type etype: enum i40iw_quad_entry_type

    :param mtype:
        type of qhash
    :type mtype: enum i40iw_quad_hash_manage_type

    :param cmnode:
        cmnode associated with connection
    :type cmnode: void \*

    :param wait:
        wait for completion
    :type wait: bool

.. _`i40iw_hw_flush_wqes`:

i40iw_hw_flush_wqes
===================

.. c:function:: enum i40iw_status_code i40iw_hw_flush_wqes(struct i40iw_device *iwdev, struct i40iw_sc_qp *qp, struct i40iw_qp_flush_info *info, bool wait)

    flush qp's wqe

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param qp:
        hardware control qp
    :type qp: struct i40iw_sc_qp \*

    :param info:
        info for flush
    :type info: struct i40iw_qp_flush_info \*

    :param wait:
        flag wait for completion
    :type wait: bool

.. _`i40iw_gen_ae`:

i40iw_gen_ae
============

.. c:function:: void i40iw_gen_ae(struct i40iw_device *iwdev, struct i40iw_sc_qp *qp, struct i40iw_gen_ae_info *info, bool wait)

    generate AE

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param qp:
        qp associated with AE
    :type qp: struct i40iw_sc_qp \*

    :param info:
        info for ae
    :type info: struct i40iw_gen_ae_info \*

    :param wait:
        wait for completion
    :type wait: bool

.. _`i40iw_hw_manage_vf_pble_bp`:

i40iw_hw_manage_vf_pble_bp
==========================

.. c:function:: enum i40iw_status_code i40iw_hw_manage_vf_pble_bp(struct i40iw_device *iwdev, struct i40iw_manage_vf_pble_info *info, bool wait)

    manage vf pbles

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param info:
        info for managing pble
    :type info: struct i40iw_manage_vf_pble_info \*

    :param wait:
        flag wait for completion
    :type wait: bool

.. _`i40iw_get_ib_wc`:

i40iw_get_ib_wc
===============

.. c:function:: enum ib_wc_status i40iw_get_ib_wc(enum i40iw_flush_opcode opcode)

    return change flush code to IB's

    :param opcode:
        iwarp flush code
    :type opcode: enum i40iw_flush_opcode

.. _`i40iw_set_flush_info`:

i40iw_set_flush_info
====================

.. c:function:: void i40iw_set_flush_info(struct i40iw_qp_flush_info *pinfo, u16 *min, u16 *maj, enum i40iw_flush_opcode opcode)

    set flush info

    :param pinfo:
        set flush info
    :type pinfo: struct i40iw_qp_flush_info \*

    :param min:
        minor err
    :type min: u16 \*

    :param maj:
        major err
    :type maj: u16 \*

    :param opcode:
        flush error code
    :type opcode: enum i40iw_flush_opcode

.. _`i40iw_flush_wqes`:

i40iw_flush_wqes
================

.. c:function:: void i40iw_flush_wqes(struct i40iw_device *iwdev, struct i40iw_qp *iwqp)

    flush wqe for qp

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param iwqp:
        qp to flush wqes
    :type iwqp: struct i40iw_qp \*

.. This file was automatic generated / don't edit.

