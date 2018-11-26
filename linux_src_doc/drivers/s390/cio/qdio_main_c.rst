.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/qdio_main.c

.. _`do_siga_output`:

do_siga_output
==============

.. c:function:: int do_siga_output(unsigned long schid, unsigned long mask, unsigned int *bb, unsigned int fc, unsigned long aob)

    perform SIGA-w/wt function

    :param schid:
        subchannel id or in case of QEBSM the subchannel token
    :type schid: unsigned long

    :param mask:
        which output queues to process
    :type mask: unsigned long

    :param bb:
        busy bit indicator, set only if SIGA-w/wt could not access a buffer
    :type bb: unsigned int \*

    :param fc:
        function code to perform
    :type fc: unsigned int

    :param aob:
        asynchronous operation block
    :type aob: unsigned long

.. _`do_siga_output.description`:

Description
-----------

Returns condition code.

.. _`do_siga_output.note`:

Note
----

For IQDC unicast queues only the highest priority queue is processed.

.. _`qdio_do_eqbs`:

qdio_do_eqbs
============

.. c:function:: int qdio_do_eqbs(struct qdio_q *q, unsigned char *state, int start, int count, int auto_ack)

    extract buffer states for QEBSM

    :param q:
        queue to manipulate
    :type q: struct qdio_q \*

    :param state:
        state of the extracted buffers
    :type state: unsigned char \*

    :param start:
        buffer number to start at
    :type start: int

    :param count:
        count of buffers to examine
    :type count: int

    :param auto_ack:
        automatically acknowledge buffers
    :type auto_ack: int

.. _`qdio_do_eqbs.description`:

Description
-----------

Returns the number of successfully extracted equal buffer states.
Stops processing if a state is different from the last buffers state.

.. _`qdio_do_sqbs`:

qdio_do_sqbs
============

.. c:function:: int qdio_do_sqbs(struct qdio_q *q, unsigned char state, int start, int count)

    set buffer states for QEBSM

    :param q:
        queue to manipulate
    :type q: struct qdio_q \*

    :param state:
        new state of the buffers
    :type state: unsigned char

    :param start:
        first buffer number to change
    :type start: int

    :param count:
        how many buffers to change
    :type count: int

.. _`qdio_do_sqbs.description`:

Description
-----------

Returns the number of successfully changed buffers.
Does retrying until the specified count of buffer states is set or an
error occurs.

.. _`qdio_get_ssqd_desc`:

qdio_get_ssqd_desc
==================

.. c:function:: int qdio_get_ssqd_desc(struct ccw_device *cdev, struct qdio_ssqd_desc *data)

    get qdio subchannel description

    :param cdev:
        ccw device to get description for
    :type cdev: struct ccw_device \*

    :param data:
        where to store the ssqd
    :type data: struct qdio_ssqd_desc \*

.. _`qdio_get_ssqd_desc.description`:

Description
-----------

Returns 0 or an error code. The results of the chsc are stored in the
specified structure.

.. _`qdio_shutdown`:

qdio_shutdown
=============

.. c:function:: int qdio_shutdown(struct ccw_device *cdev, int how)

    shut down a qdio subchannel

    :param cdev:
        associated ccw device
    :type cdev: struct ccw_device \*

    :param how:
        use halt or clear to shutdown
    :type how: int

.. _`qdio_free`:

qdio_free
=========

.. c:function:: int qdio_free(struct ccw_device *cdev)

    free data structures for a qdio subchannel

    :param cdev:
        associated ccw device
    :type cdev: struct ccw_device \*

.. _`qdio_allocate`:

qdio_allocate
=============

.. c:function:: int qdio_allocate(struct qdio_initialize *init_data)

    allocate qdio queues and associated data

    :param init_data:
        initialization data
    :type init_data: struct qdio_initialize \*

.. _`qdio_establish`:

qdio_establish
==============

.. c:function:: int qdio_establish(struct qdio_initialize *init_data)

    establish queues on a qdio subchannel

    :param init_data:
        initialization data
    :type init_data: struct qdio_initialize \*

.. _`qdio_activate`:

qdio_activate
=============

.. c:function:: int qdio_activate(struct ccw_device *cdev)

    activate queues on a qdio subchannel

    :param cdev:
        associated cdev
    :type cdev: struct ccw_device \*

