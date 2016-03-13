.. -*- coding: utf-8; mode: rst -*-

============
smscoreapi.c
============



.. _xref_smscore_register_hotplug:

smscore_register_hotplug
========================

.. c:function:: int smscore_register_hotplug (hotplug_t hotplug)

    

    :param hotplug_t hotplug:

        _undescribed_



NOTE
----

if devices exist callback is called immediately for each device


**param** hotplug callback


**return** 0 on success, <0 on error.




.. _xref_smscore_unregister_hotplug:

smscore_unregister_hotplug
==========================

.. c:function:: void smscore_unregister_hotplug (hotplug_t hotplug)

    

    :param hotplug_t hotplug:

        _undescribed_



Description
-----------



**param** hotplug callback




.. _xref_smscore_register_device:

smscore_register_device
=======================

.. c:function:: int smscore_register_device (struct smsdevice_params_t * params, struct smscore_device_t ** coredev, void * mdev)

    

    :param struct smsdevice_params_t * params:

        _undescribed_

    :param struct smscore_device_t ** coredev:

        _undescribed_

    :param void * mdev:

        _undescribed_



Description
-----------

creates buffer mappings, notifies registered hotplugs about new device.


**param** params device pointer to struct with device specific parameters
              and handlers
**param** coredev pointer to a value that receives created coredev object


**return** 0 on success, <0 on error.




.. _xref_smscore_init_ir:

smscore_init_ir
===============

.. c:function:: int smscore_init_ir (struct smscore_device_t * coredev)

    

    :param struct smscore_device_t * coredev:

        _undescribed_



Description
-----------



**return** 0 on success, < 0 on error.




.. _xref_smscore_configure_board:

smscore_configure_board
=======================

.. c:function:: int smscore_configure_board (struct smscore_device_t * coredev)

    

    :param struct smscore_device_t * coredev:

        _undescribed_



Description
-----------



**param** coredev pointer to a coredev object returned by
               smscore_register_device


**return** 0 on success, <0 on error.




.. _xref_smscore_start_device:

smscore_start_device
====================

.. c:function:: int smscore_start_device (struct smscore_device_t * coredev)

    

    :param struct smscore_device_t * coredev:

        _undescribed_



Description
-----------



**param** coredev pointer to a coredev object returned by
		  smscore_register_device


**return** 0 on success, <0 on error.




.. _xref_smscore_get_fw_filename:

smscore_get_fw_filename
=======================

.. c:function:: char * smscore_get_fw_filename (struct smscore_device_t * coredev, int mode)

    

    :param struct smscore_device_t * coredev:

        _undescribed_

    :param int mode:

        _undescribed_



Description
-----------

smscore_fw_lkup.
**param** coredev pointer to a coredev object returned by
		  smscore_register_device
**param** mode requested mode of operation
**param** lookup if 1, always get the fw filename from smscore_fw_lkup
	 table. if 0, try first to get from sms_boards


**return** 0 on success, <0 on error.




.. _xref_smscore_load_firmware_from_file:

smscore_load_firmware_from_file
===============================

.. c:function:: int smscore_load_firmware_from_file (struct smscore_device_t * coredev, int mode, loadfirmware_t loadfirmware_handler)

    

    :param struct smscore_device_t * coredev:

        _undescribed_

    :param int mode:

        _undescribed_

    :param loadfirmware_t loadfirmware_handler:

        _undescribed_



Description
-----------



**param** coredev pointer to a coredev object returned by
               smscore_register_device
**param** filename null-terminated string specifies firmware file name
**param** loadfirmware_handler device handler that loads firmware


**return** 0 on success, <0 on error.




.. _xref_smscore_unregister_device:

smscore_unregister_device
=========================

.. c:function:: void smscore_unregister_device (struct smscore_device_t * coredev)

    

    :param struct smscore_device_t * coredev:

        _undescribed_



Description
-----------

frees all buffers and coredev object


**param** coredev pointer to a coredev object returned by
               smscore_register_device


**return** 0 on success, <0 on error.




.. _xref_smscore_init_device:

smscore_init_device
===================

.. c:function:: int smscore_init_device (struct smscore_device_t * coredev, int mode)

    

    :param struct smscore_device_t * coredev:

        _undescribed_

    :param int mode:

        _undescribed_



Description
-----------



**param** coredev pointer to a coredev object returned by
               smscore_register_device
**param** mode requested mode of operation


**return** 0 on success, <0 on error.




