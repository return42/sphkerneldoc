.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_cm.c

.. _`i40iw_free_sqbuf`:

i40iw_free_sqbuf
================

.. c:function:: void i40iw_free_sqbuf(struct i40iw_sc_vsi *vsi, void *bufp)

    put back puda buffer if refcount = 0

    :param vsi:
        pointer to vsi structure
    :type vsi: struct i40iw_sc_vsi \*

    :param bufp:
        *undescribed*
    :type bufp: void \*

.. _`i40iw_derive_hw_ird_setting`:

i40iw_derive_hw_ird_setting
===========================

.. c:function:: u8 i40iw_derive_hw_ird_setting(u16 cm_ird)

    Calculate IRD

    :param cm_ird:
        IRD of connection's node
    :type cm_ird: u16

.. _`i40iw_derive_hw_ird_setting.description`:

Description
-----------

The ird from the connection is rounded to a supported HW
setting (2,8,32,64) and then encoded for ird_size field of
qp_ctx

.. _`i40iw_record_ird_ord`:

i40iw_record_ird_ord
====================

.. c:function:: void i40iw_record_ird_ord(struct i40iw_cm_node *cm_node, u32 conn_ird, u32 conn_ord)

    Record IRD/ORD passed in

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param conn_ird:
        connection IRD
    :type conn_ird: u32

    :param conn_ord:
        connection ORD
    :type conn_ord: u32

.. _`i40iw_copy_ip_ntohl`:

i40iw_copy_ip_ntohl
===================

.. c:function:: void i40iw_copy_ip_ntohl(u32 *dst, __be32 *src)

    change network to host ip

    :param dst:
        host ip
    :type dst: u32 \*

    :param src:
        big endian
    :type src: __be32 \*

.. _`i40iw_copy_ip_htonl`:

i40iw_copy_ip_htonl
===================

.. c:function:: void i40iw_copy_ip_htonl(__be32 *dst, u32 *src)

    change host addr to network ip

    :param dst:
        host ip
    :type dst: __be32 \*

    :param src:
        little endian
    :type src: u32 \*

.. _`i40iw_fill_sockaddr4`:

i40iw_fill_sockaddr4
====================

.. c:function:: void i40iw_fill_sockaddr4(struct i40iw_cm_node *cm_node, struct iw_cm_event *event)

    get addr info for passive connection

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param event:
        upper layer's cm event
    :type event: struct iw_cm_event \*

.. _`i40iw_fill_sockaddr6`:

i40iw_fill_sockaddr6
====================

.. c:function:: void i40iw_fill_sockaddr6(struct i40iw_cm_node *cm_node, struct iw_cm_event *event)

    get ipv6 addr info for passive side

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param event:
        upper layer's cm event
    :type event: struct iw_cm_event \*

.. _`i40iw_get_addr_info`:

i40iw_get_addr_info
===================

.. c:function:: void i40iw_get_addr_info(struct i40iw_cm_node *cm_node, struct i40iw_cm_info *cm_info)

    :param cm_node:
        contains ip/tcp info
    :type cm_node: struct i40iw_cm_node \*

    :param cm_info:
        to get a copy of the cm_node ip/tcp info
    :type cm_info: struct i40iw_cm_info \*

.. _`i40iw_get_cmevent_info`:

i40iw_get_cmevent_info
======================

.. c:function:: void i40iw_get_cmevent_info(struct i40iw_cm_node *cm_node, struct iw_cm_id *cm_id, struct iw_cm_event *event)

    for cm event upcall

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param cm_id:
        upper layers cm struct for the event
    :type cm_id: struct iw_cm_id \*

    :param event:
        upper layer's cm event
    :type event: struct iw_cm_event \*

.. _`i40iw_send_cm_event`:

i40iw_send_cm_event
===================

.. c:function:: int i40iw_send_cm_event(struct i40iw_cm_node *cm_node, struct iw_cm_id *cm_id, enum iw_cm_event_type type, int status)

    upcall cm's event handler

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param cm_id:
        upper layer's cm info struct
    :type cm_id: struct iw_cm_id \*

    :param type:
        Event type to indicate
    :type type: enum iw_cm_event_type

    :param status:
        status for the event type
    :type status: int

.. _`i40iw_create_event`:

i40iw_create_event
==================

.. c:function:: struct i40iw_cm_event *i40iw_create_event(struct i40iw_cm_node *cm_node, enum i40iw_cm_event_type type)

    create cm event

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param type:
        Event type to generate
    :type type: enum i40iw_cm_event_type

.. _`i40iw_free_retrans_entry`:

i40iw_free_retrans_entry
========================

.. c:function:: void i40iw_free_retrans_entry(struct i40iw_cm_node *cm_node)

    free send entry

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

