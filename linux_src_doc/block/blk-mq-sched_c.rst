.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-mq-sched.c

.. _`list_for_each_entry_rcu_rr`:

list_for_each_entry_rcu_rr
==========================

.. c:function::  list_for_each_entry_rcu_rr( pos,  skip,  head,  member)

    iterate in a round-robin fashion over rcu list

    :param  pos:
        loop cursor.

    :param  skip:
        the list element that will not be examined. Iteration starts at
        \ ``skip``\ ->next.

    :param  head:
        head of the list to examine. This list must have at least one
        element, namely \ ``skip``\ .

    :param  member:
        name of the list_head structure within typeof(\*pos).

.. This file was automatic generated / don't edit.

