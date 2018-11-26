.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/hosts.c

.. _`scsi_host_set_state`:

scsi_host_set_state
===================

.. c:function:: int scsi_host_set_state(struct Scsi_Host *shost, enum scsi_host_state state)

    Take the given host through the host state model.

    :param shost:
        scsi host to change the state of.
    :type shost: struct Scsi_Host \*

    :param state:
        state to change to.
    :type state: enum scsi_host_state

.. _`scsi_host_set_state.description`:

Description
-----------

     Returns zero if unsuccessful or an error if the requested
     transition is illegal.

.. _`scsi_remove_host`:

scsi_remove_host
================

.. c:function:: void scsi_remove_host(struct Scsi_Host *shost)

    remove a scsi host

    :param shost:
        a pointer to a scsi host to remove
    :type shost: struct Scsi_Host \*

.. _`scsi_add_host_with_dma`:

scsi_add_host_with_dma
======================

.. c:function:: int scsi_add_host_with_dma(struct Scsi_Host *shost, struct device *dev, struct device *dma_dev)

    add a scsi host with dma device

    :param shost:
        scsi host pointer to add
    :type shost: struct Scsi_Host \*

    :param dev:
        a struct device of type scsi class
    :type dev: struct device \*

    :param dma_dev:
        dma device for the host
    :type dma_dev: struct device \*

.. _`scsi_add_host_with_dma.note`:

Note
----

You rarely need to worry about this unless you're in a
virtualised host environments, so use the simpler \ :c:func:`scsi_add_host`\ 
function instead.

.. _`scsi_add_host_with_dma.return-value`:

Return value
------------

     0 on success / != 0 for error

.. _`scsi_host_alloc`:

scsi_host_alloc
===============

.. c:function:: struct Scsi_Host *scsi_host_alloc(struct scsi_host_template *sht, int privsize)

    register a scsi host adapter instance.

    :param sht:
        pointer to scsi host template
    :type sht: struct scsi_host_template \*

    :param privsize:
        extra bytes to allocate for driver
    :type privsize: int

.. _`scsi_host_alloc.note`:

Note
----

     Allocate a new Scsi_Host and perform basic initialization.
     The host is not published to the scsi midlayer until scsi_add_host
     is called.

.. _`scsi_host_alloc.return-value`:

Return value
------------

     Pointer to a new Scsi_Host

.. _`scsi_host_lookup`:

scsi_host_lookup
================

.. c:function:: struct Scsi_Host *scsi_host_lookup(unsigned short hostnum)

    get a reference to a Scsi_Host by host no

    :param hostnum:
        host number to locate
    :type hostnum: unsigned short

.. _`scsi_host_lookup.return-value`:

Return value
------------

     A pointer to located Scsi_Host or NULL.

     The caller must do a \ :c:func:`scsi_host_put`\  to drop the reference
     that \ :c:func:`scsi_host_get`\  took. The \ :c:func:`put_device`\  below dropped
     the reference from \ :c:func:`class_find_device`\ .

.. _`scsi_host_get`:

scsi_host_get
=============

.. c:function:: struct Scsi_Host *scsi_host_get(struct Scsi_Host *shost)

    inc a Scsi_Host ref count

    :param shost:
        Pointer to Scsi_Host to inc.
    :type shost: struct Scsi_Host \*

.. _`scsi_host_busy`:

scsi_host_busy
==============

.. c:function:: int scsi_host_busy(struct Scsi_Host *shost)

    Return the host busy counter

    :param shost:
        Pointer to Scsi_Host to inc.
    :type shost: struct Scsi_Host \*

.. _`scsi_host_put`:

scsi_host_put
=============

.. c:function:: void scsi_host_put(struct Scsi_Host *shost)

    dec a Scsi_Host ref count

    :param shost:
        Pointer to Scsi_Host to dec.
    :type shost: struct Scsi_Host \*

.. _`scsi_queue_work`:

scsi_queue_work
===============

.. c:function:: int scsi_queue_work(struct Scsi_Host *shost, struct work_struct *work)

    Queue work to the Scsi_Host workqueue.

    :param shost:
        Pointer to Scsi_Host.
    :type shost: struct Scsi_Host \*

    :param work:
        Work to queue for execution.
    :type work: struct work_struct \*

.. _`scsi_queue_work.return-value`:

Return value
------------

     1 - work queued for execution
     0 - work is already queued
     -EINVAL - work queue doesn't exist

.. _`scsi_flush_work`:

scsi_flush_work
===============

.. c:function:: void scsi_flush_work(struct Scsi_Host *shost)

    Flush a Scsi_Host's workqueue.

    :param shost:
        Pointer to Scsi_Host.
    :type shost: struct Scsi_Host \*

.. This file was automatic generated / don't edit.

