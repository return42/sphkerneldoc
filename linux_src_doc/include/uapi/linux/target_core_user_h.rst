.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/target_core_user.h

.. _`ring-design`:

Ring Design
===========

Ring Design
-----------

The mmaped area is divided into three parts:
1) The mailbox (struct tcmu_mailbox, below);
2) The command ring;
3) Everything beyond the command ring (data).

The mailbox tells userspace the offset of the command ring from the
start of the shared memory region, and how big the command ring is.

The kernel passes SCSI commands to userspace by putting a struct
tcmu_cmd_entry in the ring, updating mailbox->cmd_head, and poking
userspace via UIO's interrupt mechanism.

tcmu_cmd_entry contains a header. If the header type is PAD,
userspace should skip hdr->length bytes (mod cmdr_size) to find the
next cmd_entry.

Otherwise, the entry will contain offsets into the mmaped area that
contain the cdb and data buffers -- the latter accessible via the
iov array. iov addresses are also offsets into the shared area.

When userspace is completed handling the command, set
entry->rsp.scsi_status, fill in rsp.sense_buffer if appropriate,
and also set mailbox->cmd_tail equal to the old cmd_tail plus
hdr->length, mod cmdr_size. If cmd_tail doesn't equal cmd_head, it
should process the next packet the same way, and so on.

.. This file was automatic generated / don't edit.

