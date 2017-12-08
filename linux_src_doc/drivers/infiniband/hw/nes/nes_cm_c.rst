.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/nes/nes_cm.c

.. _`create_event`:

create_event
============

.. c:function:: struct nes_cm_event *create_event(struct nes_cm_node *cm_node, enum nes_cm_event_type type)

    :param struct nes_cm_node \*cm_node:
        *undescribed*

    :param enum nes_cm_event_type type:
        *undescribed*

.. _`send_mpa_request`:

send_mpa_request
================

.. c:function:: int send_mpa_request(struct nes_cm_node *cm_node, struct sk_buff *skb)

    :param struct nes_cm_node \*cm_node:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`parse_mpa`:

parse_mpa
=========

.. c:function:: int parse_mpa(struct nes_cm_node *cm_node, u8 *buffer, u32 *type, u32 len)

    process a received TCP pkt, we are expecting an IETF MPA frame

    :param struct nes_cm_node \*cm_node:
        *undescribed*

    :param u8 \*buffer:
        *undescribed*

    :param u32 \*type:
        *undescribed*

    :param u32 len:
        *undescribed*

.. _`form_cm_frame`:

form_cm_frame
=============

.. c:function:: void form_cm_frame(struct sk_buff *skb, struct nes_cm_node *cm_node, void *options, u32 optionsize, void *data, u32 datasize, u8 flags)

    get a free packet and build empty frame Use node info to build.

    :param struct sk_buff \*skb:
        *undescribed*

    :param struct nes_cm_node \*cm_node:
        *undescribed*

    :param void \*options:
        *undescribed*

    :param u32 optionsize:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param u32 datasize:
        *undescribed*

    :param u8 flags:
        *undescribed*

.. _`print_core`:

print_core
==========

.. c:function:: void print_core(struct nes_cm_core *core)

    dump a cm core

    :param struct nes_cm_core \*core:
        *undescribed*

.. _`cm_build_mpa_frame`:

cm_build_mpa_frame
==================

.. c:function:: int cm_build_mpa_frame(struct nes_cm_node *cm_node, u8 **start_buff, u16 *buff_len, u8 *pci_mem, u8 mpa_key)

    build a MPA V1 frame or MPA V2 frame

    :param struct nes_cm_node \*cm_node:
        *undescribed*

    :param u8 \*\*start_buff:
        *undescribed*

    :param u16 \*buff_len:
        *undescribed*

    :param u8 \*pci_mem:
        *undescribed*

    :param u8 mpa_key:
        *undescribed*

.. _`build_mpa_v2`:

build_mpa_v2
============

.. c:function:: void build_mpa_v2(struct nes_cm_node *cm_node, void *start_addr, u8 mpa_key)

    build a MPA V2 frame

    :param struct nes_cm_node \*cm_node:
        *undescribed*

    :param void \*start_addr:
        *undescribed*

    :param u8 mpa_key:
        *undescribed*

.. _`build_mpa_v1`:

build_mpa_v1
============

.. c:function:: void build_mpa_v1(struct nes_cm_node *cm_node, void *start_addr, u8 mpa_key)

    build a MPA V1 frame

    :param struct nes_cm_node \*cm_node:
        *undescribed*

    :param void \*start_addr:
        *undescribed*

    :param u8 mpa_key:
        *undescribed*

.. _`schedule_nes_timer`:

schedule_nes_timer
==================

.. c:function:: int schedule_nes_timer(struct nes_cm_node *cm_node, struct sk_buff *skb, enum nes_timer_type type, int send_retrans, int close_when_complete)

    note - cm_node needs to be protected before calling this. Encase in: rem_ref_cm_node(cm_core, cm_node);add_ref_cm_node(cm_node);

    :param struct nes_cm_node \*cm_node:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

    :param enum nes_timer_type type:
        *undescribed*

    :param int send_retrans:
        *undescribed*

    :param int close_when_complete:
        *undescribed*

.. _`nes_cm_timer_tick`:

nes_cm_timer_tick
=================

.. c:function:: void nes_cm_timer_tick(struct timer_list *unused)

    :param struct timer_list \*unused:
        *undescribed*

.. _`send_syn`:

send_syn
========

.. c:function:: int send_syn(struct nes_cm_node *cm_node, u32 sendack, struct sk_buff *skb)

    :param struct nes_cm_node \*cm_node:
        *undescribed*

    :param u32 sendack:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`send_reset`:

send_reset
==========

.. c:function:: int send_reset(struct nes_cm_node *cm_node, struct sk_buff *skb)

    :param struct nes_cm_node \*cm_node:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`send_ack`:

send_ack
========

