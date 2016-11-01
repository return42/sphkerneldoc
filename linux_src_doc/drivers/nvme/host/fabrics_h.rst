.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvme/host/fabrics.h

.. _`nvmf_ctrl_options`:

struct nvmf_ctrl_options
========================

.. c:type:: struct nvmf_ctrl_options

    Used to hold the options specified with the parsing opts enum.

.. _`nvmf_ctrl_options.definition`:

Definition
----------

.. code-block:: c

    struct nvmf_ctrl_options {
        unsigned mask;
        char *transport;
        char *subsysnqn;
        char *traddr;
        char *trsvcid;
        char *host_traddr;
        size_t queue_size;
        unsigned int nr_io_queues;
        unsigned int reconnect_delay;
        bool discovery_nqn;
        unsigned int kato;
        struct nvmf_host *host;
    }

.. _`nvmf_ctrl_options.members`:

Members
-------

mask
    Used by the fabrics library to parse through sysfs options
    on adding a NVMe controller.

transport
    Holds the fabric transport "technology name" (for a lack of
    better description) that will be used by an NVMe controller
    being added.

subsysnqn
    Hold the fully qualified NQN subystem name (format defined
    in the NVMe specification, "NVMe Qualified Names").

traddr
    The transport-specific TRADDR field for a port on the
    subsystem which is adding a controller.

trsvcid
    The transport-specific TRSVCID field for a port on the
    subsystem which is adding a controller.

host_traddr
    A transport-specific field identifying the NVME host port
    to use for the connection to the controller.

queue_size
    Number of IO queue elements.

nr_io_queues
    Number of controller IO queues that will be established.

reconnect_delay
    Time between two consecutive reconnect attempts.

discovery_nqn
    indicates if the subsysnqn is the well-known discovery NQN.

kato
    Keep-alive timeout.

host
    Virtual NVMe host, contains the NQN and Host ID.

.. This file was automatic generated / don't edit.

