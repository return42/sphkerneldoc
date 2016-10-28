.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/isdn/capi/kcapi.c

.. _`capi_ctr_handle_message`:

capi_ctr_handle_message
=======================

.. c:function:: void capi_ctr_handle_message(struct capi_ctr *ctr, u16 appl, struct sk_buff *skb)

    handle incoming CAPI message

    :param struct capi_ctr \*ctr:
        controller descriptor structure.

    :param u16 appl:
        application ID.

    :param struct sk_buff \*skb:
        message.

.. _`capi_ctr_handle_message.description`:

Description
-----------

Called by hardware driver to pass a CAPI message to the application.

.. _`capi_ctr_ready`:

capi_ctr_ready
==============

.. c:function:: void capi_ctr_ready(struct capi_ctr *ctr)

    signal CAPI controller ready

    :param struct capi_ctr \*ctr:
        controller descriptor structure.

.. _`capi_ctr_ready.description`:

Description
-----------

Called by hardware driver to signal that the controller is up and running.

.. _`capi_ctr_down`:

capi_ctr_down
=============

.. c:function:: void capi_ctr_down(struct capi_ctr *ctr)

    signal CAPI controller not ready

    :param struct capi_ctr \*ctr:
        controller descriptor structure.

.. _`capi_ctr_down.description`:

Description
-----------

Called by hardware driver to signal that the controller is down and
unavailable for use.

.. _`capi_ctr_suspend_output`:

capi_ctr_suspend_output
=======================

.. c:function:: void capi_ctr_suspend_output(struct capi_ctr *ctr)

    suspend controller

    :param struct capi_ctr \*ctr:
        controller descriptor structure.

.. _`capi_ctr_suspend_output.description`:

Description
-----------

Called by hardware driver to stop data flow.

.. _`capi_ctr_suspend_output.note`:

Note
----

The caller is responsible for synchronizing concurrent state changes
as well as invocations of capi_ctr_handle_message.

.. _`capi_ctr_resume_output`:

capi_ctr_resume_output
======================

.. c:function:: void capi_ctr_resume_output(struct capi_ctr *ctr)

    resume controller

    :param struct capi_ctr \*ctr:
        controller descriptor structure.

.. _`capi_ctr_resume_output.description`:

Description
-----------

Called by hardware driver to resume data flow.

.. _`capi_ctr_resume_output.note`:

Note
----

The caller is responsible for synchronizing concurrent state changes
as well as invocations of capi_ctr_handle_message.

.. _`attach_capi_ctr`:

attach_capi_ctr
===============

.. c:function:: int attach_capi_ctr(struct capi_ctr *ctr)

    register CAPI controller

    :param struct capi_ctr \*ctr:
        controller descriptor structure.

.. _`attach_capi_ctr.description`:

Description
-----------

Called by hardware driver to register a controller with the CAPI subsystem.

.. _`attach_capi_ctr.return-value`:

Return value
------------

0 on success, error code < 0 on error

.. _`detach_capi_ctr`:

detach_capi_ctr
===============

.. c:function:: int detach_capi_ctr(struct capi_ctr *ctr)

    unregister CAPI controller

    :param struct capi_ctr \*ctr:
        controller descriptor structure.

.. _`detach_capi_ctr.description`:

Description
-----------

Called by hardware driver to remove the registration of a controller
with the CAPI subsystem.

.. _`detach_capi_ctr.return-value`:

Return value
------------

0 on success, error code < 0 on error

.. _`register_capi_driver`:

register_capi_driver
====================

.. c:function:: void register_capi_driver(struct capi_driver *driver)

    register CAPI driver

    :param struct capi_driver \*driver:
        driver descriptor structure.

.. _`register_capi_driver.description`:

Description
-----------

Called by hardware driver to register itself with the CAPI subsystem.

.. _`unregister_capi_driver`:

unregister_capi_driver
======================

.. c:function:: void unregister_capi_driver(struct capi_driver *driver)

    unregister CAPI driver

    :param struct capi_driver \*driver:
        driver descriptor structure.

.. _`unregister_capi_driver.description`:

Description
-----------

Called by hardware driver to unregister itself from the CAPI subsystem.

.. _`capi20_isinstalled`:

capi20_isinstalled
==================

.. c:function:: u16 capi20_isinstalled( void)

    CAPI 2.0 operation CAPI_INSTALLED

    :param  void:
        no arguments

.. _`capi20_isinstalled.return-value`:

Return value
------------

CAPI result code (CAPI_NOERROR if at least one ISDN controller
is ready for use, CAPI_REGNOTINSTALLED otherwise)

.. _`capi20_register`:

capi20_register
===============

