.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/most/core.c

.. _`list_pop_mbo`:

list_pop_mbo
============

.. c:function::  list_pop_mbo( ptr)

    retrieves the first MBO of the list and removes it

    :param ptr:
        the list head to grab the MBO from.
    :type ptr: 

.. _`most_free_mbo_coherent`:

most_free_mbo_coherent
======================

.. c:function:: void most_free_mbo_coherent(struct mbo *mbo)

    free an MBO and its coherent buffer

    :param mbo:
        most buffer
    :type mbo: struct mbo \*

.. _`flush_channel_fifos`:

flush_channel_fifos
===================

.. c:function:: void flush_channel_fifos(struct most_channel *c)

    clear the channel fifos

    :param c:
        pointer to channel object
    :type c: struct most_channel \*

.. _`flush_trash_fifo`:

flush_trash_fifo
================

.. c:function:: int flush_trash_fifo(struct most_channel *c)

    clear the trash fifo

    :param c:
        pointer to channel object
    :type c: struct most_channel \*

.. _`split_string`:

split_string
============

.. c:function:: int split_string(char *buf, char **a, char **b, char **c, char **d)

    parses buf and extracts ':' separated substrings.

    :param buf:
        complete string from attribute 'add_channel'
    :type buf: char \*

    :param a:
        storage for 1st substring (=interface name)
    :type a: char \*\*

    :param b:
        storage for 2nd substring (=channel name)
    :type b: char \*\*

    :param c:
        storage for 3rd substring (=component name)
    :type c: char \*\*

    :param d:
        storage optional 4th substring (=user defined name)
    :type d: char \*\*

.. _`split_string.examples`:

Examples
--------


Input: "mdev0:ch6:cdev:my_channel\n" or
"mdev0:ch6:cdev:my_channel"

.. _`split_string.output`:

Output
------

\*a -> "mdev0", \*b -> "ch6", \*c -> "cdev" \*d -> "my_channel"

Input: "mdev1:ep81:cdev\n"

\*a -> "mdev1", \*b -> "ep81", \*c -> "cdev" \*d -> ""

Input: "mdev1:ep81"

\*a -> "mdev1", \*b -> "ep81", \*c -> "cdev" \*d == NULL

.. _`get_channel`:

get_channel
===========

.. c:function:: struct most_channel *get_channel(char *mdev, char *mdev_ch)

    get pointer to channel

    :param mdev:
        name of the device interface
    :type mdev: char \*

    :param mdev_ch:
        name of channel
    :type mdev_ch: char \*

.. _`add_link_store`:

add_link_store
==============

.. c:function:: ssize_t add_link_store(struct device_driver *drv, const char *buf, size_t len)

    store function for add_link attribute

    :param drv:
        device driver
    :type drv: struct device_driver \*

    :param buf:
        buffer
    :type buf: const char \*

    :param len:
        buffer length
    :type len: size_t

.. _`add_link_store.description`:

Description
-----------

This parses the string given by buf and splits it into
four substrings. Note: last substring is optional. In case a cdev
component is loaded the optional 4th substring will make up the name of
device node in the /dev directory. If omitted, the device node will
inherit the channel's name within sysfs.

Searches for (device, channel) pair and probes the component

.. _`add_link_store.example`:

Example
-------

.. code-block:: c

    (1) echo "mdev0:ch6:cdev:my_rxchannel" >add_link
    (2) echo "mdev1:ep81:cdev" >add_link

    (1) would create the device node /dev/my_rxchannel
    (2) would create the device node /dev/mdev1-ep81


.. _`remove_link_store`:

remove_link_store
=================

.. c:function:: ssize_t remove_link_store(struct device_driver *drv, const char *buf, size_t len)

    store function for remove_link attribute

    :param drv:
        device driver
    :type drv: struct device_driver \*

    :param buf:
        buffer
    :type buf: const char \*

    :param len:
        buffer length
    :type len: size_t

.. _`remove_link_store.example`:

Example
-------

.. code-block:: c

    echo "mdev0:ep81" >remove_link


.. _`arm_mbo`:

arm_mbo
=======

.. c:function:: void arm_mbo(struct mbo *mbo)

    recycle MBO for further usage

    :param mbo:
        most buffer
    :type mbo: struct mbo \*

.. _`arm_mbo.description`:

Description
-----------

This puts an MBO back to the list to have it ready for up coming
tx transactions.

In case the MBO belongs to a channel that recently has been
poisoned, the MBO is scheduled to be trashed.
Calls the completion handler of an attached component.

.. _`arm_mbo_chain`:

arm_mbo_chain
=============

.. c:function:: int arm_mbo_chain(struct most_channel *c, int dir, void (*compl)(struct mbo *))

    helper function that arms an MBO chain for the HDM

    :param c:
        pointer to interface channel
    :type c: struct most_channel \*

    :param dir:
        direction of the channel
    :type dir: int

    :param void (\*compl)(struct mbo \*):
        pointer to completion function

.. _`arm_mbo_chain.description`:

Description
-----------

This allocates buffer objects including the containing DMA coherent
buffer and puts them in the fifo.
Buffers of Rx channels are put in the kthread fifo, hence immediately
submitted to the HDM.

