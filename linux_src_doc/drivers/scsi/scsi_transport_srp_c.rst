.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi_transport_srp.c

.. _`srp_tmo_valid`:

srp_tmo_valid
=============

.. c:function:: int srp_tmo_valid(int reconnect_delay, int fast_io_fail_tmo, int dev_loss_tmo)

    check timeout combination validity

    :param int reconnect_delay:
        Reconnect delay in seconds.

    :param int fast_io_fail_tmo:
        Fast I/O fail timeout in seconds.

    :param int dev_loss_tmo:
        Device loss timeout in seconds.

.. _`srp_tmo_valid.description`:

Description
-----------

The combination of the timeout parameters must be such that SCSI commands
are finished in a reasonable time. Hence do not allow the fast I/O fail
timeout to exceed SCSI_DEVICE_BLOCK_MAX_TIMEOUT nor allow dev_loss_tmo to
exceed that limit if failing I/O fast has been disabled. Furthermore, these
parameters must be such that multipath can detect failed paths timely.
Hence do not allow all three parameters to be disabled simultaneously.

.. _`srp_reconnect_work`:

srp_reconnect_work
==================

.. c:function:: void srp_reconnect_work(struct work_struct *work)

    reconnect and schedule a new attempt if necessary

    :param struct work_struct \*work:
        Work structure used for scheduling this operation.

.. _`rport_fast_io_fail_timedout`:

rport_fast_io_fail_timedout
===========================

.. c:function:: void rport_fast_io_fail_timedout(struct work_struct *work)

    fast I/O failure timeout handler

    :param struct work_struct \*work:
        Work structure used for scheduling this operation.

.. _`rport_dev_loss_timedout`:

rport_dev_loss_timedout
=======================

.. c:function:: void rport_dev_loss_timedout(struct work_struct *work)

    device loss timeout handler

    :param struct work_struct \*work:
        Work structure used for scheduling this operation.

.. _`srp_start_tl_fail_timers`:

srp_start_tl_fail_timers
========================

.. c:function:: void srp_start_tl_fail_timers(struct srp_rport *rport)

    start the transport layer failure timers

    :param struct srp_rport \*rport:
        SRP target port.

.. _`srp_start_tl_fail_timers.description`:

Description
-----------

Start the transport layer fast I/O failure and device loss timers. Do not
modify a timer that was already started.

.. _`srp_reconnect_rport`:

srp_reconnect_rport
===================

.. c:function:: int srp_reconnect_rport(struct srp_rport *rport)

    reconnect to an SRP target port

    :param struct srp_rport \*rport:
        SRP target port.

.. _`srp_reconnect_rport.description`:

Description
-----------

Blocks SCSI command queueing before invoking \ :c:func:`reconnect`\  such that
\ :c:func:`queuecommand`\  won't be invoked concurrently with \ :c:func:`reconnect`\  from outside
the SCSI EH. This is important since a \ :c:func:`reconnect`\  implementation may
reallocate resources needed by \ :c:func:`queuecommand`\ .

.. _`srp_reconnect_rport.notes`:

Notes
-----

- This function neither waits until outstanding requests have finished nor
tries to abort these. It is the responsibility of the \ :c:func:`reconnect`\ 
function to finish outstanding commands before reconnecting to the target
port.
- It is the responsibility of the caller to ensure that the resources
reallocated by the \ :c:func:`reconnect`\  function won't be used while this function
is in progress. One possible strategy is to invoke this function from
the context of the SCSI EH thread only. Another possible strategy is to
lock the rport mutex inside each SCSI LLD callback that can be invoked by
the SCSI EH (the scsi_host_template.eh\_\*() functions and also the
scsi_host_template.queuecommand() function).

.. _`srp_timed_out`:

srp_timed_out
=============

.. c:function:: enum blk_eh_timer_return srp_timed_out(struct scsi_cmnd *scmd)

    SRP transport intercept of the SCSI timeout EH

    :param struct scsi_cmnd \*scmd:
        SCSI command.

.. _`srp_timed_out.description`:

Description
-----------

If a timeout occurs while an rport is in the blocked state, ask the SCSI
EH to continue waiting (BLK_EH_RESET_TIMER). Otherwise let the SCSI core
handle the timeout (BLK_EH_NOT_HANDLED).

.. _`srp_timed_out.note`:

Note
----

This function is called from soft-IRQ context and with the request
queue lock held.

.. _`srp_rport_get`:

srp_rport_get
=============

.. c:function:: void srp_rport_get(struct srp_rport *rport)

    increment rport reference count

    :param struct srp_rport \*rport:
        SRP target port.

.. _`srp_rport_put`:

srp_rport_put
=============

.. c:function:: void srp_rport_put(struct srp_rport *rport)

    decrement rport reference count

    :param struct srp_rport \*rport:
        SRP target port.

.. _`srp_rport_add`:

srp_rport_add
=============

.. c:function:: struct srp_rport *srp_rport_add(struct Scsi_Host *shost, struct srp_rport_identifiers *ids)

    add a SRP remote port to the device hierarchy

    :param struct Scsi_Host \*shost:
        scsi host the remote port is connected to.

    :param struct srp_rport_identifiers \*ids:
        The port id for the remote port.

.. _`srp_rport_add.description`:

Description
-----------

Publishes a port to the rest of the system.

.. _`srp_rport_del`:

srp_rport_del
=============

.. c:function:: void srp_rport_del(struct srp_rport *rport)

    remove a SRP remote port

    :param struct srp_rport \*rport:
        SRP remote port to remove

.. _`srp_rport_del.description`:

Description
-----------

Removes the specified SRP remote port.

.. _`srp_remove_host`:

srp_remove_host
===============

.. c:function:: void srp_remove_host(struct Scsi_Host *shost)

    tear down a Scsi_Host's SRP data structures

    :param struct Scsi_Host \*shost:
        Scsi Host that is torn down

.. _`srp_remove_host.description`:

Description
-----------

Removes all SRP remote ports for a given Scsi_Host.
Must be called just before scsi_remove_host for SRP HBAs.

.. _`srp_stop_rport_timers`:

srp_stop_rport_timers
=====================

.. c:function:: void srp_stop_rport_timers(struct srp_rport *rport)

    stop the transport layer recovery timers

    :param struct srp_rport \*rport:
        SRP remote port for which to stop the timers.

.. _`srp_stop_rport_timers.description`:

Description
-----------

Must be called after \ :c:func:`srp_remove_host`\  and \ :c:func:`scsi_remove_host`\ . The caller
must hold a reference on the rport (rport->dev) and on the SCSI host
(rport->dev.parent).

.. _`srp_attach_transport`:

srp_attach_transport
====================

.. c:function:: struct scsi_transport_template *srp_attach_transport(struct srp_function_template *ft)

    instantiate SRP transport template

    :param struct srp_function_template \*ft:
        SRP transport class function template

.. _`srp_release_transport`:

srp_release_transport
=====================

.. c:function:: void srp_release_transport(struct scsi_transport_template *t)

    release SRP transport template instance

    :param struct scsi_transport_template \*t:
        transport template instance

.. This file was automatic generated / don't edit.

