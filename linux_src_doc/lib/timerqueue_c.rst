.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/timerqueue.c

.. _`timerqueue_add`:

timerqueue_add
==============

.. c:function:: bool timerqueue_add(struct timerqueue_head *head, struct timerqueue_node *node)

    Adds timer to timerqueue.

    :param struct timerqueue_head \*head:
        head of timerqueue

    :param struct timerqueue_node \*node:
        timer node to be added

.. _`timerqueue_add.description`:

Description
-----------

Adds the timer node to the timerqueue, sorted by the
node's expires value.

.. _`timerqueue_del`:

timerqueue_del
==============

.. c:function:: bool timerqueue_del(struct timerqueue_head *head, struct timerqueue_node *node)

    Removes a timer from the timerqueue.

    :param struct timerqueue_head \*head:
        head of timerqueue

    :param struct timerqueue_node \*node:
        timer node to be removed

.. _`timerqueue_del.description`:

Description
-----------

Removes the timer node from the timerqueue.

.. _`timerqueue_iterate_next`:

timerqueue_iterate_next
=======================

.. c:function:: struct timerqueue_node *timerqueue_iterate_next(struct timerqueue_node *node)

    Returns the timer after the provided timer

    :param struct timerqueue_node \*node:
        Pointer to a timer.

.. _`timerqueue_iterate_next.description`:

Description
-----------

Provides the timer that is after the given node. This is used, when
necessary, to iterate through the list of timers in a timer list
without modifying the list.

.. This file was automatic generated / don't edit.

