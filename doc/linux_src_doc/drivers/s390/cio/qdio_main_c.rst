.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/qdio_main.c

.. _`do_siga_output`:

do_siga_output
==============

.. c:function:: int do_siga_output(unsigned long schid, unsigned long mask, unsigned int *bb, unsigned int fc, unsigned long aob)

    perform SIGA-w/wt function

    :param unsigned long schid:
        subchannel id or in case of QEBSM the subchannel token

    :param unsigned long mask:
        which output queues to process

    :param unsigned int \*bb:
        busy bit indicator, set only if SIGA-w/wt could not access a buffer

    :param unsigned int fc:
        function code to perform

    :param unsigned long aob:
        *undescribed*

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

    :param struct qdio_q \*q:
        queue to manipulate

    :param unsigned char \*state:
        state of the extracted buffers

    :param int start:
        buffer number to start at

    :param int count:
        count of buffers to examine

    :param int auto_ack:
        automatically acknowledge buffers

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

    :param struct qdio_q \*q:
        queue to manipulate

    :param unsigned char state:
        new state of the buffers

    :param int start:
        first buffer number to change

    :param int count:
        how many buffers to change

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

    :param struct ccw_device \*cdev:
        ccw device to get description for

    :param struct qdio_ssqd_desc \*data:
        where to store the ssqd

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

    :param struct ccw_device \*cdev:
        associated ccw device

    :param int how:
        use halt or clear to shutdown

.. _`qdio_free`:

qdio_free
=========

.. c:function:: int qdio_free(struct ccw_device *cdev)

    free data structures for a qdio subchannel

    :param struct ccw_device \*cdev:
        associated ccw device

.. _`qdio_allocate`:

qdio_allocate
=============

.. c:function:: int qdio_allocate(struct qdio_initialize *init_data)

    allocate qdio queues and associated data

    :param struct qdio_initialize \*init_data:
        initialization data

.. _`qdio_establish`:

qdio_establish
==============

.. c:function:: int qdio_establish(struct qdio_initialize *init_data)

    establish queues on a qdio subchannel

    :param struct qdio_initialize \*init_data:
        initialization data

.. _`qdio_activate`:

qdio_activate
=============

.. c:function:: int qdio_activate(struct ccw_device *cdev)

    activate queues on a qdio subchannel

    :param struct ccw_device \*cdev:
        associated cdev

.. _`handle_inbound`:

handle_inbound
==============

.. c:function:: int handle_inbound(struct qdio_q *q, unsigned int callflags, int bufnr, int count)

    reset processed input buffers

    :param struct qdio_q \*q:
        queue containing the buffers

    :param unsigned int callflags:
        flags

    :param int bufnr:
        first buffer to process

    :param int count:
        how many buffers are emptied

.. _`handle_outbound`:

handle_outbound
===============

.. c:function:: int handle_outbound(struct qdio_q *q, unsigned int callflags, int bufnr, int count)

    process filled outbound buffers

    :param struct qdio_q \*q:
        queue containing the buffers

    :param unsigned int callflags:
        flags

    :param int bufnr:
        first buffer to process

    :param int count:
        how many buffers are filled

.. _`do_qdio`:

do_QDIO
=======

.. c:function:: int do_QDIO(struct ccw_device *cdev, unsigned int callflags, int q_nr, unsigned int bufnr, unsigned int count)

    process input or output buffers

    :param struct ccw_device \*cdev:
        associated ccw_device for the qdio subchannel

    :param unsigned int callflags:
        input or output and special flags from the program

    :param int q_nr:
        queue number

    :param unsigned int bufnr:
        buffer number

    :param unsigned int count:
        how many buffers to process

.. _`qdio_start_irq`:

qdio_start_irq
==============

.. c:function:: int qdio_start_irq(struct ccw_device *cdev, int nr)

    process input buffers

    :param struct ccw_device \*cdev:
        associated ccw_device for the qdio subchannel

    :param int nr:
        input queue number

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

    :param struct ccw_device \*cdev:
        associated ccw_device for the qdio subchannel

    :param int nr:
        input queue number

    :param int \*bufnr:
        first filled buffer number

    :param int \*error:
        buffers are in error state

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

    :param struct ccw_device \*cdev:
        associated ccw_device for the qdio subchannel

    :param int nr:
        input queue number

.. _`qdio_stop_irq.description`:

Description
-----------

Return codes
0 - interrupts were already disabled
1 - interrupts successfully disabled

.. _`qdio_pnso_brinfo`:

qdio_pnso_brinfo
================

.. c:function:: int qdio_pnso_brinfo(struct subchannel_id schid, int cnc, u16 *response, void (*) cb (void *priv, enum qdio_brinfo_entry_type type, void *entry, void *priv)

    perform network subchannel op #0 - bridge info.

    :param struct subchannel_id schid:
        Subchannel ID.

    :param int cnc:
        Boolean Change-Notification Control

    :param u16 \*response:
        Response code will be stored at this address

    :param (void (\*) cb (void \*priv, enum qdio_brinfo_entry_type type, void \*entry):
        Callback function will be executed for each element
        of the address list

    :param void \*priv:
        Pointer to pass to the callback function.

.. _`qdio_pnso_brinfo.description`:

Description
-----------

Performs "Store-network-bridging-information list" operation and calls
the callback function for every entry in the list. If "change-
notification-control" is set, further changes in the address list
will be reported via the IPA command.

.. This file was automatic generated / don't edit.