.. c:function:: int send_ack(struct nes_cm_node *cm_node, struct sk_buff *skb)

    :param struct nes_cm_node \*cm_node:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`send_fin`:

send_fin
========

.. c:function:: int send_fin(struct nes_cm_node *cm_node, struct sk_buff *skb)

    :param struct nes_cm_node \*cm_node:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`find_node`:

find_node
=========

.. c:function:: struct nes_cm_node *find_node(struct nes_cm_core *cm_core, u16 rem_port, nes_addr_t rem_addr, u16 loc_port, nes_addr_t loc_addr)

    find a cm node that matches the reference cm node

    :param struct nes_cm_core \*cm_core:
        *undescribed*

    :param u16 rem_port:
        *undescribed*

    :param nes_addr_t rem_addr:
        *undescribed*

    :param u16 loc_port:
        *undescribed*

    :param nes_addr_t loc_addr:
        *undescribed*

.. _`find_listener`:

find_listener
=============

.. c:function:: struct nes_cm_listener *find_listener(struct nes_cm_core *cm_core, nes_addr_t dst_addr, u16 dst_port, enum nes_cm_listener_state listener_state)

    find a cm node listening on this addr-port pair

    :param struct nes_cm_core \*cm_core:
        *undescribed*

    :param nes_addr_t dst_addr:
        *undescribed*

    :param u16 dst_port:
        *undescribed*

    :param enum nes_cm_listener_state listener_state:
        *undescribed*

.. _`add_hte_node`:

add_hte_node
============

.. c:function:: int add_hte_node(struct nes_cm_core *cm_core, struct nes_cm_node *cm_node)

    add a cm node to the hash table

    :param struct nes_cm_core \*cm_core:
        *undescribed*

    :param struct nes_cm_node \*cm_node:
        *undescribed*

.. _`mini_cm_dec_refcnt_listen`:

mini_cm_dec_refcnt_listen
=========================

.. c:function:: int mini_cm_dec_refcnt_listen(struct nes_cm_core *cm_core, struct nes_cm_listener *listener, int free_hanging_nodes)

    :param struct nes_cm_core \*cm_core:
        *undescribed*

    :param struct nes_cm_listener \*listener:
        *undescribed*

    :param int free_hanging_nodes:
        *undescribed*

.. _`mini_cm_del_listen`:

mini_cm_del_listen
==================

.. c:function:: int mini_cm_del_listen(struct nes_cm_core *cm_core, struct nes_cm_listener *listener)

    :param struct nes_cm_core \*cm_core:
        *undescribed*

    :param struct nes_cm_listener \*listener:
        *undescribed*

.. _`mini_cm_accelerated`:

mini_cm_accelerated
===================

.. c:function:: int mini_cm_accelerated(struct nes_cm_core *cm_core, struct nes_cm_node *cm_node)

    :param struct nes_cm_core \*cm_core:
        *undescribed*

    :param struct nes_cm_node \*cm_node:
        *undescribed*

.. _`nes_addr_resolve_neigh`:

nes_addr_resolve_neigh
======================

.. c:function:: int nes_addr_resolve_neigh(struct nes_vnic *nesvnic, u32 dst_ip, int arpindex)

    :param struct nes_vnic \*nesvnic:
        *undescribed*

    :param u32 dst_ip:
        *undescribed*

    :param int arpindex:
        *undescribed*

.. _`make_cm_node`:

make_cm_node
============

.. c:function:: struct nes_cm_node *make_cm_node(struct nes_cm_core *cm_core, struct nes_vnic *nesvnic, struct nes_cm_info *cm_info, struct nes_cm_listener *listener)

    create a new instance of a cm node

    :param struct nes_cm_core \*cm_core:
        *undescribed*

    :param struct nes_vnic \*nesvnic:
        *undescribed*

    :param struct nes_cm_info \*cm_info:
        *undescribed*

    :param struct nes_cm_listener \*listener:
        *undescribed*

.. _`add_ref_cm_node`:

add_ref_cm_node
===============

.. c:function:: int add_ref_cm_node(struct nes_cm_node *cm_node)

    destroy an instance of a cm node

    :param struct nes_cm_node \*cm_node:
        *undescribed*

.. _`rem_ref_cm_node`:

rem_ref_cm_node
===============

.. c:function:: int rem_ref_cm_node(struct nes_cm_core *cm_core, struct nes_cm_node *cm_node)

    destroy an instance of a cm node

    :param struct nes_cm_core \*cm_core:
        *undescribed*

    :param struct nes_cm_node \*cm_node:
        *undescribed*

.. _`process_options`:

process_options
===============