.. _`i40iw_cleanup_retrans_entry`:

i40iw_cleanup_retrans_entry
===========================

.. c:function:: void i40iw_cleanup_retrans_entry(struct i40iw_cm_node *cm_node)

    free send entry with lock

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

.. _`i40iw_form_cm_frame`:

i40iw_form_cm_frame
===================

.. c:function:: struct i40iw_puda_buf *i40iw_form_cm_frame(struct i40iw_cm_node *cm_node, struct i40iw_kmem_info *options, struct i40iw_kmem_info *hdr, struct i40iw_kmem_info *pdata, u8 flags)

    get a free packet and build frame

    :param cm_node:
        connection's node ionfo to use in frame
    :type cm_node: struct i40iw_cm_node \*

    :param options:
        pointer to options info
    :type options: struct i40iw_kmem_info \*

    :param hdr:
        pointer mpa header
    :type hdr: struct i40iw_kmem_info \*

    :param pdata:
        pointer to private data
    :type pdata: struct i40iw_kmem_info \*

    :param flags:
        indicates FIN or ACK
    :type flags: u8

.. _`i40iw_send_reset`:

i40iw_send_reset
================

.. c:function:: int i40iw_send_reset(struct i40iw_cm_node *cm_node)

    Send RST packet

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

.. _`i40iw_active_open_err`:

i40iw_active_open_err
=====================

.. c:function:: void i40iw_active_open_err(struct i40iw_cm_node *cm_node, bool reset)

    send event for active side cm error

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param reset:
        Flag to send reset or not
    :type reset: bool

.. _`i40iw_passive_open_err`:

i40iw_passive_open_err
======================

.. c:function:: void i40iw_passive_open_err(struct i40iw_cm_node *cm_node, bool reset)

    handle passive side cm error

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param reset:
        send reset or just free cm_node
    :type reset: bool

.. _`i40iw_event_connect_error`:

i40iw_event_connect_error
=========================

.. c:function:: void i40iw_event_connect_error(struct i40iw_cm_event *event)

    to create connect error event

    :param event:
        cm information for connect event
    :type event: struct i40iw_cm_event \*

.. _`i40iw_process_options`:

i40iw_process_options
=====================

.. c:function:: int i40iw_process_options(struct i40iw_cm_node *cm_node, u8 *optionsloc, u32 optionsize, u32 syn_packet)

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param optionsloc:
        point to start of options
    :type optionsloc: u8 \*

    :param optionsize:
        size of all options
    :type optionsize: u32

    :param syn_packet:
        flag if syn packet
    :type syn_packet: u32

.. _`i40iw_handle_tcp_options`:

i40iw_handle_tcp_options
========================

.. c:function:: int i40iw_handle_tcp_options(struct i40iw_cm_node *cm_node, struct tcphdr *tcph, int optionsize, int passive)

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param tcph:
        pointer tcp header
    :type tcph: struct tcphdr \*

    :param optionsize:
        size of options rcvd
    :type optionsize: int

    :param passive:
        active or passive flag
    :type passive: int

.. _`i40iw_build_mpa_v1`:

i40iw_build_mpa_v1
==================

.. c:function:: void i40iw_build_mpa_v1(struct i40iw_cm_node *cm_node, void *start_addr, u8 mpa_key)

    build a MPA V1 frame

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param start_addr:
        *undescribed*
    :type start_addr: void \*

    :param mpa_key:
        to do read0 or write0
    :type mpa_key: u8

.. _`i40iw_build_mpa_v2`:

i40iw_build_mpa_v2
==================

.. c:function:: void i40iw_build_mpa_v2(struct i40iw_cm_node *cm_node, void *start_addr, u8 mpa_key)

    build a MPA V2 frame

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param start_addr:
        buffer start address
    :type start_addr: void \*

    :param mpa_key:
        to do read0 or write0
    :type mpa_key: u8

.. _`i40iw_cm_build_mpa_frame`:

i40iw_cm_build_mpa_frame
========================

.. c:function:: int i40iw_cm_build_mpa_frame(struct i40iw_cm_node *cm_node, struct i40iw_kmem_info *mpa, u8 mpa_key)

    build mpa frame for mpa version 1 or version 2

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param mpa:
        mpa: data buffer
    :type mpa: struct i40iw_kmem_info \*

    :param mpa_key:
        to do read0 or write0
    :type mpa_key: u8

.. _`i40iw_send_mpa_request`:

i40iw_send_mpa_request
======================

.. c:function:: int i40iw_send_mpa_request(struct i40iw_cm_node *cm_node)

    active node send mpa request to passive node

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

.. _`i40iw_send_mpa_reject`:

i40iw_send_mpa_reject
=====================

