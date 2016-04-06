
.. _API-audit-log-end:

=============
audit_log_end
=============

*man audit_log_end(9)*

*4.6.0-rc1*

end one audit record


Synopsis
========

.. c:function:: void audit_log_end( struct audit_buffer * ab )

Arguments
=========

``ab``
    the audit_buffer


Description
===========

``netlink_unicast`` cannot be called inside an irq context because it blocks (last arg, flags, is not set to MSG_DONTWAIT), so the audit buffer is placed on a queue and a tasklet
is scheduled to remove them from the queue outside the irq context. May be called in any context.
