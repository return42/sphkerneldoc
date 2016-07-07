.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aacraid/commsup.c

.. _`fib_map_alloc`:

fib_map_alloc
=============

.. c:function:: int fib_map_alloc(struct aac_dev *dev)

    allocate the fib objects

    :param struct aac_dev \*dev:
        Adapter to allocate for

.. _`fib_map_alloc.description`:

Description
-----------

Allocate and map the shared PCI space for the FIB blocks used to
talk to the Adaptec firmware.

.. _`aac_fib_map_free`:

aac_fib_map_free
================

.. c:function:: void aac_fib_map_free(struct aac_dev *dev)

    free the fib objects

    :param struct aac_dev \*dev:
        Adapter to free

.. _`aac_fib_map_free.description`:

Description
-----------

Free the PCI mappings and the memory allocated for FIB blocks
on this adapter.

.. _`aac_fib_setup`:

aac_fib_setup
=============

.. c:function:: int aac_fib_setup(struct aac_dev *dev)

    setup the fibs

    :param struct aac_dev \*dev:
        Adapter to set up

.. _`aac_fib_setup.description`:

Description
-----------

Allocate the PCI space for the fibs, map it and then initialise the
fib area, the unmapped fib data and also the free list

.. _`aac_fib_alloc_tag`:

aac_fib_alloc_tag
=================

.. c:function:: struct fib *aac_fib_alloc_tag(struct aac_dev *dev, struct scsi_cmnd *scmd)

    allocate a fib using tags

    :param struct aac_dev \*dev:
        Adapter to allocate the fib for

    :param struct scsi_cmnd \*scmd:
        *undescribed*

.. _`aac_fib_alloc_tag.description`:

Description
-----------

Allocate a fib from the adapter fib pool using tags
from the blk layer.

.. _`aac_fib_alloc`:

aac_fib_alloc
=============

.. c:function:: struct fib *aac_fib_alloc(struct aac_dev *dev)

    allocate a fib

    :param struct aac_dev \*dev:
        Adapter to allocate the fib for

.. _`aac_fib_alloc.description`:

Description
-----------

Allocate a fib from the adapter fib pool. If the pool is empty we
return NULL.

.. _`aac_fib_free`:

aac_fib_free
============

.. c:function:: void aac_fib_free(struct fib *fibptr)

    free a fib

    :param struct fib \*fibptr:
        fib to free up

.. _`aac_fib_free.description`:

Description
-----------

Frees up a fib and places it on the appropriate queue

.. _`aac_fib_init`:

aac_fib_init
============

.. c:function:: void aac_fib_init(struct fib *fibptr)

    initialise a fib

    :param struct fib \*fibptr:
        The fib to initialize

.. _`aac_fib_init.description`:

Description
-----------

Set up the generic fib fields ready for use

.. _`fib_dealloc`:

fib_dealloc
===========

.. c:function:: void fib_dealloc(struct fib *fibptr)

    deallocate a fib

    :param struct fib \*fibptr:
        fib to deallocate

.. _`fib_dealloc.description`:

Description
-----------

Will deallocate and return to the free pool the FIB pointed to by the
caller.

.. _`aac_get_entry`:

aac_get_entry
=============

.. c:function:: int aac_get_entry(struct aac_dev *dev, u32 qid, struct aac_entry **entry, u32 *index, unsigned long *nonotify)

    get a queue entry

    :param struct aac_dev \*dev:
        Adapter

    :param u32 qid:
        Queue Number

    :param struct aac_entry \*\*entry:
        Entry return

    :param u32 \*index:
        Index return

    :param unsigned long \*nonotify:
        notification control

.. _`aac_get_entry.description`:

Description
-----------

With a priority the routine returns a queue entry if the queue has free entries. If the queue
is full(no free entries) than no entry is returned and the function returns 0 otherwise 1 is
returned.

.. _`aac_queue_get`:

aac_queue_get
=============

.. c:function:: int aac_queue_get(struct aac_dev *dev, u32 *index, u32 qid, struct hw_fib *hw_fib, int wait, struct fib *fibptr, unsigned long *nonotify)

    get the next free QE

    :param struct aac_dev \*dev:
        Adapter

    :param u32 \*index:
        Returned index

    :param u32 qid:
        *undescribed*

    :param struct hw_fib \*hw_fib:
        *undescribed*

    :param int wait:
        Wait if queue full

    :param struct fib \*fibptr:
        Driver fib object to go with fib

    :param unsigned long \*nonotify:
        Don't notify the adapter

