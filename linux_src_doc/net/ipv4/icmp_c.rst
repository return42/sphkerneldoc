.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv4/icmp.c

.. _`icmp_global_allow`:

icmp_global_allow
=================

.. c:function:: bool icmp_global_allow( void)

    Are we allowed to send one more ICMP message ?

    :param  void:
        no arguments

.. _`icmp_global_allow.description`:

Description
-----------

Uses a token bucket to limit our ICMP messages to sysctl_icmp_msgs_per_sec.
Returns false if we reached the limit and can not send another packet.

.. _`icmp_global_allow.note`:

Note
----

called with BH disabled

.. This file was automatic generated / don't edit.

