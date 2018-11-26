.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aacraid/aachba.c

.. _`aac_get_config_status`:

aac_get_config_status
=====================

.. c:function:: int aac_get_config_status(struct aac_dev *dev, int commit_flag)

    check the adapter configuration

    :param dev:
        *undescribed*
    :type dev: struct aac_dev \*

    :param commit_flag:
        *undescribed*
    :type commit_flag: int

.. _`aac_get_config_status.description`:

Description
-----------

Query config status, and commit the configuration if needed.

.. _`aac_get_containers`:

aac_get_containers
==================

.. c:function:: int aac_get_containers(struct aac_dev *dev)

    list containers

    :param dev:
        *undescribed*
    :type dev: struct aac_dev \*

.. _`aac_get_containers.description`:

Description
-----------

Make a list of all containers on this controller

.. _`aac_get_container_name`:

aac_get_container_name
======================

.. c:function:: int aac_get_container_name(struct scsi_cmnd *scsicmd)

    get container name, none blocking.

    :param scsicmd:
        *undescribed*
    :type scsicmd: struct scsi_cmnd \*

.. _`aac_probe_container_callback1`:

aac_probe_container_callback1
=============================

.. c:function:: int aac_probe_container_callback1(struct scsi_cmnd *scsicmd)

    query a logical volume

    :param scsicmd:
        *undescribed*
    :type scsicmd: struct scsi_cmnd \*

.. _`aac_probe_container_callback1.description`:

Description
-----------

Queries the controller about the given volume. The volume information
is updated in the struct fsa_dev_info structure rather than returned.

.. _`inqstrcpy`:

inqstrcpy
=========

.. c:function:: void inqstrcpy(char *a, char *b)

    string merge

    :param a:
        string to copy from
    :type a: char \*

    :param b:
        string to copy to
    :type b: char \*

.. _`inqstrcpy.description`:

Description
-----------

Copy a String from one location to another
without copying \0

.. _`aac_get_container_serial`:

aac_get_container_serial
========================

.. c:function:: int aac_get_container_serial(struct scsi_cmnd *scsicmd)

    get container serial, none blocking.

    :param scsicmd:
        *undescribed*
    :type scsicmd: struct scsi_cmnd \*

.. _`aac_get_safw_ciss_luns`:

aac_get_safw_ciss_luns
======================

.. c:function:: int aac_get_safw_ciss_luns(struct aac_dev *dev)

    :param dev:
        aac_dev structure
    :type dev: struct aac_dev \*

.. _`aac_get_safw_ciss_luns.description`:

Description
-----------

Execute a CISS REPORT PHYS LUNS and process the results into
the current hba_map.

.. _`aac_set_safw_attr_all_targets`:

aac_set_safw_attr_all_targets
=============================

.. c:function:: void aac_set_safw_attr_all_targets(struct aac_dev *dev)

    update current hba map with data from FW

    :param dev:
        aac_dev structure
    :type dev: struct aac_dev \*

.. _`aac_set_safw_attr_all_targets.description`:

Description
-----------

Update our hba map with the information gathered from the FW

.. _`aac_scsi_cmd`:

aac_scsi_cmd
============

.. c:function:: int aac_scsi_cmd(struct scsi_cmnd *scsicmd)

    Process SCSI command

    :param scsicmd:
        SCSI command block
    :type scsicmd: struct scsi_cmnd \*

.. _`aac_scsi_cmd.description`:

Description
-----------

Emulate a SCSI command and queue the required request for the
aacraid firmware.

.. This file was automatic generated / don't edit.

