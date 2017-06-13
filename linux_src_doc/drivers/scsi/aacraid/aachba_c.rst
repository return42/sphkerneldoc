.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aacraid/aachba.c

.. _`aac_get_config_status`:

aac_get_config_status
=====================

.. c:function:: int aac_get_config_status(struct aac_dev *dev, int commit_flag)

    check the adapter configuration

    :param struct aac_dev \*dev:
        *undescribed*

    :param int commit_flag:
        *undescribed*

.. _`aac_get_config_status.description`:

Description
-----------

Query config status, and commit the configuration if needed.

.. _`aac_get_containers`:

aac_get_containers
==================

.. c:function:: int aac_get_containers(struct aac_dev *dev)

    list containers

    :param struct aac_dev \*dev:
        *undescribed*

.. _`aac_get_containers.description`:

Description
-----------

Make a list of all containers on this controller

.. _`aac_get_container_name`:

aac_get_container_name
======================

.. c:function:: int aac_get_container_name(struct scsi_cmnd *scsicmd)

    get container name, none blocking.

    :param struct scsi_cmnd \*scsicmd:
        *undescribed*

.. _`aac_probe_container_callback1`:

aac_probe_container_callback1
=============================

.. c:function:: int aac_probe_container_callback1(struct scsi_cmnd *scsicmd)

    query a logical volume

    :param struct scsi_cmnd \*scsicmd:
        *undescribed*

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

    :param char \*a:
        string to copy from

    :param char \*b:
        string to copy to

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

    :param struct scsi_cmnd \*scsicmd:
        *undescribed*

.. _`aac_update_hba_map`:

aac_update_hba_map
==================

.. c:function:: void aac_update_hba_map(struct aac_dev *dev, struct aac_ciss_phys_luns_resp *phys_luns, int rescan)

    update current hba map with data from FW

    :param struct aac_dev \*dev:
        aac_dev structure

    :param struct aac_ciss_phys_luns_resp \*phys_luns:
        FW information from report phys luns

    :param int rescan:
        *undescribed*

.. _`aac_update_hba_map.description`:

Description
-----------

Update our hba map with the information gathered from the FW

.. _`aac_report_phys_luns`:

aac_report_phys_luns
====================

.. c:function:: int aac_report_phys_luns(struct aac_dev *dev, struct fib *fibptr, int rescan)

    :param struct aac_dev \*dev:
        aac_dev structure

    :param struct fib \*fibptr:
        fib pointer

    :param int rescan:
        *undescribed*

.. _`aac_report_phys_luns.description`:

Description
-----------

Execute a CISS REPORT PHYS LUNS and process the results into
the current hba_map.

.. _`aac_scsi_cmd`:

aac_scsi_cmd
============

.. c:function:: int aac_scsi_cmd(struct scsi_cmnd *scsicmd)

    Process SCSI command

    :param struct scsi_cmnd \*scsicmd:
        SCSI command block

.. _`aac_scsi_cmd.description`:

Description
-----------

Emulate a SCSI command and queue the required request for the
aacraid firmware.

.. This file was automatic generated / don't edit.

