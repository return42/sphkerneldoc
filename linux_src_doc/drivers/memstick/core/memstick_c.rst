.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/memstick/core/memstick.c

.. _`memstick_detect_change`:

memstick_detect_change
======================

.. c:function:: void memstick_detect_change(struct memstick_host *host)

    schedule media detection on memstick host \ ``host``\  - host to use

    :param host:
        *undescribed*
    :type host: struct memstick_host \*

.. _`memstick_next_req`:

memstick_next_req
=================

.. c:function:: int memstick_next_req(struct memstick_host *host, struct memstick_request **mrq)

    called by host driver to obtain next request to process \ ``host``\  - host to use \ ``mrq``\  - pointer to stick the request to

    :param host:
        *undescribed*
    :type host: struct memstick_host \*

    :param mrq:
        *undescribed*
    :type mrq: struct memstick_request \*\*

.. _`memstick_next_req.description`:

Description
-----------

Host calls this function from idle state (\*mrq == NULL) or after finishing
previous request (\*mrq should point to it). If previous request was
unsuccessful, it is retried for predetermined number of times. Return value
of 0 means that new request was assigned to the host.

.. _`memstick_new_req`:

memstick_new_req
================

.. c:function:: void memstick_new_req(struct memstick_host *host)

    notify the host that some requests are pending \ ``host``\  - host to use

    :param host:
        *undescribed*
    :type host: struct memstick_host \*

.. _`memstick_init_req_sg`:

memstick_init_req_sg
====================

.. c:function:: void memstick_init_req_sg(struct memstick_request *mrq, unsigned char tpc, const struct scatterlist *sg)

    set request fields needed for bulk data transfer \ ``mrq``\  - request to use \ ``tpc``\  - memstick Transport Protocol Command \ ``sg``\  - TPC argument

    :param mrq:
        *undescribed*
    :type mrq: struct memstick_request \*

    :param tpc:
        *undescribed*
    :type tpc: unsigned char

    :param sg:
        *undescribed*
    :type sg: const struct scatterlist \*

.. _`memstick_init_req`:

memstick_init_req
=================

.. c:function:: void memstick_init_req(struct memstick_request *mrq, unsigned char tpc, const void *buf, size_t length)

    set request fields needed for short data transfer \ ``mrq``\  - request to use \ ``tpc``\  - memstick Transport Protocol Command \ ``buf``\  - TPC argument buffer \ ``length``\  - TPC argument size

    :param mrq:
        *undescribed*
    :type mrq: struct memstick_request \*

    :param tpc:
        *undescribed*
    :type tpc: unsigned char

    :param buf:
        *undescribed*
    :type buf: const void \*

    :param length:
        *undescribed*
    :type length: size_t

.. _`memstick_init_req.description`:

Description
-----------

The intended use of this function (transfer of data items several bytes
in size) allows us to just copy the value between request structure and
user supplied buffer.

.. _`memstick_set_rw_addr`:

memstick_set_rw_addr
====================

.. c:function:: int memstick_set_rw_addr(struct memstick_dev *card)

    issue SET_RW_REG_ADDR request and wait for it to complete \ ``card``\  - media device to use

    :param card:
        *undescribed*
    :type card: struct memstick_dev \*

.. _`memstick_alloc_host`:

memstick_alloc_host
===================

.. c:function:: struct memstick_host *memstick_alloc_host(unsigned int extra, struct device *dev)

    allocate a memstick_host structure

    :param extra:
        size of the user private data to allocate
    :type extra: unsigned int

    :param dev:
        parent device of the host
    :type dev: struct device \*

.. _`memstick_add_host`:

memstick_add_host
=================

.. c:function:: int memstick_add_host(struct memstick_host *host)

    start request processing on memstick host \ ``host``\  - host to use

    :param host:
        *undescribed*
    :type host: struct memstick_host \*

.. _`memstick_remove_host`:

memstick_remove_host
====================

.. c:function:: void memstick_remove_host(struct memstick_host *host)

    stop request processing on memstick host \ ``host``\  - host to use

    :param host:
        *undescribed*
    :type host: struct memstick_host \*

.. _`memstick_free_host`:

memstick_free_host
==================

.. c:function:: void memstick_free_host(struct memstick_host *host)

    free memstick host \ ``host``\  - host to use

    :param host:
        *undescribed*
    :type host: struct memstick_host \*

.. _`memstick_suspend_host`:

memstick_suspend_host
=====================

.. c:function:: void memstick_suspend_host(struct memstick_host *host)

    notify bus driver of host suspension \ ``host``\  - host to use

    :param host:
        *undescribed*
    :type host: struct memstick_host \*

.. _`memstick_resume_host`:

memstick_resume_host
====================

.. c:function:: void memstick_resume_host(struct memstick_host *host)

    notify bus driver of host resumption \ ``host``\  - host to use

    :param host:
        *undescribed*
    :type host: struct memstick_host \*

.. This file was automatic generated / don't edit.

