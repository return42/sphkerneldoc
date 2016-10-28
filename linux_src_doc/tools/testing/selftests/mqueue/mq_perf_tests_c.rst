.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/testing/selftests/mqueue/mq_perf_tests.c

.. _`open_queue`:

open_queue
==========

.. c:function:: void open_queue(struct mq_attr *attr)

    open the global queue for testing \ ``attr``\  - An attr struct specifying the desired queue traits \ ``result``\  - An attr struct that lists the actual traits the queue has

    :param struct mq_attr \*attr:
        *undescribed*

.. _`open_queue.description`:

Description
-----------

This open is not allowed to fail, failure will result in an orderly
shutdown of the program.  The global queue_path is used to set what
queue to open, the queue descriptor is saved in the global queue
variable.

.. _`perf_test_thread`:

perf_test_thread
================

.. c:function:: void *perf_test_thread(void *arg)

    :param void \*arg:
        *undescribed*

.. _`perf_test_thread.description`:

Description
-----------

1) Time to add/remove message with 0 messages on queue
1a) with constant prio
2) Time to add/remove message when queue close to capacity:
2a) with constant prio
2b) with increasing prio
2c) with decreasing prio
2d) with random prio
3) Test limits of priorities honored (double check \_SC_MQ_PRIO_MAX)

.. This file was automatic generated / don't edit.

