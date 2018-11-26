.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/link.c

.. _`tipc_link`:

struct tipc_link
================

.. c:type:: struct tipc_link

    TIPC link data structure

.. _`tipc_link.definition`:

Definition
----------

.. code-block:: c

    struct tipc_link {
        u32 addr;
        char name[TIPC_MAX_LINK_NAME];
        struct net *net;
        u16 peer_session;
        u16 session;
        u16 snd_nxt_state;
        u16 rcv_nxt_state;
        u32 peer_bearer_id;
        u32 bearer_id;
        u32 tolerance;
        u32 abort_limit;
        u32 state;
        u16 peer_caps;
        bool in_session;
        bool active;
        u32 silent_intv_cnt;
        char if_name[TIPC_MAX_IF_NAME];
        u32 priority;
        char net_plane;
        struct tipc_mon_state mon_state;
        u16 rst_cnt;
        u16 drop_point;
        struct sk_buff *failover_reasm_skb;
        u16 mtu;
        u16 advertised_mtu;
        struct sk_buff_head transmq;
        struct sk_buff_head backlogq;
        struct {
            u16 len;
            u16 limit;
        } backlog[5];
        u16 snd_nxt;
        u16 last_retransm;
        u16 window;
        u16 stale_cnt;
        unsigned long stale_limit;
        u16 rcv_nxt;
        u32 rcv_unacked;
        struct sk_buff_head deferdq;
        struct sk_buff_head *inputq;
        struct sk_buff_head *namedq;
        struct sk_buff_head wakeupq;
        struct sk_buff *reasm_buf;
        u16 ackers;
        u16 acked;
        struct tipc_link *bc_rcvlink;
        struct tipc_link *bc_sndlink;
        unsigned long prev_retr;
        u16 prev_from;
        u16 prev_to;
        u8 nack_state;
        bool bc_peer_is_up;
        struct tipc_stats stats;
    }

.. _`tipc_link.members`:

Members
-------

addr
    network address of link's peer node

name
    link name character string

net
    pointer to namespace struct

peer_session
    link session # being used by peer end of link

session
    *undescribed*

snd_nxt_state
    *undescribed*

rcv_nxt_state
    *undescribed*

peer_bearer_id
    bearer id used by link's peer endpoint

bearer_id
    local bearer id used by link

tolerance
    minimum link continuity loss needed to reset link [in ms]

abort_limit
    # of unacknowledged continuity probes needed to reset link

state
    current state of link FSM

peer_caps
    bitmap describing capabilities of peer node

in_session
    *undescribed*

active
    *undescribed*

silent_intv_cnt
    # of timer intervals without any reception from peer

if_name
    *undescribed*

priority
    current link priority

net_plane
    current link network plane ('A' through 'H')

mon_state
    cookie with information needed by link monitor

rst_cnt
    *undescribed*

drop_point
    *undescribed*

failover_reasm_skb
    *undescribed*

mtu
    current maximum packet size for this link

advertised_mtu
    advertised own mtu when link is being established

transmq
    *undescribed*

backlogq
    queue for messages waiting to be sent

backlog
    *undescribed*

snd_nxt
    *undescribed*

last_retransm
    *undescribed*

window
    *undescribed*

stale_cnt
    counter for number of identical retransmit attempts

stale_limit
    time when repeated identical retransmits must force link reset

rcv_nxt
    next sequence number to expect for inbound messages

rcv_unacked
    *undescribed*

deferdq
    *undescribed*

inputq
    buffer queue for messages to be delivered upwards

namedq
    buffer queue for name table messages to be delivered upwards

wakeupq
    linked list of wakeup msgs waiting for link congestion to abate

reasm_buf
    head of partially reassembled inbound message fragments

ackers
    # of peers that needs to ack each packet before it can be released

acked
    # last packet acked by a certain peer. Used for broadcast.

bc_rcvlink
    *undescribed*

bc_sndlink
    *undescribed*

prev_retr
    *undescribed*

prev_from
    *undescribed*

prev_to
    *undescribed*

nack_state
    *undescribed*

bc_peer_is_up
    *undescribed*

stats
    collects statistics regarding link activity

.. _`tipc_link_create`:

tipc_link_create
================

