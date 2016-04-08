
.. _API-rio-pw-enable:

=============
rio_pw_enable
=============

*man rio_pw_enable(9)*

*4.6.0-rc1*

Enables/disables port-write handling by a master port


Synopsis
========

.. c:function:: void rio_pw_enable( struct rio_mport * mport, int enable )

Arguments
=========

``mport``
    Master port associated with port-write handling

``enable``
    1=enable, 0=disable
