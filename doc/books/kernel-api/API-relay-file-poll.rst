
.. _API-relay-file-poll:

===============
relay_file_poll
===============

*man relay_file_poll(9)*

*4.6.0-rc1*

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