.. c:function:: int i40iw_send_mpa_reject(struct i40iw_cm_node *cm_node, const void *pdata, u8 plen)

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param pdata:
        reject data for connection
    :type pdata: const void \*

    :param plen:
        length of reject data
    :type plen: u8

.. _`i40iw_parse_mpa`:

i40iw_parse_mpa
===============

.. c:function:: int i40iw_parse_mpa(struct i40iw_cm_node *cm_node, u8 *buffer, u32 *type, u32 len)

    process an IETF MPA frame

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param buffer:
        Data pointer
    :type buffer: u8 \*

    :param type:
        to return accept or reject
    :type type: u32 \*

    :param len:
        Len of mpa buffer
    :type len: u32

.. _`i40iw_schedule_cm_timer`:

i40iw_schedule_cm_timer
=======================

.. c:function:: int i40iw_schedule_cm_timer(struct i40iw_cm_node *cm_node, struct i40iw_puda_buf *sqbuf, enum i40iw_timer_type type, int send_retrans, int close_when_complete)

    \ ````\ @cm_node: connection's node

    :param cm_node:
        *undescribed*
    :type cm_node: struct i40iw_cm_node \*

    :param sqbuf:
        buffer to send
    :type sqbuf: struct i40iw_puda_buf \*

    :param type:
        if it is send or close
    :type type: enum i40iw_timer_type

    :param send_retrans:
        if rexmits to be done
    :type send_retrans: int

    :param close_when_complete:
        is cm_node to be removed
    :type close_when_complete: int

.. _`i40iw_schedule_cm_timer.description`:

Description
-----------

note - cm_node needs to be protected before calling this. Encase in:
i40iw_rem_ref_cm_node(cm_core, cm_node);
i40iw_schedule_cm_timer(...)
atomic_inc(&cm_node->ref_count);

.. _`i40iw_retrans_expired`:

i40iw_retrans_expired
=====================

.. c:function:: void i40iw_retrans_expired(struct i40iw_cm_node *cm_node)

    Could not rexmit the packet

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

.. _`i40iw_handle_close_entry`:

i40iw_handle_close_entry
========================

.. c:function:: void i40iw_handle_close_entry(struct i40iw_cm_node *cm_node, u32 rem_node)

    for handling retry/timeouts

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param rem_node:
        flag for remove cm_node
    :type rem_node: u32

.. _`i40iw_build_timer_list`:

i40iw_build_timer_list
======================

.. c:function:: void i40iw_build_timer_list(struct list_head *timer_list, struct list_head *hte)

    Add cm_nodes to timer list

    :param timer_list:
        ptr to timer list
    :type timer_list: struct list_head \*

    :param hte:
        ptr to accelerated or non-accelerated list
    :type hte: struct list_head \*

.. _`i40iw_cm_timer_tick`:

i40iw_cm_timer_tick
===================

.. c:function:: void i40iw_cm_timer_tick(struct timer_list *t)

    system's timer expired callback

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`i40iw_send_syn`:

i40iw_send_syn
==============

.. c:function:: int i40iw_send_syn(struct i40iw_cm_node *cm_node, u32 sendack)

    send SYN packet

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param sendack:
        flag to set ACK bit or not
    :type sendack: u32

.. _`i40iw_send_ack`:

i40iw_send_ack
==============

.. c:function:: void i40iw_send_ack(struct i40iw_cm_node *cm_node)

    Send ACK packet

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

.. _`i40iw_send_fin`:

i40iw_send_fin
==============

.. c:function:: int i40iw_send_fin(struct i40iw_cm_node *cm_node)

    Send FIN pkt

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

.. _`i40iw_find_node`:

i40iw_find_node
===============

.. c:function:: struct i40iw_cm_node *i40iw_find_node(struct i40iw_cm_core *cm_core, u16 rem_port, u32 *rem_addr, u16 loc_port, u32 *loc_addr, bool add_refcnt, bool accelerated_list)

    find a cm node that matches the reference cm node

    :param cm_core:
        cm's core
    :type cm_core: struct i40iw_cm_core \*

    :param rem_port:
        remote tcp port num
    :type rem_port: u16

    :param rem_addr:
        remote ip addr
    :type rem_addr: u32 \*

    :param loc_port:
        local tcp port num
    :type loc_port: u16

    :param loc_addr:
        loc ip addr
    :type loc_addr: u32 \*

    :param add_refcnt:
        flag to increment refcount of cm_node
    :type add_refcnt: bool

    :param accelerated_list:
        flag for accelerated vs non-accelerated list to search
    :type accelerated_list: bool

.. _`i40iw_find_listener`:

i40iw_find_listener
===================