.. _xref_smscore_set_device_mode:

smscore_set_device_mode
=======================

.. c:function:: int smscore_set_device_mode (struct smscore_device_t * coredev, int mode)

    

    :param struct smscore_device_t * coredev:

        _undescribed_

    :param int mode:

        _undescribed_



NOTE
----

stellar/usb may disconnect when changing mode


**param** coredev pointer to a coredev object returned by
               smscore_register_device
**param** mode requested mode of operation


**return** 0 on success, <0 on error.




.. _xref_smscore_get_device_mode:

smscore_get_device_mode
=======================

.. c:function:: int smscore_get_device_mode (struct smscore_device_t * coredev)

    

    :param struct smscore_device_t * coredev:

        _undescribed_



Description
-----------



**param** coredev pointer to a coredev object returned by
               smscore_register_device


**return** current mode




.. _xref_smscore_find_client:

smscore_find_client
===================

.. c:function:: struct smscore_client_t * smscore_find_client (struct smscore_device_t * coredev, int data_type, int id)

    

    :param struct smscore_device_t * coredev:

        _undescribed_

    :param int data_type:

        _undescribed_

    :param int id:

        _undescribed_



Description
-----------

return client handle or NULL.


**param** coredev pointer to a coredev object returned by
               smscore_register_device
**param** data_type client data type (SMS_DONT_CARE for all types)
**param** id client id (SMS_DONT_CARE for all id)




.. _xref_smscore_onresponse:

smscore_onresponse
==================

.. c:function:: void smscore_onresponse (struct smscore_device_t * coredev, struct smscore_buffer_t * cb)

    

    :param struct smscore_device_t * coredev:

        _undescribed_

    :param struct smscore_buffer_t * cb:

        _undescribed_



Description
-----------

return buffer to pool on error


**param** coredev pointer to a coredev object returned by
               smscore_register_device
**param** cb pointer to response buffer descriptor




.. _xref_get_entry:

get_entry
=========

.. c:function:: struct smscore_buffer_t * get_entry (struct smscore_device_t * coredev)

    

    :param struct smscore_device_t * coredev:

        _undescribed_



Description
-----------



**param** coredev pointer to a coredev object returned by
               smscore_register_device


**return** pointer to descriptor on success, NULL on error.




.. _xref_smscore_putbuffer:

smscore_putbuffer
=================

.. c:function:: void smscore_putbuffer (struct smscore_device_t * coredev, struct smscore_buffer_t * cb)

    

    :param struct smscore_device_t * coredev:

        _undescribed_

    :param struct smscore_buffer_t * cb:

        _undescribed_



Description
-----------



**param** coredev pointer to a coredev object returned by
               smscore_register_device
**param** cb pointer buffer descriptor




.. _xref_smscore_register_client:

smscore_register_client
=======================

.. c:function:: int smscore_register_client (struct smscore_device_t * coredev, struct smsclient_params_t * params, struct smscore_client_t ** client)

    

    :param struct smscore_device_t * coredev:

        _undescribed_

    :param struct smsclient_params_t * params:

        _undescribed_

    :param struct smscore_client_t ** client:

        _undescribed_



Description
-----------



**param** coredev pointer to a coredev object from clients hotplug
**param** initial_id all messages with this id would be sent to this client
**param** data_type all messages of this type would be sent to this client
**param** onresponse_handler client handler that is called to
                          process incoming messages
**param** onremove_handler client handler that is called when device is removed
**param** context client-specific context
**param** client pointer to a value that receives created smsclient object


**return** 0 on success, <0 on error.




.. _xref_smscore_unregister_client:

smscore_unregister_client
=========================

.. c:function:: void smscore_unregister_client (struct smscore_client_t * client)

    

    :param struct smscore_client_t * client:

        _undescribed_



Description
-----------



**param** client pointer to smsclient object returned by
              smscore_register_client




.. _xref_smsclient_sendrequest:

smsclient_sendrequest
=====================

.. c:function:: int smsclient_sendrequest (struct smscore_client_t * client, void * buffer, size_t size)

    

    :param struct smscore_client_t * client:

        _undescribed_

    :param void * buffer:

        _undescribed_

    :param size_t size:

        _undescribed_



Description
-----------

calls device handler to send requests to the device


**param** client pointer to smsclient object returned by
              smscore_register_client
**param** buffer pointer to a request buffer
**param** size size (in bytes) of request buffer


**return** 0 on success, <0 on error.


