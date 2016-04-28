.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-slave-link-init:

===================
ata_slave_link_init
===================

*man ata_slave_link_init(9)*

*4.6.0-rc5*

initialize slave link


Synopsis
========

.. c:function:: int ata_slave_link_init( struct ata_port * ap )

Arguments
=========

``ap``
    port to initialize slave link for


Description
===========

Create and initialize slave link for ``ap``. This enables slave link
handling on the port.

In libata, a port contains links and a link contains devices. There is
single host link but if a PMP is attached to it, there can be multiple
fan-out links. On SATA, there's usually a single device connected to a
link but PATA and SATA controllers emulating TF based interface can have
two - master and slave.

However, there are a few controllers which don't fit into this
abstraction too well - SATA controllers which emulate TF interface with
both master and slave devices but also have separate SCR register sets
for each device. These controllers need separate links for physical link
handling (e.g. onlineness, link speed) but should be treated like a
traditional M/S controller for everything else (e.g. command issue,
softreset).

slave_link is libata's way of handling this class of controllers
without impacting core layer too much. For anything other than physical
link handling, the default host link is used for both master and slave.
For physical link handling, separate ``ap``->slave_link is used. All
dirty details are implemented inside libata core layer. From LLD's POV,
the only difference is that prereset, hardreset and postreset are called
once more for the slave link, so the reset sequence looks like the
following.

prereset(M) -> prereset(S) -> hardreset(M) -> hardreset(S) ->
softreset(M) -> postreset(M) -> postreset(S)

Note that softreset is called only for the master. Softreset resets both
M/S by definition, so SRST on master should handle both (the standard
method will work just fine).


LOCKING
=======

Should be called before host is registered.


RETURNS
=======

0 on success, -errno on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
