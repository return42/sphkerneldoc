.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/iscsi_tcp.c

.. _`iscsi_sw_tcp_recv`:

iscsi_sw_tcp_recv
=================

.. c:function:: int iscsi_sw_tcp_recv(read_descriptor_t *rd_desc, struct sk_buff *skb, unsigned int offset, size_t len)

    TCP receive in sendfile fashion

    :param rd_desc:
        read descriptor
    :type rd_desc: read_descriptor_t \*

    :param skb:
        socket buffer
    :type skb: struct sk_buff \*

    :param offset:
        offset in skb
    :type offset: unsigned int

    :param len:
        skb->len - offset
    :type len: size_t

.. _`iscsi_sw_sk_state_check`:

iscsi_sw_sk_state_check
=======================

.. c:function:: int iscsi_sw_sk_state_check(struct sock *sk)

    check socket state

    :param sk:
        socket
    :type sk: struct sock \*

.. _`iscsi_sw_sk_state_check.description`:

Description
-----------

If the socket is in CLOSE or CLOSE_WAIT we should
not close the connection if there is still some
data pending.

Must be called with sk_callback_lock.

.. _`iscsi_sw_tcp_write_space`:

iscsi_sw_tcp_write_space
========================

.. c:function:: void iscsi_sw_tcp_write_space(struct sock *sk)

    Called when more output buffer space is available

    :param sk:
        socket space is available for
    :type sk: struct sock \*

.. _`iscsi_sw_tcp_xmit_segment`:

iscsi_sw_tcp_xmit_segment
=========================

.. c:function:: int iscsi_sw_tcp_xmit_segment(struct iscsi_tcp_conn *tcp_conn, struct iscsi_segment *segment)

    transmit segment

    :param tcp_conn:
        the iSCSI TCP connection
    :type tcp_conn: struct iscsi_tcp_conn \*

    :param segment:
        the buffer to transmnit
    :type segment: struct iscsi_segment \*

.. _`iscsi_sw_tcp_xmit_segment.description`:

Description
-----------

This function transmits as much of the buffer as
the network layer will accept, and returns the number of
bytes transmitted.

If CRC hashing is enabled, the function will compute the
hash as it goes. When the entire segment has been transmitted,
it will retrieve the hash value and send it as well.

.. _`iscsi_sw_tcp_xmit`:

iscsi_sw_tcp_xmit
=================

.. c:function:: int iscsi_sw_tcp_xmit(struct iscsi_conn *conn)

    TCP transmit

    :param conn:
        iscsi connection
    :type conn: struct iscsi_conn \*

.. _`iscsi_sw_tcp_xmit_qlen`:

iscsi_sw_tcp_xmit_qlen
======================

.. c:function:: int iscsi_sw_tcp_xmit_qlen(struct iscsi_conn *conn)

    return the number of bytes queued for xmit

    :param conn:
        iscsi connection
    :type conn: struct iscsi_conn \*

.. This file was automatic generated / don't edit.