.. c:function:: u16 capi20_register(struct capi20_appl *ap)

    CAPI 2.0 operation CAPI_REGISTER

    :param struct capi20_appl \*ap:
        CAPI application descriptor structure.

.. _`capi20_register.description`:

Description
-----------

Register an application's presence with CAPI.
A unique application ID is assigned and stored in \ ``ap``\ ->applid.
After this function returns successfully, the message receive
callback function \ ``ap``\ ->\ :c:func:`recv_message`\  may be called at any time
until \ :c:func:`capi20_release`\  has been called for the same \ ``ap``\ .

.. _`capi20_register.return-value`:

Return value
------------

CAPI result code

.. _`capi20_release`:

capi20_release
==============

.. c:function:: u16 capi20_release(struct capi20_appl *ap)

    CAPI 2.0 operation CAPI_RELEASE

    :param struct capi20_appl \*ap:
        CAPI application descriptor structure.

.. _`capi20_release.description`:

Description
-----------

Terminate an application's registration with CAPI.
After this function returns successfully, the message receive
callback function \ ``ap``\ ->\ :c:func:`recv_message`\  will no longer be called.

.. _`capi20_release.return-value`:

Return value
------------

CAPI result code

.. _`capi20_put_message`:

capi20_put_message
==================

.. c:function:: u16 capi20_put_message(struct capi20_appl *ap, struct sk_buff *skb)

    CAPI 2.0 operation CAPI_PUT_MESSAGE

    :param struct capi20_appl \*ap:
        CAPI application descriptor structure.

    :param struct sk_buff \*skb:
        CAPI message.

.. _`capi20_put_message.description`:

Description
-----------

Transfer a single message to CAPI.

.. _`capi20_put_message.return-value`:

Return value
------------

CAPI result code

.. _`capi20_get_manufacturer`:

capi20_get_manufacturer
=======================

.. c:function:: u16 capi20_get_manufacturer(u32 contr, u8 *buf)

    CAPI 2.0 operation CAPI_GET_MANUFACTURER

    :param u32 contr:
        controller number.

    :param u8 \*buf:
        result buffer (64 bytes).

.. _`capi20_get_manufacturer.description`:

Description
-----------

Retrieve information about the manufacturer of the specified ISDN controller
or (for \ ``contr``\  == 0) the driver itself.

.. _`capi20_get_manufacturer.return-value`:

Return value
------------

CAPI result code

.. _`capi20_get_version`:

capi20_get_version
==================

.. c:function:: u16 capi20_get_version(u32 contr, struct capi_version *verp)

    CAPI 2.0 operation CAPI_GET_VERSION

    :param u32 contr:
        controller number.

    :param struct capi_version \*verp:
        result structure.

.. _`capi20_get_version.description`:

Description
-----------

Retrieve version information for the specified ISDN controller
or (for \ ``contr``\  == 0) the driver itself.

.. _`capi20_get_version.return-value`:

Return value
------------

CAPI result code

.. _`capi20_get_serial`:

capi20_get_serial
=================

.. c:function:: u16 capi20_get_serial(u32 contr, u8 *serial)

    CAPI 2.0 operation CAPI_GET_SERIAL_NUMBER

    :param u32 contr:
        controller number.

    :param u8 \*serial:
        result buffer (8 bytes).

.. _`capi20_get_serial.description`:

Description
-----------

Retrieve the serial number of the specified ISDN controller
or (for \ ``contr``\  == 0) the driver itself.

.. _`capi20_get_serial.return-value`:

Return value
------------

CAPI result code

.. _`capi20_get_profile`:

capi20_get_profile
==================

.. c:function:: u16 capi20_get_profile(u32 contr, struct capi_profile *profp)

    CAPI 2.0 operation CAPI_GET_PROFILE

    :param u32 contr:
        controller number.

    :param struct capi_profile \*profp:
        result structure.

.. _`capi20_get_profile.description`:

Description
-----------

Retrieve capability information for the specified ISDN controller
or (for \ ``contr``\  == 0) the number of installed controllers.

.. _`capi20_get_profile.return-value`:

Return value
------------

CAPI result code

.. _`capi20_manufacturer`:

capi20_manufacturer
===================

.. c:function:: int capi20_manufacturer(unsigned long cmd, void __user *data)

    CAPI 2.0 operation CAPI_MANUFACTURER

    :param unsigned long cmd:
        command.

    :param void __user \*data:
        parameter.

.. _`capi20_manufacturer.description`:

Description
-----------

Perform manufacturer specific command.

.. _`capi20_manufacturer.return-value`:

Return value
------------

CAPI result code

.. This file was automatic generated / don't edit.

