.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/nes/nes_cm.c

.. _`create_event`:

create_event
============

.. c:function:: struct nes_cm_event *create_event(struct nes_cm_node *cm_node, enum nes_cm_event_type type)

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

    :param type:
        *undescribed*
    :type type: enum nes_cm_event_type

.. _`send_mpa_request`:

send_mpa_request
================

.. c:function:: int send_mpa_request(struct nes_cm_node *cm_node, struct sk_buff *skb)

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`parse_mpa`:

parse_mpa
=========

.. c:function:: int parse_mpa(struct nes_cm_node *cm_node, u8 *buffer, u32 *type, u32 len)

    process a received TCP pkt, we are expecting an IETF MPA frame

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

    :param buffer:
        *undescribed*
    :type buffer: u8 \*

    :param type:
        *undescribed*
    :type type: u32 \*

    :param len:
        *undescribed*
    :type len: u32

.. _`form_cm_frame`:

form_cm_frame
=============

.. c:function:: void form_cm_frame(struct sk_buff *skb, struct nes_cm_node *cm_node, void *options, u32 optionsize, void *data, u32 datasize, u8 flags)

    get a free packet and build empty frame Use node info to build.

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

    :param options:
        *undescribed*
    :type options: void \*

    :param optionsize:
        *undescribed*
    :type optionsize: u32

    :param data:
        *undescribed*
    :type data: void \*

    :param datasize:
        *undescribed*
    :type datasize: u32

    :param flags:
        *undescribed*
    :type flags: u8

.. _`print_core`:

print_core
==========

.. c:function:: void print_core(struct nes_cm_core *core)

    dump a cm core

    :param core:
        *undescribed*
    :type core: struct nes_cm_core \*

.. _`cm_build_mpa_frame`:

cm_build_mpa_frame
==================

.. c:function:: int cm_build_mpa_frame(struct nes_cm_node *cm_node, u8 **start_buff, u16 *buff_len, u8 *pci_mem, u8 mpa_key)

    build a MPA V1 frame or MPA V2 frame

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

    :param start_buff:
        *undescribed*
    :type start_buff: u8 \*\*

    :param buff_len:
        *undescribed*
    :type buff_len: u16 \*

    :param pci_mem:
        *undescribed*
    :type pci_mem: u8 \*

    :param mpa_key:
        *undescribed*
    :type mpa_key: u8

.. _`build_mpa_v2`:

build_mpa_v2
============

.. c:function:: void build_mpa_v2(struct nes_cm_node *cm_node, void *start_addr, u8 mpa_key)

    build a MPA V2 frame

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

    :param start_addr:
        *undescribed*
    :type start_addr: void \*

    :param mpa_key:
        *undescribed*
    :type mpa_key: u8

.. _`build_mpa_v1`:

build_mpa_v1
============

.. c:function:: void build_mpa_v1(struct nes_cm_node *cm_node, void *start_addr, u8 mpa_key)

    build a MPA V1 frame

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

    :param start_addr:
        *undescribed*
    :type start_addr: void \*

    :param mpa_key:
        *undescribed*
    :type mpa_key: u8

.. _`schedule_nes_timer`:

schedule_nes_timer
==================

.. c:function:: int schedule_nes_timer(struct nes_cm_node *cm_node, struct sk_buff *skb, enum nes_timer_type type, int send_retrans, int close_when_complete)

    note - cm_node needs to be protected before calling this. Encase in: rem_ref_cm_node(cm_core, cm_node);add_ref_cm_node(cm_node);

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param type:
        *undescribed*
    :type type: enum nes_timer_type

    :param send_retrans:
        *undescribed*
    :type send_retrans: int

    :param close_when_complete:
        *undescribed*
    :type close_when_complete: int

.. _`nes_cm_timer_tick`:

nes_cm_timer_tick
=================

.. c:function:: void nes_cm_timer_tick(struct timer_list *unused)

    :param unused:
        *undescribed*
    :type unused: struct timer_list \*

.. _`send_syn`:

send_syn
========

.. c:function:: int send_syn(struct nes_cm_node *cm_node, u32 sendack, struct sk_buff *skb)

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

    :param sendack:
        *undescribed*
    :type sendack: u32

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`send_reset`:

send_reset
==========

.. c:function:: int send_reset(struct nes_cm_node *cm_node, struct sk_buff *skb)

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`send_ack`:

send_ack
========

.. c:function:: int send_ack(struct nes_cm_node *cm_node, struct sk_buff *skb)

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`send_fin`:

send_fin
========

.. c:function:: int send_fin(struct nes_cm_node *cm_node, struct sk_buff *skb)

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`find_node`:

find_node
=========

.. c:function:: struct nes_cm_node *find_node(struct nes_cm_core *cm_core, u16 rem_port, nes_addr_t rem_addr, u16 loc_port, nes_addr_t loc_addr)

    find a cm node that matches the reference cm node

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

    :param rem_port:
        *undescribed*
    :type rem_port: u16

    :param rem_addr:
        *undescribed*
    :type rem_addr: nes_addr_t

    :param loc_port:
        *undescribed*
    :type loc_port: u16

    :param loc_addr:
        *undescribed*
    :type loc_addr: nes_addr_t

.. _`find_listener`:

find_listener
=============

.. c:function:: struct nes_cm_listener *find_listener(struct nes_cm_core *cm_core, nes_addr_t dst_addr, u16 dst_port, enum nes_cm_listener_state listener_state)

    find a cm node listening on this addr-port pair

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

    :param dst_addr:
        *undescribed*
    :type dst_addr: nes_addr_t

    :param dst_port:
        *undescribed*
    :type dst_port: u16

    :param listener_state:
        *undescribed*
    :type listener_state: enum nes_cm_listener_state

.. _`add_hte_node`:

add_hte_node
============

.. c:function:: int add_hte_node(struct nes_cm_core *cm_core, struct nes_cm_node *cm_node)

    add a cm node to the hash table

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

.. _`mini_cm_dec_refcnt_listen`:

mini_cm_dec_refcnt_listen
=========================

.. c:function:: int mini_cm_dec_refcnt_listen(struct nes_cm_core *cm_core, struct nes_cm_listener *listener, int free_hanging_nodes)

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

    :param listener:
        *undescribed*
    :type listener: struct nes_cm_listener \*

    :param free_hanging_nodes:
        *undescribed*
    :type free_hanging_nodes: int

.. _`mini_cm_del_listen`:

mini_cm_del_listen
==================

.. c:function:: int mini_cm_del_listen(struct nes_cm_core *cm_core, struct nes_cm_listener *listener)

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

    :param listener:
        *undescribed*
    :type listener: struct nes_cm_listener \*

.. _`mini_cm_accelerated`:

mini_cm_accelerated
===================

.. c:function:: int mini_cm_accelerated(struct nes_cm_core *cm_core, struct nes_cm_node *cm_node)

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

.. _`nes_addr_resolve_neigh`:

nes_addr_resolve_neigh
======================

.. c:function:: int nes_addr_resolve_neigh(struct nes_vnic *nesvnic, u32 dst_ip, int arpindex)

    :param nesvnic:
        *undescribed*
    :type nesvnic: struct nes_vnic \*

    :param dst_ip:
        *undescribed*
    :type dst_ip: u32

    :param arpindex:
        *undescribed*
    :type arpindex: int

.. _`make_cm_node`:

make_cm_node
============

.. c:function:: struct nes_cm_node *make_cm_node(struct nes_cm_core *cm_core, struct nes_vnic *nesvnic, struct nes_cm_info *cm_info, struct nes_cm_listener *listener)

    create a new instance of a cm node

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

    :param nesvnic:
        *undescribed*
    :type nesvnic: struct nes_vnic \*

    :param cm_info:
        *undescribed*
    :type cm_info: struct nes_cm_info \*

    :param listener:
        *undescribed*
    :type listener: struct nes_cm_listener \*

.. _`add_ref_cm_node`:

add_ref_cm_node
===============

.. c:function:: int add_ref_cm_node(struct nes_cm_node *cm_node)

    destroy an instance of a cm node

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

.. _`rem_ref_cm_node`:

rem_ref_cm_node
===============

.. c:function:: int rem_ref_cm_node(struct nes_cm_core *cm_core, struct nes_cm_node *cm_node)

    destroy an instance of a cm node

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

.. _`process_options`:

process_options
===============

.. c:function:: int process_options(struct nes_cm_node *cm_node, u8 *optionsloc, u32 optionsize, u32 syn_packet)

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

    :param optionsloc:
        *undescribed*
    :type optionsloc: u8 \*

    :param optionsize:
        *undescribed*
    :type optionsize: u32

    :param syn_packet:
        *undescribed*
    :type syn_packet: u32

