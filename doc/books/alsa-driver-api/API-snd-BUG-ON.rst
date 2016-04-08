
.. _API-snd-BUG-ON:

==========
snd_BUG_ON
==========

*man snd_BUG_ON(9)*

*4.6.0-rc1*

debugging check macro


Synopsis
========

.. c:function:: snd_BUG_ON( cond )

Arguments
=========

``cond``
    condition to evaluate


Description
===========

Has the same behavior as WARN_ON when CONFIG_SND_DEBUG is set, otherwise just evaluates the conditional and returns the value.