.. c:function:: int process_options(struct nes_cm_node *cm_node, u8 *optionsloc, u32 optionsize, u32 syn_packet)

    :param struct nes_cm_node \*cm_node:
        *undescribed*

    :param u8 \*optionsloc:
        *undescribed*

    :param u32 optionsize:
        *undescribed*

    :param u32 syn_packet:
        *undescribed*

.. _`process_packet`:

process_packet
==============

.. c:function:: void process_packet(struct nes_cm_node *cm_node, struct sk_buff *skb, struct nes_cm_core *cm_core)

    Returns skb if to be freed, else it will return NULL if already used..

    :param struct nes_cm_node \*cm_node:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

    :param struct nes_cm_core \*cm_core:
        *undescribed*

.. _`mini_cm_listen`:

mini_cm_listen
==============

.. c:function:: struct nes_cm_listener *mini_cm_listen(struct nes_cm_core *cm_core, struct nes_vnic *nesvnic, struct nes_cm_info *cm_info)

    create a listen node with params

    :param struct nes_cm_core \*cm_core:
        *undescribed*

    :param struct nes_vnic \*nesvnic:
        *undescribed*

    :param struct nes_cm_info \*cm_info:
        *undescribed*

.. _`mini_cm_connect`:

mini_cm_connect
===============

.. c:function:: struct nes_cm_node *mini_cm_connect(struct nes_cm_core *cm_core, struct nes_vnic *nesvnic, u16 private_data_len, void *private_data, struct nes_cm_info *cm_info)

    make a connection node with params

    :param struct nes_cm_core \*cm_core:
        *undescribed*

    :param struct nes_vnic \*nesvnic:
        *undescribed*

    :param u16 private_data_len:
        *undescribed*

    :param void \*private_data:
        *undescribed*

    :param struct nes_cm_info \*cm_info:
        *undescribed*

.. _`mini_cm_accept`:

mini_cm_accept
==============

.. c:function:: int mini_cm_accept(struct nes_cm_core *cm_core, struct nes_cm_node *cm_node)

    accept a connection This function is never called

    :param struct nes_cm_core \*cm_core:
        *undescribed*

    :param struct nes_cm_node \*cm_node:
        *undescribed*

.. _`mini_cm_reject`:

mini_cm_reject
==============

.. c:function:: int mini_cm_reject(struct nes_cm_core *cm_core, struct nes_cm_node *cm_node)

    reject and teardown a connection

    :param struct nes_cm_core \*cm_core:
        *undescribed*

    :param struct nes_cm_node \*cm_node:
        *undescribed*

.. _`mini_cm_close`:

mini_cm_close
=============

.. c:function:: int mini_cm_close(struct nes_cm_core *cm_core, struct nes_cm_node *cm_node)

    :param struct nes_cm_core \*cm_core:
        *undescribed*

    :param struct nes_cm_node \*cm_node:
        *undescribed*

.. _`mini_cm_recv_pkt`:

mini_cm_recv_pkt
================

.. c:function:: int mini_cm_recv_pkt(struct nes_cm_core *cm_core, struct nes_vnic *nesvnic, struct sk_buff *skb)

    recv an ETHERNET packet, and process it through CM node state machine

    :param struct nes_cm_core \*cm_core:
        *undescribed*

    :param struct nes_vnic \*nesvnic:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`nes_cm_alloc_core`:

nes_cm_alloc_core
=================

.. c:function:: struct nes_cm_core *nes_cm_alloc_core( void)

    allocate a top level instance of a cm core

    :param  void:
        no arguments

.. _`mini_cm_dealloc_core`:

mini_cm_dealloc_core
====================

.. c:function:: int mini_cm_dealloc_core(struct nes_cm_core *cm_core)

    deallocate a top level instance of a cm core

    :param struct nes_cm_core \*cm_core:
        *undescribed*

.. _`mini_cm_get`:

mini_cm_get
===========

.. c:function:: int mini_cm_get(struct nes_cm_core *cm_core)

    :param struct nes_cm_core \*cm_core:
        *undescribed*

.. _`mini_cm_set`:

mini_cm_set
===========

.. c:function:: int mini_cm_set(struct nes_cm_core *cm_core, u32 type, u32 value)

    :param struct nes_cm_core \*cm_core:
        *undescribed*

    :param u32 type:
        *undescribed*

    :param u32 value:
        *undescribed*

.. _`nes_cm_init_tsa_conn`:

nes_cm_init_tsa_conn
====================

.. c:function:: int nes_cm_init_tsa_conn(struct nes_qp *nesqp, struct nes_cm_node *cm_node)

    successfully exchanged when this is called

    :param struct nes_qp \*nesqp:
        *undescribed*

    :param struct nes_cm_node \*cm_node:
        *undescribed*