.. _`handle_inbound`:

handle_inbound
==============

.. c:function:: int handle_inbound(struct qdio_q *q, unsigned int callflags, int bufnr, int count)

    reset processed input buffers

    :param q:
        queue containing the buffers
    :type q: struct qdio_q \*

    :param callflags:
        flags
    :type callflags: unsigned int

    :param bufnr:
        first buffer to process
    :type bufnr: int

    :param count:
        how many buffers are emptied
    :type count: int

.. _`handle_outbound`:

handle_outbound
===============

.. c:function:: int handle_outbound(struct qdio_q *q, unsigned int callflags, int bufnr, int count)

    process filled outbound buffers

    :param q:
        queue containing the buffers
    :type q: struct qdio_q \*

    :param callflags:
        flags
    :type callflags: unsigned int

    :param bufnr:
        first buffer to process
    :type bufnr: int

    :param count:
        how many buffers are filled
    :type count: int

.. _`do_qdio`:

do_QDIO
=======

.. c:function:: int do_QDIO(struct ccw_device *cdev, unsigned int callflags, int q_nr, unsigned int bufnr, unsigned int count)

    process input or output buffers

    :param cdev:
        associated ccw_device for the qdio subchannel
    :type cdev: struct ccw_device \*

    :param callflags:
        input or output and special flags from the program
    :type callflags: unsigned int

    :param q_nr:
        queue number
    :type q_nr: int

    :param bufnr:
        buffer number
    :type bufnr: unsigned int

    :param count:
        how many buffers to process
    :type count: unsigned int

.. _`qdio_start_irq`:

qdio_start_irq
==============

.. c:function:: int qdio_start_irq(struct ccw_device *cdev, int nr)

    process input buffers

    :param cdev:
        associated ccw_device for the qdio subchannel
    :type cdev: struct ccw_device \*

    :param nr:
        input queue number
    :type nr: int

.. _`qdio_start_irq.description`:

Description
-----------

Return codes
0 - success
1 - irqs not started since new data is available

.. _`qdio_get_next_buffers`:

qdio_get_next_buffers
=====================

.. c:function:: int qdio_get_next_buffers(struct ccw_device *cdev, int nr, int *bufnr, int *error)

    process input buffers

    :param cdev:
        associated ccw_device for the qdio subchannel
    :type cdev: struct ccw_device \*

    :param nr:
        input queue number
    :type nr: int

    :param bufnr:
        first filled buffer number
    :type bufnr: int \*

    :param error:
        buffers are in error state
    :type error: int \*

.. _`qdio_get_next_buffers.description`:

Description
-----------

Return codes
< 0 - error
= 0 - no new buffers found
> 0 - number of processed buffers

.. _`qdio_stop_irq`:

qdio_stop_irq
=============

.. c:function:: int qdio_stop_irq(struct ccw_device *cdev, int nr)

    disable interrupt processing for the device

    :param cdev:
        associated ccw_device for the qdio subchannel
    :type cdev: struct ccw_device \*

    :param nr:
        input queue number
    :type nr: int

.. _`qdio_stop_irq.description`:

Description
-----------

Return codes
0 - interrupts were already disabled
1 - interrupts successfully disabled

.. _`qdio_pnso_brinfo`:

qdio_pnso_brinfo
================

.. c:function:: int qdio_pnso_brinfo(struct subchannel_id schid, int cnc, u16 *response, void (*cb)(void *priv, enum qdio_brinfo_entry_type type, void *entry), void *priv)

    perform network subchannel op #0 - bridge info.

    :param schid:
        Subchannel ID.
    :type schid: struct subchannel_id

    :param cnc:
        Boolean Change-Notification Control
    :type cnc: int

    :param response:
        Response code will be stored at this address
    :type response: u16 \*

    :param void (\*cb)(void \*priv, enum qdio_brinfo_entry_type type, void \*entry):
        Callback function will be executed for each element
        of the address list

    :param priv:
        Pointer to pass to the callback function.
    :type priv: void \*

.. _`qdio_pnso_brinfo.description`:

Description
-----------

Performs "Store-network-bridging-information list" operation and calls
the callback function for every entry in the list. If "change-
notification-control" is set, further changes in the address list
will be reported via the IPA command.

.. This file was automatic generated / don't edit.

