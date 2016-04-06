
.. _queues:

================================
Wait Queues include/linux/wait.h
================================

*[SLEEPS]*

A wait queue is used to wait for someone to wake you up when a certain condition is true. They must be used carefully to ensure there is no race condition. You declare a
``wait_queue_head_t``, and then processes which want to wait for that condition declare a ``wait_queue_t`` referring to themselves, and place that in the queue.


.. _queue-declaring:

Declaring
=========

You declare a ``wait_queue_head_t`` using the ``DECLARE_WAIT_QUEUE_HEAD()`` macro, or using the ``init_waitqueue_head()`` routine in your initialization code.


.. _queue-waitqueue:

Queuing
=======

Placing yourself in the waitqueue is fairly complex, because you must put yourself in the queue before checking the condition. There is a macro to do this:
``wait_event_interruptible()`` ``include/linux/wait.h`` The first argument is the wait queue head, and the second is an expression which is evaluated; the macro returns 0 when this
expression is true, or -ERESTARTSYS if a signal is received. The ``wait_event()`` version ignores signals.


.. _queue-waking:

Waking Up Queued Tasks
======================

Call ``wake_up()`` ``include/linux/wait.h``;, which will wake up every process in the queue. The exception is if one has ``TASK_EXCLUSIVE`` set, in which case the remainder of the
queue will not be woken. There are other variants of this basic function available in the same header.