.. _`aac_queue_get.description`:

Description
-----------

Gets the next free QE off the requested priorty adapter command
queue and associates the Fib with the QE. The QE represented by
index is ready to insert on the queue when this routine returns
success.

.. _`aac_fib_send`:

aac_fib_send
============

.. c:function:: int aac_fib_send(u16 command, struct fib *fibptr, unsigned long size, int priority, int wait, int reply, fib_callback callback, void *callback_data)

    send a fib to the adapter

    :param u16 command:
        Command to send

    :param struct fib \*fibptr:
        The fib

    :param unsigned long size:
        Size of fib data area

    :param int priority:
        Priority of Fib

    :param int wait:
        Async/sync select

    :param int reply:
        True if a reply is wanted

    :param fib_callback callback:
        Called with reply

    :param void \*callback_data:
        Passed to callback

.. _`aac_fib_send.description`:

Description
-----------

Sends the requested FIB to the adapter and optionally will wait for a
response FIB. If the caller does not wish to wait for a response than
an event to wait on must be supplied. This event will be set when a
response FIB is received from the adapter.

.. _`aac_consumer_get`:

aac_consumer_get
================

.. c:function:: int aac_consumer_get(struct aac_dev *dev, struct aac_queue *q, struct aac_entry **entry)

    get the top of the queue

    :param struct aac_dev \*dev:
        Adapter

    :param struct aac_queue \*q:
        Queue

    :param struct aac_entry \*\*entry:
        Return entry

.. _`aac_consumer_get.description`:

Description
-----------

Will return a pointer to the entry on the top of the queue requested that
we are a consumer of, and return the address of the queue entry. It does
not change the state of the queue.

.. _`aac_consumer_free`:

aac_consumer_free
=================

.. c:function:: void aac_consumer_free(struct aac_dev *dev, struct aac_queue *q, u32 qid)

    free consumer entry

    :param struct aac_dev \*dev:
        Adapter

    :param struct aac_queue \*q:
        Queue

    :param u32 qid:
        Queue ident

.. _`aac_consumer_free.description`:

Description
-----------

Frees up the current top of the queue we are a consumer of. If the
queue was full notify the producer that the queue is no longer full.

.. _`aac_fib_adapter_complete`:

aac_fib_adapter_complete
========================

.. c:function:: int aac_fib_adapter_complete(struct fib *fibptr, unsigned short size)

    complete adapter issued fib

    :param struct fib \*fibptr:
        fib to complete

    :param unsigned short size:
        size of fib

.. _`aac_fib_adapter_complete.description`:

Description
-----------

Will do all necessary work to complete a FIB that was sent from
the adapter.

.. _`aac_fib_complete`:

aac_fib_complete
================

.. c:function:: int aac_fib_complete(struct fib *fibptr)

    fib completion handler

    :param struct fib \*fibptr:
        *undescribed*

.. _`aac_fib_complete.description`:

Description
-----------

Will do all necessary work to complete a FIB.

.. _`aac_printf`:

aac_printf
==========

.. c:function:: void aac_printf(struct aac_dev *dev, u32 val)

    handle printf from firmware

    :param struct aac_dev \*dev:
        Adapter

    :param u32 val:
        Message info

.. _`aac_printf.description`:

Description
-----------

Print a message passed to us by the controller firmware on the
Adaptec board

.. _`aif_sniff_timeout`:

AIF_SNIFF_TIMEOUT
=================

.. c:function::  AIF_SNIFF_TIMEOUT()

    Handle a message from the firmware

.. _`aif_sniff_timeout.description`:

Description
-----------

This routine handles a driver notify fib from the adapter and
dispatches it to the appropriate routine for handling.

.. _`aac_command_thread`:

aac_command_thread
==================

.. c:function:: int aac_command_thread(void *data)

    command processing thread

    :param void \*data:
        *undescribed*

.. _`aac_command_thread.description`:

Description
-----------

Waits on the commandready event in it's queue. When the event gets set
it will pull FIBs off it's queue. It will continue to pull FIBs off
until the queue is empty. When the queue is empty it will wait for
more FIBs.

.. This file was automatic generated / don't edit.