.. c:function:: struct i40iw_cm_listener *i40iw_find_listener(struct i40iw_cm_core *cm_core, u32 *dst_addr, u16 dst_port, u16 vlan_id, enum i40iw_cm_listener_state listener_state)

    find a cm node listening on this addr-port pair

    :param cm_core:
        cm's core
    :type cm_core: struct i40iw_cm_core \*

    :param dst_addr:
        listener ip addr
    :type dst_addr: u32 \*

    :param dst_port:
        listener tcp port num
    :type dst_port: u16

    :param vlan_id:
        *undescribed*
    :type vlan_id: u16

    :param listener_state:
        state to match with listen node's
    :type listener_state: enum i40iw_cm_listener_state

.. _`i40iw_add_hte_node`:

i40iw_add_hte_node
==================

.. c:function:: void i40iw_add_hte_node(struct i40iw_cm_core *cm_core, struct i40iw_cm_node *cm_node)

    add a cm node to the hash table

    :param cm_core:
        cm's core
    :type cm_core: struct i40iw_cm_core \*

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

.. _`i40iw_find_port`:

i40iw_find_port
===============

.. c:function:: bool i40iw_find_port(struct list_head *hte, u16 port)

    find port that matches reference port

    :param hte:
        ptr to accelerated or non-accelerated list
    :type hte: struct list_head \*

    :param port:
        *undescribed*
    :type port: u16

.. _`i40iw_port_in_use`:

i40iw_port_in_use
=================

.. c:function:: bool i40iw_port_in_use(struct i40iw_cm_core *cm_core, u16 port)

    determine if port is in use

    :param cm_core:
        cm's core
    :type cm_core: struct i40iw_cm_core \*

    :param port:
        port number
    :type port: u16

.. _`i40iw_del_multiple_qhash`:

i40iw_del_multiple_qhash
========================

.. c:function:: enum i40iw_status_code i40iw_del_multiple_qhash(struct i40iw_device *iwdev, struct i40iw_cm_info *cm_info, struct i40iw_cm_listener *cm_parent_listen_node)

    Remove qhash and child listens

    :param iwdev:
        iWarp device
    :type iwdev: struct i40iw_device \*

    :param cm_info:
        CM info for parent listen node
    :type cm_info: struct i40iw_cm_info \*

    :param cm_parent_listen_node:
        The parent listen node
    :type cm_parent_listen_node: struct i40iw_cm_listener \*

.. _`i40iw_netdev_vlan_ipv6`:

i40iw_netdev_vlan_ipv6
======================

.. c:function:: struct net_device *i40iw_netdev_vlan_ipv6(u32 *addr, u16 *vlan_id)

    Gets the netdev and vlan

    :param addr:
        local IPv6 address
    :type addr: u32 \*

    :param vlan_id:
        vlan id for the given IPv6 address
    :type vlan_id: u16 \*

.. _`i40iw_netdev_vlan_ipv6.description`:

Description
-----------

Returns the net_device of the IPv6 address and also sets the
vlan id for that address.

.. _`i40iw_get_vlan_ipv4`:

i40iw_get_vlan_ipv4
===================

.. c:function:: u16 i40iw_get_vlan_ipv4(u32 *addr)

    Returns the vlan_id for IPv4 address

    :param addr:
        local IPv4 address
    :type addr: u32 \*

.. _`i40iw_add_mqh_6`:

i40iw_add_mqh_6
===============

.. c:function:: enum i40iw_status_code i40iw_add_mqh_6(struct i40iw_device *iwdev, struct i40iw_cm_info *cm_info, struct i40iw_cm_listener *cm_parent_listen_node)

    Adds multiple qhashes for IPv6

    :param iwdev:
        iWarp device
    :type iwdev: struct i40iw_device \*

    :param cm_info:
        CM info for parent listen node
    :type cm_info: struct i40iw_cm_info \*

    :param cm_parent_listen_node:
        The parent listen node
    :type cm_parent_listen_node: struct i40iw_cm_listener \*

.. _`i40iw_add_mqh_6.description`:

Description
-----------

Adds a qhash and a child listen node for every IPv6 address
on the adapter and adds the associated qhash filter

.. _`i40iw_add_mqh_4`:

i40iw_add_mqh_4
===============

.. c:function:: enum i40iw_status_code i40iw_add_mqh_4(struct i40iw_device *iwdev, struct i40iw_cm_info *cm_info, struct i40iw_cm_listener *cm_parent_listen_node)

    Adds multiple qhashes for IPv4

    :param iwdev:
        iWarp device
    :type iwdev: struct i40iw_device \*

    :param cm_info:
        CM info for parent listen node
    :type cm_info: struct i40iw_cm_info \*

    :param cm_parent_listen_node:
        The parent listen node
    :type cm_parent_listen_node: struct i40iw_cm_listener \*

.. _`i40iw_add_mqh_4.description`:

