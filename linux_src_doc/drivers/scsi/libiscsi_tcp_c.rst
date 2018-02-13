.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libiscsi_tcp.c

.. _`iscsi_tcp_segment_init_sg`:

iscsi_tcp_segment_init_sg
=========================

.. c:function:: void iscsi_tcp_segment_init_sg(struct iscsi_segment *segment, struct scatterlist *sg, unsigned int offset)

    init indicated scatterlist entry

    :param struct iscsi_segment \*segment:
        the buffer object

    :param struct scatterlist \*sg:
        scatterlist

    :param unsigned int offset:
        byte offset into that sg entry

.. _`iscsi_tcp_segment_init_sg.description`:

Description
-----------

This function sets up the segment so that subsequent
data is copied to the indicated sg entry, at the given
offset.

.. _`iscsi_tcp_segment_map`:

iscsi_tcp_segment_map
=====================

.. c:function:: void iscsi_tcp_segment_map(struct iscsi_segment *segment, int recv)

    map the current S/G page

    :param struct iscsi_segment \*segment:
        iscsi_segment

    :param int recv:
        1 if called from recv path

.. _`iscsi_tcp_segment_map.description`:

Description
-----------

We only need to possibly kmap data if scatter lists are being used,
because the iscsi passthrough and internal IO paths will never use high
mem pages.

.. _`iscsi_tcp_segment_done`:

iscsi_tcp_segment_done
======================

.. c:function:: int iscsi_tcp_segment_done(struct iscsi_tcp_conn *tcp_conn, struct iscsi_segment *segment, int recv, unsigned copied)

    check whether the segment is complete

    :param struct iscsi_tcp_conn \*tcp_conn:
        iscsi tcp connection

    :param struct iscsi_segment \*segment:
        iscsi segment to check

    :param int recv:
        set to one of this is called from the recv path

    :param unsigned copied:
        number of bytes copied

.. _`iscsi_tcp_segment_done.description`:

Description
-----------

Check if we're done receiving this segment. If the receive
buffer is full but we expect more data, move on to the
next entry in the scatterlist.

If the amount of data we received isn't a multiple of 4,
we will transparently receive the pad bytes, too.

This function must be re-entrant.

.. _`iscsi_tcp_segment_recv`:

iscsi_tcp_segment_recv
======================

.. c:function:: int iscsi_tcp_segment_recv(struct iscsi_tcp_conn *tcp_conn, struct iscsi_segment *segment, const void *ptr, unsigned int len)

    copy data to segment

    :param struct iscsi_tcp_conn \*tcp_conn:
        the iSCSI TCP connection

    :param struct iscsi_segment \*segment:
        the buffer to copy to

    :param const void \*ptr:
        data pointer

    :param unsigned int len:
        amount of data available

.. _`iscsi_tcp_segment_recv.description`:

Description
-----------

This function copies up to \ ``len``\  bytes to the
given buffer, and returns the number of bytes
consumed, which can actually be less than \ ``len``\ .

If hash digest is enabled, the function will update the
hash while copying.
Combining these two operations doesn't buy us a lot (yet),
but in the future we could implement combined copy+crc,
just way we do for network layer checksums.

.. _`iscsi_tcp_hdr_recv_prep`:

iscsi_tcp_hdr_recv_prep
=======================

.. c:function:: void iscsi_tcp_hdr_recv_prep(struct iscsi_tcp_conn *tcp_conn)

    prep segment for hdr reception

    :param struct iscsi_tcp_conn \*tcp_conn:
        iscsi connection to prep for

.. _`iscsi_tcp_hdr_recv_prep.description`:

Description
-----------

This function always passes NULL for the hash argument, because when this
function is called we do not yet know the final size of the header and want
to delay the digest processing until we know that.

.. _`iscsi_tcp_cleanup_task`:

iscsi_tcp_cleanup_task
======================

.. c:function:: void iscsi_tcp_cleanup_task(struct iscsi_task *task)

    free tcp_task resources

    :param struct iscsi_task \*task:
        iscsi task

.. _`iscsi_tcp_cleanup_task.description`:

Description
-----------

must be called with session back_lock

