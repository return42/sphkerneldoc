.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_cm.c

.. _`i40iw_free_sqbuf`:

i40iw_free_sqbuf
================

.. c:function:: void i40iw_free_sqbuf(struct i40iw_sc_dev *dev, void *bufp)

    put back puda buffer if refcount = 0

    :param struct i40iw_sc_dev \*dev:
        FPK device

    :param void \*bufp:
        *undescribed*

.. _`i40iw_derive_hw_ird_setting`:

i40iw_derive_hw_ird_setting
===========================

.. c:function:: u8 i40iw_derive_hw_ird_setting(u16 cm_ird)

    Calculate IRD

    :param u16 cm_ird:
        IRD of connection's node

.. _`i40iw_derive_hw_ird_setting.description`:

Description
-----------

The ird from the connection is rounded to a supported HW
setting (2,8,32,64) and then encoded for ird_size field of
qp_ctx

.. _`i40iw_record_ird_ord`:

i40iw_record_ird_ord
====================

.. c:function:: void i40iw_record_ird_ord(struct i40iw_cm_node *cm_node, u16 conn_ird, u16 conn_ord)

    Record IRD/ORD passed in

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param u16 conn_ird:
        connection IRD

    :param u16 conn_ord:
        connection ORD

.. _`i40iw_copy_ip_ntohl`:

i40iw_copy_ip_ntohl
===================

.. c:function:: void i40iw_copy_ip_ntohl(u32 *dst, __be32 *src)

    change network to host ip

    :param u32 \*dst:
        host ip

    :param __be32 \*src:
        big endian

.. _`i40iw_copy_ip_htonl`:

i40iw_copy_ip_htonl
===================

.. c:function:: void i40iw_copy_ip_htonl(__be32 *dst, u32 *src)

    change host addr to network ip

    :param __be32 \*dst:
        host ip

    :param u32 \*src:
        little endian

.. _`i40iw_fill_sockaddr4`:

i40iw_fill_sockaddr4
====================

.. c:function:: void i40iw_fill_sockaddr4(struct i40iw_cm_node *cm_node, struct iw_cm_event *event)

    get addr info for passive connection

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param struct iw_cm_event \*event:
        upper layer's cm event

.. _`i40iw_fill_sockaddr6`:

i40iw_fill_sockaddr6
====================

.. c:function:: void i40iw_fill_sockaddr6(struct i40iw_cm_node *cm_node, struct iw_cm_event *event)

    get ipv6 addr info for passive side

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param struct iw_cm_event \*event:
        upper layer's cm event

.. _`i40iw_get_addr_info`:

i40iw_get_addr_info
===================

.. c:function:: void i40iw_get_addr_info(struct i40iw_cm_node *cm_node, struct i40iw_cm_info *cm_info)

    :param struct i40iw_cm_node \*cm_node:
        contains ip/tcp info

    :param struct i40iw_cm_info \*cm_info:
        to get a copy of the cm_node ip/tcp info

.. _`i40iw_get_cmevent_info`:

i40iw_get_cmevent_info
======================

.. c:function:: void i40iw_get_cmevent_info(struct i40iw_cm_node *cm_node, struct iw_cm_id *cm_id, struct iw_cm_event *event)

    for cm event upcall

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param struct iw_cm_id \*cm_id:
        upper layers cm struct for the event

    :param struct iw_cm_event \*event:
        upper layer's cm event

.. _`i40iw_send_cm_event`:

i40iw_send_cm_event
===================

.. c:function:: int i40iw_send_cm_event(struct i40iw_cm_node *cm_node, struct iw_cm_id *cm_id, enum iw_cm_event_type type, int status)

    upcall cm's event handler

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param struct iw_cm_id \*cm_id:
        upper layer's cm info struct

    :param enum iw_cm_event_type type:
        Event type to indicate

    :param int status:
        status for the event type

.. _`i40iw_create_event`:

i40iw_create_event
==================

.. c:function:: struct i40iw_cm_event *i40iw_create_event(struct i40iw_cm_node *cm_node, enum i40iw_cm_event_type type)

    create cm event

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param enum i40iw_cm_event_type type:
        Event type to generate

.. _`i40iw_free_retrans_entry`:

i40iw_free_retrans_entry
========================

.. c:function:: void i40iw_free_retrans_entry(struct i40iw_cm_node *cm_node)

    free send entry

    :param struct i40iw_cm_node \*cm_node:
        connection's node