Description
-----------

Adds a qhash and a child listen node for every IPv4 address
on the adapter and adds the associated qhash filter

.. _`i40iw_dec_refcnt_listen`:

i40iw_dec_refcnt_listen
=======================

.. c:function:: int i40iw_dec_refcnt_listen(struct i40iw_cm_core *cm_core, struct i40iw_cm_listener *listener, int free_hanging_nodes, bool apbvt_del)

    delete listener and associated cm nodes

    :param cm_core:
        cm's core
    :type cm_core: struct i40iw_cm_core \*

    :param listener:
        *undescribed*
    :type listener: struct i40iw_cm_listener \*

    :param free_hanging_nodes:
        to free associated cm_nodes
    :type free_hanging_nodes: int

    :param apbvt_del:
        flag to delete the apbvt
    :type apbvt_del: bool

.. _`i40iw_cm_del_listen`:

i40iw_cm_del_listen
===================

.. c:function:: int i40iw_cm_del_listen(struct i40iw_cm_core *cm_core, struct i40iw_cm_listener *listener, bool apbvt_del)

    delete a linstener

    :param cm_core:
        cm's core
    :type cm_core: struct i40iw_cm_core \*

    :param listener:
        passive connection's listener
    :type listener: struct i40iw_cm_listener \*

    :param apbvt_del:
        flag to delete apbvt
    :type apbvt_del: bool

.. _`i40iw_addr_resolve_neigh`:

i40iw_addr_resolve_neigh
========================

.. c:function:: int i40iw_addr_resolve_neigh(struct i40iw_device *iwdev, u32 src_ip, u32 dst_ip, int arpindex)

    resolve neighbor address

    :param iwdev:
        iwarp device structure
    :type iwdev: struct i40iw_device \*

    :param src_ip:
        local ip address
    :type src_ip: u32

    :param dst_ip:
        remote ip address
    :type dst_ip: u32

    :param arpindex:
        if there is an arp entry
    :type arpindex: int

.. _`i40iw_get_dst_ipv6`:

i40iw_get_dst_ipv6
==================

.. c:function:: struct dst_entry *i40iw_get_dst_ipv6(struct sockaddr_in6 *src_addr, struct sockaddr_in6 *dst_addr)

    :param src_addr:
        *undescribed*
    :type src_addr: struct sockaddr_in6 \*

    :param dst_addr:
        *undescribed*
    :type dst_addr: struct sockaddr_in6 \*

.. _`i40iw_addr_resolve_neigh_ipv6`:

i40iw_addr_resolve_neigh_ipv6
=============================

.. c:function:: int i40iw_addr_resolve_neigh_ipv6(struct i40iw_device *iwdev, u32 *src, u32 *dest, int arpindex)

    resolve neighbor ipv6 address

    :param iwdev:
        iwarp device structure
    :type iwdev: struct i40iw_device \*

    :param src:
        *undescribed*
    :type src: u32 \*

    :param dest:
        *undescribed*
    :type dest: u32 \*

    :param arpindex:
        if there is an arp entry
    :type arpindex: int

.. _`i40iw_ipv4_is_loopback`:

i40iw_ipv4_is_loopback
======================

.. c:function:: bool i40iw_ipv4_is_loopback(u32 loc_addr, u32 rem_addr)

    check if loopback

    :param loc_addr:
        local addr to compare
    :type loc_addr: u32

    :param rem_addr:
        remote address
    :type rem_addr: u32

.. _`i40iw_ipv6_is_loopback`:

i40iw_ipv6_is_loopback
======================

.. c:function:: bool i40iw_ipv6_is_loopback(u32 *loc_addr, u32 *rem_addr)

    check if loopback

    :param loc_addr:
        local addr to compare
    :type loc_addr: u32 \*

    :param rem_addr:
        remote address
    :type rem_addr: u32 \*

.. _`i40iw_make_cm_node`:

i40iw_make_cm_node
==================

.. c:function:: struct i40iw_cm_node *i40iw_make_cm_node(struct i40iw_cm_core *cm_core, struct i40iw_device *iwdev, struct i40iw_cm_info *cm_info, struct i40iw_cm_listener *listener)

    create a new instance of a cm node

    :param cm_core:
        cm's core
    :type cm_core: struct i40iw_cm_core \*

    :param iwdev:
        iwarp device structure
    :type iwdev: struct i40iw_device \*

    :param cm_info:
        quad info for connection
    :type cm_info: struct i40iw_cm_info \*

    :param listener:
        passive connection's listener
    :type listener: struct i40iw_cm_listener \*

.. _`i40iw_rem_ref_cm_node`:

i40iw_rem_ref_cm_node
=====================

.. c:function:: void i40iw_rem_ref_cm_node(struct i40iw_cm_node *cm_node)

    destroy an instance of a cm node

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

