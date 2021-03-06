.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/host1x/syncpt.c

.. _`host1x_syncpt_id`:

host1x_syncpt_id
================

.. c:function:: u32 host1x_syncpt_id(struct host1x_syncpt *sp)

    retrieve syncpoint ID

    :param sp:
        host1x syncpoint
    :type sp: struct host1x_syncpt \*

.. _`host1x_syncpt_id.description`:

Description
-----------

Given a pointer to a struct host1x_syncpt, retrieves its ID. This ID is
often used as a value to program into registers that control how hardware
blocks interact with syncpoints.

.. _`host1x_syncpt_incr_max`:

host1x_syncpt_incr_max
======================

.. c:function:: u32 host1x_syncpt_incr_max(struct host1x_syncpt *sp, u32 incrs)

    update the value sent to hardware

    :param sp:
        host1x syncpoint
    :type sp: struct host1x_syncpt \*

    :param incrs:
        number of increments
    :type incrs: u32

.. _`host1x_syncpt_incr`:

host1x_syncpt_incr
==================

.. c:function:: int host1x_syncpt_incr(struct host1x_syncpt *sp)

    increment syncpoint value from CPU, updating cache

    :param sp:
        host1x syncpoint
    :type sp: struct host1x_syncpt \*

.. _`host1x_syncpt_wait`:

host1x_syncpt_wait
==================

.. c:function:: int host1x_syncpt_wait(struct host1x_syncpt *sp, u32 thresh, long timeout, u32 *value)

    wait for a syncpoint to reach a given value

    :param sp:
        host1x syncpoint
    :type sp: struct host1x_syncpt \*

    :param thresh:
        threshold
    :type thresh: u32

    :param timeout:
        maximum time to wait for the syncpoint to reach the given value
    :type timeout: long

    :param value:
        return location for the syncpoint value
    :type value: u32 \*

.. _`host1x_syncpt_request`:

host1x_syncpt_request
=====================

.. c:function:: struct host1x_syncpt *host1x_syncpt_request(struct host1x_client *client, unsigned long flags)

    request a syncpoint

    :param client:
        client requesting the syncpoint
    :type client: struct host1x_client \*

    :param flags:
        flags
    :type flags: unsigned long

.. _`host1x_syncpt_request.description`:

Description
-----------

host1x client drivers can use this function to allocate a syncpoint for
subsequent use. A syncpoint returned by this function will be reserved for
use by the client exclusively. When no longer using a syncpoint, a host1x
client driver needs to release it using \ :c:func:`host1x_syncpt_free`\ .

.. _`host1x_syncpt_free`:

host1x_syncpt_free
==================

.. c:function:: void host1x_syncpt_free(struct host1x_syncpt *sp)

    free a requested syncpoint

    :param sp:
        host1x syncpoint
    :type sp: struct host1x_syncpt \*

.. _`host1x_syncpt_free.description`:

Description
-----------

Release a syncpoint previously allocated using \ :c:func:`host1x_syncpt_request`\ . A
host1x client driver should call this when the syncpoint is no longer in
use. Note that client drivers must ensure that the syncpoint doesn't remain
under the control of hardware after calling this function, otherwise two
clients may end up trying to access the same syncpoint concurrently.

.. _`host1x_syncpt_read_max`:

host1x_syncpt_read_max
======================

.. c:function:: u32 host1x_syncpt_read_max(struct host1x_syncpt *sp)

    read maximum syncpoint value

    :param sp:
        host1x syncpoint
    :type sp: struct host1x_syncpt \*

.. _`host1x_syncpt_read_max.description`:

Description
-----------

The maximum syncpoint value indicates how many operations there are in
queue, either in channel or in a software thread.

.. _`host1x_syncpt_read_min`:

host1x_syncpt_read_min
======================

.. c:function:: u32 host1x_syncpt_read_min(struct host1x_syncpt *sp)

    read minimum syncpoint value

    :param sp:
        host1x syncpoint
    :type sp: struct host1x_syncpt \*

.. _`host1x_syncpt_read_min.description`:

Description
-----------

The minimum syncpoint value is a shadow of the current sync point value in
hardware.

.. _`host1x_syncpt_read`:

host1x_syncpt_read
==================

.. c:function:: u32 host1x_syncpt_read(struct host1x_syncpt *sp)

    read the current syncpoint value

    :param sp:
        host1x syncpoint
    :type sp: struct host1x_syncpt \*

.. _`host1x_syncpt_get`:

host1x_syncpt_get
=================

.. c:function:: struct host1x_syncpt *host1x_syncpt_get(struct host1x *host, unsigned int id)

    obtain a syncpoint by ID

    :param host:
        host1x controller
    :type host: struct host1x \*

    :param id:
        syncpoint ID
    :type id: unsigned int

.. _`host1x_syncpt_get_base`:

host1x_syncpt_get_base
======================

.. c:function:: struct host1x_syncpt_base *host1x_syncpt_get_base(struct host1x_syncpt *sp)

    obtain the wait base associated with a syncpoint

    :param sp:
        host1x syncpoint
    :type sp: struct host1x_syncpt \*

.. _`host1x_syncpt_base_id`:

host1x_syncpt_base_id
=====================

.. c:function:: u32 host1x_syncpt_base_id(struct host1x_syncpt_base *base)

    retrieve the ID of a syncpoint wait base

    :param base:
        host1x syncpoint wait base
    :type base: struct host1x_syncpt_base \*

.. This file was automatic generated / don't edit.