.. _`i40iw_cleanup_retrans_entry`:

i40iw_cleanup_retrans_entry
===========================

.. c:function:: void i40iw_cleanup_retrans_entry(struct i40iw_cm_node *cm_node)

    free send entry with lock

    :param struct i40iw_cm_node \*cm_node:
        connection's node

.. _`i40iw_form_cm_frame`:

i40iw_form_cm_frame
===================

.. c:function:: struct i40iw_puda_buf *i40iw_form_cm_frame(struct i40iw_cm_node *cm_node, struct i40iw_kmem_info *options, struct i40iw_kmem_info *hdr, struct i40iw_kmem_info *pdata, u8 flags)

    get a free packet and build frame

    :param struct i40iw_cm_node \*cm_node:
        connection's node ionfo to use in frame

    :param struct i40iw_kmem_info \*options:
        pointer to options info

    :param struct i40iw_kmem_info \*hdr:
        pointer mpa header

    :param struct i40iw_kmem_info \*pdata:
        pointer to private data

    :param u8 flags:
        indicates FIN or ACK

.. _`i40iw_send_reset`:

i40iw_send_reset
================

.. c:function:: int i40iw_send_reset(struct i40iw_cm_node *cm_node)

    Send RST packet

    :param struct i40iw_cm_node \*cm_node:
        connection's node

.. _`i40iw_active_open_err`:

i40iw_active_open_err
=====================

.. c:function:: void i40iw_active_open_err(struct i40iw_cm_node *cm_node, bool reset)

    send event for active side cm error

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param bool reset:
        Flag to send reset or not

.. _`i40iw_passive_open_err`:

i40iw_passive_open_err
======================

.. c:function:: void i40iw_passive_open_err(struct i40iw_cm_node *cm_node, bool reset)

    handle passive side cm error

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param bool reset:
        send reset or just free cm_node

.. _`i40iw_event_connect_error`:

i40iw_event_connect_error
=========================

.. c:function:: void i40iw_event_connect_error(struct i40iw_cm_event *event)

    to create connect error event

    :param struct i40iw_cm_event \*event:
        cm information for connect event

.. _`i40iw_process_options`:

i40iw_process_options
=====================

.. c:function:: int i40iw_process_options(struct i40iw_cm_node *cm_node, u8 *optionsloc, u32 optionsize, u32 syn_packet)

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param u8 \*optionsloc:
        point to start of options

    :param u32 optionsize:
        size of all options

    :param u32 syn_packet:
        flag if syn packet

.. _`i40iw_handle_tcp_options`:

i40iw_handle_tcp_options
========================

.. c:function:: int i40iw_handle_tcp_options(struct i40iw_cm_node *cm_node, struct tcphdr *tcph, int optionsize, int passive)

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param struct tcphdr \*tcph:
        pointer tcp header

    :param int optionsize:
        size of options rcvd

    :param int passive:
        active or passive flag

.. _`i40iw_build_mpa_v1`:

i40iw_build_mpa_v1
==================

.. c:function:: void i40iw_build_mpa_v1(struct i40iw_cm_node *cm_node, void *start_addr, u8 mpa_key)

    build a MPA V1 frame

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param void \*start_addr:
        *undescribed*

    :param u8 mpa_key:
        to do read0 or write0

.. _`i40iw_build_mpa_v2`:

i40iw_build_mpa_v2
==================

.. c:function:: void i40iw_build_mpa_v2(struct i40iw_cm_node *cm_node, void *start_addr, u8 mpa_key)

    build a MPA V2 frame

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param void \*start_addr:
        buffer start address

    :param u8 mpa_key:
        to do read0 or write0

.. _`i40iw_cm_build_mpa_frame`:

i40iw_cm_build_mpa_frame
========================

.. c:function:: int i40iw_cm_build_mpa_frame(struct i40iw_cm_node *cm_node, struct i40iw_kmem_info *mpa, u8 mpa_key)

    build mpa frame for mpa version 1 or version 2

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param struct i40iw_kmem_info \*mpa:
        mpa: data buffer

    :param u8 mpa_key:
        to do read0 or write0

.. _`i40iw_send_mpa_request`:

i40iw_send_mpa_request
======================

.. c:function:: int i40iw_send_mpa_request(struct i40iw_cm_node *cm_node)

    active node send mpa request to passive node

    :param struct i40iw_cm_node \*cm_node:
        connection's node

