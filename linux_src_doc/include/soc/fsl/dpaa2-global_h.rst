.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/soc/fsl/dpaa2-global.h

.. _`dpaa2_dq_flags`:

dpaa2_dq_flags
==============

.. c:function:: u32 dpaa2_dq_flags(const struct dpaa2_dq *dq)

    Get the stat field of dequeue response

    :param dq:
        the dequeue result.
    :type dq: const struct dpaa2_dq \*

.. _`dpaa2_dq_is_pull`:

dpaa2_dq_is_pull
================

.. c:function:: int dpaa2_dq_is_pull(const struct dpaa2_dq *dq)

    Check whether the dq response is from a pull command.

    :param dq:
        the dequeue result
    :type dq: const struct dpaa2_dq \*

.. _`dpaa2_dq_is_pull.description`:

Description
-----------

Return 1 for volatile(pull) dequeue, 0 for static dequeue.

.. _`dpaa2_dq_is_pull_complete`:

dpaa2_dq_is_pull_complete
=========================

.. c:function:: bool dpaa2_dq_is_pull_complete(const struct dpaa2_dq *dq)

    Check whether the pull command is completed.

    :param dq:
        the dequeue result
    :type dq: const struct dpaa2_dq \*

.. _`dpaa2_dq_is_pull_complete.description`:

Description
-----------

Return boolean.

.. _`dpaa2_dq_seqnum`:

dpaa2_dq_seqnum
===============

.. c:function:: u16 dpaa2_dq_seqnum(const struct dpaa2_dq *dq)

    Get the seqnum field in dequeue response

    :param dq:
        the dequeue result
    :type dq: const struct dpaa2_dq \*

.. _`dpaa2_dq_seqnum.description`:

Description
-----------

seqnum is valid only if VALIDFRAME flag is TRUE

Return seqnum.

.. _`dpaa2_dq_odpid`:

dpaa2_dq_odpid
==============

.. c:function:: u16 dpaa2_dq_odpid(const struct dpaa2_dq *dq)

    Get the odpid field in dequeue response

    :param dq:
        the dequeue result
    :type dq: const struct dpaa2_dq \*

.. _`dpaa2_dq_odpid.description`:

Description
-----------

odpid is valid only if ODPVALID flag is TRUE.

Return odpid.

.. _`dpaa2_dq_fqid`:

dpaa2_dq_fqid
=============

.. c:function:: u32 dpaa2_dq_fqid(const struct dpaa2_dq *dq)

    Get the fqid in dequeue response

    :param dq:
        the dequeue result
    :type dq: const struct dpaa2_dq \*

.. _`dpaa2_dq_fqid.description`:

Description
-----------

Return fqid.

.. _`dpaa2_dq_byte_count`:

dpaa2_dq_byte_count
===================

.. c:function:: u32 dpaa2_dq_byte_count(const struct dpaa2_dq *dq)

    Get the byte count in dequeue response

    :param dq:
        the dequeue result
    :type dq: const struct dpaa2_dq \*

.. _`dpaa2_dq_byte_count.description`:

Description
-----------

Return the byte count remaining in the FQ.

.. _`dpaa2_dq_frame_count`:

dpaa2_dq_frame_count
====================

.. c:function:: u32 dpaa2_dq_frame_count(const struct dpaa2_dq *dq)

    Get the frame count in dequeue response

    :param dq:
        the dequeue result
    :type dq: const struct dpaa2_dq \*

.. _`dpaa2_dq_frame_count.description`:

Description
-----------

Return the frame count remaining in the FQ.

.. _`dpaa2_dq_fqd_ctx`:

dpaa2_dq_fqd_ctx
================

.. c:function:: u64 dpaa2_dq_fqd_ctx(const struct dpaa2_dq *dq)

    Get the frame queue context in dequeue response

    :param dq:
        the dequeue result
    :type dq: const struct dpaa2_dq \*

.. _`dpaa2_dq_fqd_ctx.description`:

Description
-----------

Return the frame queue context.

.. _`dpaa2_dq_fd`:

dpaa2_dq_fd
===========

.. c:function:: const struct dpaa2_fd *dpaa2_dq_fd(const struct dpaa2_dq *dq)

    Get the frame descriptor in dequeue response

    :param dq:
        the dequeue result
    :type dq: const struct dpaa2_dq \*

.. _`dpaa2_dq_fd.description`:

Description
-----------

Return the frame descriptor.

.. _`dpaa2_cscn_state_congested`:

dpaa2_cscn_state_congested
==========================

.. c:function:: bool dpaa2_cscn_state_congested(struct dpaa2_dq *cscn)

    Check congestion state

    :param cscn:
        congestion SCN (delivered to WQ or memory)
    :type cscn: struct dpaa2_dq \*

.. This file was automatic generated / don't edit.

