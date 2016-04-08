
.. _API-snd-BUG:

=======
snd_BUG
=======

*man snd_BUG(9)*

*4.6.0-rc1*

give a BUG warning message and stack trace


Synopsis
========

.. c:function:: snd_BUG(  )

Arguments
=========

None


Description
===========

Calls ``WARN`` if CONFIG_SND_DEBUG is set. Ignored when CONFIG_SND_DEBUG is not set.