Returns the number of allocated and enqueued MBOs.

.. _`most_submit_mbo`:

most_submit_mbo
===============

.. c:function:: void most_submit_mbo(struct mbo *mbo)

    submits an MBO to fifo

    :param mbo:
        most buffer
    :type mbo: struct mbo \*

.. _`most_write_completion`:

most_write_completion
=====================

.. c:function:: void most_write_completion(struct mbo *mbo)

    write completion handler

    :param mbo:
        most buffer
    :type mbo: struct mbo \*

.. _`most_write_completion.description`:

Description
-----------

This recycles the MBO for further usage. In case the channel has been
poisoned, the MBO is scheduled to be trashed.

.. _`most_get_mbo`:

most_get_mbo
============

.. c:function:: struct mbo *most_get_mbo(struct most_interface *iface, int id, struct core_component *comp)

    get pointer to an MBO of pool

    :param iface:
        pointer to interface instance
    :type iface: struct most_interface \*

    :param id:
        channel ID
    :type id: int

    :param comp:
        driver component
    :type comp: struct core_component \*

.. _`most_get_mbo.description`:

Description
-----------

This attempts to get a free buffer out of the channel fifo.
Returns a pointer to MBO on success or NULL otherwise.

.. _`most_put_mbo`:

most_put_mbo
============

.. c:function:: void most_put_mbo(struct mbo *mbo)

    return buffer to pool

    :param mbo:
        most buffer
    :type mbo: struct mbo \*

.. _`most_read_completion`:

most_read_completion
====================

.. c:function:: void most_read_completion(struct mbo *mbo)

    read completion handler

    :param mbo:
        most buffer
    :type mbo: struct mbo \*

.. _`most_read_completion.description`:

Description
-----------

This function is called by the HDM when data has been received from the
hardware and copied to the buffer of the MBO.

In case the channel has been poisoned it puts the buffer in the trash queue.
Otherwise, it passes the buffer to an component for further processing.

.. _`most_start_channel`:

most_start_channel
==================

.. c:function:: int most_start_channel(struct most_interface *iface, int id, struct core_component *comp)

    prepares a channel for communication

    :param iface:
        pointer to interface instance
    :type iface: struct most_interface \*

    :param id:
        channel ID
    :type id: int

    :param comp:
        driver component
    :type comp: struct core_component \*

.. _`most_start_channel.description`:

Description
-----------

This prepares the channel for usage. Cross-checks whether the
channel's been properly configured.

Returns 0 on success or error code otherwise.

.. _`most_stop_channel`:

most_stop_channel
=================

.. c:function:: int most_stop_channel(struct most_interface *iface, int id, struct core_component *comp)

    stops a running channel

    :param iface:
        pointer to interface instance
    :type iface: struct most_interface \*

    :param id:
        channel ID
    :type id: int

    :param comp:
        driver component
    :type comp: struct core_component \*

.. _`most_register_component`:

most_register_component
=======================

.. c:function:: int most_register_component(struct core_component *comp)

    registers a driver component with the core

    :param comp:
        driver component
    :type comp: struct core_component \*

.. _`most_deregister_component`:

most_deregister_component
=========================

.. c:function:: int most_deregister_component(struct core_component *comp)

    deregisters a driver component with the core

    :param comp:
        driver component
    :type comp: struct core_component \*

.. _`most_register_interface`:

most_register_interface
=======================

.. c:function:: int most_register_interface(struct most_interface *iface)

    registers an interface with core

    :param iface:
        device interface
    :type iface: struct most_interface \*

.. _`most_register_interface.description`:

Description
-----------

Allocates and initializes a new interface instance and all of its channels.
Returns a pointer to kobject or an error pointer.

.. _`most_deregister_interface`:

most_deregister_interface
=========================

.. c:function:: void most_deregister_interface(struct most_interface *iface)

    deregisters an interface with core

    :param iface:
        device interface
    :type iface: struct most_interface \*

.. _`most_deregister_interface.description`:

Description
-----------

Before removing an interface instance from the list, all running
channels are stopped and poisoned.

.. _`most_stop_enqueue`:

most_stop_enqueue
=================

.. c:function:: void most_stop_enqueue(struct most_interface *iface, int id)

    prevents core from enqueueing MBOs

    :param iface:
        pointer to interface
    :type iface: struct most_interface \*

    :param id:
        channel id
    :type id: int

.. _`most_stop_enqueue.description`:

Description
-----------

This is called by an HDM that \_cannot\_ attend to its duties and
is imminent to get run over by the core. The core is not going to
enqueue any further packets unless the flagging HDM calls
most_resume \ :c:func:`enqueue`\ .

.. _`most_resume_enqueue`:

most_resume_enqueue
===================

.. c:function:: void most_resume_enqueue(struct most_interface *iface, int id)

    allow core to enqueue MBOs again

    :param iface:
        pointer to interface
    :type iface: struct most_interface \*

    :param id:
        channel id
    :type id: int

.. _`most_resume_enqueue.description`:

Description
-----------

This clears the enqueue halt flag and enqueues all MBOs currently
sitting in the wait fifo.

.. This file was automatic generated / don't edit.

