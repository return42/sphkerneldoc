.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/broadcom/bnx2x/bnx2x_sp.c

.. _`bnx2x_exe_queue_init`:

bnx2x_exe_queue_init
====================

.. c:function:: void bnx2x_exe_queue_init(struct bnx2x *bp, struct bnx2x_exe_queue_obj *o, int exe_len, union bnx2x_qable_obj *owner, exe_q_validate validate, exe_q_remove remove, exe_q_optimize optimize, exe_q_execute exec, exe_q_get get)

    init the Exe Queue object

    :param bp:
        *undescribed*
    :type bp: struct bnx2x \*

    :param o:
        pointer to the object
    :type o: struct bnx2x_exe_queue_obj \*

    :param exe_len:
        length
    :type exe_len: int

    :param owner:
        pointer to the owner
    :type owner: union bnx2x_qable_obj \*

    :param validate:
        validate function pointer
    :type validate: exe_q_validate

    :param remove:
        *undescribed*
    :type remove: exe_q_remove

    :param optimize:
        optimize function pointer
    :type optimize: exe_q_optimize

    :param exec:
        execute function pointer
    :type exec: exe_q_execute

    :param get:
        get function pointer
    :type get: exe_q_get

.. _`bnx2x_exe_queue_add`:

bnx2x_exe_queue_add
===================

.. c:function:: int bnx2x_exe_queue_add(struct bnx2x *bp, struct bnx2x_exe_queue_obj *o, struct bnx2x_exeq_elem *elem, bool restore)

    add a new element to the execution queue

    :param bp:
        driver handle
    :type bp: struct bnx2x \*

    :param o:
        queue
    :type o: struct bnx2x_exe_queue_obj \*

    :param elem:
        *undescribed*
    :type elem: struct bnx2x_exeq_elem \*

    :param restore:
        true - do not optimize the command
    :type restore: bool

.. _`bnx2x_exe_queue_add.description`:

Description
-----------

If the element is optimized or is illegal, frees it.

.. _`bnx2x_exe_queue_step`:

bnx2x_exe_queue_step
====================

.. c:function:: int bnx2x_exe_queue_step(struct bnx2x *bp, struct bnx2x_exe_queue_obj *o, unsigned long *ramrod_flags)

    execute one execution chunk atomically

    :param bp:
        driver handle
    :type bp: struct bnx2x \*

    :param o:
        queue
    :type o: struct bnx2x_exe_queue_obj \*

    :param ramrod_flags:
        flags
    :type ramrod_flags: unsigned long \*

.. _`bnx2x_exe_queue_step.description`:

Description
-----------

(Should be called while holding the exe_queue->lock).

.. _`bnx2x_state_wait`:

bnx2x_state_wait
================

.. c:function:: int bnx2x_state_wait(struct bnx2x *bp, int state, unsigned long *pstate)

    wait until the given bit(state) is cleared

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param state:
        state which is to be cleared
    :type state: int

    :param pstate:
        *undescribed*
    :type pstate: unsigned long \*

.. _`__bnx2x_vlan_mac_h_write_trylock`:

\__bnx2x_vlan_mac_h_write_trylock
=================================

.. c:function:: int __bnx2x_vlan_mac_h_write_trylock(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *o)

    try getting the vlan mac writer lock

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        vlan_mac object
    :type o: struct bnx2x_vlan_mac_obj \*

.. _`__bnx2x_vlan_mac_h_exec_pending`:

\__bnx2x_vlan_mac_h_exec_pending
================================

.. c:function:: void __bnx2x_vlan_mac_h_exec_pending(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *o)

    execute step instead of a previous step

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        vlan_mac object
    :type o: struct bnx2x_vlan_mac_obj \*

.. _`__bnx2x_vlan_mac_h_exec_pending.description`:

Description
-----------

\ ``details``\  Should be called under execution queue lock; notice it might release
and reclaim it during its run.

.. _`__bnx2x_vlan_mac_h_pend`:

\__bnx2x_vlan_mac_h_pend
========================

.. c:function:: void __bnx2x_vlan_mac_h_pend(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *o, unsigned long ramrod_flags)

    Pend an execution step which couldn't run

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        vlan_mac object
    :type o: struct bnx2x_vlan_mac_obj \*

    :param ramrod_flags:
        ramrod flags of missed execution
    :type ramrod_flags: unsigned long

.. _`__bnx2x_vlan_mac_h_pend.description`:

Description
-----------

\ ``details``\  Should be called under execution queue lock.

.. _`__bnx2x_vlan_mac_h_write_unlock`:

\__bnx2x_vlan_mac_h_write_unlock
================================

.. c:function:: void __bnx2x_vlan_mac_h_write_unlock(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *o)

    unlock the vlan mac head list writer lock

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        vlan_mac object
    :type o: struct bnx2x_vlan_mac_obj \*

.. _`__bnx2x_vlan_mac_h_write_unlock.description`:

Description
-----------

\ ``details``\  Should be called under execution queue lock. Notice if a pending
execution exists, it would perform it - possibly releasing and
reclaiming the execution queue lock.

.. _`__bnx2x_vlan_mac_h_read_lock`:

\__bnx2x_vlan_mac_h_read_lock
=============================

.. c:function:: int __bnx2x_vlan_mac_h_read_lock(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *o)

    lock the vlan mac head list reader lock

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        vlan_mac object
    :type o: struct bnx2x_vlan_mac_obj \*

.. _`__bnx2x_vlan_mac_h_read_lock.description`:

Description
-----------

\ ``details``\  Should be called under the execution queue lock. May sleep. May
release and reclaim execution queue lock during its run.

.. _`bnx2x_vlan_mac_h_read_lock`:

bnx2x_vlan_mac_h_read_lock
==========================

.. c:function:: int bnx2x_vlan_mac_h_read_lock(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *o)

    lock the vlan mac head list reader lock

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        vlan_mac object
    :type o: struct bnx2x_vlan_mac_obj \*

.. _`bnx2x_vlan_mac_h_read_lock.description`:

Description
-----------

\ ``details``\  May sleep. Claims and releases execution queue lock during its run.

.. _`__bnx2x_vlan_mac_h_read_unlock`:

\__bnx2x_vlan_mac_h_read_unlock
===============================

.. c:function:: void __bnx2x_vlan_mac_h_read_unlock(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *o)

    unlock the vlan mac head list reader lock

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        vlan_mac object
    :type o: struct bnx2x_vlan_mac_obj \*

.. _`__bnx2x_vlan_mac_h_read_unlock.description`:

Description
-----------

\ ``details``\  Should be called under execution queue lock. Notice if a pending
execution exists, it would be performed if this was the last
reader. possibly releasing and reclaiming the execution queue lock.

.. _`bnx2x_vlan_mac_h_read_unlock`:

bnx2x_vlan_mac_h_read_unlock
============================

.. c:function:: void bnx2x_vlan_mac_h_read_unlock(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *o)

    unlock the vlan mac head list reader lock

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        vlan_mac object
    :type o: struct bnx2x_vlan_mac_obj \*

.. _`bnx2x_vlan_mac_h_read_unlock.description`:

Description
-----------

\ ``details``\  Notice if a pending execution exists, it would be performed if this
was the last reader. Claims and releases the execution queue lock
during its run.

.. _`bnx2x_vlan_mac_set_cmd_hdr_e2`:

bnx2x_vlan_mac_set_cmd_hdr_e2
=============================

.. c:function:: void bnx2x_vlan_mac_set_cmd_hdr_e2(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *o, bool add, int opcode, struct eth_classify_cmd_header *hdr)

    set a header in a single classify ramrod

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        queue for which we want to configure this rule
    :type o: struct bnx2x_vlan_mac_obj \*

    :param add:
        if true the command is an ADD command, DEL otherwise
    :type add: bool

    :param opcode:
        CLASSIFY_RULE_OPCODE_XXX
    :type opcode: int

    :param hdr:
        pointer to a header to setup
    :type hdr: struct eth_classify_cmd_header \*

.. _`bnx2x_vlan_mac_set_rdata_hdr_e2`:

bnx2x_vlan_mac_set_rdata_hdr_e2
===============================

.. c:function:: void bnx2x_vlan_mac_set_rdata_hdr_e2(u32 cid, int type, struct eth_classify_header *hdr, int rule_cnt)

    set the classify ramrod data header

    :param cid:
        connection id
    :type cid: u32

    :param type:
        BNX2X_FILTER_XXX_PENDING
    :type type: int

    :param hdr:
        pointer to header to setup
    :type hdr: struct eth_classify_header \*

    :param rule_cnt:
        *undescribed*
    :type rule_cnt: int

.. _`bnx2x_vlan_mac_set_rdata_hdr_e2.description`:

Description
-----------

currently we always configure one rule and echo field to contain a CID and an
opcode type.

.. _`bnx2x_vlan_mac_set_rdata_hdr_e1x`:

bnx2x_vlan_mac_set_rdata_hdr_e1x
================================

.. c:function:: void bnx2x_vlan_mac_set_rdata_hdr_e1x(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *o, int type, int cam_offset, struct mac_configuration_hdr *hdr)

    set a header in a single classify ramrod

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        queue
    :type o: struct bnx2x_vlan_mac_obj \*

    :param type:
        *undescribed*
    :type type: int

    :param cam_offset:
        offset in cam memory
    :type cam_offset: int

    :param hdr:
        pointer to a header to setup
    :type hdr: struct mac_configuration_hdr \*

.. _`bnx2x_vlan_mac_set_rdata_hdr_e1x.description`:

Description
-----------

E1/E1H

.. _`bnx2x_set_one_mac_e1x`:

bnx2x_set_one_mac_e1x
=====================