.. _`i40iw_send_mpa_reject`:

i40iw_send_mpa_reject
=====================

.. c:function:: int i40iw_send_mpa_reject(struct i40iw_cm_node *cm_node, const void *pdata, u8 plen)

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param const void \*pdata:
        reject data for connection

    :param u8 plen:
        length of reject data

.. _`i40iw_parse_mpa`:

i40iw_parse_mpa
===============

.. c:function:: int i40iw_parse_mpa(struct i40iw_cm_node *cm_node, u8 *buffer, u32 *type, u32 len)

    process an IETF MPA frame

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param u8 \*buffer:
        Data pointer

    :param u32 \*type:
        to return accept or reject

    :param u32 len:
        Len of mpa buffer

.. _`i40iw_schedule_cm_timer`:

i40iw_schedule_cm_timer
=======================

.. c:function:: int i40iw_schedule_cm_timer(struct i40iw_cm_node *cm_node, struct i40iw_puda_buf *sqbuf, enum i40iw_timer_type type, int send_retrans, int close_when_complete)

    @@cm_node: connection's node

    :param struct i40iw_cm_node \*cm_node:
        *undescribed*

    :param struct i40iw_puda_buf \*sqbuf:
        buffer to send

    :param enum i40iw_timer_type type:
        if it es send ot close

    :param int send_retrans:
        if rexmits to be done

    :param int close_when_complete:
        is cm_node to be removed

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

    :param struct i40iw_cm_node \*cm_node:
        connection's node

.. _`i40iw_handle_close_entry`:

i40iw_handle_close_entry
========================

.. c:function:: void i40iw_handle_close_entry(struct i40iw_cm_node *cm_node, u32 rem_node)

    for handling retry/timeouts

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param u32 rem_node:
        flag for remove cm_node

.. _`i40iw_cm_timer_tick`:

i40iw_cm_timer_tick
===================

.. c:function:: void i40iw_cm_timer_tick(unsigned long pass)

    system's timer expired callback

    :param unsigned long pass:
        Pointing to cm_core

.. _`i40iw_send_syn`:

i40iw_send_syn
==============

.. c:function:: int i40iw_send_syn(struct i40iw_cm_node *cm_node, u32 sendack)

    send SYN packet

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param u32 sendack:
        flag to set ACK bit or not

.. _`i40iw_send_ack`:

i40iw_send_ack
==============

.. c:function:: void i40iw_send_ack(struct i40iw_cm_node *cm_node)

    Send ACK packet

    :param struct i40iw_cm_node \*cm_node:
        connection's node

.. _`i40iw_send_fin`:

i40iw_send_fin
==============

.. c:function:: int i40iw_send_fin(struct i40iw_cm_node *cm_node)

    Send FIN pkt

    :param struct i40iw_cm_node \*cm_node:
        connection's node

.. _`i40iw_find_node`:

i40iw_find_node
===============

.. c:function:: struct i40iw_cm_node *i40iw_find_node(struct i40iw_cm_core *cm_core, u16 rem_port, u32 *rem_addr, u16 loc_port, u32 *loc_addr, bool add_refcnt)

    find a cm node that matches the reference cm node

    :param struct i40iw_cm_core \*cm_core:
        cm's core

    :param u16 rem_port:
        remote tcp port num

    :param u32 \*rem_addr:
        remote ip addr

    :param u16 loc_port:
        local tcp port num

    :param u32 \*loc_addr:
        loc ip addr

    :param bool add_refcnt:
        flag to increment refcount of cm_node

.. _`i40iw_find_listener`:

i40iw_find_listener
===================

.. c:function:: struct i40iw_cm_listener *i40iw_find_listener(struct i40iw_cm_core *cm_core, u32 *dst_addr, u16 dst_port, u16 vlan_id, enum i40iw_cm_listener_state listener_state)

    find a cm node listening on this addr-port pair

    :param struct i40iw_cm_core \*cm_core:
        cm's core

    :param u32 \*dst_addr:
        listener ip addr

    :param u16 dst_port:
        listener tcp port num

    :param u16 vlan_id:
        *undescribed*

    :param enum i40iw_cm_listener_state listener_state:
        state to match with listen node's

.. _`i40iw_add_hte_node`:

i40iw_add_hte_node
==================

.. c:function:: void i40iw_add_hte_node(struct i40iw_cm_core *cm_core, struct i40iw_cm_node *cm_node)

    add a cm node to the hash table

    :param struct i40iw_cm_core \*cm_core:
        cm's core

    :param struct i40iw_cm_node \*cm_node:
        connection's node

