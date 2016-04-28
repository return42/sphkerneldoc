.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-clk-notifier:

===================
struct clk_notifier
===================

*man struct clk_notifier(9)*

*4.6.0-rc5*

associate a clk with a notifier


Synopsis
========

.. code-block:: c

    struct clk_notifier {
      struct clk * clk;
      struct srcu_notifier_head notifier_head;
      struct list_head node;
    };


Members
=======

clk
    struct clk * to associate the notifier with

notifier_head
    a blocking_notifier_head for this clk

node
    linked list pointers


Description
===========

A list of struct clk_notifier is maintained by the notifier code. An
entry is created whenever code registers the first notifier on a
particular ``clk``. Future notifiers on that ``clk`` are added to the
``notifier_head``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
