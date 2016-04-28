.. -*- coding: utf-8; mode: rst -*-

.. _API-wdev-priv:

=========
wdev_priv
=========

*man wdev_priv(9)*

*4.6.0-rc5*

return wiphy priv from wireless_dev


Synopsis
========

.. c:function:: void * wdev_priv( struct wireless_dev * wdev )

Arguments
=========

``wdev``
    The wireless device whose wiphy's priv pointer to return


Return
======

The wiphy priv of ``wdev``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
