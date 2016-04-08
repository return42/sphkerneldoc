
.. _API-wdev-priv:

=========
wdev_priv
=========

*man wdev_priv(9)*

*4.6.0-rc1*

return wiphy priv from wireless_dev


Synopsis
========

.. c:function:: void ⋆ wdev_priv( struct wireless_dev * wdev )

Arguments
=========

``wdev``
    The wireless device whose wiphy's priv pointer to return


Return
======

The wiphy priv of ``wdev``.
