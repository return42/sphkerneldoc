.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/trace/events/workqueue.h

.. _`trace_workqueue_queue_work`:

trace_workqueue_queue_work
==========================

.. c:function:: void trace_workqueue_queue_work(unsigned int req_cpu, struct pool_workqueue *pwq, struct work_struct *work)

    called when a work gets queued

    :param unsigned int req_cpu:
        the requested cpu

    :param struct pool_workqueue \*pwq:
        pointer to struct pool_workqueue

    :param struct work_struct \*work:
        pointer to struct work_struct

.. _`trace_workqueue_queue_work.description`:

Description
-----------

This event occurs when a work is queued immediately or once a
delayed work is actually queued on a workqueue (ie: once the delay
has been reached).

.. _`trace_workqueue_activate_work`:

trace_workqueue_activate_work
=============================

.. c:function:: void trace_workqueue_activate_work(struct work_struct *work)

    called when a work gets activated

    :param struct work_struct \*work:
        pointer to struct work_struct

.. _`trace_workqueue_activate_work.description`:

Description
-----------

This event occurs when a queued work is put on the active queue,
which happens immediately after queueing unless \ ``max_active``\  limit
is reached.

.. _`trace_workqueue_execute_start`:

trace_workqueue_execute_start
=============================

.. c:function:: void trace_workqueue_execute_start(struct work_struct *work)

    called immediately before the workqueue callback

    :param struct work_struct \*work:
        pointer to struct work_struct

.. _`trace_workqueue_execute_start.description`:

Description
-----------

Allows to track workqueue execution.

.. _`trace_workqueue_execute_end`:

trace_workqueue_execute_end
===========================

.. c:function:: void trace_workqueue_execute_end(struct work_struct *work)

    called immediately after the workqueue callback

    :param struct work_struct \*work:
        pointer to struct work_struct

.. _`trace_workqueue_execute_end.description`:

Description
-----------

Allows to track workqueue execution.

.. This file was automatic generated / don't edit.

