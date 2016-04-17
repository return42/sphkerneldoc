.. -*- coding: utf-8; mode: rst -*-

========
common.c
========


.. _`gigaset_dbg_buffer`:

gigaset_dbg_buffer
==================

.. c:function:: void gigaset_dbg_buffer (enum debuglevel level, const unsigned char *msg, size_t len, const unsigned char *buf)

    dump data in ASCII and hex for debugging

    :param enum debuglevel level:
        debugging level.

    :param const unsigned char \*msg:
        message prefix.

    :param size_t len:
        number of bytes to dump.

    :param const unsigned char \*buf:
        data to dump.



.. _`gigaset_dbg_buffer.description`:

Description
-----------

If the current debugging level includes one of the bits set in ``level``\ ,
``len`` bytes starting at ``buf`` are logged to dmesg at KERN_DEBUG prio,
prefixed by the text ``msg``\ .



.. _`gigaset_add_event`:

gigaset_add_event
=================

.. c:function:: struct event_t *gigaset_add_event (struct cardstate *cs, struct at_state_t *at_state, int type, void *ptr, int parameter, void *arg)

    add event to device event queue

    :param struct cardstate \*cs:
        device descriptor structure.

    :param struct at_state_t \*at_state:
        connection state structure.

    :param int type:
        event type.

    :param void \*ptr:
        pointer parameter for event.

    :param int parameter:
        integer parameter for event.

    :param void \*arg:
        pointer parameter for event.



.. _`gigaset_add_event.description`:

Description
-----------

Allocate an event queue entry from the device's event queue, and set it up
with the parameters given.



.. _`gigaset_add_event.return-value`:

Return value
------------

added event



.. _`gigaset_freecs`:

gigaset_freecs
==============

.. c:function:: void gigaset_freecs (struct cardstate *cs)

    free all associated ressources of a device

    :param struct cardstate \*cs:
        device descriptor structure.



.. _`gigaset_freecs.description`:

Description
-----------

Stops all tasklets and timers, unregisters the device from all
subsystems it was registered to, deallocates the device structure
``cs`` and all structures referenced from it.
Operations on the device should be stopped before calling this.



.. _`gigaset_fill_inbuf`:

gigaset_fill_inbuf
==================

.. c:function:: int gigaset_fill_inbuf (struct inbuf_t *inbuf, const unsigned char *src, unsigned numbytes)

    append received data to input buffer

    :param struct inbuf_t \*inbuf:
        buffer structure.

    :param const unsigned char \*src:
        received data.

    :param unsigned numbytes:
        number of bytes received.



.. _`gigaset_fill_inbuf.return-value`:

Return value
------------

!=0 if some data was appended



.. _`gigaset_initcs`:

gigaset_initcs
==============

.. c:function:: struct cardstate *gigaset_initcs (struct gigaset_driver *drv, int channels, int onechannel, int ignoreframes, int cidmode, const char *modulename)

    initialize device structure

    :param struct gigaset_driver \*drv:
        hardware driver the device belongs to

    :param int channels:
        number of B channels supported by device

    :param int onechannel:
        !=0 if B channel data and AT commands share one
        communication channel (M10x),
        ==0 if B channels have separate communication channels (base)

    :param int ignoreframes:
        number of frames to ignore after setting up B channel

    :param int cidmode:
        !=0: start in CallID mode

    :param const char \*modulename:
        name of driver module for LL registration



.. _`gigaset_initcs.description`:

Description
-----------

Allocate and initialize cardstate structure for Gigaset driver
Calls hardware dependent :c:func:`gigaset_initcshw` function
Calls B channel initialization function :c:func:`gigaset_initbcs` for each B channel



.. _`gigaset_initcs.return-value`:

Return value
------------

pointer to cardstate structure



.. _`gigaset_start`:

gigaset_start
=============

.. c:function:: int gigaset_start (struct cardstate *cs)

    start device operations

    :param struct cardstate \*cs:
        device descriptor structure.



.. _`gigaset_start.description`:

Description
-----------

Prepares the device for use by setting up communication parameters,
scheduling an EV_START event to initiate device initialization, and
waiting for completion of the initialization.



.. _`gigaset_start.return-value`:

Return value
------------

0 on success, error code < 0 on failure



.. _`gigaset_shutdown`:

gigaset_shutdown
================

.. c:function:: int gigaset_shutdown (struct cardstate *cs)

    shut down device operations

    :param struct cardstate \*cs:
        device descriptor structure.



.. _`gigaset_shutdown.description`:

Description
-----------

Deactivates the device by scheduling an EV_SHUTDOWN event and
waiting for completion of the shutdown.



.. _`gigaset_shutdown.return-value`:

Return value
------------

0 - success, -ENODEV - error (no device associated)



.. _`gigaset_stop`:

gigaset_stop
============

.. c:function:: void gigaset_stop (struct cardstate *cs)

    stop device operations

    :param struct cardstate \*cs:
        device descriptor structure.



.. _`gigaset_stop.description`:

Description
-----------

Stops operations on the device by scheduling an EV_STOP event and
waiting for completion of the shutdown.



.. _`gigaset_freedriver`:

gigaset_freedriver
==================

.. c:function:: void gigaset_freedriver (struct gigaset_driver *drv)

    free all associated ressources of a driver

    :param struct gigaset_driver \*drv:
        driver descriptor structure.



.. _`gigaset_freedriver.description`:

Description
-----------

Unregisters the driver from the system and deallocates the driver
structure ``drv`` and all structures referenced from it.
All devices should be shut down before calling this.



.. _`gigaset_initdriver`:

gigaset_initdriver
==================

.. c:function:: struct gigaset_driver *gigaset_initdriver (unsigned minor, unsigned minors, const char *procname, const char *devname, const struct gigaset_ops *ops, struct module *owner)

    initialize driver structure

    :param unsigned minor:
        First minor number

    :param unsigned minors:
        Number of minors this driver can handle

    :param const char \*procname:
        Name of the driver

    :param const char \*devname:
        Name of the device files (prefix without minor number)

    :param const struct gigaset_ops \*ops:

        *undescribed*

    :param struct module \*owner:

        *undescribed*



.. _`gigaset_initdriver.description`:

Description
-----------

Allocate and initialize gigaset_driver structure. Initialize interface.



.. _`gigaset_initdriver.return-value`:

Return value
------------

Pointer to the gigaset_driver structure on success, NULL on failure.



.. _`gigaset_blockdriver`:

gigaset_blockdriver
===================

.. c:function:: void gigaset_blockdriver (struct gigaset_driver *drv)

    block driver

    :param struct gigaset_driver \*drv:
        driver descriptor structure.



.. _`gigaset_blockdriver.description`:

Description
-----------

Prevents the driver from attaching new devices, in preparation for
deregistration.