.. _`iscsi_tcp_data_in`:

iscsi_tcp_data_in
=================

.. c:function:: int iscsi_tcp_data_in(struct iscsi_conn *conn, struct iscsi_task *task)

    SCSI Data-In Response processing

    :param struct iscsi_conn \*conn:
        iscsi connection

    :param struct iscsi_task \*task:
        scsi command task

.. _`iscsi_tcp_r2t_rsp`:

iscsi_tcp_r2t_rsp
=================

.. c:function:: int iscsi_tcp_r2t_rsp(struct iscsi_conn *conn, struct iscsi_task *task)

    iSCSI R2T Response processing

    :param struct iscsi_conn \*conn:
        iscsi connection

    :param struct iscsi_task \*task:
        scsi command task

.. _`iscsi_tcp_hdr_dissect`:

iscsi_tcp_hdr_dissect
=====================

.. c:function:: int iscsi_tcp_hdr_dissect(struct iscsi_conn *conn, struct iscsi_hdr *hdr)

    process PDU header

    :param struct iscsi_conn \*conn:
        iSCSI connection

    :param struct iscsi_hdr \*hdr:
        PDU header

.. _`iscsi_tcp_hdr_dissect.description`:

Description
-----------

This function analyzes the header of the PDU received,
and performs several sanity checks. If the PDU is accompanied
by data, the receive buffer is set up to copy the incoming data
to the correct location.

.. _`iscsi_tcp_hdr_recv_done`:

iscsi_tcp_hdr_recv_done
=======================

.. c:function:: int iscsi_tcp_hdr_recv_done(struct iscsi_tcp_conn *tcp_conn, struct iscsi_segment *segment)

    process PDU header

    :param struct iscsi_tcp_conn \*tcp_conn:
        iSCSI TCP connection

    :param struct iscsi_segment \*segment:
        the buffer segment being processed

.. _`iscsi_tcp_hdr_recv_done.description`:

Description
-----------

This is the callback invoked when the PDU header has
been received. If the header is followed by additional
header segments, we go back for more data.

.. _`iscsi_tcp_recv_segment_is_hdr`:

iscsi_tcp_recv_segment_is_hdr
=============================

.. c:function:: int iscsi_tcp_recv_segment_is_hdr(struct iscsi_tcp_conn *tcp_conn)

    tests if we are reading in a header

    :param struct iscsi_tcp_conn \*tcp_conn:
        iscsi tcp conn

.. _`iscsi_tcp_recv_segment_is_hdr.description`:

Description
-----------

returns non zero if we are currently processing or setup to process
a header.

.. _`iscsi_tcp_recv_skb`:

iscsi_tcp_recv_skb
==================

.. c:function:: int iscsi_tcp_recv_skb(struct iscsi_conn *conn, struct sk_buff *skb, unsigned int offset, bool offloaded, int *status)

    Process skb

    :param struct iscsi_conn \*conn:
        iscsi connection

    :param struct sk_buff \*skb:
        network buffer with header and/or data segment

    :param unsigned int offset:
        offset in skb

    :param bool offloaded:
        bool indicating if transfer was offloaded

    :param int \*status:
        iscsi TCP status result

.. _`iscsi_tcp_recv_skb.description`:

Description
-----------

Will return status of transfer in \ ``status``\ . And will return
number of bytes copied.

.. _`iscsi_tcp_task_init`:

iscsi_tcp_task_init
===================

.. c:function:: int iscsi_tcp_task_init(struct iscsi_task *task)

    Initialize iSCSI SCSI_READ or SCSI_WRITE commands

    :param struct iscsi_task \*task:
        scsi command task

.. _`iscsi_tcp_task_xmit`:

iscsi_tcp_task_xmit
===================

.. c:function:: int iscsi_tcp_task_xmit(struct iscsi_task *task)

    xmit normal PDU task

    :param struct iscsi_task \*task:
        iscsi command task

.. _`iscsi_tcp_task_xmit.description`:

Description
-----------

We're expected to return 0 when everything was transmitted successfully,
-EAGAIN if there's still data in the queue, or != 0 for any other kind
of error.

.. This file was automatic generated / don't edit.

