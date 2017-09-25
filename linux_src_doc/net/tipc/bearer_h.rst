.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/bearer.h

.. _`tipc_media_addr`:

struct tipc_media_addr
======================

.. c:type:: struct tipc_media_addr

    destination address used by TIPC bearers

.. _`tipc_media_addr.definition`:

Definition
----------

.. code-block:: c

    struct tipc_media_addr {
        u8 value[TIPC_MEDIA_INFO_SIZE];
        u8 media_id;
        u8 broadcast;
    }

.. _`tipc_media_addr.members`:

Members
-------

value
    address info (format defined by media)

media_id
    TIPC media type identifier

broadcast
    non-zero if address is a broadcast address

.. _`tipc_media`:

struct tipc_media
=================

.. c:type:: struct tipc_media

    Media specific info exposed to generic bearer layer

.. _`tipc_media.definition`:

Definition
----------

.. code-block:: c

    struct tipc_media {
        int (*send_msg)(struct net *net, struct sk_buff *buf,struct tipc_bearer *b, struct tipc_media_addr *dest);
        int (*enable_media)(struct net *net, struct tipc_bearer *b, struct nlattr *attr[]);
        void (*disable_media)(struct tipc_bearer *b);
        int (*addr2str)(struct tipc_media_addr *addr,char *strbuf, int bufsz);
        int (*addr2msg)(char *msg, struct tipc_media_addr *addr);
        int (*msg2addr)(struct tipc_bearer *b,struct tipc_media_addr *addr, char *msg);
        int (*raw2addr)(struct tipc_bearer *b,struct tipc_media_addr *addr, char *raw);
        u32 priority;
        u32 tolerance;
        u32 window;
        u32 type_id;
        u32 hwaddr_len;
        char name[TIPC_MAX_MEDIA_NAME];
    }

.. _`tipc_media.members`:

Members
-------

send_msg
    routine which handles buffer transmission

enable_media
    routine which enables a media

disable_media
    routine which disables a media

addr2str
    convert media address format to string

addr2msg
    convert from media addr format to discovery msg addr format

msg2addr
    convert from discovery msg addr format to media addr format

raw2addr
    convert from raw addr format to media addr format

priority
    default link (and bearer) priority

tolerance
    default time (in ms) before declaring link failure

window
    default window (in packets) before declaring link congestion

type_id
    TIPC media identifier

hwaddr_len
    TIPC media address len

name
    media name

.. _`tipc_bearer`:

struct tipc_bearer
==================

.. c:type:: struct tipc_bearer

    Generic TIPC bearer structure

.. _`tipc_bearer.definition`:

Definition
----------

.. code-block:: c

    struct tipc_bearer {
        void __rcu *media_ptr;
        u32 mtu;
        struct tipc_media_addr addr;
        char name[TIPC_MAX_BEARER_NAME];
        struct tipc_media *media;
        struct tipc_media_addr bcast_addr;
        struct packet_type pt;
        struct rcu_head rcu;
        u32 priority;
        u32 window;
        u32 tolerance;
        u32 domain;
        u32 identity;
        struct tipc_link_req *link_req;
        char net_plane;
        unsigned long up;
    }

.. _`tipc_bearer.members`:

Members
-------

media_ptr
    pointer to additional media-specific information about bearer

mtu
    max packet size bearer can support

addr
    media-specific address associated with bearer

name
    bearer name (format = media:interface)

media
    ptr to media structure associated with bearer

bcast_addr
    media address used in broadcasting

pt
    packet type for bearer

rcu
    rcu struct for tipc_bearer

priority
    default link priority for bearer

window
    default window size for bearer

tolerance
    default link tolerance for bearer

domain
    network domain to which links can be established

identity
    array index of this bearer within TIPC bearer array

link_req
    ptr to (optional) structure making periodic link setup requests

net_plane
    network plane ('A' through 'H') currently associated with bearer

up
    *undescribed*

.. _`tipc_bearer.note`:

Note
----

media-specific code is responsible for initialization of the fields
indicated below when a bearer is enabled; TIPC's generic bearer code takes
care of initializing all other fields.

.. This file was automatic generated / don't edit.

