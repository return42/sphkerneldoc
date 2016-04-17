.. -*- coding: utf-8; mode: rst -*-

======
dccp.h
======


.. _`dccp_request_sock`:

struct dccp_request_sock
========================

.. c:type:: dccp_request_sock

    represent DCCP-specific connection request


.. _`dccp_request_sock.definition`:

Definition
----------

.. code-block:: c

  struct dccp_request_sock {
    struct inet_request_sock dreq_inet_rsk;
    __u64 dreq_iss;
    __u64 dreq_gss;
    __u64 dreq_isr;
    __u64 dreq_gsr;
    __be32 dreq_service;
    struct list_head dreq_featneg;
    __u32 dreq_timestamp_echo;
  };


.. _`dccp_request_sock.members`:

Members
-------

:``dreq_inet_rsk``:
    structure inherited from

:``dreq_iss``:
    initial sequence number, sent on the first Response (RFC 4340, 7.1)

:``dreq_gss``:
    greatest sequence number sent (for retransmitted Responses)

:``dreq_isr``:
    initial sequence number received in the first Request

:``dreq_gsr``:
    greatest sequence number received (for retransmitted Request(s))

:``dreq_service``:
    service code present on the Request (there is just one)

:``dreq_featneg``:
    feature negotiation options for this connection

:``dreq_timestamp_echo``:
    the time of receiving the last ``dreq_timestamp_echo``




.. _`dccp_sock`:

struct dccp_sock
================

.. c:type:: dccp_sock

    DCCP socket state


.. _`dccp_sock.definition`:

Definition
----------

.. code-block:: c

  struct dccp_sock {
    #define dccps_syn_rtt			dccps_inet_connection.icsk_ack.lrcvtime
  };


.. _`dccp_sock.members`:

Members
-------




.. _`dccp_sock.description`:

Description
-----------


``dccps_swl`` - sequence number window low
``dccps_swh`` - sequence number window high
``dccps_awl`` - acknowledgement number window low
``dccps_awh`` - acknowledgement number window high
``dccps_iss`` - initial sequence number sent
``dccps_isr`` - initial sequence number received
``dccps_osr`` - first OPEN sequence number received
``dccps_gss`` - greatest sequence number sent
``dccps_gsr`` - greatest valid sequence number received
``dccps_gar`` - greatest valid ack number received on a non-Sync; initialized to ``dccps_iss``
``dccps_service`` - first (passive sock) or unique (active sock) service code
``dccps_service_list`` - second .. last service code on passive socket
``dccps_timestamp_echo`` - latest timestamp received on a TIMESTAMP option
``dccps_timestamp_time`` - time of receiving latest ``dccps_timestamp_echo``
``dccps_l_ack_ratio`` - feature-local Ack Ratio
``dccps_r_ack_ratio`` - feature-remote Ack Ratio
``dccps_l_seq_win`` - local Sequence Window (influences ack number validity)
``dccps_r_seq_win`` - remote Sequence Window (influences seq number validity)
``dccps_pcslen`` - sender   partial checksum coverage (via sockopt)
``dccps_pcrlen`` - receiver partial checksum coverage (via sockopt)
``dccps_send_ndp_count`` - local Send NDP Count feature (7.7.2)
``dccps_ndp_count`` - number of Non Data Packets since last data packet
``dccps_mss_cache`` - current value of MSS (path MTU minus header sizes)
``dccps_rate_last`` - timestamp for rate-limiting DCCP-Sync (RFC 4340, 7.5.4)
``dccps_featneg`` - tracks feature-negotiation state (mostly during handshake)
``dccps_hc_rx_ackvec`` - rx half connection ack vector
``dccps_hc_rx_ccid`` - CCID used for the receiver (or receiving half-connection)
``dccps_hc_tx_ccid`` - CCID used for the sender (or sending half-connection)
``dccps_options_received`` - parsed set of retrieved options
``dccps_qpolicy`` - TX dequeueing policy, one of ``dccp_packet_dequeueing_policy``
``dccps_tx_qlen`` - maximum length of the TX queue
``dccps_role`` - role of this sock, one of ``dccp_role``
``dccps_hc_rx_insert_options`` - receiver wants to add options when acking
``dccps_hc_tx_insert_options`` - sender wants to add options when sending
``dccps_server_timewait`` - server holds timewait state on close (RFC 4340, 8.3)
``dccps_sync_scheduled`` - flag which signals "send out-of-band message soon"
``dccps_xmitlet`` - tasklet scheduled by the TX CCID to dequeue data packets
``dccps_xmit_timer`` - used by the TX CCID to delay sending (rate-based pacing)
``dccps_syn_rtt`` - RTT sample from Request/Response exchange (in usecs)