.. _`i40iw_listen_port_in_use`:

i40iw_listen_port_in_use
========================

.. c:function:: bool i40iw_listen_port_in_use(struct i40iw_cm_core *cm_core, u16 port)

    determine if port is in use

    :param struct i40iw_cm_core \*cm_core:
        *undescribed*

    :param u16 port:
        Listen port number

.. _`i40iw_del_multiple_qhash`:

i40iw_del_multiple_qhash
========================

.. c:function:: enum i40iw_status_code i40iw_del_multiple_qhash(struct i40iw_device *iwdev, struct i40iw_cm_info *cm_info, struct i40iw_cm_listener *cm_parent_listen_node)

    Remove qhash and child listens

    :param struct i40iw_device \*iwdev:
        iWarp device

    :param struct i40iw_cm_info \*cm_info:
        CM info for parent listen node

    :param struct i40iw_cm_listener \*cm_parent_listen_node:
        The parent listen node

.. _`i40iw_netdev_vlan_ipv6`:

i40iw_netdev_vlan_ipv6
======================

.. c:function:: struct net_device *i40iw_netdev_vlan_ipv6(u32 *addr, u16 *vlan_id, u8 *mac)

    Gets the netdev and mac

    :param u32 \*addr:
        local IPv6 address

    :param u16 \*vlan_id:
        vlan id for the given IPv6 address

    :param u8 \*mac:
        mac address for the given IPv6 address

.. _`i40iw_netdev_vlan_ipv6.description`:

Description
-----------

Returns the net_device of the IPv6 address and also sets the
vlan id and mac for that address.

.. _`i40iw_get_vlan_ipv4`:

i40iw_get_vlan_ipv4
===================

.. c:function:: u16 i40iw_get_vlan_ipv4(u32 *addr)

    Returns the vlan_id for IPv4 address

    :param u32 \*addr:
        local IPv4 address

.. _`i40iw_add_mqh_6`:

i40iw_add_mqh_6
===============

.. c:function:: enum i40iw_status_code i40iw_add_mqh_6(struct i40iw_device *iwdev, struct i40iw_cm_info *cm_info, struct i40iw_cm_listener *cm_parent_listen_node)

    Adds multiple qhashes for IPv6

    :param struct i40iw_device \*iwdev:
        iWarp device

    :param struct i40iw_cm_info \*cm_info:
        CM info for parent listen node

    :param struct i40iw_cm_listener \*cm_parent_listen_node:
        The parent listen node

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

    :param struct i40iw_device \*iwdev:
        iWarp device

    :param struct i40iw_cm_info \*cm_info:
        CM info for parent listen node

    :param struct i40iw_cm_listener \*cm_parent_listen_node:
        The parent listen node

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

    :param struct i40iw_cm_core \*cm_core:
        cm's core

    :param struct i40iw_cm_listener \*listener:
        *undescribed*

    :param int free_hanging_nodes:
        to free associated cm_nodes

    :param bool apbvt_del:
        flag to delete the apbvt

.. _`i40iw_cm_del_listen`:

i40iw_cm_del_listen
===================

.. c:function:: int i40iw_cm_del_listen(struct i40iw_cm_core *cm_core, struct i40iw_cm_listener *listener, bool apbvt_del)

    delete a linstener

    :param struct i40iw_cm_core \*cm_core:
        cm's core

    :param struct i40iw_cm_listener \*listener:
        passive connection's listener

    :param bool apbvt_del:
        flag to delete apbvt

.. _`i40iw_addr_resolve_neigh`:

i40iw_addr_resolve_neigh
========================

.. c:function:: int i40iw_addr_resolve_neigh(struct i40iw_device *iwdev, u32 src_ip, u32 dst_ip, int arpindex)

    resolve neighbor address

    :param struct i40iw_device \*iwdev:
        iwarp device structure

    :param u32 src_ip:
        local ip address

    :param u32 dst_ip:
        remote ip address

    :param int arpindex:
        if there is an arp entry

.. _`i40iw_get_dst_ipv6`:

i40iw_get_dst_ipv6
==================

.. c:function:: struct dst_entry *i40iw_get_dst_ipv6(struct sockaddr_in6 *src_addr, struct sockaddr_in6 *dst_addr)

    :param struct sockaddr_in6 \*src_addr:
        *undescribed*

    :param struct sockaddr_in6 \*dst_addr:
        *undescribed*

