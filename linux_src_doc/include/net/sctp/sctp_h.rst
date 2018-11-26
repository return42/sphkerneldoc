.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/sctp/sctp.h

.. _`sctp_list_dequeue`:

sctp_list_dequeue
=================

.. c:function:: struct list_head *sctp_list_dequeue(struct list_head *list)

    remove from the head of the queue

    :param list:
        list to dequeue from
    :type list: struct list_head \*

.. _`sctp_list_dequeue.description`:

Description
-----------

Remove the head of the list. The head item is
returned or \ ``NULL``\  if the list is empty.

.. This file was automatic generated / don't edit.