.. c:function:: void bnx2x_set_one_mac_e1x(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *o, struct bnx2x_exeq_elem *elem, int rule_idx, int cam_offset)

    fill a single MAC rule ramrod data

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        bnx2x_vlan_mac_obj
    :type o: struct bnx2x_vlan_mac_obj \*

    :param elem:
        bnx2x_exeq_elem
    :type elem: struct bnx2x_exeq_elem \*

    :param rule_idx:
        rule_idx
    :type rule_idx: int

    :param cam_offset:
        cam_offset
    :type cam_offset: int

.. _`bnx2x_set_one_vlan_mac_e1h`:

bnx2x_set_one_vlan_mac_e1h
==========================

.. c:function:: void bnx2x_set_one_vlan_mac_e1h(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *o, struct bnx2x_exeq_elem *elem, int rule_idx, int cam_offset)

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        bnx2x_vlan_mac_obj
    :type o: struct bnx2x_vlan_mac_obj \*

    :param elem:
        bnx2x_exeq_elem
    :type elem: struct bnx2x_exeq_elem \*

    :param rule_idx:
        rule_idx
    :type rule_idx: int

    :param cam_offset:
        cam_offset
    :type cam_offset: int

.. _`bnx2x_vlan_mac_restore`:

bnx2x_vlan_mac_restore
======================

.. c:function:: int bnx2x_vlan_mac_restore(struct bnx2x *bp, struct bnx2x_vlan_mac_ramrod_params *p, struct bnx2x_vlan_mac_registry_elem **ppos)

    reconfigure next MAC/VLAN/VLAN-MAC element

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param p:
        command parameters
    :type p: struct bnx2x_vlan_mac_ramrod_params \*

    :param ppos:
        pointer to the cookie
    :type ppos: struct bnx2x_vlan_mac_registry_elem \*\*

.. _`bnx2x_vlan_mac_restore.description`:

Description
-----------

reconfigure next MAC/VLAN/VLAN-MAC element from the
previously configured elements list.

from command parameters only RAMROD_COMP_WAIT bit in ramrod_flags is taken
into an account

pointer to the cookie  - that should be given back in the next call to make
function handle the next element. If \*ppos is set to NULL it will restart the
iterator. If returned \*ppos == NULL this means that the last element has been
handled.

.. _`bnx2x_validate_vlan_mac_add`:

bnx2x_validate_vlan_mac_add
===========================

.. c:function:: int bnx2x_validate_vlan_mac_add(struct bnx2x *bp, union bnx2x_qable_obj *qo, struct bnx2x_exeq_elem *elem)

    check if an ADD command can be executed

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param qo:
        bnx2x_qable_obj
    :type qo: union bnx2x_qable_obj \*

    :param elem:
        bnx2x_exeq_elem
    :type elem: struct bnx2x_exeq_elem \*

.. _`bnx2x_validate_vlan_mac_add.description`:

Description
-----------

Checks that the requested configuration can be added. If yes and if
requested, consume CAM credit.

The 'validate' is run after the 'optimize'.

.. _`bnx2x_validate_vlan_mac_del`:

bnx2x_validate_vlan_mac_del
===========================

.. c:function:: int bnx2x_validate_vlan_mac_del(struct bnx2x *bp, union bnx2x_qable_obj *qo, struct bnx2x_exeq_elem *elem)

    check if the DEL command can be executed

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param qo:
        quable object to check
    :type qo: union bnx2x_qable_obj \*

    :param elem:
        element that needs to be deleted
    :type elem: struct bnx2x_exeq_elem \*

.. _`bnx2x_validate_vlan_mac_del.description`:

Description
-----------

Checks that the requested configuration can be deleted. If yes and if
requested, returns a CAM credit.

The 'validate' is run after the 'optimize'.

.. _`bnx2x_validate_vlan_mac_move`:

bnx2x_validate_vlan_mac_move
============================

.. c:function:: int bnx2x_validate_vlan_mac_move(struct bnx2x *bp, union bnx2x_qable_obj *qo, struct bnx2x_exeq_elem *elem)

    check if the MOVE command can be executed

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param qo:
        quable object to check (source)
    :type qo: union bnx2x_qable_obj \*

    :param elem:
        element that needs to be moved
    :type elem: struct bnx2x_exeq_elem \*

.. _`bnx2x_validate_vlan_mac_move.description`:

Description
-----------

Checks that the requested configuration can be moved. If yes and if
requested, returns a CAM credit.

The 'validate' is run after the 'optimize'.

.. _`bnx2x_wait_vlan_mac`:

bnx2x_wait_vlan_mac
===================

.. c:function:: int bnx2x_wait_vlan_mac(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *o)

    passively wait for 5 seconds until all work completes.

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        bnx2x_vlan_mac_obj
    :type o: struct bnx2x_vlan_mac_obj \*

.. _`bnx2x_complete_vlan_mac`:

bnx2x_complete_vlan_mac
=======================

.. c:function:: int bnx2x_complete_vlan_mac(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *o, union event_ring_elem *cqe, unsigned long *ramrod_flags)

    complete one VLAN-MAC ramrod

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        bnx2x_vlan_mac_obj
    :type o: struct bnx2x_vlan_mac_obj \*

    :param cqe:
        *undescribed*
    :type cqe: union event_ring_elem \*

    :param ramrod_flags:
        *undescribed*
    :type ramrod_flags: unsigned long \*

.. _`bnx2x_optimize_vlan_mac`:

bnx2x_optimize_vlan_mac
=======================

.. c:function:: int bnx2x_optimize_vlan_mac(struct bnx2x *bp, union bnx2x_qable_obj *qo, struct bnx2x_exeq_elem *elem)

    optimize ADD and DEL commands.

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param qo:
        *undescribed*
    :type qo: union bnx2x_qable_obj \*

    :param elem:
        bnx2x_exeq_elem
    :type elem: struct bnx2x_exeq_elem \*

.. _`bnx2x_vlan_mac_get_registry_elem`:

bnx2x_vlan_mac_get_registry_elem
================================

.. c:function:: int bnx2x_vlan_mac_get_registry_elem(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *o, struct bnx2x_exeq_elem *elem, bool restore, struct bnx2x_vlan_mac_registry_elem **re)

    prepare a registry element

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        *undescribed*
    :type o: struct bnx2x_vlan_mac_obj \*

    :param elem:
        *undescribed*
    :type elem: struct bnx2x_exeq_elem \*

    :param restore:
        *undescribed*
    :type restore: bool

    :param re:
        *undescribed*
    :type re: struct bnx2x_vlan_mac_registry_elem \*\*

.. _`bnx2x_vlan_mac_get_registry_elem.description`:

Description
-----------

prepare a registry element according to the current command request.

.. _`bnx2x_execute_vlan_mac`:

bnx2x_execute_vlan_mac
======================

.. c:function:: int bnx2x_execute_vlan_mac(struct bnx2x *bp, union bnx2x_qable_obj *qo, struct list_head *exe_chunk, unsigned long *ramrod_flags)

    execute vlan mac command

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param qo:
        *undescribed*
    :type qo: union bnx2x_qable_obj \*

    :param exe_chunk:
        *undescribed*
    :type exe_chunk: struct list_head \*

    :param ramrod_flags:
        *undescribed*
    :type ramrod_flags: unsigned long \*

.. _`bnx2x_execute_vlan_mac.description`:

Description
-----------

go and send a ramrod!

.. _`bnx2x_config_vlan_mac`:

bnx2x_config_vlan_mac
=====================

.. c:function:: int bnx2x_config_vlan_mac(struct bnx2x *bp, struct bnx2x_vlan_mac_ramrod_params *p)

    configure VLAN/MAC/VLAN_MAC filtering rules.

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param p:
        *undescribed*
    :type p: struct bnx2x_vlan_mac_ramrod_params \*

.. _`bnx2x_vlan_mac_del_all`:

bnx2x_vlan_mac_del_all
======================

.. c:function:: int bnx2x_vlan_mac_del_all(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *o, unsigned long *vlan_mac_flags, unsigned long *ramrod_flags)

    delete elements with given vlan_mac_flags spec

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        *undescribed*
    :type o: struct bnx2x_vlan_mac_obj \*

    :param vlan_mac_flags:
        *undescribed*
    :type vlan_mac_flags: unsigned long \*

    :param ramrod_flags:
        execution flags to be used for this deletion
    :type ramrod_flags: unsigned long \*

.. _`bnx2x_vlan_mac_del_all.description`:

Description
-----------

if the last operation has completed successfully and there are no
more elements left, positive value if the last operation has completed
successfully and there are more previously configured elements, negative
value is current operation has failed.

.. _`bnx2x_mcast_get_next_bin`:

bnx2x_mcast_get_next_bin
========================

.. c:function:: int bnx2x_mcast_get_next_bin(struct bnx2x_mcast_obj *o, int last)

    get the next set bin (index)

    :param o:
        *undescribed*
    :type o: struct bnx2x_mcast_obj \*

    :param last:
        index to start looking from (including)
    :type last: int

.. _`bnx2x_mcast_get_next_bin.description`:

Description
-----------

returns the next found (set) bin or a negative value if none is found.

.. _`bnx2x_mcast_clear_first_bin`:

bnx2x_mcast_clear_first_bin
===========================

.. c:function:: int bnx2x_mcast_clear_first_bin(struct bnx2x_mcast_obj *o)

    find the first set bin and clear it

    :param o:
        *undescribed*
    :type o: struct bnx2x_mcast_obj \*

.. _`bnx2x_mcast_clear_first_bin.description`:

Description
-----------

returns the index of the found bin or -1 if none is found

