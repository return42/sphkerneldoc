.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/ccid.h

.. _`ccid_operations`:

struct ccid_operations
======================

.. c:type:: struct ccid_operations

    Interface to Congestion-Control Infrastructure

.. _`ccid_operations.definition`:

Definition
----------

.. code-block:: c

    struct ccid_operations {
        unsigned char ccid_id;
        __u32 ccid_ccmps;
        const char *ccid_name;
        struct kmem_cache *ccid_hc_rx_slab;
        struct kmem_cache * *ccid_hc_tx_slab;
        char ccid_hc_rx_slab_name[CCID_SLAB_NAME_LENGTH];
        char ccid_hc_tx_slab_name[CCID_SLAB_NAME_LENGTH];
        __u32 ccid_hc_rx_obj_size;
        __u32 ccid_hc_tx_obj_size;
        int (*ccid_hc_rx_init)(struct ccid *ccid, struct sock *sk);
        int (*ccid_hc_tx_init)(struct ccid *ccid, struct sock *sk);
        void (*ccid_hc_rx_exit)(struct sock *sk);
        void (*ccid_hc_tx_exit)(struct sock *sk);
        void (*ccid_hc_rx_packet_recv)(struct sock *sk,struct sk_buff *skb);
        int (*ccid_hc_rx_parse_options)(struct sock *sk, u8 pkt,u8 opt, u8 *val, u8 len);
        int (*ccid_hc_rx_insert_options)(struct sock *sk,struct sk_buff *skb);
        void (*ccid_hc_tx_packet_recv)(struct sock *sk,struct sk_buff *skb);
        int (*ccid_hc_tx_parse_options)(struct sock *sk, u8 pkt,u8 opt, u8 *val, u8 len);
        int (*ccid_hc_tx_send_packet)(struct sock *sk,struct sk_buff *skb);
        void (*ccid_hc_tx_packet_sent)(struct sock *sk,unsigned int len);
        void (*ccid_hc_rx_get_info)(struct sock *sk,struct tcp_info *info);
        void (*ccid_hc_tx_get_info)(struct sock *sk,struct tcp_info *info);
        int (*ccid_hc_rx_getsockopt)(struct sock *sk,const int optname, int len,u32 __user *optval,int __user *optlen);
        int (*ccid_hc_tx_getsockopt)(struct sock *sk,const int optname, int len,u32 __user *optval,int __user *optlen);
    }

.. _`ccid_operations.members`:

Members
-------

ccid_id
    numerical CCID ID (up to \ ``CCID_MAX``\ , cf. table 5 in RFC 4340, 10.)

ccid_ccmps
    the CCMPS including network/transport headers (0 when disabled)

ccid_name
    alphabetical identifier string for \ ``ccid_id``\ 

ccid_hc_rx_slab
    *undescribed*

ccid_hc_tx_slab
    *undescribed*

ccid_hc_rx_obj_size
    *undescribed*

ccid_hc_tx_obj_size
    *undescribed*

ccid_hc_rx_init
    *undescribed*

ccid_hc_tx_init
    *undescribed*

ccid_hc_rx_exit
    *undescribed*

ccid_hc_tx_exit
    *undescribed*

ccid_hc_rx_packet_recv
    implements the HC-receiver side

ccid_hc_rx_parse_options
    *undescribed*

ccid_hc_rx_insert_options
    *undescribed*

ccid_hc_tx_packet_recv
    implements feedback processing for the HC-sender

ccid_hc_tx_parse_options
    *undescribed*

ccid_hc_tx_send_packet
    implements the sending part of the HC-sender

ccid_hc_tx_packet_sent
    does accounting for packets in flight by HC-sender

ccid_hc_rx_get_info
    *undescribed*

ccid_hc_tx_get_info
    *undescribed*

ccid_hc_rx_getsockopt
    *undescribed*

ccid_hc_tx_getsockopt
    *undescribed*

.. _`ccid_hc_tx_parse_options`:

ccid_hc_tx_parse_options
========================

.. c:function:: int ccid_hc_tx_parse_options(struct ccid *ccid, struct sock *sk, u8 pkt, u8 opt, u8 *val, u8 len)

    Parse CCID-specific options sent by the receiver

    :param struct ccid \*ccid:
        *undescribed*

    :param struct sock \*sk:
        *undescribed*

    :param u8 pkt:
        type of packet that \ ``opt``\  appears on (RFC 4340, 5.1)

    :param u8 opt:
        the CCID-specific option type (RFC 4340, 5.8 and 10.3)

    :param u8 \*val:
        value of \ ``opt``\ 

    :param u8 len:
        length of \ ``val``\  in bytes

.. _`ccid_hc_rx_parse_options`:

ccid_hc_rx_parse_options
========================

.. c:function:: int ccid_hc_rx_parse_options(struct ccid *ccid, struct sock *sk, u8 pkt, u8 opt, u8 *val, u8 len)

    Parse CCID-specific options sent by the sender Arguments are analogous to \ :c:func:`ccid_hc_tx_parse_options`\ 

    :param struct ccid \*ccid:
        *undescribed*

    :param struct sock \*sk:
        *undescribed*

    :param u8 pkt:
        *undescribed*

    :param u8 opt:
        *undescribed*

    :param u8 \*val:
        *undescribed*

    :param u8 len:
        *undescribed*

.. This file was automatic generated / don't edit.