.. c:function:: bool tipc_link_create(struct net *net, char *if_name, int bearer_id, int tolerance, char net_plane, u32 mtu, int priority, int window, u32 session, u32 self, u32 peer, u8 *peer_id, u16 peer_caps, struct tipc_link *bc_sndlink, struct tipc_link *bc_rcvlink, struct sk_buff_head *inputq, struct sk_buff_head *namedq, struct tipc_link **link)

    create a new link

    :param net:
        *undescribed*
    :type net: struct net \*

    :param if_name:
        associated interface name
    :type if_name: char \*

    :param bearer_id:
        id (index) of associated bearer
    :type bearer_id: int

    :param tolerance:
        link tolerance to be used by link
    :type tolerance: int

    :param net_plane:
        network plane (A,B,c..) this link belongs to
    :type net_plane: char

    :param mtu:
        mtu to be advertised by link
    :type mtu: u32

    :param priority:
        priority to be used by link
    :type priority: int

    :param window:
        send window to be used by link
    :type window: int

    :param session:
        session to be used by link
    :type session: u32

    :param self:
        *undescribed*
    :type self: u32

    :param peer:
        node id of peer node
    :type peer: u32

    :param peer_id:
        *undescribed*
    :type peer_id: u8 \*

    :param peer_caps:
        bitmap describing peer node capabilities
    :type peer_caps: u16

    :param bc_sndlink:
        the namespace global link used for broadcast sending
    :type bc_sndlink: struct tipc_link \*

    :param bc_rcvlink:
        the peer specific link used for broadcast reception
    :type bc_rcvlink: struct tipc_link \*

    :param inputq:
        queue to put messages ready for delivery
    :type inputq: struct sk_buff_head \*

    :param namedq:
        queue to put binding table update messages ready for delivery
    :type namedq: struct sk_buff_head \*

    :param link:
        return value, pointer to put the created link
    :type link: struct tipc_link \*\*

.. _`tipc_link_create.description`:

Description
-----------

Returns true if link was created, otherwise false

.. _`tipc_link_bc_create`:

tipc_link_bc_create
===================

.. c:function:: bool tipc_link_bc_create(struct net *net, u32 ownnode, u32 peer, int mtu, int window, u16 peer_caps, struct sk_buff_head *inputq, struct sk_buff_head *namedq, struct tipc_link *bc_sndlink, struct tipc_link **link)

    create new link to be used for broadcast

    :param net:
        *undescribed*
    :type net: struct net \*

    :param ownnode:
        *undescribed*
    :type ownnode: u32

    :param peer:
        *undescribed*
    :type peer: u32

    :param mtu:
        mtu to be used initially if no peers
    :type mtu: int

    :param window:
        send window to be used
    :type window: int

    :param peer_caps:
        *undescribed*
    :type peer_caps: u16

    :param inputq:
        queue to put messages ready for delivery
    :type inputq: struct sk_buff_head \*

    :param namedq:
        queue to put binding table update messages ready for delivery
    :type namedq: struct sk_buff_head \*

    :param bc_sndlink:
        *undescribed*
    :type bc_sndlink: struct tipc_link \*

    :param link:
        return value, pointer to put the created link
    :type link: struct tipc_link \*\*

.. _`tipc_link_bc_create.description`:

Description
-----------

Returns true if link was created, otherwise false

.. _`tipc_link_fsm_evt`:

tipc_link_fsm_evt
=================

.. c:function:: int tipc_link_fsm_evt(struct tipc_link *l, int evt)

    link finite state machine

    :param l:
        pointer to link
    :type l: struct tipc_link \*

    :param evt:
        state machine event to be processed
    :type evt: int

.. _`link_schedule_user`:

link_schedule_user
==================

.. c:function:: int link_schedule_user(struct tipc_link *l, struct tipc_msg *hdr)

    schedule a message sender for wakeup after congestion

    :param l:
        congested link
    :type l: struct tipc_link \*

    :param hdr:
        header of message that is being sent
        Create pseudo msg to send back to user when congestion abates
    :type hdr: struct tipc_msg \*

.. _`link_prepare_wakeup`:

link_prepare_wakeup
===================

.. c:function:: void link_prepare_wakeup(struct tipc_link *l)

    prepare users for wakeup after congestion

    :param l:
        congested link
        Wake up a number of waiting users, as permitted by available space
        in the send queue
    :type l: struct tipc_link \*

.. _`tipc_link_xmit`:

tipc_link_xmit
==============

.. c:function:: int tipc_link_xmit(struct tipc_link *l, struct sk_buff_head *list, struct sk_buff_head *xmitq)

    enqueue buffer list according to queue situation

    :param l:
        *undescribed*
    :type l: struct tipc_link \*

    :param list:
        chain of buffers containing message
    :type list: struct sk_buff_head \*

    :param xmitq:
        returned list of packets to be sent by caller
    :type xmitq: struct sk_buff_head \*

.. _`tipc_link_xmit.description`:

Description
-----------

Consumes the buffer chain.
Returns 0 if success, or errno: -ELINKCONG, -EMSGSIZE or -ENOBUFS
Messages at TIPC_SYSTEM_IMPORTANCE are always accepted

.. _`tipc_link_reset_stats`:

tipc_link_reset_stats
=====================

.. c:function:: void tipc_link_reset_stats(struct tipc_link *l)

    reset link statistics

    :param l:
        pointer to link
    :type l: struct tipc_link \*

.. This file was automatic generated / don't edit.