.. _`bnx2x_mcast_handle_restore_cmd_e2`:

bnx2x_mcast_handle_restore_cmd_e2
=================================

.. c:function:: int bnx2x_mcast_handle_restore_cmd_e2(struct bnx2x *bp, struct bnx2x_mcast_obj *o, int start_bin, int *rdata_idx)

    restore configuration from the registry

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        *undescribed*
    :type o: struct bnx2x_mcast_obj \*

    :param start_bin:
        index in the registry to start from (including)
    :type start_bin: int

    :param rdata_idx:
        index in the ramrod data to start from
    :type rdata_idx: int \*

.. _`bnx2x_mcast_handle_restore_cmd_e2.description`:

Description
-----------

returns last handled bin index or -1 if all bins have been handled

.. _`bnx2x_mcast_handle_current_cmd`:

bnx2x_mcast_handle_current_cmd
==============================

.. c:function:: int bnx2x_mcast_handle_current_cmd(struct bnx2x *bp, struct bnx2x_mcast_ramrod_params *p, enum bnx2x_mcast_cmd cmd, int start_cnt)

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param p:
        *undescribed*
    :type p: struct bnx2x_mcast_ramrod_params \*

    :param cmd:
        *undescribed*
    :type cmd: enum bnx2x_mcast_cmd

    :param start_cnt:
        first line in the ramrod data that may be used
    :type start_cnt: int

.. _`bnx2x_mcast_handle_current_cmd.description`:

Description
-----------

This function is called iff there is enough place for the current command in
the ramrod data.
Returns number of lines filled in the ramrod data in total.

.. _`bnx2x_mcast_set_rdata_hdr_e2`:

bnx2x_mcast_set_rdata_hdr_e2
============================

.. c:function:: void bnx2x_mcast_set_rdata_hdr_e2(struct bnx2x *bp, struct bnx2x_mcast_ramrod_params *p, u8 len)

    sets a header values

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param p:
        *undescribed*
    :type p: struct bnx2x_mcast_ramrod_params \*

    :param len:
        number of rules to handle
    :type len: u8

.. _`bnx2x_mcast_refresh_registry_e2`:

bnx2x_mcast_refresh_registry_e2
===============================

.. c:function:: int bnx2x_mcast_refresh_registry_e2(struct bnx2x *bp, struct bnx2x_mcast_obj *o)

    recalculate the actual number of set bins

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        *undescribed*
    :type o: struct bnx2x_mcast_obj \*

.. _`bnx2x_mcast_refresh_registry_e2.description`:

Description
-----------

Recalculate the actual number of set bins in the registry using Brian
Kernighan's algorithm: it's execution complexity is as a number of set bins.

returns 0 for the compliance with \ :c:func:`bnx2x_mcast_refresh_registry_e1`\ .

.. _`bnx2x_mcast_set_rdata_hdr_e1`:

bnx2x_mcast_set_rdata_hdr_e1
============================

.. c:function:: void bnx2x_mcast_set_rdata_hdr_e1(struct bnx2x *bp, struct bnx2x_mcast_ramrod_params *p, u8 len)

    set header values in mac_configuration_cmd

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param p:
        *undescribed*
    :type p: struct bnx2x_mcast_ramrod_params \*

    :param len:
        number of rules to handle
    :type len: u8

.. _`bnx2x_mcast_handle_restore_cmd_e1`:

bnx2x_mcast_handle_restore_cmd_e1
=================================

.. c:function:: int bnx2x_mcast_handle_restore_cmd_e1(struct bnx2x *bp, struct bnx2x_mcast_obj *o, int start_idx, int *rdata_idx)

    restore command for 57710

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        *undescribed*
    :type o: struct bnx2x_mcast_obj \*

    :param start_idx:
        index in the registry to start from
    :type start_idx: int

    :param rdata_idx:
        index in the ramrod data to start from
    :type rdata_idx: int \*

.. _`bnx2x_mcast_handle_restore_cmd_e1.description`:

Description
-----------

restore command for 57710 is like all other commands - always a stand alone
command - start_idx and rdata_idx will always be 0. This function will always
succeed.
returns -1 to comply with 57712 variant.

.. _`bnx2x_get_fw_mac_addr`:

bnx2x_get_fw_mac_addr
=====================

.. c:function:: void bnx2x_get_fw_mac_addr(__le16 *fw_hi, __le16 *fw_mid, __le16 *fw_lo, u8 *mac)

    revert the \ :c:func:`bnx2x_set_fw_mac_addr`\ .

    :param fw_hi:
        *undescribed*
    :type fw_hi: __le16 \*

    :param fw_mid:
        *undescribed*
    :type fw_mid: __le16 \*

    :param fw_lo:
        *undescribed*
    :type fw_lo: __le16 \*

    :param mac:
        *undescribed*
    :type mac: u8 \*

.. _`bnx2x_mcast_refresh_registry_e1`:

bnx2x_mcast_refresh_registry_e1
===============================

.. c:function:: int bnx2x_mcast_refresh_registry_e1(struct bnx2x *bp, struct bnx2x_mcast_obj *o)

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        *undescribed*
    :type o: struct bnx2x_mcast_obj \*

.. _`bnx2x_mcast_refresh_registry_e1.description`:

Description
-----------

Check the ramrod data first entry flag to see if it's a DELETE or ADD command

.. _`bnx2x_mcast_refresh_registry_e1.and-update-the-registry-correspondingly`:

and update the registry correspondingly
---------------------------------------

if ADD - allocate a memory and add
the entries to the registry (list), if DELETE - clear the registry and free
the memory.

.. _`__atomic_add_ifless`:

\__atomic_add_ifless
====================

.. c:function:: bool __atomic_add_ifless(atomic_t *v, int a, int u)

    add if the result is less than a given value.

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

    :param a:
        the amount to add to v...
    :type a: int

    :param u:
        ...if (v + a) is less than u.
    :type u: int

.. _`__atomic_add_ifless.description`:

Description
-----------

returns true if (v + a) was less than u, and false otherwise.

.. _`__atomic_dec_ifmoe`:

\__atomic_dec_ifmoe
===================

.. c:function:: bool __atomic_dec_ifmoe(atomic_t *v, int a, int u)

    dec if the result is more or equal than a given value.

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

    :param a:
        the amount to dec from v...
    :type a: int

    :param u:
        ...if (v - a) is more or equal than u.
    :type u: int

.. _`__atomic_dec_ifmoe.description`:

Description
-----------

returns true if (v - a) was more or equal than u, and false
otherwise.

.. _`bnx2x_init_credit_pool`:

bnx2x_init_credit_pool
======================

.. c:function:: void bnx2x_init_credit_pool(struct bnx2x_credit_pool_obj *p, int base, int credit)

    initialize credit pool internals.

    :param p:
        *undescribed*
    :type p: struct bnx2x_credit_pool_obj \*

    :param base:
        Base entry in the CAM to use.
    :type base: int

    :param credit:
        pool size.
    :type credit: int

.. _`bnx2x_init_credit_pool.description`:

Description
-----------

If base is negative no CAM entries handling will be performed.
If credit is negative pool operations will always succeed (unlimited pool).

.. _`bnx2x_debug_print_ind_table`:

bnx2x_debug_print_ind_table
===========================

.. c:function:: void bnx2x_debug_print_ind_table(struct bnx2x *bp, struct bnx2x_config_rss_params *p)

    prints the indirection table configuration.

    :param bp:
        driver handle
    :type bp: struct bnx2x \*

    :param p:
        pointer to rss configuration
    :type p: struct bnx2x_config_rss_params \*

.. _`bnx2x_debug_print_ind_table.description`:

Description
-----------

Prints it when NETIF_MSG_IFUP debug level is configured.

.. _`bnx2x_setup_rss`:

bnx2x_setup_rss
===============

.. c:function:: int bnx2x_setup_rss(struct bnx2x *bp, struct bnx2x_config_rss_params *p)

    configure RSS

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param p:
        rss configuration
    :type p: struct bnx2x_config_rss_params \*

.. _`bnx2x_setup_rss.description`:

Description
-----------

sends on UPDATE ramrod for that matter.

.. _`bnx2x_queue_state_change`:

bnx2x_queue_state_change
========================

.. c:function:: int bnx2x_queue_state_change(struct bnx2x *bp, struct bnx2x_queue_state_params *params)

    perform Queue state change transition

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param params:
        parameters to perform the transition
    :type params: struct bnx2x_queue_state_params \*

.. _`bnx2x_queue_state_change.description`:

Description
-----------

returns 0 in case of successfully completed transition, negative error
code in case of failure, positive (EBUSY) value if there is a completion
to that is still pending (possible only if RAMROD_COMP_WAIT is
not set in params->ramrod_flags for asynchronous commands).

.. _`bnx2x_queue_comp_cmd`:

bnx2x_queue_comp_cmd
====================

.. c:function:: int bnx2x_queue_comp_cmd(struct bnx2x *bp, struct bnx2x_queue_sp_obj *o, enum bnx2x_queue_cmd cmd)

    complete the state change command.

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        *undescribed*
    :type o: struct bnx2x_queue_sp_obj \*

    :param cmd:
        *undescribed*
    :type cmd: enum bnx2x_queue_cmd

.. _`bnx2x_queue_comp_cmd.description`:

Description
-----------

Checks that the arrived completion is expected.

.. _`bnx2x_q_init`:

bnx2x_q_init
============

.. c:function:: int bnx2x_q_init(struct bnx2x *bp, struct bnx2x_queue_state_params *params)

    init HW/FW queue

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param params:
        *undescribed*
    :type params: struct bnx2x_queue_state_params \*

.. _`bnx2x_q_init.description`:

Description
-----------

HW/FW initial Queue configuration:
- HC: Rx and Tx
- CDU context validation

.. _`bnx2x_q_send_deactivate`:

bnx2x_q_send_deactivate
=======================

.. c:function:: int bnx2x_q_send_deactivate(struct bnx2x *bp, struct bnx2x_queue_state_params *params)

    send DEACTIVATE command

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param params:
        *undescribed*
    :type params: struct bnx2x_queue_state_params \*

.. _`bnx2x_q_send_deactivate.description`:

Description
-----------

implemented using the UPDATE command.

.. _`bnx2x_q_send_activate`:

bnx2x_q_send_activate
=====================

.. c:function:: int bnx2x_q_send_activate(struct bnx2x *bp, struct bnx2x_queue_state_params *params)

    send ACTIVATE command

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param params:
        *undescribed*
    :type params: struct bnx2x_queue_state_params \*

.. _`bnx2x_q_send_activate.description`:

Description
-----------

implemented using the UPDATE command.

.. _`bnx2x_queue_chk_transition`:

bnx2x_queue_chk_transition
==========================

.. c:function:: int bnx2x_queue_chk_transition(struct bnx2x *bp, struct bnx2x_queue_sp_obj *o, struct bnx2x_queue_state_params *params)

    check state machine of a regular Queue

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        *undescribed*
    :type o: struct bnx2x_queue_sp_obj \*

    :param params:
        *undescribed*
    :type params: struct bnx2x_queue_state_params \*

.. _`bnx2x_queue_chk_transition.description`:

Description
-----------