.. _`process_packet`:

process_packet
==============

.. c:function:: void process_packet(struct nes_cm_node *cm_node, struct sk_buff *skb, struct nes_cm_core *cm_core)

    Returns skb if to be freed, else it will return NULL if already used..

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

.. _`mini_cm_listen`:

mini_cm_listen
==============

.. c:function:: struct nes_cm_listener *mini_cm_listen(struct nes_cm_core *cm_core, struct nes_vnic *nesvnic, struct nes_cm_info *cm_info)

    create a listen node with params

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

    :param nesvnic:
        *undescribed*
    :type nesvnic: struct nes_vnic \*

    :param cm_info:
        *undescribed*
    :type cm_info: struct nes_cm_info \*

.. _`mini_cm_connect`:

mini_cm_connect
===============

.. c:function:: struct nes_cm_node *mini_cm_connect(struct nes_cm_core *cm_core, struct nes_vnic *nesvnic, u16 private_data_len, void *private_data, struct nes_cm_info *cm_info)

    make a connection node with params

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

    :param nesvnic:
        *undescribed*
    :type nesvnic: struct nes_vnic \*

    :param private_data_len:
        *undescribed*
    :type private_data_len: u16

    :param private_data:
        *undescribed*
    :type private_data: void \*

    :param cm_info:
        *undescribed*
    :type cm_info: struct nes_cm_info \*

.. _`mini_cm_accept`:

mini_cm_accept
==============

.. c:function:: int mini_cm_accept(struct nes_cm_core *cm_core, struct nes_cm_node *cm_node)

    accept a connection This function is never called

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

.. _`mini_cm_reject`:

mini_cm_reject
==============

.. c:function:: int mini_cm_reject(struct nes_cm_core *cm_core, struct nes_cm_node *cm_node)

    reject and teardown a connection

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

.. _`mini_cm_close`:

mini_cm_close
=============

.. c:function:: int mini_cm_close(struct nes_cm_core *cm_core, struct nes_cm_node *cm_node)

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

.. _`mini_cm_recv_pkt`:

mini_cm_recv_pkt
================

.. c:function:: int mini_cm_recv_pkt(struct nes_cm_core *cm_core, struct nes_vnic *nesvnic, struct sk_buff *skb)

    recv an ETHERNET packet, and process it through CM node state machine

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

    :param nesvnic:
        *undescribed*
    :type nesvnic: struct nes_vnic \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`nes_cm_alloc_core`:

nes_cm_alloc_core
=================

.. c:function:: struct nes_cm_core *nes_cm_alloc_core( void)

    allocate a top level instance of a cm core

    :param void:
        no arguments
    :type void: 

.. _`mini_cm_dealloc_core`:

mini_cm_dealloc_core
====================

.. c:function:: int mini_cm_dealloc_core(struct nes_cm_core *cm_core)

    deallocate a top level instance of a cm core

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

.. _`mini_cm_get`:

mini_cm_get
===========

.. c:function:: int mini_cm_get(struct nes_cm_core *cm_core)

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

.. _`mini_cm_set`:

mini_cm_set
===========

.. c:function:: int mini_cm_set(struct nes_cm_core *cm_core, u32 type, u32 value)

    :param cm_core:
        *undescribed*
    :type cm_core: struct nes_cm_core \*

    :param type:
        *undescribed*
    :type type: u32

    :param value:
        *undescribed*
    :type value: u32

.. _`nes_cm_init_tsa_conn`:

nes_cm_init_tsa_conn
====================

.. c:function:: int nes_cm_init_tsa_conn(struct nes_qp *nesqp, struct nes_cm_node *cm_node)

    successfully exchanged when this is called

    :param nesqp:
        *undescribed*
    :type nesqp: struct nes_qp \*

    :param cm_node:
        *undescribed*
    :type cm_node: struct nes_cm_node \*

.. _`nes_cm_disconn`:

nes_cm_disconn
==============

.. c:function:: int nes_cm_disconn(struct nes_qp *nesqp)

    :param nesqp:
        *undescribed*
    :type nesqp: struct nes_qp \*

.. _`nes_disconnect_worker`:

nes_disconnect_worker
=====================

.. c:function:: void nes_disconnect_worker(struct work_struct *work)

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. _`nes_cm_disconn_true`:

