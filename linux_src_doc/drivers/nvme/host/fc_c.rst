.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvme/host/fc.c

.. _`nvme_fc_register_localport`:

nvme_fc_register_localport
==========================

.. c:function:: int nvme_fc_register_localport(struct nvme_fc_port_info *pinfo, struct nvme_fc_port_template *template, struct device *dev, struct nvme_fc_local_port **portptr)

    transport entry point called by an LLDD to register the existence of a NVME host FC port.

    :param struct nvme_fc_port_info \*pinfo:
        pointer to information about the port to be registered

    :param struct nvme_fc_port_template \*template:
        LLDD entrypoints and operational parameters for the port

    :param struct device \*dev:
        physical hardware device node port corresponds to. Will be
        used for DMA mappings

    :param struct nvme_fc_local_port \*\*portptr:
        *undescribed*

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

    :param struct nvme_fc_local_port \*portptr:
        *undescribed*

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

    :param struct nvme_fc_local_port \*localport:
        pointer to the (registered) local port that the remote
        subsystem port is connected to.

    :param struct nvme_fc_port_info \*pinfo:
        pointer to information about the port to be registered

    :param struct nvme_fc_remote_port \*\*portptr:
        *undescribed*

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

    :param struct nvme_fc_remote_port \*portptr:
        *undescribed*

.. _`nvme_fc_unregister_remoteport.return`:

Return
------

a completion status. Must be 0 upon success; a negative errno
(ex: -ENXIO) upon failure.

.. This file was automatic generated / don't edit.
