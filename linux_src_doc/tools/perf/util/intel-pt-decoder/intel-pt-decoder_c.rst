.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/intel-pt-decoder/intel-pt-decoder.c

.. _`intel_pt_next_psb`:

intel_pt_next_psb
=================

.. c:function:: bool intel_pt_next_psb(unsigned char **buf, size_t *len)

    move buffer pointer to the start of the next PSB packet.

    :param unsigned char \*\*buf:
        pointer to buffer pointer

    :param size_t \*len:
        size of buffer

.. _`intel_pt_next_psb.description`:

Description
-----------

Updates the buffer pointer to point to the start of the next PSB packet if
there is one, otherwise the buffer pointer is unchanged.  If \ ``buf``\  is updated,
\ ``len``\  is adjusted accordingly.

.. _`intel_pt_next_psb.return`:

Return
------

%true if a PSB packet is found, \ ``false``\  otherwise.

.. _`intel_pt_step_psb`:

intel_pt_step_psb
=================

.. c:function:: bool intel_pt_step_psb(unsigned char **buf, size_t *len)

    move buffer pointer to the start of the following PSB packet.

    :param unsigned char \*\*buf:
        pointer to buffer pointer

    :param size_t \*len:
        size of buffer

.. _`intel_pt_step_psb.description`:

Description
-----------

Updates the buffer pointer to point to the start of the following PSB packet
(skipping the PSB at \ ``buf``\  itself) if there is one, otherwise the buffer
pointer is unchanged.  If \ ``buf``\  is updated, \ ``len``\  is adjusted accordingly.

.. _`intel_pt_step_psb.return`:

Return
------

%true if a PSB packet is found, \ ``false``\  otherwise.

.. _`intel_pt_last_psb`:

intel_pt_last_psb
=================

.. c:function:: unsigned char *intel_pt_last_psb(unsigned char *buf, size_t len)

    find the last PSB packet in a buffer.

    :param unsigned char \*buf:
        buffer

    :param size_t len:
        size of buffer

.. _`intel_pt_last_psb.description`:

Description
-----------

This function finds the last PSB in a buffer.

.. _`intel_pt_last_psb.return`:

Return
------

A pointer to the last PSB in \ ``buf``\  if found, \ ``NULL``\  otherwise.

.. _`intel_pt_next_tsc`:

intel_pt_next_tsc
=================

.. c:function:: bool intel_pt_next_tsc(unsigned char *buf, size_t len, uint64_t *tsc)

    find and return next TSC.

    :param unsigned char \*buf:
        buffer

    :param size_t len:
        size of buffer

    :param uint64_t \*tsc:
        TSC value returned

.. _`intel_pt_next_tsc.description`:

Description
-----------

Find a TSC packet in \ ``buf``\  and return the TSC value.  This function assumes
that \ ``buf``\  starts at a PSB and that PSB+ will contain TSC and so stops if a
PSBEND packet is found.

.. _`intel_pt_next_tsc.return`:

Return
------

%true if TSC is found, false otherwise.

.. _`intel_pt_tsc_cmp`:

intel_pt_tsc_cmp
================

.. c:function:: int intel_pt_tsc_cmp(uint64_t tsc1, uint64_t tsc2)

    compare 7-byte TSCs.

    :param uint64_t tsc1:
        first TSC to compare

    :param uint64_t tsc2:
        second TSC to compare

.. _`intel_pt_tsc_cmp.description`:

Description
-----------

This function compares 7-byte TSC values allowing for the possibility that
TSC wrapped around.  Generally it is not possible to know if TSC has wrapped
around so for that purpose this function assumes the absolute difference is
less than half the maximum difference.

.. _`intel_pt_tsc_cmp.return`:

Return
------

%-1 if \ ``tsc1``\  is before \ ``tsc2``\ , \ ``0``\  if \ ``tsc1``\  == \ ``tsc2``\ , \ ``1``\  if \ ``tsc1``\  is
after \ ``tsc2``\ .

.. _`intel_pt_find_overlap_tsc`:

intel_pt_find_overlap_tsc
=========================

.. c:function:: unsigned char *intel_pt_find_overlap_tsc(unsigned char *buf_a, size_t len_a, unsigned char *buf_b, size_t len_b)

    determine start of non-overlapped trace data using TSC.

    :param unsigned char \*buf_a:
        first buffer

    :param size_t len_a:
        size of first buffer

    :param unsigned char \*buf_b:
        second buffer

    :param size_t len_b:
        size of second buffer

.. _`intel_pt_find_overlap_tsc.description`:

Description
-----------

If the trace contains TSC we can look at the last TSC of \ ``buf_a``\  and the
first TSC of \ ``buf_b``\  in order to determine if the buffers overlap, and then
walk forward in \ ``buf_b``\  until a later TSC is found.  A precondition is that
\ ``buf_a``\  and \ ``buf_b``\  are positioned at a PSB.

.. _`intel_pt_find_overlap_tsc.return`:

Return
------

A pointer into \ ``buf_b``\  from where non-overlapped data starts, or
\ ``buf_b``\  + \ ``len_b``\  if there is no non-overlapped data.

.. _`intel_pt_find_overlap`:

intel_pt_find_overlap
=====================

.. c:function:: unsigned char *intel_pt_find_overlap(unsigned char *buf_a, size_t len_a, unsigned char *buf_b, size_t len_b, bool have_tsc)

    determine start of non-overlapped trace data.

    :param unsigned char \*buf_a:
        first buffer

    :param size_t len_a:
        size of first buffer

    :param unsigned char \*buf_b:
        second buffer

    :param size_t len_b:
        size of second buffer

    :param bool have_tsc:
        can use TSC packets to detect overlap

.. _`intel_pt_find_overlap.description`:

Description
-----------

When trace samples or snapshots are recorded there is the possibility that
the data overlaps.  Note that, for the purposes of decoding, data is only
useful if it begins with a PSB packet.

.. _`intel_pt_find_overlap.return`:

Return
------

A pointer into \ ``buf_b``\  from where non-overlapped data starts, or
\ ``buf_b``\  + \ ``len_b``\  if there is no non-overlapped data.

.. This file was automatic generated / don't edit.