.. _`i40iw_handle_fin_pkt`:

i40iw_handle_fin_pkt
====================

.. c:function:: void i40iw_handle_fin_pkt(struct i40iw_cm_node *cm_node)

    FIN packet received

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

.. _`i40iw_handle_rst_pkt`:

i40iw_handle_rst_pkt
====================

.. c:function:: void i40iw_handle_rst_pkt(struct i40iw_cm_node *cm_node, struct i40iw_puda_buf *rbuf)

    process received RST packet

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param rbuf:
        receive buffer
    :type rbuf: struct i40iw_puda_buf \*

.. _`i40iw_handle_rcv_mpa`:

i40iw_handle_rcv_mpa
====================

.. c:function:: void i40iw_handle_rcv_mpa(struct i40iw_cm_node *cm_node, struct i40iw_puda_buf *rbuf)

    Process a recv'd mpa buffer

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param rbuf:
        receive buffer
    :type rbuf: struct i40iw_puda_buf \*

.. _`i40iw_indicate_pkt_err`:

i40iw_indicate_pkt_err
======================

.. c:function:: void i40iw_indicate_pkt_err(struct i40iw_cm_node *cm_node)

    Send up err event to cm

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

.. _`i40iw_check_syn`:

i40iw_check_syn
===============

.. c:function:: int i40iw_check_syn(struct i40iw_cm_node *cm_node, struct tcphdr *tcph)

    Check for error on received syn ack

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param tcph:
        pointer tcp header
    :type tcph: struct tcphdr \*

.. _`i40iw_check_seq`:

i40iw_check_seq
===============

.. c:function:: int i40iw_check_seq(struct i40iw_cm_node *cm_node, struct tcphdr *tcph)

    check seq numbers if OK

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param tcph:
        pointer tcp header
    :type tcph: struct tcphdr \*

.. _`i40iw_handle_syn_pkt`:

i40iw_handle_syn_pkt
====================

.. c:function:: void i40iw_handle_syn_pkt(struct i40iw_cm_node *cm_node, struct i40iw_puda_buf *rbuf)

    is for Passive node

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param rbuf:
        receive buffer
    :type rbuf: struct i40iw_puda_buf \*

.. _`i40iw_handle_synack_pkt`:

i40iw_handle_synack_pkt
=======================

.. c:function:: void i40iw_handle_synack_pkt(struct i40iw_cm_node *cm_node, struct i40iw_puda_buf *rbuf)

    Process SYN+ACK packet (active side)

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param rbuf:
        receive buffer
    :type rbuf: struct i40iw_puda_buf \*

.. _`i40iw_handle_ack_pkt`:

i40iw_handle_ack_pkt
====================

.. c:function:: int i40iw_handle_ack_pkt(struct i40iw_cm_node *cm_node, struct i40iw_puda_buf *rbuf)

    process packet with ACK

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param rbuf:
        receive buffer
    :type rbuf: struct i40iw_puda_buf \*

.. _`i40iw_process_packet`:

i40iw_process_packet
====================

.. c:function:: void i40iw_process_packet(struct i40iw_cm_node *cm_node, struct i40iw_puda_buf *rbuf)

    process cm packet

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param rbuf:
        receive buffer
    :type rbuf: struct i40iw_puda_buf \*

.. _`i40iw_make_listen_node`:

i40iw_make_listen_node
======================

.. c:function:: struct i40iw_cm_listener *i40iw_make_listen_node(struct i40iw_cm_core *cm_core, struct i40iw_device *iwdev, struct i40iw_cm_info *cm_info)

    create a listen node with params

    :param cm_core:
        cm's core
    :type cm_core: struct i40iw_cm_core \*

    :param iwdev:
        iwarp device structure
    :type iwdev: struct i40iw_device \*

    :param cm_info:
        quad info for connection
    :type cm_info: struct i40iw_cm_info \*

.. _`i40iw_create_cm_node`:

i40iw_create_cm_node
====================

.. c:function:: struct i40iw_cm_node *i40iw_create_cm_node(struct i40iw_cm_core *cm_core, struct i40iw_device *iwdev, struct iw_cm_conn_param *conn_param, struct i40iw_cm_info *cm_info)

    make a connection node with params

    :param cm_core:
        cm's core
    :type cm_core: struct i40iw_cm_core \*

    :param iwdev:
        iwarp device structure
    :type iwdev: struct i40iw_device \*

    :param conn_param:
        upper layer connection parameters
    :type conn_param: struct iw_cm_conn_param \*

    :param cm_info:
        quad info for connection
    :type cm_info: struct i40iw_cm_info \*

.. _`i40iw_cm_reject`:

i40iw_cm_reject
===============

