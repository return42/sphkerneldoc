.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/ti-st/st_kim.c

.. _`st_get_plat_device`:

st_get_plat_device
==================

.. c:function:: struct platform_device *st_get_plat_device(int id)

    function which returns the reference to the platform device requested by id. As of now only 1 such device exists (id=0) the context requesting for reference can get the id to be requested by a. The protocol driver which is registering or b. the tty device which is opened.

    :param int id:
        *undescribed*

.. _`validate_firmware_response`:

validate_firmware_response
==========================

.. c:function:: void validate_firmware_response(struct kim_data_s *kim_gdata)

    function to return whether the firmware response was proper in case of error don't complete so that waiting for proper response times out

    :param struct kim_data_s \*kim_gdata:
        *undescribed*

.. _`kim_int_recv`:

kim_int_recv
============

.. c:function:: void kim_int_recv(struct kim_data_s *kim_gdata, const unsigned char *data, long count)

    receive function called during firmware download firmware download responses on different UART drivers have been observed to come in bursts of different tty_receive and hence the logic

    :param struct kim_data_s \*kim_gdata:
        *undescribed*

    :param const unsigned char \*data:
        *undescribed*

    :param long count:
        *undescribed*

.. _`download_firmware`:

download_firmware
=================

.. c:function:: long download_firmware(struct kim_data_s *kim_gdata)

    internal function which parses through the .bts firmware script file intreprets SEND, DELAY actions only as of now

    :param struct kim_data_s \*kim_gdata:
        *undescribed*

.. _`st_kim_start`:

st_kim_start
============

.. c:function:: long st_kim_start(void *kim_data)

    called from ST Core upon 1st registration This involves toggling the chip enable gpio, reading the firmware version from chip, forming the fw file name based on the chip version, requesting the fw, parsing it and perform download(send/recv).

    :param void \*kim_data:
        *undescribed*

.. _`st_kim_stop`:

st_kim_stop
===========

.. c:function:: long st_kim_stop(void *kim_data)

    stop communication with chip. This can be called from ST Core/KIM, on the- (a) last un-register when chip need not be powered there-after, (b) upon failure to either install ldisc or download firmware. The function is responsible to (a) notify UIM about un-installation, (b) flush UART if the ldisc was installed. (c) reset BT_EN - pull down nshutdown at the end. (d) invoke platform's chip disabling routine.

    :param void \*kim_data:
        *undescribed*

.. _`st_kim_ref`:

st_kim_ref
==========

.. c:function:: void st_kim_ref(struct st_data_s **core_data, int id)

    reference the core's data This references the per-ST platform device in the arch/xx/ board-xx.c file. This would enable multiple such platform devices to exist on a given platform

    :param struct st_data_s \*\*core_data:
        *undescribed*

    :param int id:
        *undescribed*

.. This file was automatic generated / don't edit.

