.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/isdn/gigaset/common.c

.. _`gigaset_dbg_buffer`:

gigaset_dbg_buffer
==================

.. c:function:: void gigaset_dbg_buffer(enum debuglevel level, const unsigned char *msg, size_t len, const unsigned char *buf)

    dump data in ASCII and hex for debugging

    :param level:
        debugging level.
    :type level: enum debuglevel

    :param msg:
        message prefix.
    :type msg: const unsigned char \*

    :param len:
        number of bytes to dump.
    :type len: size_t

    :param buf:
        data to dump.
    :type buf: const unsigned char \*

.. _`gigaset_dbg_buffer.description`:

Description
-----------

If the current debugging level includes one of the bits set in \ ``level``\ ,
\ ``len``\  bytes starting at \ ``buf``\  are logged to dmesg at KERN_DEBUG prio,
prefixed by the text \ ``msg``\ .

.. _`gigaset_add_event`:

gigaset_add_event
=================

.. c:function:: struct event_t *gigaset_add_event(struct cardstate *cs, struct at_state_t *at_state, int type, void *ptr, int parameter, void *arg)

    add event to device event queue

    :param cs:
        device descriptor structure.
    :type cs: struct cardstate \*

    :param at_state:
        connection state structure.
    :type at_state: struct at_state_t \*

    :param type:
        event type.
    :type type: int

    :param ptr:
        pointer parameter for event.
    :type ptr: void \*

    :param parameter:
        integer parameter for event.
    :type parameter: int

    :param arg:
        pointer parameter for event.
    :type arg: void \*

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

.. c:function:: void gigaset_freecs(struct cardstate *cs)

    free all associated ressources of a device

    :param cs:
        device descriptor structure.
    :type cs: struct cardstate \*

.. _`gigaset_freecs.description`:

Description
-----------

Stops all tasklets and timers, unregisters the device from all
subsystems it was registered to, deallocates the device structure
\ ``cs``\  and all structures referenced from it.
Operations on the device should be stopped before calling this.

.. _`gigaset_fill_inbuf`:

gigaset_fill_inbuf
==================

.. c:function:: int gigaset_fill_inbuf(struct inbuf_t *inbuf, const unsigned char *src, unsigned numbytes)

    append received data to input buffer

    :param inbuf:
        buffer structure.
    :type inbuf: struct inbuf_t \*

    :param src:
        received data.
    :type src: const unsigned char \*

    :param numbytes:
        number of bytes received.
    :type numbytes: unsigned

.. _`gigaset_fill_inbuf.return-value`:

Return value
------------

!=0 if some data was appended

.. _`gigaset_initcs`:

gigaset_initcs
==============

.. c:function:: struct cardstate *gigaset_initcs(struct gigaset_driver *drv, int channels, int onechannel, int ignoreframes, int cidmode, const char *modulename)

    initialize device structure

    :param drv:
        hardware driver the device belongs to
    :type drv: struct gigaset_driver \*

    :param channels:
        number of B channels supported by device
    :type channels: int

    :param onechannel:
        !=0 if B channel data and AT commands share one
        communication channel (M10x),
        ==0 if B channels have separate communication channels (base)
    :type onechannel: int

    :param ignoreframes:
        number of frames to ignore after setting up B channel
    :type ignoreframes: int

    :param cidmode:
        !=0: start in CallID mode
    :type cidmode: int

    :param modulename:
        name of driver module for LL registration
    :type modulename: const char \*

.. _`gigaset_initcs.description`:

Description
-----------

Allocate and initialize cardstate structure for Gigaset driver
Calls hardware dependent \ :c:func:`gigaset_initcshw`\  function
Calls B channel initialization function \ :c:func:`gigaset_initbcs`\  for each B channel

.. _`gigaset_initcs.return-value`:

Return value
------------

pointer to cardstate structure

.. _`gigaset_start`:

gigaset_start
=============

.. c:function:: int gigaset_start(struct cardstate *cs)

    start device operations

    :param cs:
        device descriptor structure.
    :type cs: struct cardstate \*

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

.. c:function:: int gigaset_shutdown(struct cardstate *cs)

    shut down device operations

    :param cs:
        device descriptor structure.
    :type cs: struct cardstate \*

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

.. c:function:: void gigaset_stop(struct cardstate *cs)

    stop device operations

    :param cs:
        device descriptor structure.
    :type cs: struct cardstate \*

.. _`gigaset_stop.description`:

Description
-----------

Stops operations on the device by scheduling an EV_STOP event and
waiting for completion of the shutdown.

.. _`gigaset_freedriver`:

gigaset_freedriver
==================

.. c:function:: void gigaset_freedriver(struct gigaset_driver *drv)

    free all associated ressources of a driver

    :param drv:
        driver descriptor structure.
    :type drv: struct gigaset_driver \*

.. _`gigaset_freedriver.description`:

Description
-----------

Unregisters the driver from the system and deallocates the driver
structure \ ``drv``\  and all structures referenced from it.
All devices should be shut down before calling this.

.. _`gigaset_initdriver`:

gigaset_initdriver
==================

.. c:function:: struct gigaset_driver *gigaset_initdriver(unsigned minor, unsigned minors, const char *procname, const char *devname, const struct gigaset_ops *ops, struct module *owner)

    initialize driver structure

    :param minor:
        First minor number
    :type minor: unsigned

    :param minors:
        Number of minors this driver can handle
    :type minors: unsigned

    :param procname:
        Name of the driver
    :type procname: const char \*

    :param devname:
        Name of the device files (prefix without minor number)
    :type devname: const char \*

    :param ops:
        *undescribed*
    :type ops: const struct gigaset_ops \*

    :param owner:
        *undescribed*
    :type owner: struct module \*

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

.. c:function:: void gigaset_blockdriver(struct gigaset_driver *drv)

    block driver

    :param drv:
        driver descriptor structure.
    :type drv: struct gigaset_driver \*

.. _`gigaset_blockdriver.description`:

Description
-----------

Prevents the driver from attaching new devices, in preparation for
deregistration.

.. This file was automatic generated / don't edit.