nes_cm_disconn_true
===================

.. c:function:: int nes_cm_disconn_true(struct nes_qp *nesqp)

    :param nesqp:
        *undescribed*
    :type nesqp: struct nes_qp \*

.. _`nes_disconnect`:

nes_disconnect
==============

.. c:function:: int nes_disconnect(struct nes_qp *nesqp, int abrupt)

    :param nesqp:
        *undescribed*
    :type nesqp: struct nes_qp \*

    :param abrupt:
        *undescribed*
    :type abrupt: int

.. _`nes_accept`:

nes_accept
==========

.. c:function:: int nes_accept(struct iw_cm_id *cm_id, struct iw_cm_conn_param *conn_param)

    :param cm_id:
        *undescribed*
    :type cm_id: struct iw_cm_id \*

    :param conn_param:
        *undescribed*
    :type conn_param: struct iw_cm_conn_param \*

.. _`nes_reject`:

nes_reject
==========

.. c:function:: int nes_reject(struct iw_cm_id *cm_id, const void *pdata, u8 pdata_len)

    :param cm_id:
        *undescribed*
    :type cm_id: struct iw_cm_id \*

    :param pdata:
        *undescribed*
    :type pdata: const void \*

    :param pdata_len:
        *undescribed*
    :type pdata_len: u8

.. _`nes_connect`:

nes_connect
===========

.. c:function:: int nes_connect(struct iw_cm_id *cm_id, struct iw_cm_conn_param *conn_param)

    setup and launch cm connect node

    :param cm_id:
        *undescribed*
    :type cm_id: struct iw_cm_id \*

    :param conn_param:
        *undescribed*
    :type conn_param: struct iw_cm_conn_param \*

.. _`nes_create_listen`:

nes_create_listen
=================

.. c:function:: int nes_create_listen(struct iw_cm_id *cm_id, int backlog)

    :param cm_id:
        *undescribed*
    :type cm_id: struct iw_cm_id \*

    :param backlog:
        *undescribed*
    :type backlog: int

.. _`nes_destroy_listen`:

nes_destroy_listen
==================

.. c:function:: int nes_destroy_listen(struct iw_cm_id *cm_id)

    :param cm_id:
        *undescribed*
    :type cm_id: struct iw_cm_id \*

.. _`nes_cm_recv`:

nes_cm_recv
===========

.. c:function:: int nes_cm_recv(struct sk_buff *skb, struct net_device *netdevice)

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param netdevice:
        *undescribed*
    :type netdevice: struct net_device \*

.. _`nes_cm_start`:

nes_cm_start
============

.. c:function:: int nes_cm_start( void)

    Start and init a cm core module

    :param void:
        no arguments
    :type void: 

.. _`nes_cm_stop`:

nes_cm_stop
===========

.. c:function:: int nes_cm_stop( void)

    stop and dealloc all cm core instances

    :param void:
        no arguments
    :type void: 

.. _`cm_event_connected`:

cm_event_connected
==================

.. c:function:: void cm_event_connected(struct nes_cm_event *event)

    handle a connected event, setup QPs and HW

    :param event:
        *undescribed*
    :type event: struct nes_cm_event \*

.. _`cm_event_connect_error`:

cm_event_connect_error
======================

.. c:function:: void cm_event_connect_error(struct nes_cm_event *event)

    :param event:
        *undescribed*
    :type event: struct nes_cm_event \*

.. _`cm_event_reset`:

cm_event_reset
==============

.. c:function:: void cm_event_reset(struct nes_cm_event *event)

    :param event:
        *undescribed*
    :type event: struct nes_cm_event \*

.. _`cm_event_mpa_req`:

cm_event_mpa_req
================

.. c:function:: void cm_event_mpa_req(struct nes_cm_event *event)

    :param event:
        *undescribed*
    :type event: struct nes_cm_event \*

.. _`nes_cm_post_event`:

nes_cm_post_event
=================

.. c:function:: int nes_cm_post_event(struct nes_cm_event *event)

    post an event to the cm event handler

    :param event:
        *undescribed*
    :type event: struct nes_cm_event \*

.. _`nes_cm_event_handler`:

nes_cm_event_handler
====================

.. c:function:: void nes_cm_event_handler(struct work_struct *work)

    worker function to handle cm events will free instance of nes_cm_event

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. This file was automatic generated / don't edit.