.. _`i40iw_addr_resolve_neigh_ipv6`:

i40iw_addr_resolve_neigh_ipv6
=============================

.. c:function:: int i40iw_addr_resolve_neigh_ipv6(struct i40iw_device *iwdev, u32 *src, u32 *dest, int arpindex)

    resolve neighbor ipv6 address

    :param struct i40iw_device \*iwdev:
        iwarp device structure

    :param u32 \*src:
        *undescribed*

    :param u32 \*dest:
        *undescribed*

    :param int arpindex:
        if there is an arp entry

.. _`i40iw_ipv4_is_loopback`:

i40iw_ipv4_is_loopback
======================

.. c:function:: bool i40iw_ipv4_is_loopback(u32 loc_addr, u32 rem_addr)

    check if loopback

    :param u32 loc_addr:
        local addr to compare

    :param u32 rem_addr:
        remote address

.. _`i40iw_ipv6_is_loopback`:

i40iw_ipv6_is_loopback
======================

.. c:function:: bool i40iw_ipv6_is_loopback(u32 *loc_addr, u32 *rem_addr)

    check if loopback

    :param u32 \*loc_addr:
        local addr to compare

    :param u32 \*rem_addr:
        remote address

.. _`i40iw_make_cm_node`:

i40iw_make_cm_node
==================

.. c:function:: struct i40iw_cm_node *i40iw_make_cm_node(struct i40iw_cm_core *cm_core, struct i40iw_device *iwdev, struct i40iw_cm_info *cm_info, struct i40iw_cm_listener *listener)

    create a new instance of a cm node

    :param struct i40iw_cm_core \*cm_core:
        cm's core

    :param struct i40iw_device \*iwdev:
        iwarp device structure

    :param struct i40iw_cm_info \*cm_info:
        quad info for connection

    :param struct i40iw_cm_listener \*listener:
        passive connection's listener

.. _`i40iw_rem_ref_cm_node`:

i40iw_rem_ref_cm_node
=====================

.. c:function:: void i40iw_rem_ref_cm_node(struct i40iw_cm_node *cm_node)

    destroy an instance of a cm node

    :param struct i40iw_cm_node \*cm_node:
        connection's node

.. _`i40iw_handle_fin_pkt`:

i40iw_handle_fin_pkt
====================

.. c:function:: void i40iw_handle_fin_pkt(struct i40iw_cm_node *cm_node)

    FIN packet received

    :param struct i40iw_cm_node \*cm_node:
        connection's node

.. _`i40iw_handle_rst_pkt`:

i40iw_handle_rst_pkt
====================

.. c:function:: void i40iw_handle_rst_pkt(struct i40iw_cm_node *cm_node, struct i40iw_puda_buf *rbuf)

    process received RST packet

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param struct i40iw_puda_buf \*rbuf:
        receive buffer

.. _`i40iw_handle_rcv_mpa`:

i40iw_handle_rcv_mpa
====================

.. c:function:: void i40iw_handle_rcv_mpa(struct i40iw_cm_node *cm_node, struct i40iw_puda_buf *rbuf)

    Process a recv'd mpa buffer

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param struct i40iw_puda_buf \*rbuf:
        receive buffer

.. _`i40iw_indicate_pkt_err`:

i40iw_indicate_pkt_err
======================

.. c:function:: void i40iw_indicate_pkt_err(struct i40iw_cm_node *cm_node)

    Send up err event to cm

    :param struct i40iw_cm_node \*cm_node:
        connection's node

.. _`i40iw_check_syn`:

i40iw_check_syn
===============

.. c:function:: int i40iw_check_syn(struct i40iw_cm_node *cm_node, struct tcphdr *tcph)

    Check for error on received syn ack

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param struct tcphdr \*tcph:
        pointer tcp header

.. _`i40iw_check_seq`:

i40iw_check_seq
===============

.. c:function:: int i40iw_check_seq(struct i40iw_cm_node *cm_node, struct tcphdr *tcph)

    check seq numbers if OK

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param struct tcphdr \*tcph:
        pointer tcp header

.. _`i40iw_handle_syn_pkt`:

i40iw_handle_syn_pkt
====================

.. c:function:: void i40iw_handle_syn_pkt(struct i40iw_cm_node *cm_node, struct i40iw_puda_buf *rbuf)

    is for Passive node

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param struct i40iw_puda_buf \*rbuf:
        receive buffer