.. c:function:: int i40iw_cm_reject(struct i40iw_cm_node *cm_node, const void *pdata, u8 plen)

    reject and teardown a connection

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param pdata:
        *undescribed*
    :type pdata: const void \*

    :param plen:
        size of private data
    :type plen: u8

.. _`i40iw_cm_close`:

i40iw_cm_close
==============

.. c:function:: int i40iw_cm_close(struct i40iw_cm_node *cm_node)

    close of cm connection

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

.. _`i40iw_receive_ilq`:

i40iw_receive_ilq
=================

.. c:function:: void i40iw_receive_ilq(struct i40iw_sc_vsi *vsi, struct i40iw_puda_buf *rbuf)

    recv an ETHERNET packet, and process it through CM

    :param vsi:
        pointer to the vsi structure
    :type vsi: struct i40iw_sc_vsi \*

    :param rbuf:
        receive buffer
    :type rbuf: struct i40iw_puda_buf \*

.. _`i40iw_setup_cm_core`:

i40iw_setup_cm_core
===================

.. c:function:: void i40iw_setup_cm_core(struct i40iw_device *iwdev)

    allocate a top level instance of a cm core

    :param iwdev:
        iwarp device structure
    :type iwdev: struct i40iw_device \*

.. _`i40iw_cleanup_cm_core`:

i40iw_cleanup_cm_core
=====================

.. c:function:: void i40iw_cleanup_cm_core(struct i40iw_cm_core *cm_core)

    deallocate a top level instance of a cm core

    :param cm_core:
        cm's core
    :type cm_core: struct i40iw_cm_core \*

.. _`i40iw_init_tcp_ctx`:

i40iw_init_tcp_ctx
==================

.. c:function:: void i40iw_init_tcp_ctx(struct i40iw_cm_node *cm_node, struct i40iw_tcp_offload_info *tcp_info, struct i40iw_qp *iwqp)

    setup qp context

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

    :param tcp_info:
        offload info for tcp
    :type tcp_info: struct i40iw_tcp_offload_info \*

    :param iwqp:
        associate qp for the connection
    :type iwqp: struct i40iw_qp \*

.. _`i40iw_cm_init_tsa_conn`:

i40iw_cm_init_tsa_conn
======================

.. c:function:: void i40iw_cm_init_tsa_conn(struct i40iw_qp *iwqp, struct i40iw_cm_node *cm_node)

    setup qp for RTS

    :param iwqp:
        associate qp for the connection
    :type iwqp: struct i40iw_qp \*

    :param cm_node:
        connection's node
    :type cm_node: struct i40iw_cm_node \*

.. _`i40iw_cm_disconn`:

i40iw_cm_disconn
================

.. c:function:: void i40iw_cm_disconn(struct i40iw_qp *iwqp)

    when a connection is being closed

    :param iwqp:
        associate qp for the connection
    :type iwqp: struct i40iw_qp \*

.. _`i40iw_qp_disconnect`:

i40iw_qp_disconnect
===================

.. c:function:: void i40iw_qp_disconnect(struct i40iw_qp *iwqp)

    free qp and close cm

    :param iwqp:
        associate qp for the connection
    :type iwqp: struct i40iw_qp \*

.. _`i40iw_cm_disconn_true`:

i40iw_cm_disconn_true
=====================

.. c:function:: void i40iw_cm_disconn_true(struct i40iw_qp *iwqp)

    called by worker thread to disconnect qp

    :param iwqp:
        associate qp for the connection
    :type iwqp: struct i40iw_qp \*

.. _`i40iw_disconnect_worker`:

i40iw_disconnect_worker
=======================

.. c:function:: void i40iw_disconnect_worker(struct work_struct *work)

    worker for connection close

    :param work:
        points or disconn structure
    :type work: struct work_struct \*

.. _`i40iw_accept`:

i40iw_accept
============

.. c:function:: int i40iw_accept(struct iw_cm_id *cm_id, struct iw_cm_conn_param *conn_param)

    registered call for connection to be accepted

    :param cm_id:
        cm information for passive connection
    :type cm_id: struct iw_cm_id \*

    :param conn_param:
        accpet parameters
    :type conn_param: struct iw_cm_conn_param \*

.. _`i40iw_reject`:

i40iw_reject
============

.. c:function:: int i40iw_reject(struct iw_cm_id *cm_id, const void *pdata, u8 pdata_len)

    registered call for connection to be rejected

    :param cm_id:
        cm information for passive connection
    :type cm_id: struct iw_cm_id \*

    :param pdata:
        private data to be sent
    :type pdata: const void \*

    :param pdata_len:
        private data length
    :type pdata_len: u8

.. _`i40iw_connect`:

i40iw_connect
=============

