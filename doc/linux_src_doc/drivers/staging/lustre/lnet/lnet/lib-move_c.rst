.. -*- coding: utf-8; mode: rst -*-

==========
lib-move.c
==========


.. _`lnetput`:

LNetPut
=======

.. c:function:: int LNetPut (lnet_nid_t self, lnet_handle_md_t mdh, lnet_ack_req_t ack, lnet_process_id_t target, unsigned int portal, __u64 match_bits, unsigned int offset, __u64 hdr_data)

    :param lnet_nid_t self:

        *undescribed*

    :param lnet_handle_md_t mdh:

        *undescribed*

    :param lnet_ack_req_t ack:

        *undescribed*

    :param lnet_process_id_t target:

        *undescribed*

    :param unsigned int portal:

        *undescribed*

    :param __u64 match_bits:

        *undescribed*

    :param unsigned int offset:

        *undescribed*

    :param __u64 hdr_data:

        *undescribed*



.. _`lnetput.there-are-several-events-associated-with-a-put`:

There are several events associated with a PUT
----------------------------------------------

completion of the send on
the initiator node (LNET_EVENT_SEND), and when the send completes
successfully, the receipt of an acknowledgment (LNET_EVENT_ACK) indicating
that the operation was accepted by the target. The event LNET_EVENT_PUT is
used at the target node to indicate the completion of incoming data
delivery.

The local events will be logged in the EQ associated with the MD pointed to
by \a mdh handle. Using a MD without an associated EQ results in these
events being discarded. In this case, the caller must have another
mechanism (e.g., a higher level protocol) for determining when it is safe
to modify the memory region associated with the MD.

Note that LNet does not guarantee the order of LNET_EVENT_SEND and
LNET_EVENT_ACK, though intuitively ACK should happen after SEND.

\param self Indicates the NID of a local interface through which to send
the PUT request. Use LNET_NID_ANY to let LNet choose one by itself.
\param mdh A handle for the MD that describes the memory to be sent. The MD
must be "free floating" (See :c:func:`LNetMDBind`).
\param ack Controls whether an acknowledgment is requested.
Acknowledgments are only sent when they are requested by the initiating
process and the target MD enables them.
\param target A process identifier for the target process.
\param portal The index in the \a target's portal table.
\param match_bits The match bits to use for MD selection at the target
process.
\param offset The offset into the target MD (only used when the target
MD has the LNET_MD_MANAGE_REMOTE option set).
\param hdr_data 64 bits of user data that can be included in the message
header. This data is written to an event queue entry at the target if an
EQ is present on the matching MD.

\retval  0      Success, and only in this case events will be generated
and logged to EQ (if it exists).
\retval -EIO    Simulated failure.
\retval -ENOMEM Memory allocation failure.
\retval -ENOENT Invalid MD object.

\see lnet_event_t::hdr_data and lnet_event_kind_t.



.. _`lnetget`:

LNetGet
=======

.. c:function:: int LNetGet (lnet_nid_t self, lnet_handle_md_t mdh, lnet_process_id_t target, unsigned int portal, __u64 match_bits, unsigned int offset)

    :param lnet_nid_t self:

        *undescribed*

    :param lnet_handle_md_t mdh:

        *undescribed*

    :param lnet_process_id_t target:

        *undescribed*

    :param unsigned int portal:

        *undescribed*

    :param __u64 match_bits:

        *undescribed*

    :param unsigned int offset:

        *undescribed*



.. _`lnetget.description`:

Description
-----------


On the initiator node, an LNET_EVENT_SEND is logged when the GET request
is sent, and an LNET_EVENT_REPLY is logged when the data returned from
the target node in the REPLY has been written to local MD.

On the target node, an LNET_EVENT_GET is logged when the GET request
arrives and is accepted into a MD.

\param self,target,portal,match_bits,offset See the discussion in :c:func:`LNetPut`.
\param mdh A handle for the MD that describes the memory into which the
requested data will be received. The MD must be "free floating"
(See :c:func:`LNetMDBind`).

\retval  0      Success, and only in this case events will be generated
and logged to EQ (if it exists) of the MD.
\retval -EIO    Simulated failure.
\retval -ENOMEM Memory allocation failure.
\retval -ENOENT Invalid MD object.



.. _`lnetdist`:

LNetDist
========

.. c:function:: int LNetDist (lnet_nid_t dstnid, lnet_nid_t *srcnidp, __u32 *orderp)

    :param lnet_nid_t dstnid:

        *undescribed*

    :param lnet_nid_t \*srcnidp:

        *undescribed*

    :param __u32 \*orderp:

        *undescribed*



.. _`lnetdist.description`:

Description
-----------


\param dstnid Target NID.
\param srcnidp If not NULL, NID of the local interface to reach \a dstnid
is saved here.
\param orderp If not NULL, order of the route to reach \a dstnid is saved
here.

\retval 0 If \a dstnid belongs to a local interface, and reserved option
local_nid_dist_zero is set, which is the default.
\retval positives Distance to target NID, i.e. number of hops plus one.
\retval -EHOSTUNREACH If \a dstnid is not reachable.

