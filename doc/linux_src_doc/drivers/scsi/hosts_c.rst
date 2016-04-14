.. -*- coding: utf-8; mode: rst -*-

=======
hosts.c
=======

.. _`scsi_host_set_state`:

scsi_host_set_state
===================

.. c:function:: int scsi_host_set_state (struct Scsi_Host *shost, enum scsi_host_state state)

    Take the given host through the host state model.

    :param struct Scsi_Host \*shost:
        scsi host to change the state of.

    :param enum scsi_host_state state:
        state to change to.


.. _`scsi_host_set_state.description`:

Description
-----------

Returns zero if unsuccessful or an error if the requested
transition is illegal.


.. _`scsi_remove_host`:

scsi_remove_host
================

.. c:function:: void scsi_remove_host (struct Scsi_Host *shost)

    remove a scsi host

    :param struct Scsi_Host \*shost:
        a pointer to a scsi host to remove


.. _`scsi_add_host_with_dma`:

scsi_add_host_with_dma
======================

.. c:function:: int scsi_add_host_with_dma (struct Scsi_Host *shost, struct device *dev, struct device *dma_dev)

    add a scsi host with dma device

    :param struct Scsi_Host \*shost:
        scsi host pointer to add

    :param struct device \*dev:
        a struct device of type scsi class

    :param struct device \*dma_dev:
        dma device for the host


.. _`scsi_add_host_with_dma.description`:

Description
-----------

Note: You rarely need to worry about this unless you're in a
virtualised host environments, so use the simpler :c:func:`scsi_add_host`
function instead.

Return value: 
0 on success / != 0 for error


.. _`scsi_host_alloc`:

scsi_host_alloc
===============

.. c:function:: struct Scsi_Host *scsi_host_alloc (struct scsi_host_template *sht, int privsize)

    register a scsi host adapter instance.

    :param struct scsi_host_template \*sht:
        pointer to scsi host template

    :param int privsize:
        extra bytes to allocate for driver


.. _`scsi_host_alloc.description`:

Description
-----------

Note::

        Allocate a new Scsi_Host and perform basic initialization.
        The host is not published to the scsi midlayer until scsi_add_host
        is called.

Return value::

        Pointer to a new Scsi_Host


.. _`scsi_host_lookup`:

scsi_host_lookup
================

.. c:function:: struct Scsi_Host *scsi_host_lookup (unsigned short hostnum)

    get a reference to a Scsi_Host by host no

    :param unsigned short hostnum:
        host number to locate


.. _`scsi_host_lookup.description`:

Description
-----------

Return value::

        A pointer to located Scsi_Host or NULL.

        The caller must do a :c:func:`scsi_host_put` to drop the reference
        that :c:func:`scsi_host_get` took. The :c:func:`put_device` below dropped
        the reference from :c:func:`class_find_device`.


.. _`scsi_host_get`:

scsi_host_get
=============

.. c:function:: struct Scsi_Host *scsi_host_get (struct Scsi_Host *shost)

    inc a Scsi_Host ref count

    :param struct Scsi_Host \*shost:
        Pointer to Scsi_Host to inc.


.. _`scsi_host_put`:

scsi_host_put
=============

.. c:function:: void scsi_host_put (struct Scsi_Host *shost)

    dec a Scsi_Host ref count

    :param struct Scsi_Host \*shost:
        Pointer to Scsi_Host to dec.


.. _`scsi_queue_work`:

scsi_queue_work
===============

.. c:function:: int scsi_queue_work (struct Scsi_Host *shost, struct work_struct *work)

    Queue work to the Scsi_Host workqueue.

    :param struct Scsi_Host \*shost:
        Pointer to Scsi_Host.

    :param struct work_struct \*work:
        Work to queue for execution.


.. _`scsi_queue_work.description`:

Description
-----------

Return value::

        1 - work queued for execution
        0 - work is already queued
        -EINVAL - work queue doesn't exist


.. _`scsi_flush_work`:

scsi_flush_work
===============

.. c:function:: void scsi_flush_work (struct Scsi_Host *shost)

    Flush a Scsi_Host's workqueue.

    :param struct Scsi_Host \*shost:
        Pointer to Scsi_Host.

