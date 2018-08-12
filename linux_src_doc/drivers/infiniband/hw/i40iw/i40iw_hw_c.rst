.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_hw.c

.. _`i40iw_initialize_hw_resources`:

i40iw_initialize_hw_resources
=============================

.. c:function:: u32 i40iw_initialize_hw_resources(struct i40iw_device *iwdev)

    initialize hw resource during open

    :param struct i40iw_device \*iwdev:
        iwarp device

.. _`i40iw_cqp_ce_handler`:

i40iw_cqp_ce_handler
====================

.. c:function:: void i40iw_cqp_ce_handler(struct i40iw_device *iwdev, struct i40iw_sc_cq *cq, bool arm)

    handle cqp completions

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_sc_cq \*cq:
        cq for cqp completions

    :param bool arm:
        flag to arm after completions

.. _`i40iw_iwarp_ce_handler`:

i40iw_iwarp_ce_handler
======================

.. c:function:: void i40iw_iwarp_ce_handler(struct i40iw_device *iwdev, struct i40iw_sc_cq *iwcq)

    handle iwarp completions

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_sc_cq \*iwcq:
        *undescribed*

.. _`i40iw_puda_ce_handler`:

i40iw_puda_ce_handler
=====================

.. c:function:: void i40iw_puda_ce_handler(struct i40iw_device *iwdev, struct i40iw_sc_cq *cq)

    handle puda completion events

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_sc_cq \*cq:
        puda completion q for event

.. _`i40iw_process_ceq`:

i40iw_process_ceq
=================

.. c:function:: void i40iw_process_ceq(struct i40iw_device *iwdev, struct i40iw_ceq *ceq)

    handle ceq for completions

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_ceq \*ceq:
        ceq having cq for completion

.. _`i40iw_next_iw_state`:

i40iw_next_iw_state
===================

.. c:function:: void i40iw_next_iw_state(struct i40iw_qp *iwqp, u8 state, u8 del_hash, u8 term, u8 termlen)

    modify qp state

    :param struct i40iw_qp \*iwqp:
        iwarp qp to modify

    :param u8 state:
        next state for qp

    :param u8 del_hash:
        del hash

    :param u8 term:
        term message

    :param u8 termlen:
        length of term message

.. _`i40iw_process_aeq`:

i40iw_process_aeq
=================

.. c:function:: void i40iw_process_aeq(struct i40iw_device *iwdev)

    handle aeq events

    :param struct i40iw_device \*iwdev:
        iwarp device

.. _`i40iw_manage_apbvt`:

i40iw_manage_apbvt
==================

.. c:function:: int i40iw_manage_apbvt(struct i40iw_device *iwdev, u16 accel_local_port, bool add_port)

    add or delete tcp port

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param u16 accel_local_port:
        port for apbvt

    :param bool add_port:
        add or delete port

.. _`i40iw_manage_arp_cache`:

i40iw_manage_arp_cache
======================

.. c:function:: void i40iw_manage_arp_cache(struct i40iw_device *iwdev, unsigned char *mac_addr, u32 *ip_addr, bool ipv4, u32 action)

    manage hw arp cache

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param unsigned char \*mac_addr:
        mac address ptr

    :param u32 \*ip_addr:
        ip addr for arp cache

    :param bool ipv4:
        *undescribed*

    :param u32 action:
        add, delete or modify

.. _`i40iw_send_syn_cqp_callback`:

i40iw_send_syn_cqp_callback
===========================

.. c:function:: void i40iw_send_syn_cqp_callback(struct i40iw_cqp_request *cqp_request, u32 send_ack)

    do syn/ack after qhash

    :param struct i40iw_cqp_request \*cqp_request:
        qhash cqp completion

    :param u32 send_ack:
        flag send ack

.. _`i40iw_manage_qhash`:

i40iw_manage_qhash
==================

.. c:function:: enum i40iw_status_code i40iw_manage_qhash(struct i40iw_device *iwdev, struct i40iw_cm_info *cminfo, enum i40iw_quad_entry_type etype, enum i40iw_quad_hash_manage_type mtype, void *cmnode, bool wait)

    add or modify qhash

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_cm_info \*cminfo:
        cm info for qhash

    :param enum i40iw_quad_entry_type etype:
        type (syn or quad)

    :param enum i40iw_quad_hash_manage_type mtype:
        type of qhash

    :param void \*cmnode:
        cmnode associated with connection

    :param bool wait:
        wait for completion

.. _`i40iw_hw_flush_wqes`:

i40iw_hw_flush_wqes
===================

.. c:function:: enum i40iw_status_code i40iw_hw_flush_wqes(struct i40iw_device *iwdev, struct i40iw_sc_qp *qp, struct i40iw_qp_flush_info *info, bool wait)

    flush qp's wqe

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_sc_qp \*qp:
        hardware control qp

    :param struct i40iw_qp_flush_info \*info:
        info for flush

    :param bool wait:
        flag wait for completion

.. _`i40iw_gen_ae`:

i40iw_gen_ae
============

.. c:function:: void i40iw_gen_ae(struct i40iw_device *iwdev, struct i40iw_sc_qp *qp, struct i40iw_gen_ae_info *info, bool wait)

    generate AE

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_sc_qp \*qp:
        qp associated with AE

    :param struct i40iw_gen_ae_info \*info:
        info for ae

    :param bool wait:
        wait for completion

.. _`i40iw_hw_manage_vf_pble_bp`:

i40iw_hw_manage_vf_pble_bp
==========================

.. c:function:: enum i40iw_status_code i40iw_hw_manage_vf_pble_bp(struct i40iw_device *iwdev, struct i40iw_manage_vf_pble_info *info, bool wait)

    manage vf pbles

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_manage_vf_pble_info \*info:
        info for managing pble

    :param bool wait:
        flag wait for completion

.. _`i40iw_get_ib_wc`:

i40iw_get_ib_wc
===============

.. c:function:: enum ib_wc_status i40iw_get_ib_wc(enum i40iw_flush_opcode opcode)

    return change flush code to IB's

    :param enum i40iw_flush_opcode opcode:
        iwarp flush code

.. _`i40iw_set_flush_info`:

i40iw_set_flush_info
====================

.. c:function:: void i40iw_set_flush_info(struct i40iw_qp_flush_info *pinfo, u16 *min, u16 *maj, enum i40iw_flush_opcode opcode)

    set flush info

    :param struct i40iw_qp_flush_info \*pinfo:
        set flush info

    :param u16 \*min:
        minor err

    :param u16 \*maj:
        major err

    :param enum i40iw_flush_opcode opcode:
        flush error code

.. _`i40iw_flush_wqes`:

i40iw_flush_wqes
================

.. c:function:: void i40iw_flush_wqes(struct i40iw_device *iwdev, struct i40iw_qp *iwqp)

    flush wqe for qp

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_qp \*iwqp:
        qp to flush wqes

.. This file was automatic generated / don't edit.