.. _`i40iw_handle_synack_pkt`:

i40iw_handle_synack_pkt
=======================

.. c:function:: void i40iw_handle_synack_pkt(struct i40iw_cm_node *cm_node, struct i40iw_puda_buf *rbuf)

    Process SYN+ACK packet (active side)

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param struct i40iw_puda_buf \*rbuf:
        receive buffer

.. _`i40iw_handle_ack_pkt`:

i40iw_handle_ack_pkt
====================

.. c:function:: int i40iw_handle_ack_pkt(struct i40iw_cm_node *cm_node, struct i40iw_puda_buf *rbuf)

    process packet with ACK

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param struct i40iw_puda_buf \*rbuf:
        receive buffer

.. _`i40iw_process_packet`:

i40iw_process_packet
====================

.. c:function:: void i40iw_process_packet(struct i40iw_cm_node *cm_node, struct i40iw_puda_buf *rbuf)

    process cm packet

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param struct i40iw_puda_buf \*rbuf:
        receive buffer

.. _`i40iw_make_listen_node`:

i40iw_make_listen_node
======================

.. c:function:: struct i40iw_cm_listener *i40iw_make_listen_node(struct i40iw_cm_core *cm_core, struct i40iw_device *iwdev, struct i40iw_cm_info *cm_info)

    create a listen node with params

    :param struct i40iw_cm_core \*cm_core:
        cm's core

    :param struct i40iw_device \*iwdev:
        iwarp device structure

    :param struct i40iw_cm_info \*cm_info:
        quad info for connection

.. _`i40iw_create_cm_node`:

i40iw_create_cm_node
====================

.. c:function:: struct i40iw_cm_node *i40iw_create_cm_node(struct i40iw_cm_core *cm_core, struct i40iw_device *iwdev, u16 private_data_len, void *private_data, struct i40iw_cm_info *cm_info)

    make a connection node with params

    :param struct i40iw_cm_core \*cm_core:
        cm's core

    :param struct i40iw_device \*iwdev:
        iwarp device structure

    :param u16 private_data_len:
        len to provate data for mpa request

    :param void \*private_data:
        pointer to private data for connection

    :param struct i40iw_cm_info \*cm_info:
        quad info for connection

.. _`i40iw_cm_reject`:

i40iw_cm_reject
===============

.. c:function:: int i40iw_cm_reject(struct i40iw_cm_node *cm_node, const void *pdata, u8 plen)

    reject and teardown a connection

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param const void \*pdata:
        *undescribed*

    :param u8 plen:
        size of private data

.. _`i40iw_cm_close`:

i40iw_cm_close
==============

.. c:function:: int i40iw_cm_close(struct i40iw_cm_node *cm_node)

    close of cm connection

    :param struct i40iw_cm_node \*cm_node:
        connection's node

.. _`i40iw_receive_ilq`:

i40iw_receive_ilq
=================

.. c:function:: void i40iw_receive_ilq(struct i40iw_sc_dev *dev, struct i40iw_puda_buf *rbuf)

    recv an ETHERNET packet, and process it through CM

    :param struct i40iw_sc_dev \*dev:
        FPK dev struct

    :param struct i40iw_puda_buf \*rbuf:
        receive buffer

.. _`i40iw_setup_cm_core`:

i40iw_setup_cm_core
===================

.. c:function:: void i40iw_setup_cm_core(struct i40iw_device *iwdev)

    allocate a top level instance of a cm core

    :param struct i40iw_device \*iwdev:
        iwarp device structure

.. _`i40iw_cleanup_cm_core`:

i40iw_cleanup_cm_core
=====================

.. c:function:: void i40iw_cleanup_cm_core(struct i40iw_cm_core *cm_core)

    deallocate a top level instance of a cm core

    :param struct i40iw_cm_core \*cm_core:
        cm's core

.. _`i40iw_init_tcp_ctx`:

i40iw_init_tcp_ctx
==================

.. c:function:: void i40iw_init_tcp_ctx(struct i40iw_cm_node *cm_node, struct i40iw_tcp_offload_info *tcp_info, struct i40iw_qp *iwqp)

    setup qp context

    :param struct i40iw_cm_node \*cm_node:
        connection's node

    :param struct i40iw_tcp_offload_info \*tcp_info:
        offload info for tcp

    :param struct i40iw_qp \*iwqp:
        associate qp for the connection

