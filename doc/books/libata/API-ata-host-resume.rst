
.. _API-ata-host-resume:

===============
ata_host_resume
===============

*man ata_host_resume(9)*

*4.6.0-rc1*

resume host


Synopsis
========

.. c:function:: void ata_host_resume( struct ata_host * host )

Arguments
=========

``host``
    host to resume


Description
===========

Resume ``host``. Actual operation is performed by port resume.