.. c:function:: int i40iw_connect(struct iw_cm_id *cm_id, struct iw_cm_conn_param *conn_param)

    registered call for connection to be established

    :param cm_id:
        cm information for passive connection
    :type cm_id: struct iw_cm_id \*

    :param conn_param:
        Information about the connection
    :type conn_param: struct iw_cm_conn_param \*

.. _`i40iw_create_listen`:

i40iw_create_listen
===================

.. c:function:: int i40iw_create_listen(struct iw_cm_id *cm_id, int backlog)

    registered call creating listener

    :param cm_id:
        cm information for passive connection
    :type cm_id: struct iw_cm_id \*

    :param backlog:
        to max accept pending count
    :type backlog: int

.. _`i40iw_destroy_listen`:

i40iw_destroy_listen
====================

.. c:function:: int i40iw_destroy_listen(struct iw_cm_id *cm_id)

    registered call to destroy listener

    :param cm_id:
        cm information for passive connection
    :type cm_id: struct iw_cm_id \*

.. _`i40iw_cm_event_connected`:

i40iw_cm_event_connected
========================

.. c:function:: void i40iw_cm_event_connected(struct i40iw_cm_event *event)

    handle connected active node

    :param event:
        the info for cm_node of connection
    :type event: struct i40iw_cm_event \*

.. _`i40iw_cm_event_reset`:

i40iw_cm_event_reset
====================

.. c:function:: void i40iw_cm_event_reset(struct i40iw_cm_event *event)

    handle reset

    :param event:
        the info for cm_node of connection
    :type event: struct i40iw_cm_event \*

.. _`i40iw_cm_event_handler`:

i40iw_cm_event_handler
======================

.. c:function:: void i40iw_cm_event_handler(struct work_struct *work)

    worker thread callback to send event to cm upper layer

    :param work:
        pointer of cm event info.
    :type work: struct work_struct \*

.. _`i40iw_cm_post_event`:

i40iw_cm_post_event
===================

.. c:function:: void i40iw_cm_post_event(struct i40iw_cm_event *event)

    queue event request for worker thread

    :param event:
        cm node's info for up event call
    :type event: struct i40iw_cm_event \*

.. _`i40iw_qhash_ctrl`:

i40iw_qhash_ctrl
================

.. c:function:: void i40iw_qhash_ctrl(struct i40iw_device *iwdev, struct i40iw_cm_listener *parent_listen_node, struct i40iw_cm_info *nfo, u32 *ipaddr, bool ipv4, bool ifup)

    enable/disable qhash for list

    :param iwdev:
        device pointer
    :type iwdev: struct i40iw_device \*

    :param parent_listen_node:
        parent listen node
    :type parent_listen_node: struct i40iw_cm_listener \*

    :param nfo:
        cm info node
    :type nfo: struct i40iw_cm_info \*

    :param ipaddr:
        Pointer to IPv4 or IPv6 address
    :type ipaddr: u32 \*

    :param ipv4:
        flag indicating IPv4 when true
    :type ipv4: bool

    :param ifup:
        flag indicating interface up when true
    :type ifup: bool

.. _`i40iw_qhash_ctrl.description`:

Description
-----------

Enables or disables the qhash for the node in the child
listen list that matches ipaddr. If no matching IP was found
it will allocate and add a new child listen node to the
parent listen node. The listen_list_lock is assumed to be
held when called.

.. _`i40iw_cm_teardown_connections`:

i40iw_cm_teardown_connections
=============================

.. c:function:: void i40iw_cm_teardown_connections(struct i40iw_device *iwdev, u32 *ipaddr, struct i40iw_cm_info *nfo, bool disconnect_all)

    teardown QPs

    :param iwdev:
        device pointer
    :type iwdev: struct i40iw_device \*

    :param ipaddr:
        Pointer to IPv4 or IPv6 address
    :type ipaddr: u32 \*

    :param nfo:
        *undescribed*
    :type nfo: struct i40iw_cm_info \*

    :param disconnect_all:
        flag indicating disconnect all QPs
        teardown QPs where source or destination addr matches ip addr
    :type disconnect_all: bool

.. _`i40iw_if_notify`:

i40iw_if_notify
===============

.. c:function:: void i40iw_if_notify(struct i40iw_device *iwdev, struct net_device *netdev, u32 *ipaddr, bool ipv4, bool ifup)

    process an ifdown on an interface

    :param iwdev:
        device pointer
    :type iwdev: struct i40iw_device \*

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param ipaddr:
        Pointer to IPv4 or IPv6 address
    :type ipaddr: u32 \*

    :param ipv4:
        flag indicating IPv4 when true
    :type ipv4: bool

    :param ifup:
        flag indicating interface up when true
    :type ifup: bool

.. This file was automatic generated / don't edit.

