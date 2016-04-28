.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-file-poll:

===============
relay_file_poll
===============

*man relay_file_poll(9)*

*4.6.0-rc5*

poll file op for relay files


Synopsis
========

.. c:function:: unsigned int relay_file_poll( struct file * filp, poll_table * wait )

Arguments
=========

``filp``
    the file

``wait``
    poll table


Description
===========

Poll implemention.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
