.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvme/host/fc.c

.. _`nvme_fc_register_localport`:

nvme_fc_register_localport
==========================

.. c:function:: int nvme_fc_register_localport(struct nvme_fc_port_info *pinfo, struct nvme_fc_port_template *template, struct device *dev, struct nvme_fc_local_port **portptr)

    transport entry point called by an LLDD to register the existence of a NVME host FC port.

    :param pinfo:
        pointer to information about the port to be registered
    :type pinfo: struct nvme_fc_port_info \*

    :param template:
        LLDD entrypoints and operational parameters for the port
    :type template: struct nvme_fc_port_template \*

    :param dev:
        physical hardware device node port corresponds to. Will be
        used for DMA mappings
    :type dev: struct device \*

    :param portptr:
        pointer to a local port pointer. Upon success, the routine
        will allocate a nvme_fc_local_port structure and place its
        address in the local port pointer. Upon failure, local port
        pointer will be set to 0.
    :type portptr: struct nvme_fc_local_port \*\*

.. _`nvme_fc_register_localport.return`:

Return
------

a completion status. Must be 0 upon success; a negative errno
(ex: -ENXIO) upon failure.

.. _`nvme_fc_unregister_localport`:

nvme_fc_unregister_localport
============================

.. c:function:: int nvme_fc_unregister_localport(struct nvme_fc_local_port *portptr)

    transport entry point called by an LLDD to deregister/remove a previously registered a NVME host FC port.

    :param portptr:
        pointer to the (registered) local port that is to be deregistered.
    :type portptr: struct nvme_fc_local_port \*

.. _`nvme_fc_unregister_localport.return`:

Return
------

a completion status. Must be 0 upon success; a negative errno
(ex: -ENXIO) upon failure.

.. _`nvme_fc_register_remoteport`:

nvme_fc_register_remoteport
===========================

.. c:function:: int nvme_fc_register_remoteport(struct nvme_fc_local_port *localport, struct nvme_fc_port_info *pinfo, struct nvme_fc_remote_port **portptr)

    transport entry point called by an LLDD to register the existence of a NVME subsystem FC port on its fabric.

    :param localport:
        pointer to the (registered) local port that the remote
        subsystem port is connected to.
    :type localport: struct nvme_fc_local_port \*

    :param pinfo:
        pointer to information about the port to be registered
    :type pinfo: struct nvme_fc_port_info \*

    :param portptr:
        pointer to a remote port pointer. Upon success, the routine
        will allocate a nvme_fc_remote_port structure and place its
        address in the remote port pointer. Upon failure, remote port
        pointer will be set to 0.
    :type portptr: struct nvme_fc_remote_port \*\*

.. _`nvme_fc_register_remoteport.return`:

Return
------

a completion status. Must be 0 upon success; a negative errno
(ex: -ENXIO) upon failure.

.. _`nvme_fc_unregister_remoteport`:

nvme_fc_unregister_remoteport
=============================

.. c:function:: int nvme_fc_unregister_remoteport(struct nvme_fc_remote_port *portptr)

    transport entry point called by an LLDD to deregister/remove a previously registered a NVME subsystem FC port.

    :param portptr:
        pointer to the (registered) remote port that is to be
        deregistered.
    :type portptr: struct nvme_fc_remote_port \*

.. _`nvme_fc_unregister_remoteport.return`:

Return
------

a completion status. Must be 0 upon success; a negative errno
(ex: -ENXIO) upon failure.

.. _`nvme_fc_rescan_remoteport`:

nvme_fc_rescan_remoteport
=========================

.. c:function:: void nvme_fc_rescan_remoteport(struct nvme_fc_remote_port *remoteport)

    transport entry point called by an LLDD to request a nvme device rescan.

    :param remoteport:
        pointer to the (registered) remote port that is to be
        rescanned.
    :type remoteport: struct nvme_fc_remote_port \*

.. _`nvme_fc_rescan_remoteport.return`:

Return
------

N/A

.. This file was automatic generated / don't edit.

