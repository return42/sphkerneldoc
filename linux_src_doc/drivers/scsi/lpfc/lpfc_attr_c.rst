.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_attr.c

.. _`lpfc_jedec_to_ascii`:

lpfc_jedec_to_ascii
===================

.. c:function:: void lpfc_jedec_to_ascii(int incr, char hdw)

    Hex to ascii convertor according to JEDEC rules

    :param int incr:
        integer to convert.

    :param char hdw:
        ascii string holding converted integer plus a string terminator.

.. _`lpfc_jedec_to_ascii.description`:

Description
-----------

JEDEC Joint Electron Device Engineering Council.
Convert a 32 bit integer composed of 8 nibbles into an 8 byte ascii
character string. The string is then terminated with a NULL in byte 9.
Hex 0-9 becomes ascii '0' to '9'.
Hex a-f becomes ascii '=' to 'B' capital B.

.. _`lpfc_jedec_to_ascii.notes`:

Notes
-----

Coded for 32 bit integers only.

.. _`lpfc_drvr_version_show`:

lpfc_drvr_version_show
======================

.. c:function:: ssize_t lpfc_drvr_version_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the Emulex driver string with version number

    :param struct device \*dev:
        class unused variable.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the module description text.

.. _`lpfc_drvr_version_show.return`:

Return
------

size of formatted string.

.. _`lpfc_enable_fip_show`:

lpfc_enable_fip_show
====================

.. c:function:: ssize_t lpfc_enable_fip_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the fip mode of the HBA

    :param struct device \*dev:
        class unused variable.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the module description text.

.. _`lpfc_enable_fip_show.return`:

Return
------

size of formatted string.

.. _`lpfc_info_show`:

lpfc_info_show
==============

.. c:function:: ssize_t lpfc_info_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return some pci info about the host in ascii

    :param struct device \*dev:
        class converted to a Scsi_host structure.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the formatted text from \ :c:func:`lpfc_info`\ .

.. _`lpfc_info_show.return`:

Return
------

size of formatted string.

.. _`lpfc_serialnum_show`:

lpfc_serialnum_show
===================

.. c:function:: ssize_t lpfc_serialnum_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the hba serial number in ascii

    :param struct device \*dev:
        class converted to a Scsi_host structure.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the formatted text serial number.

.. _`lpfc_serialnum_show.return`:

Return
------

size of formatted string.

.. _`lpfc_temp_sensor_show`:

lpfc_temp_sensor_show
=====================

.. c:function:: ssize_t lpfc_temp_sensor_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the temperature sensor level

    :param struct device \*dev:
        class converted to a Scsi_host structure.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the formatted support level.

.. _`lpfc_temp_sensor_show.description`:

Description
-----------

Returns a number indicating the temperature sensor level currently
supported, zero or one in ascii.

.. _`lpfc_temp_sensor_show.return`:

Return
------

size of formatted string.

.. _`lpfc_modeldesc_show`:

lpfc_modeldesc_show
===================

.. c:function:: ssize_t lpfc_modeldesc_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the model description of the hba

    :param struct device \*dev:
        class converted to a Scsi_host structure.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the scsi vpd model description.

.. _`lpfc_modeldesc_show.return`:

Return
------

size of formatted string.

.. _`lpfc_modelname_show`:

lpfc_modelname_show
===================

.. c:function:: ssize_t lpfc_modelname_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the model name of the hba

    :param struct device \*dev:
        class converted to a Scsi_host structure.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the scsi vpd model name.

.. _`lpfc_modelname_show.return`:

Return
------

size of formatted string.

.. _`lpfc_programtype_show`:

lpfc_programtype_show
=====================

.. c:function:: ssize_t lpfc_programtype_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the program type of the hba

    :param struct device \*dev:
        class converted to a Scsi_host structure.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the scsi vpd program type.

.. _`lpfc_programtype_show.return`:

Return
------

size of formatted string.

.. _`lpfc_mlomgmt_show`:

lpfc_mlomgmt_show
=================

.. c:function:: ssize_t lpfc_mlomgmt_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the Menlo Maintenance sli flag

    :param struct device \*dev:
        class converted to a Scsi_host structure.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the Menlo Maintenance sli flag.

.. _`lpfc_mlomgmt_show.return`:

Return
------

size of formatted string.

.. _`lpfc_vportnum_show`:

lpfc_vportnum_show
==================

.. c:function:: ssize_t lpfc_vportnum_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the port number in ascii of the hba

    :param struct device \*dev:
        class converted to a Scsi_host structure.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains scsi vpd program type.

.. _`lpfc_vportnum_show.return`:

Return
------

size of formatted string.

.. _`lpfc_fwrev_show`:

lpfc_fwrev_show
===============

.. c:function:: ssize_t lpfc_fwrev_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the firmware rev running in the hba

    :param struct device \*dev:
        class converted to a Scsi_host structure.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the scsi vpd program type.

.. _`lpfc_fwrev_show.return`:

Return
------

size of formatted string.

.. _`lpfc_hdw_show`:

lpfc_hdw_show
=============

.. c:function:: ssize_t lpfc_hdw_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the jedec information about the hba

    :param struct device \*dev:
        class converted to a Scsi_host structure.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the scsi vpd program type.

.. _`lpfc_hdw_show.return`:

Return
------

size of formatted string.

.. _`lpfc_option_rom_version_show`:

lpfc_option_rom_version_show
============================

.. c:function:: ssize_t lpfc_option_rom_version_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the adapter ROM FCode version

    :param struct device \*dev:
        class converted to a Scsi_host structure.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the ROM and FCode ascii strings.

.. _`lpfc_option_rom_version_show.return`:

Return
------

size of formatted string.

.. _`lpfc_link_state_show`:

lpfc_link_state_show
====================

.. c:function:: ssize_t lpfc_link_state_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the link state of the port

    :param struct device \*dev:
        class converted to a Scsi_host structure.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains text describing the state of the link.

.. _`lpfc_link_state_show.notes`:

Notes
-----

The switch statement has no default so zero will be returned.

.. _`lpfc_link_state_show.return`:

Return
------

size of formatted string.

.. _`lpfc_sli4_protocol_show`:

lpfc_sli4_protocol_show
=======================

.. c:function:: ssize_t lpfc_sli4_protocol_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the fip mode of the HBA

    :param struct device \*dev:
        class unused variable.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the module description text.

.. _`lpfc_sli4_protocol_show.return`:

Return
------

size of formatted string.

.. _`lpfc_oas_supported_show`:

lpfc_oas_supported_show
=======================

.. c:function:: ssize_t lpfc_oas_supported_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return whether or not Optimized Access Storage (OAS) is supported.

    :param struct device \*dev:
        class unused variable.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the module description text.

.. _`lpfc_oas_supported_show.return`:

Return
------

size of formatted string.

.. _`lpfc_link_state_store`:

lpfc_link_state_store
=====================

.. c:function:: ssize_t lpfc_link_state_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Transition the link_state on an HBA port

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        one or more lpfc_polling_flags values.

    :param size_t count:
        not used.

.. _`lpfc_link_state_store.return`:

Return
------

-EINVAL if the buffer is not "up" or "down"
return from link state change function if non-zero
length of the buf on success

.. _`lpfc_num_discovered_ports_show`:

lpfc_num_discovered_ports_show
==============================

.. c:function:: ssize_t lpfc_num_discovered_ports_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return sum of mapped and unmapped vports

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the sum of fc mapped and unmapped.

.. _`lpfc_num_discovered_ports_show.description`:

Description
-----------

Returns the ascii text number of the sum of the fc mapped and unmapped
vport counts.

.. _`lpfc_num_discovered_ports_show.return`:

Return
------

size of formatted string.

.. _`lpfc_issue_lip`:

lpfc_issue_lip
==============

.. c:function:: int lpfc_issue_lip(struct Scsi_Host *shost)

    Misnomer, name carried over from long ago

    :param struct Scsi_Host \*shost:
        Scsi_Host pointer.

.. _`lpfc_issue_lip.description`:

Description
-----------

Bring the link down gracefully then re-init the link. The firmware will
re-init the fiber channel interface as required. Does not issue a LIP.

.. _`lpfc_issue_lip.return`:

Return
------

-EPERM port offline or management commands are being blocked
-ENOMEM cannot allocate memory for the mailbox command
-EIO error sending the mailbox command
zero for success

.. _`lpfc_do_offline`:

lpfc_do_offline
===============

.. c:function:: int lpfc_do_offline(struct lpfc_hba *phba, uint32_t type)

    Issues a mailbox command to bring the link down

    :param struct lpfc_hba \*phba:
        lpfc_hba pointer.

    :param uint32_t type:
        LPFC_EVT_OFFLINE, LPFC_EVT_WARM_START, LPFC_EVT_KILL.

