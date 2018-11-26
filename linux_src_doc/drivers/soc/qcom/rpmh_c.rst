.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/rpmh.c

.. _`cache_req`:

struct cache_req
================

.. c:type:: struct cache_req

    the request object for caching

.. _`cache_req.definition`:

Definition
----------

.. code-block:: c

    struct cache_req {
        u32 addr;
        u32 sleep_val;
        u32 wake_val;
        struct list_head list;
    }

.. _`cache_req.members`:

Members
-------

addr
    the address of the resource

sleep_val
    the sleep vote

wake_val
    the wake vote

list
    linked list obj

.. _`batch_cache_req`:

struct batch_cache_req
======================

.. c:type:: struct batch_cache_req

    An entry in our batch catch

.. _`batch_cache_req.definition`:

Definition
----------

.. code-block:: c

    struct batch_cache_req {
        struct list_head list;
        int count;
        struct rpmh_request rpm_msgs[];
    }

.. _`batch_cache_req.members`:

Members
-------

list
    linked list obj

count
    number of messages

rpm_msgs
    the messages

.. _`__rpmh_write`:

\__rpmh_write
=============

.. c:function:: int __rpmh_write(const struct device *dev, enum rpmh_state state, struct rpmh_request *rpm_msg)

    Cache and send the RPMH request

    :param dev:
        The device making the request
    :type dev: const struct device \*

    :param state:
        Active/Sleep request type
    :type state: enum rpmh_state

    :param rpm_msg:
        The data that needs to be sent (cmds).
    :type rpm_msg: struct rpmh_request \*

.. _`__rpmh_write.description`:

Description
-----------

Cache the RPMH request and send if the state is ACTIVE_ONLY.
SLEEP/WAKE_ONLY requests are not sent to the controller at
this time. Use \ :c:func:`rpmh_flush`\  to send them to the controller.

.. _`rpmh_write_async`:

rpmh_write_async
================

.. c:function:: int rpmh_write_async(const struct device *dev, enum rpmh_state state, const struct tcs_cmd *cmd, u32 n)

    Write a set of RPMH commands

    :param dev:
        The device making the request
    :type dev: const struct device \*

    :param state:
        Active/sleep set
    :type state: enum rpmh_state

    :param cmd:
        The payload data
    :type cmd: const struct tcs_cmd \*

    :param n:
        The number of elements in payload
    :type n: u32

.. _`rpmh_write_async.description`:

Description
-----------

Write a set of RPMH commands, the order of commands is maintained
and will be sent as a single shot.

.. _`rpmh_write`:

rpmh_write
==========

.. c:function:: int rpmh_write(const struct device *dev, enum rpmh_state state, const struct tcs_cmd *cmd, u32 n)

    Write a set of RPMH commands and block until response

    :param dev:
        *undescribed*
    :type dev: const struct device \*

    :param state:
        Active/sleep set
    :type state: enum rpmh_state

    :param cmd:
        The payload data
    :type cmd: const struct tcs_cmd \*

    :param n:
        The number of elements in \ ``cmd``\ 
    :type n: u32

.. _`rpmh_write.description`:

Description
-----------

May sleep. Do not call from atomic contexts.

.. _`rpmh_write_batch`:

rpmh_write_batch
================

.. c:function:: int rpmh_write_batch(const struct device *dev, enum rpmh_state state, const struct tcs_cmd *cmd, u32 *n)

    Write multiple sets of RPMH commands and wait for the batch to finish.

    :param dev:
        the device making the request
    :type dev: const struct device \*

    :param state:
        Active/sleep set
    :type state: enum rpmh_state

    :param cmd:
        The payload data
    :type cmd: const struct tcs_cmd \*

    :param n:
        The array of count of elements in each batch, 0 terminated.
    :type n: u32 \*

.. _`rpmh_write_batch.description`:

Description
-----------

Write a request to the RSC controller without caching. If the request
state is ACTIVE, then the requests are treated as completion request
and sent to the controller immediately. The function waits until all the
commands are complete. If the request was to SLEEP or WAKE_ONLY, then the
request is sent as fire-n-forget and no ack is expected.

May sleep. Do not call from atomic contexts for ACTIVE_ONLY requests.

.. _`rpmh_flush`:

rpmh_flush
==========

.. c:function:: int rpmh_flush(const struct device *dev)

    Flushes the buffered active and sleep sets to TCS

    :param dev:
        The device making the request
    :type dev: const struct device \*

.. _`rpmh_flush.return`:

Return
------

-EBUSY if the controller is busy, probably waiting on a response
to a RPMH request sent earlier.

This function is always called from the sleep code from the last CPU
that is powering down the entire system. Since no other RPMH API would be
executing at this time, it is safe to run lockless.

.. _`rpmh_invalidate`:

rpmh_invalidate
===============

.. c:function:: int rpmh_invalidate(const struct device *dev)

    Invalidate all sleep and active sets sets.

    :param dev:
        The device making the request
    :type dev: const struct device \*

.. _`rpmh_invalidate.description`:

Description
-----------

Invalidate the sleep and active values in the TCS blocks.

.. This file was automatic generated / don't edit.

