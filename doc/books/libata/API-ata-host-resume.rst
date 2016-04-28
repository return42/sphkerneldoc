.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-host-resume:

===============
ata_host_resume
===============

*man ata_host_resume(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
