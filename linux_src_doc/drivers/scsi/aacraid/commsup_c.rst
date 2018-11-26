.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aacraid/commsup.c

.. _`fib_map_alloc`:

fib_map_alloc
=============

.. c:function:: int fib_map_alloc(struct aac_dev *dev)

    allocate the fib objects

    :param dev:
        Adapter to allocate for
    :type dev: struct aac_dev \*

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

    :param dev:
        Adapter to free
    :type dev: struct aac_dev \*

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

    :param dev:
        Adapter to set up
    :type dev: struct aac_dev \*

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

    :param dev:
        Adapter to allocate the fib for
    :type dev: struct aac_dev \*

    :param scmd:
        *undescribed*
    :type scmd: struct scsi_cmnd \*

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

    :param dev:
        Adapter to allocate the fib for
    :type dev: struct aac_dev \*

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

    :param fibptr:
        fib to free up
    :type fibptr: struct fib \*

.. _`aac_fib_free.description`:

Description
-----------

Frees up a fib and places it on the appropriate queue

.. _`aac_fib_init`:

aac_fib_init
============

.. c:function:: void aac_fib_init(struct fib *fibptr)

    initialise a fib

    :param fibptr:
        The fib to initialize
    :type fibptr: struct fib \*

.. _`aac_fib_init.description`:

Description
-----------

Set up the generic fib fields ready for use

.. _`fib_dealloc`:

fib_dealloc
===========

.. c:function:: void fib_dealloc(struct fib *fibptr)

    deallocate a fib

    :param fibptr:
        fib to deallocate
    :type fibptr: struct fib \*

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

    :param dev:
        Adapter
    :type dev: struct aac_dev \*

    :param qid:
        Queue Number
    :type qid: u32

    :param entry:
        Entry return
    :type entry: struct aac_entry \*\*

    :param index:
        Index return
    :type index: u32 \*

    :param nonotify:
        notification control
    :type nonotify: unsigned long \*

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

    :param dev:
        Adapter
    :type dev: struct aac_dev \*

    :param index:
        Returned index
    :type index: u32 \*

    :param qid:
        *undescribed*
    :type qid: u32

    :param hw_fib:
        *undescribed*
    :type hw_fib: struct hw_fib \*

    :param wait:
        Wait if queue full
    :type wait: int

    :param fibptr:
        Driver fib object to go with fib
    :type fibptr: struct fib \*

    :param nonotify:
        Don't notify the adapter
    :type nonotify: unsigned long \*

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

    :param command:
        Command to send
    :type command: u16

    :param fibptr:
        The fib
    :type fibptr: struct fib \*

    :param size:
        Size of fib data area
    :type size: unsigned long

    :param priority:
        Priority of Fib
    :type priority: int

    :param wait:
        Async/sync select
    :type wait: int

    :param reply:
        True if a reply is wanted
    :type reply: int

    :param callback:
        Called with reply
    :type callback: fib_callback

    :param callback_data:
        Passed to callback
    :type callback_data: void \*

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

    :param dev:
        Adapter
    :type dev: struct aac_dev \*

    :param q:
        Queue
    :type q: struct aac_queue \*

    :param entry:
        Return entry
    :type entry: struct aac_entry \*\*

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

    :param dev:
        Adapter
    :type dev: struct aac_dev \*

    :param q:
        Queue
    :type q: struct aac_queue \*

    :param qid:
        Queue ident
    :type qid: u32

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

    :param fibptr:
        fib to complete
    :type fibptr: struct fib \*

    :param size:
        size of fib
    :type size: unsigned short

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

    :param fibptr:
        *undescribed*
    :type fibptr: struct fib \*

.. _`aac_fib_complete.description`:

Description
-----------

Will do all necessary work to complete a FIB.

.. _`aac_printf`:

aac_printf
==========

.. c:function:: void aac_printf(struct aac_dev *dev, u32 val)

    handle printf from firmware

    :param dev:
        Adapter
    :type dev: struct aac_dev \*

    :param val:
        Message info
    :type val: u32

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

.. _`aac_handle_sa_aif`:

aac_handle_sa_aif
=================

.. c:function:: void aac_handle_sa_aif(struct aac_dev *dev, struct fib *fibptr)

    :param dev:
        Which adapter this fib is from
    :type dev: struct aac_dev \*

    :param fibptr:
        Pointer to fibptr from adapter
    :type fibptr: struct fib \*

.. _`aac_handle_sa_aif.description`:

Description
-----------

This routine handles a driver notify fib from the adapter and
dispatches it to the appropriate routine for handling.

.. _`aac_command_thread`:

aac_command_thread
==================

.. c:function:: int aac_command_thread(void *data)

    command processing thread

    :param data:
        *undescribed*
    :type data: void \*

.. _`aac_command_thread.description`:

Description
-----------

Waits on the commandready event in it's queue. When the event gets set
it will pull FIBs off it's queue. It will continue to pull FIBs off
until the queue is empty. When the queue is empty it will wait for
more FIBs.

.. This file was automatic generated / don't edit.