(not Forwarding)
It both checks if the requested command is legal in a current
state and, if it's legal, sets a \`next_state' in the object
that will be used in the completion flow to set the \`state'
of the object.

returns 0 if a requested command is a legal transition,
-EINVAL otherwise.

.. _`bnx2x_func_state_change_comp`:

bnx2x_func_state_change_comp
============================

.. c:function:: int bnx2x_func_state_change_comp(struct bnx2x *bp, struct bnx2x_func_sp_obj *o, enum bnx2x_func_cmd cmd)

    complete the state machine transition

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        *undescribed*
    :type o: struct bnx2x_func_sp_obj \*

    :param cmd:
        *undescribed*
    :type cmd: enum bnx2x_func_cmd

.. _`bnx2x_func_state_change_comp.description`:

Description
-----------

Called on state change transition. Completes the state
machine transition only - no HW interaction.

.. _`bnx2x_func_comp_cmd`:

bnx2x_func_comp_cmd
===================

.. c:function:: int bnx2x_func_comp_cmd(struct bnx2x *bp, struct bnx2x_func_sp_obj *o, enum bnx2x_func_cmd cmd)

    complete the state change command

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        *undescribed*
    :type o: struct bnx2x_func_sp_obj \*

    :param cmd:
        *undescribed*
    :type cmd: enum bnx2x_func_cmd

.. _`bnx2x_func_comp_cmd.description`:

Description
-----------

Checks that the arrived completion is expected.

.. _`bnx2x_func_chk_transition`:

bnx2x_func_chk_transition
=========================

.. c:function:: int bnx2x_func_chk_transition(struct bnx2x *bp, struct bnx2x_func_sp_obj *o, struct bnx2x_func_state_params *params)

    perform function state machine transition

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param o:
        *undescribed*
    :type o: struct bnx2x_func_sp_obj \*

    :param params:
        *undescribed*
    :type params: struct bnx2x_func_state_params \*

.. _`bnx2x_func_chk_transition.description`:

Description
-----------

It both checks if the requested command is legal in a current
state and, if it's legal, sets a \`next_state' in the object
that will be used in the completion flow to set the \`state'
of the object.

returns 0 if a requested command is a legal transition,
-EINVAL otherwise.

.. _`bnx2x_func_init_func`:

bnx2x_func_init_func
====================

.. c:function:: int bnx2x_func_init_func(struct bnx2x *bp, const struct bnx2x_func_sp_drv_ops *drv)

    performs HW init at function stage

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param drv:
        *undescribed*
    :type drv: const struct bnx2x_func_sp_drv_ops \*

.. _`bnx2x_func_init_func.description`:

Description
-----------

Init HW when the current phase is

.. _`bnx2x_func_init_func.fw_msg_code_drv_load_function`:

FW_MSG_CODE_DRV_LOAD_FUNCTION
-----------------------------

initialize only FUNCTION-only
HW blocks.

.. _`bnx2x_func_init_port`:

bnx2x_func_init_port
====================

.. c:function:: int bnx2x_func_init_port(struct bnx2x *bp, const struct bnx2x_func_sp_drv_ops *drv)

    performs HW init at port stage

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param drv:
        *undescribed*
    :type drv: const struct bnx2x_func_sp_drv_ops \*

.. _`bnx2x_func_init_port.description`:

Description
-----------

Init HW when the current phase is

.. _`bnx2x_func_init_port.fw_msg_code_drv_load_port`:

FW_MSG_CODE_DRV_LOAD_PORT
-------------------------

initialize PORT-only and
FUNCTION-only HW blocks.

.. _`bnx2x_func_init_cmn_chip`:

bnx2x_func_init_cmn_chip
========================

.. c:function:: int bnx2x_func_init_cmn_chip(struct bnx2x *bp, const struct bnx2x_func_sp_drv_ops *drv)

    performs HW init at chip-common stage

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param drv:
        *undescribed*
    :type drv: const struct bnx2x_func_sp_drv_ops \*

.. _`bnx2x_func_init_cmn_chip.description`:

Description
-----------

Init HW when the current phase is

.. _`bnx2x_func_init_cmn_chip.fw_msg_code_drv_load_common_chip`:

FW_MSG_CODE_DRV_LOAD_COMMON_CHIP
--------------------------------

initialize COMMON_CHIP,
PORT-only and FUNCTION-only HW blocks.

.. _`bnx2x_func_init_cmn`:

bnx2x_func_init_cmn
===================

.. c:function:: int bnx2x_func_init_cmn(struct bnx2x *bp, const struct bnx2x_func_sp_drv_ops *drv)

    performs HW init at common stage

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param drv:
        *undescribed*
    :type drv: const struct bnx2x_func_sp_drv_ops \*

.. _`bnx2x_func_init_cmn.description`:

Description
-----------

Init HW when the current phase is

.. _`bnx2x_func_init_cmn.fw_msg_code_drv_load_common_chip`:

FW_MSG_CODE_DRV_LOAD_COMMON_CHIP
--------------------------------

initialize COMMON,
PORT-only and FUNCTION-only HW blocks.

.. _`bnx2x_func_reset_func`:

bnx2x_func_reset_func
=====================

.. c:function:: void bnx2x_func_reset_func(struct bnx2x *bp, const struct bnx2x_func_sp_drv_ops *drv)

    reset HW at function stage

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param drv:
        *undescribed*
    :type drv: const struct bnx2x_func_sp_drv_ops \*

.. _`bnx2x_func_reset_func.reset-hw-at-fw_msg_code_drv_unload_function-stage`:

Reset HW at FW_MSG_CODE_DRV_UNLOAD_FUNCTION stage
-------------------------------------------------

reset only
FUNCTION-only HW blocks.

.. _`bnx2x_func_reset_port`:

bnx2x_func_reset_port
=====================

.. c:function:: void bnx2x_func_reset_port(struct bnx2x *bp, const struct bnx2x_func_sp_drv_ops *drv)

    reset HW at port stage

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param drv:
        *undescribed*
    :type drv: const struct bnx2x_func_sp_drv_ops \*

.. _`bnx2x_func_reset_port.reset-hw-at-fw_msg_code_drv_unload_port-stage`:

Reset HW at FW_MSG_CODE_DRV_UNLOAD_PORT stage
---------------------------------------------

reset
FUNCTION-only and PORT-only HW blocks.

!!!IMPORTANT!!!

It's important to call reset_port before \ :c:func:`reset_func`\  as the last thing
reset_func does is \ :c:func:`pf_disable`\  thus disabling PGLUE_B, which
makes impossible any DMAE transactions.

.. _`bnx2x_func_reset_cmn`:

bnx2x_func_reset_cmn
====================

.. c:function:: void bnx2x_func_reset_cmn(struct bnx2x *bp, const struct bnx2x_func_sp_drv_ops *drv)

    reset HW at common stage

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param drv:
        *undescribed*
    :type drv: const struct bnx2x_func_sp_drv_ops \*

.. _`bnx2x_func_reset_cmn.description`:

Description
-----------

Reset HW at FW_MSG_CODE_DRV_UNLOAD_COMMON and

.. _`bnx2x_func_reset_cmn.fw_msg_code_drv_unload_common_chip-stages`:

FW_MSG_CODE_DRV_UNLOAD_COMMON_CHIP stages
-----------------------------------------

reset COMMON,
COMMON_CHIP, FUNCTION-only and PORT-only HW blocks.

.. _`bnx2x_func_state_change`:

bnx2x_func_state_change
=======================

.. c:function:: int bnx2x_func_state_change(struct bnx2x *bp, struct bnx2x_func_state_params *params)

    perform Function state change transition

    :param bp:
        device handle
    :type bp: struct bnx2x \*

    :param params:
        parameters to perform the transaction
    :type params: struct bnx2x_func_state_params \*

.. _`bnx2x_func_state_change.description`:

Description
-----------

returns 0 in case of successfully completed transition,
negative error code in case of failure, positive
(EBUSY) value if there is a completion to that is
still pending (possible only if RAMROD_COMP_WAIT is
not set in params->ramrod_flags for asynchronous
commands).

.. This file was automatic generated / don't edit.

