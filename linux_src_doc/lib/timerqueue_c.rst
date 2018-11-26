.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/timerqueue.c

.. _`timerqueue_add`:

timerqueue_add
==============

.. c:function:: bool timerqueue_add(struct timerqueue_head *head, struct timerqueue_node *node)

    Adds timer to timerqueue.

    :param head:
        head of timerqueue
    :type head: struct timerqueue_head \*

    :param node:
        timer node to be added
    :type node: struct timerqueue_node \*

.. _`timerqueue_add.description`:

Description
-----------

Adds the timer node to the timerqueue, sorted by the node's expires
value. Returns true if the newly added timer is the first expiring timer in
the queue.

.. _`timerqueue_del`:

timerqueue_del
==============

.. c:function:: bool timerqueue_del(struct timerqueue_head *head, struct timerqueue_node *node)

    Removes a timer from the timerqueue.

    :param head:
        head of timerqueue
    :type head: struct timerqueue_head \*

    :param node:
        timer node to be removed
    :type node: struct timerqueue_node \*

.. _`timerqueue_del.description`:

Description
-----------

Removes the timer node from the timerqueue. Returns true if the queue is
not empty after the remove.

.. _`timerqueue_iterate_next`:

timerqueue_iterate_next
=======================

.. c:function:: struct timerqueue_node *timerqueue_iterate_next(struct timerqueue_node *node)

    Returns the timer after the provided timer

    :param node:
        Pointer to a timer.
    :type node: struct timerqueue_node \*

.. _`timerqueue_iterate_next.description`:

Description
-----------

Provides the timer that is after the given node. This is used, when
necessary, to iterate through the list of timers in a timer list
without modifying the list.

.. This file was automatic generated / don't edit.

