.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lnet/lnet/lib-me.c

.. _`lnetmeattach`:

LNetMEAttach
============

.. c:function:: int LNetMEAttach(unsigned int portal, struct lnet_process_id match_id, __u64 match_bits, __u64 ignore_bits, enum lnet_unlink unlink, enum lnet_ins_pos pos, struct lnet_handle_me *handle)

    ME is empty, i.e. not associated with a memory descriptor. \ :c:func:`LNetMDAttach`\  can be used to attach a MD to an empty ME.

    :param unsigned int portal:
        *undescribed*

    :param struct lnet_process_id match_id:
        *undescribed*

    :param __u64 match_bits:
        *undescribed*

    :param __u64 ignore_bits:
        *undescribed*

    :param enum lnet_unlink unlink:
        *undescribed*

    :param enum lnet_ins_pos pos:
        *undescribed*

    :param struct lnet_handle_me \*handle:
        *undescribed*

.. _`lnetmeattach.description`:

Description
-----------

\param portal The portal table index where the ME should be attached.
\param match_id Specifies the match criteria for the process ID of
the requester. The constants LNET_PID_ANY and LNET_NID_ANY can be
used to wildcard either of the identifiers in the lnet_process_id
structure.
\param match_bits,ignore_bits Specify the match criteria to apply
to the match bits in the incoming request. The ignore bits are used
to mask out insignificant bits in the incoming match bits. The resulting
bits are then compared to the ME's match bits to determine if the
incoming request meets the match criteria.
\param unlink Indicates whether the ME should be unlinked when the memory
descriptor associated with it is unlinked (Note that the check for
unlinking a ME only occurs when the memory descriptor is unlinked.).
Valid values are LNET_RETAIN and LNET_UNLINK.
\param pos Indicates whether the new ME should be prepended or
appended to the match list. Allowed constants: LNET_INS_BEFORE,
LNET_INS_AFTER.
\param handle On successful returns, a handle to the newly created ME
object is saved here. This handle can be used later in \ :c:func:`LNetMEInsert`\ ,
\ :c:func:`LNetMEUnlink`\ , or \ :c:func:`LNetMDAttach`\  functions.

\retval 0       On success.
\retval -EINVAL If \a portal is invalid.
\retval -ENOMEM If new ME object cannot be allocated.

.. _`lnetmeinsert`:

LNetMEInsert
============

.. c:function:: int LNetMEInsert(struct lnet_handle_me current_meh, struct lnet_process_id match_id, __u64 match_bits, __u64 ignore_bits, enum lnet_unlink unlink, enum lnet_ins_pos pos, struct lnet_handle_me *handle)

    \a current_meh. The new ME is empty, i.e. not associated with a memory descriptor. \ :c:func:`LNetMDAttach`\  can be used to attach a MD to an empty ME.

    :param struct lnet_handle_me current_meh:
        *undescribed*

    :param struct lnet_process_id match_id:
        *undescribed*

    :param __u64 match_bits:
        *undescribed*

    :param __u64 ignore_bits:
        *undescribed*

    :param enum lnet_unlink unlink:
        *undescribed*

    :param enum lnet_ins_pos pos:
        *undescribed*

    :param struct lnet_handle_me \*handle:
        *undescribed*

.. _`lnetmeinsert.description`:

Description
-----------

This function is identical to \ :c:func:`LNetMEAttach`\  except for the position
where the new ME is inserted.

\param current_meh A handle for a ME. The new ME will be inserted
immediately before or immediately after this ME.
\param match_id,match_bits,ignore_bits,unlink,pos,handle See the discussion
for \ :c:func:`LNetMEAttach`\ .

\retval 0       On success.
\retval -ENOMEM If new ME object cannot be allocated.
\retval -ENOENT If \a current_meh does not point to a valid match entry.

.. _`lnetmeunlink`:

LNetMEUnlink
============

.. c:function:: int LNetMEUnlink(struct lnet_handle_me meh)

    :param struct lnet_handle_me meh:
        *undescribed*

.. _`lnetmeunlink.description`:

Description
-----------

This operation also releases any resources associated with the ME. If a
memory descriptor is attached to the ME, then it will be unlinked as well
and an unlink event will be generated. It is an error to use the ME handle
after calling \ :c:func:`LNetMEUnlink`\ .

\param meh A handle for the ME to be unlinked.

\retval 0       On success.
\retval -ENOENT If \a meh does not point to a valid ME.
\see \ :c:func:`LNetMDUnlink`\  for the discussion on delivering unlink event.

.. This file was automatic generated / don't edit.