.. _`i40iw_cm_init_tsa_conn`:

i40iw_cm_init_tsa_conn
======================

.. c:function:: void i40iw_cm_init_tsa_conn(struct i40iw_qp *iwqp, struct i40iw_cm_node *cm_node)

    setup qp for RTS

    :param struct i40iw_qp \*iwqp:
        associate qp for the connection

    :param struct i40iw_cm_node \*cm_node:
        connection's node

.. _`i40iw_cm_disconn`:

i40iw_cm_disconn
================

.. c:function:: int i40iw_cm_disconn(struct i40iw_qp *iwqp)

    when a connection is being closed

    :param struct i40iw_qp \*iwqp:
        associate qp for the connection

.. _`i40iw_qp_disconnect`:

i40iw_qp_disconnect
===================

.. c:function:: void i40iw_qp_disconnect(struct i40iw_qp *iwqp)

    free qp and close cm

    :param struct i40iw_qp \*iwqp:
        associate qp for the connection

.. _`i40iw_cm_disconn_true`:

i40iw_cm_disconn_true
=====================

.. c:function:: void i40iw_cm_disconn_true(struct i40iw_qp *iwqp)

    called by worker thread to disconnect qp

    :param struct i40iw_qp \*iwqp:
        associate qp for the connection

.. _`i40iw_disconnect_worker`:

i40iw_disconnect_worker
=======================

.. c:function:: void i40iw_disconnect_worker(struct work_struct *work)

    worker for connection close

    :param struct work_struct \*work:
        points or disconn structure

.. _`i40iw_accept`:

i40iw_accept
============

.. c:function:: int i40iw_accept(struct iw_cm_id *cm_id, struct iw_cm_conn_param *conn_param)

    registered call for connection to be accepted

    :param struct iw_cm_id \*cm_id:
        cm information for passive connection

    :param struct iw_cm_conn_param \*conn_param:
        accpet parameters

.. _`i40iw_reject`:

i40iw_reject
============

.. c:function:: int i40iw_reject(struct iw_cm_id *cm_id, const void *pdata, u8 pdata_len)

    registered call for connection to be rejected

    :param struct iw_cm_id \*cm_id:
        cm information for passive connection

    :param const void \*pdata:
        private data to be sent

    :param u8 pdata_len:
        private data length

.. _`i40iw_connect`:

i40iw_connect
=============

.. c:function:: int i40iw_connect(struct iw_cm_id *cm_id, struct iw_cm_conn_param *conn_param)

    registered call for connection to be established

    :param struct iw_cm_id \*cm_id:
        cm information for passive connection

    :param struct iw_cm_conn_param \*conn_param:
        Information about the connection

.. _`i40iw_create_listen`:

i40iw_create_listen
===================

.. c:function:: int i40iw_create_listen(struct iw_cm_id *cm_id, int backlog)

    registered call creating listener

    :param struct iw_cm_id \*cm_id:
        cm information for passive connection

    :param int backlog:
        to max accept pending count

.. _`i40iw_destroy_listen`:

i40iw_destroy_listen
====================

.. c:function:: int i40iw_destroy_listen(struct iw_cm_id *cm_id)

    registered call to destroy listener

    :param struct iw_cm_id \*cm_id:
        cm information for passive connection

.. _`i40iw_cm_event_connected`:

i40iw_cm_event_connected
========================

.. c:function:: void i40iw_cm_event_connected(struct i40iw_cm_event *event)

    handle connected active node

    :param struct i40iw_cm_event \*event:
        the info for cm_node of connection

.. _`i40iw_cm_event_reset`:

i40iw_cm_event_reset
====================

.. c:function:: void i40iw_cm_event_reset(struct i40iw_cm_event *event)

    handle reset

    :param struct i40iw_cm_event \*event:
        the info for cm_node of connection

.. _`i40iw_cm_event_handler`:

i40iw_cm_event_handler
======================

.. c:function:: void i40iw_cm_event_handler(struct work_struct *work)

    worker thread callback to send event to cm upper layer

    :param struct work_struct \*work:
        pointer of cm event info.

.. _`i40iw_cm_post_event`:

i40iw_cm_post_event
===================

.. c:function:: void i40iw_cm_post_event(struct i40iw_cm_event *event)

    queue event request for worker thread

    :param struct i40iw_cm_event \*event:
        cm node's info for up event call

.. This file was automatic generated / don't edit.

