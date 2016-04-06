
.. _API-cpupri-set:

==========
cpupri_set
==========

*man cpupri_set(9)*

*4.6.0-rc1*

update the cpu priority setting


Synopsis
========

.. c:function:: void cpupri_set( struct cpupri * cp, int cpu, int newpri )

Arguments
=========

``cp``
    The cpupri context

``cpu``
    The target cpu

``newpri``
    The priority (INVALID-RT99) to assign to this CPU


Note
====

Assumes cpu_rq(cpu)->lock is locked


Returns
=======

(void)