.. _`lpfc_do_offline.notes`:

Notes
-----

Assumes any error from \ :c:func:`lpfc_do_offline`\  will be negative.
Can wait up to 5 seconds for the port ring buffers count
to reach zero, prints a warning if it is not zero and continues.
\ :c:func:`lpfc_workq_post_event`\  returns a non-zero return code if call fails.

.. _`lpfc_do_offline.return`:

Return
------

-EIO error posting the event
zero for success

.. _`lpfc_selective_reset`:

lpfc_selective_reset
====================

.. c:function:: int lpfc_selective_reset(struct lpfc_hba *phba)

    Offline then onlines the port

    :param struct lpfc_hba \*phba:
        lpfc_hba pointer.

.. _`lpfc_selective_reset.description`:

Description
-----------

If the port is configured to allow a reset then the hba is brought
offline then online.

.. _`lpfc_selective_reset.notes`:

Notes
-----

Assumes any error from \ :c:func:`lpfc_do_offline`\  will be negative.
Do not make this function static.

.. _`lpfc_selective_reset.return`:

Return
------

lpfc_do_offline() return code if not zero
-EIO reset not configured or error posting the event
zero for success

.. _`lpfc_issue_reset`:

lpfc_issue_reset
================

.. c:function:: ssize_t lpfc_issue_reset(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Selectively resets an adapter

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        containing the string "selective".

    :param size_t count:
        unused variable.

.. _`lpfc_issue_reset.description`:

Description
-----------

If the buf contains the string "selective" then \ :c:func:`lpfc_selective_reset`\ 
is called to perform the reset.

.. _`lpfc_issue_reset.notes`:

Notes
-----

Assumes any error from \ :c:func:`lpfc_selective_reset`\  will be negative.
If \ :c:func:`lpfc_selective_reset`\  returns zero then the length of the buffer
is returned which indicates success

.. _`lpfc_issue_reset.return`:

Return
------

-EINVAL if the buffer does not contain the string "selective"
length of buf if lpfc-selective_reset() if the call succeeds
return value of \ :c:func:`lpfc_selective_reset`\  if the call fails

.. _`lpfc_sli4_pdev_status_reg_wait`:

lpfc_sli4_pdev_status_reg_wait
==============================

.. c:function:: int lpfc_sli4_pdev_status_reg_wait(struct lpfc_hba *phba)

    Wait for pdev status register for readyness

    :param struct lpfc_hba \*phba:
        lpfc_hba pointer.

.. _`lpfc_sli4_pdev_status_reg_wait.description`:

Description
-----------

SLI4 interface type-2 device to wait on the sliport status register for
the readyness after performing a firmware reset.

.. _`lpfc_sli4_pdev_status_reg_wait.return`:

Return
------

zero for success, -EPERM when port does not have privilege to perform the
reset, -EIO when port timeout from recovering from the reset.

.. _`lpfc_sli4_pdev_status_reg_wait.note`:

Note
----

As the caller will interpret the return code by value, be careful in making
change or addition to return codes.

.. _`lpfc_sli4_pdev_reg_request`:

lpfc_sli4_pdev_reg_request
==========================

.. c:function:: ssize_t lpfc_sli4_pdev_reg_request(struct lpfc_hba *phba, uint32_t opcode)

    Request physical dev to perform a register acc

    :param struct lpfc_hba \*phba:
        lpfc_hba pointer.

    :param uint32_t opcode:
        *undescribed*

.. _`lpfc_sli4_pdev_reg_request.description`:

Description
-----------

Request SLI4 interface type-2 device to perform a physical register set
access.

.. _`lpfc_sli4_pdev_reg_request.return`:

Return
------

zero for success

.. _`lpfc_nport_evt_cnt_show`:

lpfc_nport_evt_cnt_show
=======================

.. c:function:: ssize_t lpfc_nport_evt_cnt_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the number of nport events

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the ascii number of nport events.

.. _`lpfc_nport_evt_cnt_show.return`:

Return
------

size of formatted string.

.. _`lpfc_board_mode_show`:

lpfc_board_mode_show
====================

.. c:function:: ssize_t lpfc_board_mode_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the state of the board

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the state of the adapter.

.. _`lpfc_board_mode_show.return`:

Return
------

size of formatted string.

.. _`lpfc_board_mode_store`:

lpfc_board_mode_store
=====================

.. c:function:: ssize_t lpfc_board_mode_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Puts the hba in online, offline, warm or error state

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        containing one of the strings "online", "offline", "warm" or "error".

    :param size_t count:
        unused variable.

.. _`lpfc_board_mode_store.return`:

Return
------

-EACCES if enable hba reset not enabled
-EINVAL if the buffer does not contain a valid string (see above)
-EIO if \ :c:func:`lpfc_workq_post_event`\  or \ :c:func:`lpfc_do_offline`\  fails
buf length greater than zero indicates success

.. _`lpfc_get_hba_info`:

lpfc_get_hba_info
=================

.. c:function:: int lpfc_get_hba_info(struct lpfc_hba *phba, uint32_t *mxri, uint32_t *axri, uint32_t *mrpi, uint32_t *arpi, uint32_t *mvpi, uint32_t *avpi)

    Return various bits of informaton about the adapter

    :param struct lpfc_hba \*phba:
        pointer to the adapter structure.

    :param uint32_t \*mxri:
        max xri count.

    :param uint32_t \*axri:
        available xri count.

    :param uint32_t \*mrpi:
        max rpi count.

    :param uint32_t \*arpi:
        available rpi count.

    :param uint32_t \*mvpi:
        max vpi count.

    :param uint32_t \*avpi:
        available vpi count.

.. _`lpfc_get_hba_info.description`:

Description
-----------

If an integer pointer for an count is not null then the value for the
count is returned.

.. _`lpfc_get_hba_info.return`:

Return
------

zero on error
one for success

.. _`lpfc_max_rpi_show`:

lpfc_max_rpi_show
=================

.. c:function:: ssize_t lpfc_max_rpi_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return maximum rpi

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the maximum rpi count in decimal or "Unknown".

.. _`lpfc_max_rpi_show.description`:

Description
-----------

Calls \ :c:func:`lpfc_get_hba_info`\  asking for just the mrpi count.
If \ :c:func:`lpfc_get_hba_info`\  returns zero (failure) the buffer text is set
to "Unknown" and the buffer length is returned, therefore the caller
must check for "Unknown" in the buffer to detect a failure.

.. _`lpfc_max_rpi_show.return`:

Return
------

size of formatted string.

.. _`lpfc_used_rpi_show`:

lpfc_used_rpi_show
==================

.. c:function:: ssize_t lpfc_used_rpi_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return maximum rpi minus available rpi

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        containing the used rpi count in decimal or "Unknown".

.. _`lpfc_used_rpi_show.description`:

Description
-----------

Calls \ :c:func:`lpfc_get_hba_info`\  asking for just the mrpi and arpi counts.
If \ :c:func:`lpfc_get_hba_info`\  returns zero (failure) the buffer text is set
to "Unknown" and the buffer length is returned, therefore the caller
must check for "Unknown" in the buffer to detect a failure.

.. _`lpfc_used_rpi_show.return`:

Return
------

size of formatted string.

.. _`lpfc_max_xri_show`:

lpfc_max_xri_show
=================

.. c:function:: ssize_t lpfc_max_xri_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return maximum xri

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the maximum xri count in decimal or "Unknown".

.. _`lpfc_max_xri_show.description`:

Description
-----------

Calls \ :c:func:`lpfc_get_hba_info`\  asking for just the mrpi count.
If \ :c:func:`lpfc_get_hba_info`\  returns zero (failure) the buffer text is set
to "Unknown" and the buffer length is returned, therefore the caller
must check for "Unknown" in the buffer to detect a failure.

.. _`lpfc_max_xri_show.return`:

Return
------

size of formatted string.

.. _`lpfc_used_xri_show`:

lpfc_used_xri_show
==================

.. c:function:: ssize_t lpfc_used_xri_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return maximum xpi minus the available xpi

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the used xri count in decimal or "Unknown".

.. _`lpfc_used_xri_show.description`:

Description
-----------

Calls \ :c:func:`lpfc_get_hba_info`\  asking for just the mxri and axri counts.
If \ :c:func:`lpfc_get_hba_info`\  returns zero (failure) the buffer text is set
to "Unknown" and the buffer length is returned, therefore the caller
must check for "Unknown" in the buffer to detect a failure.

.. _`lpfc_used_xri_show.return`:

Return
------

size of formatted string.

.. _`lpfc_max_vpi_show`:

lpfc_max_vpi_show
=================

.. c:function:: ssize_t lpfc_max_vpi_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return maximum vpi

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the maximum vpi count in decimal or "Unknown".

.. _`lpfc_max_vpi_show.description`:

Description
-----------

Calls \ :c:func:`lpfc_get_hba_info`\  asking for just the mvpi count.
If \ :c:func:`lpfc_get_hba_info`\  returns zero (failure) the buffer text is set
to "Unknown" and the buffer length is returned, therefore the caller
must check for "Unknown" in the buffer to detect a failure.

.. _`lpfc_max_vpi_show.return`:

Return
------

size of formatted string.

.. _`lpfc_used_vpi_show`:

lpfc_used_vpi_show
==================

.. c:function:: ssize_t lpfc_used_vpi_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return maximum vpi minus the available vpi

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the used vpi count in decimal or "Unknown".

.. _`lpfc_used_vpi_show.description`:

Description
-----------

Calls \ :c:func:`lpfc_get_hba_info`\  asking for just the mvpi and avpi counts.
If \ :c:func:`lpfc_get_hba_info`\  returns zero (failure) the buffer text is set
to "Unknown" and the buffer length is returned, therefore the caller
must check for "Unknown" in the buffer to detect a failure.

.. _`lpfc_used_vpi_show.return`:

Return
------

size of formatted string.

.. _`lpfc_npiv_info_show`:

lpfc_npiv_info_show
===================

.. c:function:: ssize_t lpfc_npiv_info_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return text about NPIV support for the adapter

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        text that must be interpreted to determine if npiv is supported.

.. _`lpfc_npiv_info_show.description`:

Description
-----------

Buffer will contain text indicating npiv is not suppoerted on the port,
the port is an NPIV physical port, or it is an npiv virtual port with
the id of the vport.

.. _`lpfc_npiv_info_show.return`:

Return
------

size of formatted string.

.. _`lpfc_poll_show`:

lpfc_poll_show
==============

.. c:function:: ssize_t lpfc_poll_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return text about poll support for the adapter

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the cfg_poll in hex.

.. _`lpfc_poll_show.notes`:

Notes
-----

cfg_poll should be a lpfc_polling_flags type.

.. _`lpfc_poll_show.return`:

Return
------

size of formatted string.

.. _`lpfc_poll_store`:

lpfc_poll_store
===============

.. c:function:: ssize_t lpfc_poll_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Set the value of cfg_poll for the adapter

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        one or more lpfc_polling_flags values.

    :param size_t count:
        not used.

.. _`lpfc_poll_store.notes`:

Notes
-----

buf contents converted to integer and checked for a valid value.

.. _`lpfc_poll_store.return`:

Return
------

-EINVAL if the buffer connot be converted or is out of range
length of the buf on success

.. _`lpfc_fips_level_show`:

lpfc_fips_level_show
====================

.. c:function:: ssize_t lpfc_fips_level_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the current FIPS level for the HBA

    :param struct device \*dev:
        class unused variable.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the module description text.

.. _`lpfc_fips_level_show.return`:

Return
------

size of formatted string.

.. _`lpfc_fips_rev_show`:

lpfc_fips_rev_show
==================

.. c:function:: ssize_t lpfc_fips_rev_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the FIPS Spec revision for the HBA

    :param struct device \*dev:
        class unused variable.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the module description text.

.. _`lpfc_fips_rev_show.return`:

Return
------

size of formatted string.

.. _`lpfc_dss_show`:

lpfc_dss_show
=============

.. c:function:: ssize_t lpfc_dss_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the current state of dss and the configured state

    :param struct device \*dev:
        class converted to a Scsi_host structure.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the formatted text.

.. _`lpfc_dss_show.return`:

Return
------

size of formatted string.

.. _`lpfc_sriov_hw_max_virtfn_show`:

lpfc_sriov_hw_max_virtfn_show
=============================

.. c:function:: ssize_t lpfc_sriov_hw_max_virtfn_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return maximum number of virtual functions

    :param struct device \*dev:
        class converted to a Scsi_host structure.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the formatted support level.

.. _`lpfc_sriov_hw_max_virtfn_show.description`:

Description
-----------

Returns the maximum number of virtual functions a physical function can
support, 0 will be returned if called on virtual function.

.. _`lpfc_sriov_hw_max_virtfn_show.return`:

Return
------

size of formatted string.

.. _`lpfc_enable_bbcr_set`:

lpfc_enable_bbcr_set
====================

.. c:function:: ssize_t lpfc_enable_bbcr_set(struct lpfc_hba *phba, uint val)

    Sets an attribute value.

    :param struct lpfc_hba \*phba:
        pointer the the adapter structure.

    :param uint val:
        integer attribute value.

.. _`lpfc_enable_bbcr_set.description`:

Description
-----------

Validates the min and max values then sets the
adapter config field if in the valid range. prints error message
and does not set the parameter if invalid.

.. _`lpfc_enable_bbcr_set.return`:

Return
------

zero on success
-EINVAL if val is invalid

.. _`lpfc_param_show`:

lpfc_param_show
===============

.. c:function::  lpfc_param_show( attr)

    Return a cfg attribute value in decimal

    :param  attr:
        device attribute, not used.

.. _`lpfc_param_show.description`:

Description
-----------

Macro that given an attr e.g. hba_queue_depth expands
into a function with the name lpfc_hba_queue_depth_show.

lpfc_##attr##_show: Return the decimal value of an adapters cfg_xxx field.

.. _`lpfc_param_show.return`:

Return
------

size of formatted string.

.. _`lpfc_param_hex_show`:

lpfc_param_hex_show
===================

.. c:function::  lpfc_param_hex_show( attr)

    Return a cfg attribute value in hex

    :param  attr:
        device attribute, not used.

.. _`lpfc_param_hex_show.description`:

Description
-----------

Macro that given an attr e.g. hba_queue_depth expands
into a function with the name lpfc_hba_queue_depth_show

lpfc_##attr##_show: Return the hex value of an adapters cfg_xxx field.

.. _`lpfc_param_hex_show.return`:

Return
------

size of formatted string.

.. _`lpfc_param_init`:

lpfc_param_init
===============

.. c:function::  lpfc_param_init( attr,  default,  minval,  maxval)

    Initializes a cfg attribute

    :param  attr:
        *undescribed*

    :param  default:
        *undescribed*

    :param  minval:
        *undescribed*

    :param  maxval:
        *undescribed*

.. _`lpfc_param_init.description`:

Description
-----------

Macro that given an attr e.g. hba_queue_depth expands
into a function with the name lpfc_hba_queue_depth_init. The macro also
takes a default argument, a minimum and maximum argument.

lpfc_##attr##_init: Initializes an attribute.

Validates the min and max values then sets the adapter config field
accordingly, or uses the default if out of range and prints an error message.

.. _`lpfc_param_init.return`:

Return
------

zero on success
-EINVAL if default used

.. _`lpfc_param_set`:

lpfc_param_set
==============

.. c:function::  lpfc_param_set( attr,  default,  minval,  maxval)

    Set a cfg attribute value

    :param  attr:
        *undescribed*

    :param  default:
        *undescribed*

    :param  minval:
        *undescribed*

    :param  maxval:
        *undescribed*

.. _`lpfc_param_set.description`:

Description
-----------

Macro that given an attr e.g. hba_queue_depth expands
into a function with the name lpfc_hba_queue_depth_set

lpfc_##attr##_set: Sets an attribute value.

Validates the min and max values then sets the
adapter config field if in the valid range. prints error message
and does not set the parameter if invalid.

.. _`lpfc_param_set.return`:

Return
------

zero on success
-EINVAL if val is invalid

.. _`lpfc_param_store`:

lpfc_param_store
================

.. c:function::  lpfc_param_store( attr)

    Set a vport attribute value

    :param  attr:
        device attribute, not used.

.. _`lpfc_param_store.description`:

Description
-----------

Macro that given an attr e.g. hba_queue_depth expands
into a function with the name lpfc_hba_queue_depth_store.

lpfc_##attr##_store: Set an sttribute value.

Convert the ascii text number to an integer, then
use the lpfc_##attr##_set function to set the value.

.. _`lpfc_param_store.return`:

Return
------

-EINVAL if val is invalid or lpfc_##attr##_set() fails
length of buffer upon success.

.. _`lpfc_vport_param_show`:

lpfc_vport_param_show
=====================

.. c:function::  lpfc_vport_param_show( attr)

    Return decimal formatted cfg attribute value

    :param  attr:
        device attribute, not used.

.. _`lpfc_vport_param_show.description`:

Description
-----------

Macro that given an attr e.g. hba_queue_depth expands
into a function with the name lpfc_hba_queue_depth_show

lpfc_##attr##_show: prints the attribute value in decimal.

.. _`lpfc_vport_param_show.return`:

Return
------

length of formatted string.

.. _`lpfc_vport_param_hex_show`:

lpfc_vport_param_hex_show
=========================

.. c:function::  lpfc_vport_param_hex_show( attr)

    Return hex formatted attribute value

    :param  attr:
        device attribute, not used.

.. _`lpfc_vport_param_hex_show.description`:

Description
-----------

Macro that given an attr e.g.
hba_queue_depth expands into a function with the name
lpfc_hba_queue_depth_show

lpfc_##attr##_show: prints the attribute value in hexadecimal.

.. _`lpfc_vport_param_hex_show.return`:

Return
------

length of formatted string.

.. _`lpfc_vport_param_init`:

lpfc_vport_param_init
=====================

.. c:function::  lpfc_vport_param_init( attr,  default,  minval,  maxval)

    Initialize a vport cfg attribute

    :param  attr:
        *undescribed*

    :param  default:
        *undescribed*

    :param  minval:
        *undescribed*

    :param  maxval:
        *undescribed*

.. _`lpfc_vport_param_init.description`:

Description
-----------

Macro that given an attr e.g. hba_queue_depth expands
into a function with the name lpfc_hba_queue_depth_init. The macro also
takes a default argument, a minimum and maximum argument.

lpfc_##attr##_init: validates the min and max values then sets the
adapter config field accordingly, or uses the default if out of range
and prints an error message.

.. _`lpfc_vport_param_init.return`:

Return
------

zero on success
-EINVAL if default used

.. _`lpfc_vport_param_set`:

lpfc_vport_param_set
====================

.. c:function::  lpfc_vport_param_set( attr,  default,  minval,  maxval)

    Set a vport cfg attribute

    :param  attr:
        *undescribed*

    :param  default:
        *undescribed*

    :param  minval:
        *undescribed*

    :param  maxval:
        *undescribed*

.. _`lpfc_vport_param_set.description`:

Description
-----------

Macro that given an attr e.g. hba_queue_depth expands
into a function with the name lpfc_hba_queue_depth_set

lpfc_##attr##_set: validates the min and max values then sets the
adapter config field if in the valid range. prints error message
and does not set the parameter if invalid.

.. _`lpfc_vport_param_set.return`:

Return
------

zero on success
-EINVAL if val is invalid

.. _`lpfc_vport_param_store`:

lpfc_vport_param_store
======================

.. c:function::  lpfc_vport_param_store( attr)

    Set a vport attribute

    :param  attr:
        *undescribed*

.. _`lpfc_vport_param_store.description`:

Description
-----------

Macro that given an attr e.g. hba_queue_depth
expands into a function with the name lpfc_hba_queue_depth_store

lpfc_##attr##_store: convert the ascii text number to an integer, then
use the lpfc_##attr##_set function to set the value.

.. _`lpfc_vport_param_store.return`:

Return
------

-EINVAL if val is invalid or lpfc_##attr##_set() fails
length of buffer upon success.

.. _`lpfc_wwn_set`:

lpfc_wwn_set
============

.. c:function:: size_t lpfc_wwn_set(const char *buf, size_t cnt, char wwn)

    Convert string to the 8 byte WWN value.

    :param const char \*buf:
        WWN string.

    :param size_t cnt:
        Length of string.

    :param char wwn:
        Array to receive converted wwn value.

.. _`lpfc_wwn_set.return`:

Return
------

-EINVAL if the buffer does not contain a valid wwn
0 success

.. _`lpfc_soft_wwn_enable_store`:

lpfc_soft_wwn_enable_store
==========================

.. c:function:: ssize_t lpfc_soft_wwn_enable_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Allows setting of the wwn if the key is valid

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        containing the string lpfc_soft_wwn_key.

    :param size_t count:
        must be size of lpfc_soft_wwn_key.

.. _`lpfc_soft_wwn_enable_store.return`:

Return
------

-EINVAL if the buffer does not contain lpfc_soft_wwn_key
length of buf indicates success

.. _`lpfc_soft_wwpn_show`:

lpfc_soft_wwpn_show
===================

.. c:function:: ssize_t lpfc_soft_wwpn_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the cfg soft ww port name of the adapter

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the wwpn in hexadecimal.

.. _`lpfc_soft_wwpn_show.return`:

Return
------

size of formatted string.

.. _`lpfc_soft_wwpn_store`:

lpfc_soft_wwpn_store
====================

.. c:function:: ssize_t lpfc_soft_wwpn_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Set the ww port name of the adapter \ ``dev``\  class device that is converted into a Scsi_host.

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        contains the wwpn in hexadecimal.

    :param size_t count:
        number of wwpn bytes in buf

.. _`lpfc_soft_wwpn_store.return`:

Return
------

-EACCES hba reset not enabled, adapter over temp
-EINVAL soft wwn not enabled, count is invalid, invalid wwpn byte invalid
-EIO error taking adapter offline or online
value of count on success

.. _`lpfc_soft_wwnn_show`:

lpfc_soft_wwnn_show
===================

.. c:function:: ssize_t lpfc_soft_wwnn_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the cfg soft ww node name for the adapter

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the wwnn in hexadecimal.

.. _`lpfc_soft_wwnn_show.return`:

Return
------

size of formatted string.

.. _`lpfc_soft_wwnn_store`:

lpfc_soft_wwnn_store
====================

.. c:function:: ssize_t lpfc_soft_wwnn_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    sets the ww node name of the adapter

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param const char \*buf:
        contains the ww node name in hexadecimal.

    :param size_t count:
        number of wwnn bytes in buf.

.. _`lpfc_soft_wwnn_store.return`:

Return
------

-EINVAL soft wwn not enabled, count is invalid, invalid wwnn byte invalid
value of count on success

.. _`lpfc_oas_tgt_show`:

lpfc_oas_tgt_show
=================

.. c:function:: ssize_t lpfc_oas_tgt_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return wwpn of target whose luns maybe enabled for Optimized Access Storage (OAS) operations.

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        buffer for passing information.

.. _`lpfc_oas_tgt_show.return`:

Return
------

value of count

.. _`lpfc_oas_tgt_store`:

lpfc_oas_tgt_store
==================

.. c:function:: ssize_t lpfc_oas_tgt_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Store wwpn of target whose luns maybe enabled for Optimized Access Storage (OAS) operations.

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        buffer for passing information.

    :param size_t count:
        Size of the data buffer.

.. _`lpfc_oas_tgt_store.return`:

Return
------

-EINVAL count is invalid, invalid wwpn byte invalid
-EPERM oas is not supported by hba
value of count on success

.. _`lpfc_oas_priority_show`:

lpfc_oas_priority_show
======================

.. c:function:: ssize_t lpfc_oas_priority_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return wwpn of target whose luns maybe enabled for Optimized Access Storage (OAS) operations.

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        buffer for passing information.

.. _`lpfc_oas_priority_show.return`:

Return
------

value of count

.. _`lpfc_oas_priority_store`:

lpfc_oas_priority_store
=======================

.. c:function:: ssize_t lpfc_oas_priority_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Store wwpn of target whose luns maybe enabled for Optimized Access Storage (OAS) operations.

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        buffer for passing information.

    :param size_t count:
        Size of the data buffer.

.. _`lpfc_oas_priority_store.return`:

Return
------

-EINVAL count is invalid, invalid wwpn byte invalid
-EPERM oas is not supported by hba
value of count on success

.. _`lpfc_oas_vpt_show`:

lpfc_oas_vpt_show
=================

.. c:function:: ssize_t lpfc_oas_vpt_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return wwpn of vport whose targets maybe enabled for Optimized Access Storage (OAS) operations.

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        buffer for passing information.

.. _`lpfc_oas_vpt_show.return`:

Return
------

value of count on success

.. _`lpfc_oas_vpt_store`:

lpfc_oas_vpt_store
==================

.. c:function:: ssize_t lpfc_oas_vpt_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Store wwpn of vport whose targets maybe enabled for Optimized Access Storage (OAS) operations.

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        buffer for passing information.

    :param size_t count:
        Size of the data buffer.

.. _`lpfc_oas_vpt_store.return`:

Return
------

-EINVAL count is invalid, invalid wwpn byte invalid
-EPERM oas is not supported by hba
value of count on success

.. _`lpfc_oas_lun_state_show`:

lpfc_oas_lun_state_show
=======================

.. c:function:: ssize_t lpfc_oas_lun_state_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the current state (enabled or disabled) of whether luns will be enabled or disabled for Optimized Access Storage (OAS) operations.

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        buffer for passing information.

.. _`lpfc_oas_lun_state_show.return`:

Return
------

size of formatted string.

.. _`lpfc_oas_lun_state_store`:

lpfc_oas_lun_state_store
========================

.. c:function:: ssize_t lpfc_oas_lun_state_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Store the state (enabled or disabled) of whether luns will be enabled or disabled for Optimized Access Storage (OAS) operations.

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        buffer for passing information.

    :param size_t count:
        Size of the data buffer.

.. _`lpfc_oas_lun_state_store.return`:

Return
------

-EINVAL count is invalid, invalid wwpn byte invalid
-EPERM oas is not supported by hba
value of count on success

.. _`lpfc_oas_lun_status_show`:

lpfc_oas_lun_status_show
========================

.. c:function:: ssize_t lpfc_oas_lun_status_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the status of the Optimized Access Storage (OAS) lun returned by the lpfc_oas_lun_show function.

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        buffer for passing information.

.. _`lpfc_oas_lun_status_show.return`:

Return
------

size of formatted string.

.. _`lpfc_oas_lun_state_set`:

lpfc_oas_lun_state_set
======================

.. c:function:: size_t lpfc_oas_lun_state_set(struct lpfc_hba *phba, uint8_t vpt_wwpn, uint8_t tgt_wwpn, uint64_t lun, uint32_t oas_state, uint8_t pri)

    enable or disable a lun for Optimized Access Storage (OAS) operations.

    :param struct lpfc_hba \*phba:
        lpfc_hba pointer.

    :param uint8_t vpt_wwpn:
        *undescribed*

    :param uint8_t tgt_wwpn:
        *undescribed*

    :param uint64_t lun:
        the fc lun for setting oas state.

    :param uint32_t oas_state:
        the oas state to be set to the lun.

    :param uint8_t pri:
        *undescribed*

.. _`lpfc_oas_lun_state_set.return`:

Return
------

SUCCESS : 0
-EPERM OAS is not enabled or not supported by this port.

.. _`lpfc_oas_lun_get_next`:

lpfc_oas_lun_get_next
=====================

.. c:function:: uint64_t lpfc_oas_lun_get_next(struct lpfc_hba *phba, uint8_t vpt_wwpn, uint8_t tgt_wwpn, uint32_t *lun_status, uint32_t *lun_pri)

    get the next lun that has been enabled for Optimized Access Storage (OAS) operations.

    :param struct lpfc_hba \*phba:
        lpfc_hba pointer.

    :param uint8_t vpt_wwpn:
        wwpn of the vport associated with the returned lun

    :param uint8_t tgt_wwpn:
        wwpn of the target associated with the returned lun

    :param uint32_t \*lun_status:
        status of the lun returned lun

    :param uint32_t \*lun_pri:
        *undescribed*

.. _`lpfc_oas_lun_get_next.description`:

Description
-----------

Returns the first or next lun enabled for OAS operations for the vport/target
specified.  If a lun is found, its vport wwpn, target wwpn and status is
returned.  If the lun is not found, NOT_OAS_ENABLED_LUN is returned.

.. _`lpfc_oas_lun_get_next.return`:

Return
------

lun that is OAS enabled for the vport/target
NOT_OAS_ENABLED_LUN when no oas enabled lun found.

.. _`lpfc_oas_lun_state_change`:

lpfc_oas_lun_state_change
=========================

.. c:function:: ssize_t lpfc_oas_lun_state_change(struct lpfc_hba *phba, uint8_t vpt_wwpn, uint8_t tgt_wwpn, uint64_t lun, uint32_t oas_state, uint8_t pri)

    enable/disable a lun for OAS operations

    :param struct lpfc_hba \*phba:
        lpfc_hba pointer.

    :param uint8_t vpt_wwpn:
        vport wwpn by reference.

    :param uint8_t tgt_wwpn:
        target wwpn by reference.

    :param uint64_t lun:
        the fc lun for setting oas state.

    :param uint32_t oas_state:
        the oas state to be set to the oas_lun.

    :param uint8_t pri:
        *undescribed*

.. _`lpfc_oas_lun_state_change.description`:

Description
-----------

This routine enables (OAS_LUN_ENABLE) or disables (OAS_LUN_DISABLE)
a lun for OAS operations.

.. _`lpfc_oas_lun_state_change.success`:

SUCCESS
-------

0
-ENOMEM: failed to enable an lun for OAS operations
-EPERM: OAS is not enabled

.. _`lpfc_oas_lun_show`:

lpfc_oas_lun_show
=================

.. c:function:: ssize_t lpfc_oas_lun_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return oas enabled luns from a chosen target

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        buffer for passing information.

.. _`lpfc_oas_lun_show.description`:

Description
-----------

This routine returns a lun enabled for OAS each time the function
is called.

.. _`lpfc_oas_lun_show.success`:

SUCCESS
-------

size of formatted string.
-EFAULT: target or vport wwpn was not set properly.
-EPERM: oas is not enabled.

.. _`lpfc_oas_lun_store`:

lpfc_oas_lun_store
==================

.. c:function:: ssize_t lpfc_oas_lun_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Sets the OAS state for lun

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        buffer for passing information.

    :param size_t count:
        *undescribed*

.. _`lpfc_oas_lun_store.description`:

Description
-----------

This function sets the OAS state for lun.  Before this function is called,
the vport wwpn, target wwpn, and oas state need to be set.

.. _`lpfc_oas_lun_store.success`:

SUCCESS
-------

size of formatted string.
-EFAULT: target or vport wwpn was not set properly.
-EPERM: oas is not enabled.
size of formatted string.

.. _`lpfc_nodev_tmo_show`:

lpfc_nodev_tmo_show
===================

.. c:function:: ssize_t lpfc_nodev_tmo_show(struct device *dev, struct device_attribute *attr, char *buf)

    Return the hba dev loss timeout value

    :param struct device \*dev:
        class converted to a Scsi_host structure.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains the dev loss timeout in decimal.

.. _`lpfc_nodev_tmo_show.return`:

Return
------

size of formatted string.

.. _`lpfc_nodev_tmo_init`:

lpfc_nodev_tmo_init
===================

.. c:function:: int lpfc_nodev_tmo_init(struct lpfc_vport *vport, int val)

    Set the hba nodev timeout value

    :param struct lpfc_vport \*vport:
        lpfc vport structure pointer.

    :param int val:
        contains the nodev timeout value.

.. _`lpfc_nodev_tmo_init.description`:

Description
-----------

If the devloss tmo is already set then nodev tmo is set to devloss tmo,
a kernel error message is printed and zero is returned.
Else if val is in range then nodev tmo and devloss tmo are set to val.
Otherwise nodev tmo is set to the default value.

.. _`lpfc_nodev_tmo_init.return`:

Return
------

zero if already set or if val is in range
-EINVAL val out of range

.. _`lpfc_update_rport_devloss_tmo`:

lpfc_update_rport_devloss_tmo
=============================

.. c:function:: void lpfc_update_rport_devloss_tmo(struct lpfc_vport *vport)

    Update dev loss tmo value

    :param struct lpfc_vport \*vport:
        lpfc vport structure pointer.

.. _`lpfc_update_rport_devloss_tmo.description`:

Description
-----------

Update all the ndlp's dev loss tmo with the vport devloss tmo value.

.. _`lpfc_nodev_tmo_set`:

lpfc_nodev_tmo_set
==================

.. c:function:: int lpfc_nodev_tmo_set(struct lpfc_vport *vport, int val)

    Set the vport nodev tmo and devloss tmo values

    :param struct lpfc_vport \*vport:
        lpfc vport structure pointer.

    :param int val:
        contains the tmo value.

.. _`lpfc_nodev_tmo_set.description`:

Description
-----------

If the devloss tmo is already set or the vport dev loss tmo has changed
then a kernel error message is printed and zero is returned.
Else if val is in range then nodev tmo and devloss tmo are set to val.
Otherwise nodev tmo is set to the default value.

.. _`lpfc_nodev_tmo_set.return`:

Return
------

zero if already set or if val is in range
-EINVAL val out of range

.. _`lpfc_devloss_tmo_set`:

lpfc_devloss_tmo_set
====================

.. c:function:: int lpfc_devloss_tmo_set(struct lpfc_vport *vport, int val)

    Sets vport nodev tmo, devloss tmo values, changed bit

    :param struct lpfc_vport \*vport:
        lpfc vport structure pointer.

    :param int val:
        contains the tmo value.

.. _`lpfc_devloss_tmo_set.description`:

Description
-----------

If val is in a valid range then set the vport nodev tmo,
devloss tmo, also set the vport dev loss tmo changed flag.
Else a kernel error message is printed.

.. _`lpfc_devloss_tmo_set.return`:

Return
------

zero if val is in range
-EINVAL val out of range

.. _`lpfc_restrict_login_init`:

lpfc_restrict_login_init
========================

.. c:function:: int lpfc_restrict_login_init(struct lpfc_vport *vport, int val)

    Set the vport restrict login flag

    :param struct lpfc_vport \*vport:
        lpfc vport structure pointer.

    :param int val:
        contains the restrict login value.

.. _`lpfc_restrict_login_init.description`:

Description
-----------

If val is not in a valid range then log a kernel error message and set
the vport restrict login to one.
If the port type is physical clear the restrict login flag and return.
Else set the restrict login flag to val.

.. _`lpfc_restrict_login_init.return`:

Return
------

zero if val is in range
-EINVAL val out of range

.. _`lpfc_restrict_login_set`:

lpfc_restrict_login_set
=======================

.. c:function:: int lpfc_restrict_login_set(struct lpfc_vport *vport, int val)

    Set the vport restrict login flag

    :param struct lpfc_vport \*vport:
        lpfc vport structure pointer.

    :param int val:
        contains the restrict login value.

.. _`lpfc_restrict_login_set.description`:

Description
-----------

If val is not in a valid range then log a kernel error message and set
the vport restrict login to one.
If the port type is physical and the val is not zero log a kernel
error message, clear the restrict login flag and return zero.
Else set the restrict login flag to val.

.. _`lpfc_restrict_login_set.return`:

Return
------

zero if val is in range
-EINVAL val out of range

.. _`lpfc_topology_store`:

lpfc_topology_store
===================

.. c:function:: ssize_t lpfc_topology_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Set the adapters topology field

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param const char \*buf:
        *undescribed*

    :param size_t count:
        *undescribed*

.. _`lpfc_topology_store.description`:

Description
-----------

If val is in a valid range then set the adapter's topology field and
issue a lip; if the lip fails reset the topology to the old value.

If the value is not in range log a kernel error message and return an error.

.. _`lpfc_topology_store.return`:

Return
------

zero if val is in range and lip okay
non-zero return value from \ :c:func:`lpfc_issue_lip`\ 
-EINVAL val out of range

.. _`lpfc_static_vport_show`:

lpfc_static_vport_show
======================

.. c:function:: ssize_t lpfc_static_vport_show(struct device *dev, struct device_attribute *attr, char *buf)

    Read callback function for lpfc_static_vport sysfs file.

    :param struct device \*dev:
        Pointer to class device object.

    :param struct device_attribute \*attr:
        device attribute structure.

    :param char \*buf:
        Data buffer.

.. _`lpfc_static_vport_show.description`:

Description
-----------

This function is the read call back function for
lpfc_static_vport sysfs file. The lpfc_static_vport
sysfs file report the mageability of the vport.

.. _`lpfc_stat_data_ctrl_store`:

lpfc_stat_data_ctrl_store
=========================

.. c:function:: ssize_t lpfc_stat_data_ctrl_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    write call back for lpfc_stat_data_ctrl sysfs file

    :param struct device \*dev:
        Pointer to class device.

    :param struct device_attribute \*attr:
        *undescribed*

    :param const char \*buf:
        Data buffer.

    :param size_t count:
        Size of the data buffer.

.. _`lpfc_stat_data_ctrl_store.description`:

Description
-----------

This function get called when a user write to the lpfc_stat_data_ctrl
sysfs file. This function parse the command written to the sysfs file
and take appropriate action. These commands are used for controlling
driver statistical data collection.
Following are the command this function handles.

setbucket <bucket_type> <base> <step>
= Set the latency buckets.
destroybucket            = destroy all the buckets.
start                    = start data collection
stop                     = stop data collection
reset                    = reset the collected data

.. _`lpfc_stat_data_ctrl_show`:

lpfc_stat_data_ctrl_show
========================

.. c:function:: ssize_t lpfc_stat_data_ctrl_show(struct device *dev, struct device_attribute *attr, char *buf)

    Read function for lpfc_stat_data_ctrl sysfs file

    :param struct device \*dev:
        Pointer to class device object.

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        Data buffer.

.. _`lpfc_stat_data_ctrl_show.description`:

Description
-----------

This function is the read call back function for
lpfc_stat_data_ctrl sysfs file. This function report the
current statistical data collection state.

.. _`sysfs_drvr_stat_data_read`:

sysfs_drvr_stat_data_read
=========================

.. c:function:: ssize_t sysfs_drvr_stat_data_read(struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buf, loff_t off, size_t count)

    Read function for lpfc_drvr_stat_data attribute

    :param struct file \*filp:
        sysfs file

    :param struct kobject \*kobj:
        Pointer to the kernel object

    :param struct bin_attribute \*bin_attr:
        Attribute object

    :param char \*buf:
        *undescribed*

    :param loff_t off:
        File offset

    :param size_t count:
        Buffer size

.. _`sysfs_drvr_stat_data_read.description`:

Description
-----------

This function is the read call back function for lpfc_drvr_stat_data
sysfs file. This function export the statistical data to user
applications.

.. _`lpfc_link_speed_store`:

lpfc_link_speed_store
=====================

.. c:function:: ssize_t lpfc_link_speed_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Set the adapters link speed

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param const char \*buf:
        *undescribed*

    :param size_t count:
        *undescribed*

.. _`lpfc_link_speed_store.description`:

Description
-----------

If val is in a valid range then set the adapter's link speed field and
issue a lip; if the lip fails reset the link speed to the old value.

.. _`lpfc_link_speed_store.notes`:

Notes
-----

If the value is not in range log a kernel error message and return an error.

.. _`lpfc_link_speed_store.return`:

Return
------

zero if val is in range and lip okay.
non-zero return value from \ :c:func:`lpfc_issue_lip`\ 
-EINVAL val out of range

.. _`lpfc_link_speed_init`:

lpfc_link_speed_init
====================

.. c:function:: int lpfc_link_speed_init(struct lpfc_hba *phba, int val)

    Set the adapters link speed

    :param struct lpfc_hba \*phba:
        lpfc_hba pointer.

    :param int val:
        link speed value.

.. _`lpfc_link_speed_init.description`:

Description
-----------

If val is in a valid range then set the adapter's link speed field.

.. _`lpfc_link_speed_init.notes`:

Notes
-----

If the value is not in range log a kernel error message, clear the link
speed and return an error.

.. _`lpfc_link_speed_init.return`:

Return
------

zero if val saved.
-EINVAL val out of range

.. _`lpfc_aer_support_store`:

lpfc_aer_support_store
======================

.. c:function:: ssize_t lpfc_aer_support_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Set the adapter for aer support

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        containing enable or disable aer flag.

    :param size_t count:
        unused variable.

.. _`lpfc_aer_support_store.description`:

Description
-----------

If the val is 1 and currently the device's AER capability was not
enabled, invoke the kernel's enable AER helper routine, trying to
enable the device's AER capability. If the helper routine enabling
AER returns success, update the device's cfg_aer_support flag to
indicate AER is supported by the device; otherwise, if the device
AER capability is already enabled to support AER, then do nothing.

If the val is 0 and currently the device's AER support was enabled,
invoke the kernel's disable AER helper routine. After that, update
the device's cfg_aer_support flag to indicate AER is not supported
by the device; otherwise, if the device AER capability is already
disabled from supporting AER, then do nothing.

.. _`lpfc_aer_support_store.return`:

Return
------

length of the buf on success if val is in range the intended mode
is supported.
-EINVAL if val out of range or intended mode is not supported.

.. _`lpfc_aer_cleanup_state`:

lpfc_aer_cleanup_state
======================

.. c:function:: ssize_t lpfc_aer_cleanup_state(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Clean up aer state to the aer enabled device

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        containing flag 1 for aer cleanup state.

    :param size_t count:
        unused variable.

.. _`lpfc_aer_cleanup_state.description`:

Description
-----------

If the \ ``buf``\  contains 1 and the device currently has the AER support
enabled, then invokes the kernel AER helper routine
pci_cleanup_aer_uncorrect_error_status to clean up the uncorrectable
error status register.

.. _`lpfc_aer_cleanup_state.return`:

Return
------


-EINVAL if the buf does not contain the 1 or the device is not currently
enabled with the AER support.

.. _`lpfc_sriov_nr_virtfn_store`:

lpfc_sriov_nr_virtfn_store
==========================

.. c:function:: ssize_t lpfc_sriov_nr_virtfn_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Enable the adapter for sr-iov virtual functions

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        containing the string the number of vfs to be enabled.

    :param size_t count:
        unused variable.

.. _`lpfc_sriov_nr_virtfn_store.description`:

Description
-----------

When this api is called either through user sysfs, the driver shall
try to enable or disable SR-IOV virtual functions according to the

.. _`lpfc_sriov_nr_virtfn_store.following`:

following
---------


If zero virtual function has been enabled to the physical function,
the driver shall invoke the pci enable virtual function api trying
to enable the virtual functions. If the nr_vfn provided is greater
than the maximum supported, the maximum virtual function number will
be used for invoking the api; otherwise, the nr_vfn provided shall
be used for invoking the api. If the api call returned success, the
actual number of virtual functions enabled will be set to the driver
cfg_sriov_nr_virtfn; otherwise, -EINVAL shall be returned and driver
cfg_sriov_nr_virtfn remains zero.

If none-zero virtual functions have already been enabled to the
physical function, as reflected by the driver's cfg_sriov_nr_virtfn,
-EINVAL will be returned and the driver does nothing;

If the nr_vfn provided is zero and none-zero virtual functions have
been enabled, as indicated by the driver's cfg_sriov_nr_virtfn, the
disabling virtual function api shall be invoded to disable all the
virtual functions and driver's cfg_sriov_nr_virtfn shall be set to
zero. Otherwise, if zero virtual function has been enabled, do
nothing.

.. _`lpfc_sriov_nr_virtfn_store.return`:

Return
------

length of the buf on success if val is in range the intended mode
is supported.
-EINVAL if val out of range or intended mode is not supported.

.. _`lpfc_request_firmware_upgrade_store`:

lpfc_request_firmware_upgrade_store
===================================

.. c:function:: ssize_t lpfc_request_firmware_upgrade_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Request for Linux generic firmware upgrade

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        containing the string the number of vfs to be enabled.

    :param size_t count:
        unused variable.

.. _`lpfc_request_firmware_upgrade_store.return`:

Return
------


length of the buf on success if val is in range the intended mode
is supported.
-EINVAL if val out of range or intended mode is not supported.

.. _`lpfc_request_firmware_upgrade_init`:

lpfc_request_firmware_upgrade_init
==================================

.. c:function:: int lpfc_request_firmware_upgrade_init(struct lpfc_hba *phba, int val)

    Enable initial linux generic fw upgrade

    :param struct lpfc_hba \*phba:
        lpfc_hba pointer.

    :param int val:
        0 or 1.

.. _`lpfc_request_firmware_upgrade_init.description`:

Description
-----------

Set the initial Linux generic firmware upgrade enable or disable flag.

.. _`lpfc_request_firmware_upgrade_init.return`:

Return
------

zero if val saved.
-EINVAL val out of range

.. _`lpfc_fcp_imax_store`:

lpfc_fcp_imax_store
===================

.. c:function:: ssize_t lpfc_fcp_imax_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        string with the number of fast-path FCP interrupts per second.

    :param size_t count:
        unused variable.

.. _`lpfc_fcp_imax_store.description`:

Description
-----------

If val is in a valid range [636,651042], then set the adapter's
maximum number of fast-path FCP interrupts per second.

.. _`lpfc_fcp_imax_store.return`:

Return
------

length of the buf on success if val is in range the intended mode
is supported.
-EINVAL if val out of range or intended mode is not supported.

.. _`lpfc_fcp_imax_init`:

lpfc_fcp_imax_init
==================

.. c:function:: int lpfc_fcp_imax_init(struct lpfc_hba *phba, int val)

    Set the initial sr-iov virtual function enable

    :param struct lpfc_hba \*phba:
        lpfc_hba pointer.

    :param int val:
        link speed value.

.. _`lpfc_fcp_imax_init.description`:

Description
-----------

If val is in a valid range [636,651042], then initialize the adapter's
maximum number of fast-path FCP interrupts per second.

.. _`lpfc_fcp_imax_init.return`:

Return
------

zero if val saved.
-EINVAL val out of range

.. _`lpfc_fcp_cpu_map_show`:

lpfc_fcp_cpu_map_show
=====================

.. c:function:: ssize_t lpfc_fcp_cpu_map_show(struct device *dev, struct device_attribute *attr, char *buf)

    Display current driver CPU affinity

    :param struct device \*dev:
        class converted to a Scsi_host structure.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        on return contains text describing the state of the link.

.. _`lpfc_fcp_cpu_map_show.return`:

Return
------

size of formatted string.

.. _`lpfc_fcp_cpu_map_store`:

lpfc_fcp_cpu_map_store
======================

.. c:function:: ssize_t lpfc_fcp_cpu_map_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Change CPU affinity of driver vectors

    :param struct device \*dev:
        class device that is converted into a Scsi_host.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param const char \*buf:
        one or more lpfc_polling_flags values.

    :param size_t count:
        not used.

.. _`lpfc_fcp_cpu_map_store.return`:

Return
------

-EINVAL  - Not implemented yet.

.. _`lpfc_fcp_cpu_map_init`:

lpfc_fcp_cpu_map_init
=====================

.. c:function:: int lpfc_fcp_cpu_map_init(struct lpfc_hba *phba, int val)

    Set the initial sr-iov virtual function enable

    :param struct lpfc_hba \*phba:
        lpfc_hba pointer.

    :param int val:
        link speed value.

.. _`lpfc_fcp_cpu_map_init.description`:

Description
-----------

If val is in a valid range [0-2], then affinitze the adapter's
MSIX vectors.

.. _`lpfc_fcp_cpu_map_init.return`:

Return
------

zero if val saved.
-EINVAL val out of range

.. _`sysfs_ctlreg_write`:

sysfs_ctlreg_write
==================

.. c:function:: ssize_t sysfs_ctlreg_write(struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buf, loff_t off, size_t count)

    Write method for writing to ctlreg

    :param struct file \*filp:
        open sysfs file

    :param struct kobject \*kobj:
        kernel kobject that contains the kernel class device.

    :param struct bin_attribute \*bin_attr:
        kernel attributes passed to us.

    :param char \*buf:
        contains the data to be written to the adapter IOREG space.

    :param loff_t off:
        offset into buffer to beginning of data.

    :param size_t count:
        bytes to transfer.

.. _`sysfs_ctlreg_write.description`:

Description
-----------

Accessed via /sys/class/scsi_host/hostxxx/ctlreg.
Uses the adapter io control registers to send buf contents to the adapter.

.. _`sysfs_ctlreg_write.return`:

Return
------

-ERANGE off and count combo out of range
-EINVAL off, count or buff address invalid
-EPERM adapter is offline
value of count, buf contents written

.. _`sysfs_ctlreg_read`:

sysfs_ctlreg_read
=================

.. c:function:: ssize_t sysfs_ctlreg_read(struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buf, loff_t off, size_t count)

    Read method for reading from ctlreg

    :param struct file \*filp:
        open sysfs file

    :param struct kobject \*kobj:
        kernel kobject that contains the kernel class device.

    :param struct bin_attribute \*bin_attr:
        kernel attributes passed to us.

    :param char \*buf:
        if successful contains the data from the adapter IOREG space.

    :param loff_t off:
        offset into buffer to beginning of data.

    :param size_t count:
        bytes to transfer.

.. _`sysfs_ctlreg_read.description`:

Description
-----------

Accessed via /sys/class/scsi_host/hostxxx/ctlreg.
Uses the adapter io control registers to read data into buf.

.. _`sysfs_ctlreg_read.return`:

Return
------

-ERANGE off and count combo out of range
-EINVAL off, count or buff address invalid
value of count, buf contents read

.. _`sysfs_mbox_write`:

sysfs_mbox_write
================

.. c:function:: ssize_t sysfs_mbox_write(struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buf, loff_t off, size_t count)

    Write method for writing information via mbox

    :param struct file \*filp:
        open sysfs file

    :param struct kobject \*kobj:
        kernel kobject that contains the kernel class device.

    :param struct bin_attribute \*bin_attr:
        kernel attributes passed to us.

    :param char \*buf:
        contains the data to be written to sysfs mbox.

    :param loff_t off:
        offset into buffer to beginning of data.

    :param size_t count:
        bytes to transfer.

.. _`sysfs_mbox_write.description`:

Description
-----------

Deprecated function. All mailbox access from user space is performed via the
bsg interface.

.. _`sysfs_mbox_write.return`:

Return
------

-EPERM operation not permitted

.. _`sysfs_mbox_read`:

sysfs_mbox_read
===============

.. c:function:: ssize_t sysfs_mbox_read(struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buf, loff_t off, size_t count)

    Read method for reading information via mbox

    :param struct file \*filp:
        open sysfs file

    :param struct kobject \*kobj:
        kernel kobject that contains the kernel class device.

    :param struct bin_attribute \*bin_attr:
        kernel attributes passed to us.

    :param char \*buf:
        contains the data to be read from sysfs mbox.

    :param loff_t off:
        offset into buffer to beginning of data.

    :param size_t count:
        bytes to transfer.

.. _`sysfs_mbox_read.description`:

Description
-----------

Deprecated function. All mailbox access from user space is performed via the
bsg interface.

.. _`sysfs_mbox_read.return`:

Return
------

-EPERM operation not permitted

.. _`lpfc_alloc_sysfs_attr`:

lpfc_alloc_sysfs_attr
=====================

.. c:function:: int lpfc_alloc_sysfs_attr(struct lpfc_vport *vport)

    Creates the ctlreg and mbox entries

    :param struct lpfc_vport \*vport:
        address of lpfc vport structure.

.. _`lpfc_alloc_sysfs_attr.return-codes`:

Return codes
------------

zero on success
error return code from \ :c:func:`sysfs_create_bin_file`\ 

.. _`lpfc_free_sysfs_attr`:

lpfc_free_sysfs_attr
====================

.. c:function:: void lpfc_free_sysfs_attr(struct lpfc_vport *vport)

    Removes the ctlreg and mbox entries

    :param struct lpfc_vport \*vport:
        address of lpfc vport structure.

.. _`lpfc_get_host_symbolic_name`:

lpfc_get_host_symbolic_name
===========================

.. c:function:: void lpfc_get_host_symbolic_name(struct Scsi_Host *shost)

    Copy symbolic name into the scsi host

    :param struct Scsi_Host \*shost:
        kernel scsi host pointer.

.. _`lpfc_get_host_port_id`:

lpfc_get_host_port_id
=====================

.. c:function:: void lpfc_get_host_port_id(struct Scsi_Host *shost)

    Copy the vport DID into the scsi host port id

    :param struct Scsi_Host \*shost:
        kernel scsi host pointer.

.. _`lpfc_get_host_port_type`:

lpfc_get_host_port_type
=======================

.. c:function:: void lpfc_get_host_port_type(struct Scsi_Host *shost)

    Set the value of the scsi host port type

    :param struct Scsi_Host \*shost:
        kernel scsi host pointer.

.. _`lpfc_get_host_port_state`:

lpfc_get_host_port_state
========================

.. c:function:: void lpfc_get_host_port_state(struct Scsi_Host *shost)

    Set the value of the scsi host port state

    :param struct Scsi_Host \*shost:
        kernel scsi host pointer.

.. _`lpfc_get_host_speed`:

lpfc_get_host_speed
===================

.. c:function:: void lpfc_get_host_speed(struct Scsi_Host *shost)

    Set the value of the scsi host speed

    :param struct Scsi_Host \*shost:
        kernel scsi host pointer.

.. _`lpfc_get_host_fabric_name`:

lpfc_get_host_fabric_name
=========================

.. c:function:: void lpfc_get_host_fabric_name(struct Scsi_Host *shost)

    Set the value of the scsi host fabric name

    :param struct Scsi_Host \*shost:
        kernel scsi host pointer.

.. _`lpfc_get_stats`:

lpfc_get_stats
==============

.. c:function:: struct fc_host_statistics *lpfc_get_stats(struct Scsi_Host *shost)

    Return statistical information about the adapter

    :param struct Scsi_Host \*shost:
        kernel scsi host pointer.

.. _`lpfc_get_stats.notes`:

Notes
-----

NULL on error for link down, no mbox pool, sli2 active,
management not allowed, memory allocation error, or mbox error.

.. _`lpfc_get_stats.return`:

Return
------

NULL for error
address of the adapter host statistics

.. _`lpfc_reset_stats`:

lpfc_reset_stats
================

.. c:function:: void lpfc_reset_stats(struct Scsi_Host *shost)

    Copy the adapter link stats information

    :param struct Scsi_Host \*shost:
        kernel scsi host pointer.

.. _`lpfc_get_node_by_target`:

lpfc_get_node_by_target
=======================

.. c:function:: struct lpfc_nodelist *lpfc_get_node_by_target(struct scsi_target *starget)

    Return the nodelist for a target

    :param struct scsi_target \*starget:
        kernel scsi target pointer.

.. _`lpfc_get_node_by_target.return`:

Return
------

address of the node list if found
NULL target not found

.. _`lpfc_get_starget_port_id`:

lpfc_get_starget_port_id
========================

.. c:function:: void lpfc_get_starget_port_id(struct scsi_target *starget)

    Set the target port id to the ndlp DID or -1

    :param struct scsi_target \*starget:
        kernel scsi target pointer.

.. _`lpfc_get_starget_node_name`:

lpfc_get_starget_node_name
==========================

.. c:function:: void lpfc_get_starget_node_name(struct scsi_target *starget)

    Set the target node name

    :param struct scsi_target \*starget:
        kernel scsi target pointer.

.. _`lpfc_get_starget_node_name.description`:

Description
-----------

Set the target node name to the ndlp node name wwn or zero.

.. _`lpfc_get_starget_port_name`:

lpfc_get_starget_port_name
==========================

.. c:function:: void lpfc_get_starget_port_name(struct scsi_target *starget)

    Set the target port name

    :param struct scsi_target \*starget:
        kernel scsi target pointer.

.. _`lpfc_get_starget_port_name.description`:

Description
-----------

set the target port name to the ndlp port name wwn or zero.

.. _`lpfc_set_rport_loss_tmo`:

lpfc_set_rport_loss_tmo
=======================

.. c:function:: void lpfc_set_rport_loss_tmo(struct fc_rport *rport, uint32_t timeout)

    Set the rport dev loss tmo

    :param struct fc_rport \*rport:
        fc rport address.

    :param uint32_t timeout:
        new value for dev loss tmo.

.. _`lpfc_set_rport_loss_tmo.description`:

Description
-----------

If timeout is non zero set the dev_loss_tmo to timeout, else set
dev_loss_tmo to one.

.. _`lpfc_rport_show_function`:

lpfc_rport_show_function
========================

.. c:function::  lpfc_rport_show_function( field,  format_string,  sz,  cast)

    Return rport target information

    :param  field:
        *undescribed*

    :param  format_string:
        *undescribed*

    :param  sz:
        *undescribed*

    :param  cast:
        *undescribed*

.. _`lpfc_rport_show_function.description`:

Description
-----------

Macro that uses field to generate a function with the name lpfc_show_rport\_

lpfc_show_rport_##field: returns the bytes formatted in buf

.. _`lpfc_rport_show_function.return`:

Return
------

size of formatted string.

.. _`lpfc_set_vport_symbolic_name`:

lpfc_set_vport_symbolic_name
============================

.. c:function:: void lpfc_set_vport_symbolic_name(struct fc_vport *fc_vport)

    Set the vport's symbolic name

    :param struct fc_vport \*fc_vport:
        The fc_vport who's symbolic name has been changed.

.. _`lpfc_set_vport_symbolic_name.description`:

Description
-----------

This function is called by the transport after the \ ``fc_vport``\ 's symbolic name
has been changed. This function re-registers the symbolic name with the
switch to propagate the change into the fabric if the vport is active.

.. _`lpfc_hba_log_verbose_init`:

lpfc_hba_log_verbose_init
=========================

.. c:function:: void lpfc_hba_log_verbose_init(struct lpfc_hba *phba, uint32_t verbose)

    Set hba's log verbose level

    :param struct lpfc_hba \*phba:
        Pointer to lpfc_hba struct.

    :param uint32_t verbose:
        *undescribed*

.. _`lpfc_hba_log_verbose_init.description`:

Description
-----------

This function is called by the \ :c:func:`lpfc_get_cfgparam`\  routine to set the
module lpfc_log_verbose into the \ ``phba``\  cfg_log_verbose for use with
log message according to the module's lpfc_log_verbose parameter setting
before hba port or vport created.

.. _`lpfc_get_cfgparam`:

lpfc_get_cfgparam
=================

.. c:function:: void lpfc_get_cfgparam(struct lpfc_hba *phba)

    Used during probe_one to init the adapter structure

    :param struct lpfc_hba \*phba:
        lpfc_hba pointer.

.. _`lpfc_nvme_mod_param_dep`:

lpfc_nvme_mod_param_dep
=======================

.. c:function:: void lpfc_nvme_mod_param_dep(struct lpfc_hba *phba)

    Adjust module parameter value based on dependencies between protocols and roles.

    :param struct lpfc_hba \*phba:
        lpfc_hba pointer.

.. _`lpfc_get_vport_cfgparam`:

lpfc_get_vport_cfgparam
=======================

.. c:function:: void lpfc_get_vport_cfgparam(struct lpfc_vport *vport)

    Used during port create, init the vport structure

    :param struct lpfc_vport \*vport:
        lpfc_vport pointer.

.. This file was automatic generated / don't edit.