.. _`nes_cm_disconn`:

nes_cm_disconn
==============

.. c:function:: int nes_cm_disconn(struct nes_qp *nesqp)

    :param struct nes_qp \*nesqp:
        *undescribed*

.. _`nes_disconnect_worker`:

nes_disconnect_worker
=====================

.. c:function:: void nes_disconnect_worker(struct work_struct *work)

    :param struct work_struct \*work:
        *undescribed*

.. _`nes_cm_disconn_true`:

nes_cm_disconn_true
===================

.. c:function:: int nes_cm_disconn_true(struct nes_qp *nesqp)

    :param struct nes_qp \*nesqp:
        *undescribed*

.. _`nes_disconnect`:

nes_disconnect
==============

.. c:function:: int nes_disconnect(struct nes_qp *nesqp, int abrupt)

    :param struct nes_qp \*nesqp:
        *undescribed*

    :param int abrupt:
        *undescribed*

.. _`nes_accept`:

nes_accept
==========

.. c:function:: int nes_accept(struct iw_cm_id *cm_id, struct iw_cm_conn_param *conn_param)

    :param struct iw_cm_id \*cm_id:
        *undescribed*

    :param struct iw_cm_conn_param \*conn_param:
        *undescribed*

.. _`nes_reject`:

nes_reject
==========

.. c:function:: int nes_reject(struct iw_cm_id *cm_id, const void *pdata, u8 pdata_len)

    :param struct iw_cm_id \*cm_id:
        *undescribed*

    :param const void \*pdata:
        *undescribed*

    :param u8 pdata_len:
        *undescribed*

.. _`nes_connect`:

nes_connect
===========

.. c:function:: int nes_connect(struct iw_cm_id *cm_id, struct iw_cm_conn_param *conn_param)

    setup and launch cm connect node

    :param struct iw_cm_id \*cm_id:
        *undescribed*

    :param struct iw_cm_conn_param \*conn_param:
        *undescribed*

.. _`nes_create_listen`:

nes_create_listen
=================

.. c:function:: int nes_create_listen(struct iw_cm_id *cm_id, int backlog)

    :param struct iw_cm_id \*cm_id:
        *undescribed*

    :param int backlog:
        *undescribed*

.. _`nes_destroy_listen`:

nes_destroy_listen
==================

.. c:function:: int nes_destroy_listen(struct iw_cm_id *cm_id)

    :param struct iw_cm_id \*cm_id:
        *undescribed*

.. _`nes_cm_recv`:

nes_cm_recv
===========

.. c:function:: int nes_cm_recv(struct sk_buff *skb, struct net_device *netdevice)

    :param struct sk_buff \*skb:
        *undescribed*

    :param struct net_device \*netdevice:
        *undescribed*

.. _`nes_cm_start`:

nes_cm_start
============

.. c:function:: int nes_cm_start( void)

    Start and init a cm core module

    :param  void:
        no arguments

.. _`nes_cm_stop`:

nes_cm_stop
===========

.. c:function:: int nes_cm_stop( void)

    stop and dealloc all cm core instances

    :param  void:
        no arguments

.. _`cm_event_connected`:

cm_event_connected
==================

.. c:function:: void cm_event_connected(struct nes_cm_event *event)

    handle a connected event, setup QPs and HW

    :param struct nes_cm_event \*event:
        *undescribed*

.. _`cm_event_connect_error`:

cm_event_connect_error
======================

.. c:function:: void cm_event_connect_error(struct nes_cm_event *event)

    :param struct nes_cm_event \*event:
        *undescribed*

.. _`cm_event_reset`:

cm_event_reset
==============

.. c:function:: void cm_event_reset(struct nes_cm_event *event)

    :param struct nes_cm_event \*event:
        *undescribed*

.. _`cm_event_mpa_req`:

cm_event_mpa_req
================

.. c:function:: void cm_event_mpa_req(struct nes_cm_event *event)

    :param struct nes_cm_event \*event:
        *undescribed*

.. _`nes_cm_post_event`:

nes_cm_post_event
=================

.. c:function:: int nes_cm_post_event(struct nes_cm_event *event)

    post an event to the cm event handler

    :param struct nes_cm_event \*event:
        *undescribed*

.. _`nes_cm_event_handler`:

nes_cm_event_handler
====================

.. c:function:: void nes_cm_event_handler(struct work_struct *work)

    worker function to handle cm events will free instance of nes_cm_event

    :param struct work_struct \*work:
        *undescribed*

.. This file was automatic generated / don't edit.

