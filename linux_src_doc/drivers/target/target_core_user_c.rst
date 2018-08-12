.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/target/target_core_user.c

.. _`userspace-i-o`:

Userspace I/O
=============

Userspace I/O
-------------

Define a shared-memory interface for LIO to pass SCSI commands and
data to userspace for processing. This is to allow backends that
are too complex for in-kernel support to be possible.

It uses the UIO framework to do a lot of the device-creation and
introspection work for us.

See the .h file for how the ring is laid out. Note that while the
command ring is defined, the particulars of the data area are
not. Offset values in the command entry point to other locations
internal to the mmap-ed area. There is separate space outside the
command ring for data buffers. This leaves maximum flexibility for
moving buffer allocations, or even page flipping or other
allocation techniques, without altering the command ring layout.

SECURITY:
The user process must be assumed to be malicious. There's no way to
prevent it breaking the command ring protocol if it wants, but in
order to prevent other issues we must only ever read *data* from
the shared memory area, not offsets or sizes. This applies to
command ring entries as well as the mailbox. Extra code needed for
this may have a 'UAM' comment.

.. _`queue_cmd_ring`:

queue_cmd_ring
==============

.. c:function:: sense_reason_t queue_cmd_ring(struct tcmu_cmd *tcmu_cmd, int *scsi_err)

    queue cmd to ring or internally

    :param struct tcmu_cmd \*tcmu_cmd:
        cmd to queue

    :param int \*scsi_err:
        TCM error code if failure (-1) returned.

.. _`queue_cmd_ring.return`:

Return
------

-1 we cannot queue internally or to the ring.
 0 success
 1 internally queued to wait for ring memory to free.

.. This file was automatic generated / don't edit.

