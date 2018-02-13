.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/xdp.h

.. _`xdp-rx-queue-information`:

XDP RX-queue information
========================

The XDP RX-queue info (xdp_rxq_info) is associated with the driver
level RX-ring queues.  It is information that is specific to how
the driver have configured a given RX-ring queue.

Each xdp_buff frame received in the driver carry a (pointer)
reference to this xdp_rxq_info structure.  This provides the XDP
data-path read-access to RX-info for both kernel and bpf-side
(limited subset).

For now, direct access is only safe while running in NAPI/softirq
context.  Contents is read-mostly and must not be updated during
driver NAPI/softirq poll.

The driver usage API is a register and unregister API.

The struct is not directly tied to the XDP prog.  A new XDP prog
can be attached as long as it doesn't change the underlying
RX-ring.  If the RX-ring does change significantly, the NIC driver
naturally need to stop the RX-ring before purging and reallocating
memory.  In that process the driver MUST call unregistor (which
also apply for driver shutdown and unload).  The register API is
also mandatory during RX-ring setup.

.. This file was automatic generated / don't edit.

