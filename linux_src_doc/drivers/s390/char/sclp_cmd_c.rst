.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/char/sclp_cmd.c

.. _`sclp_chp_configure`:

sclp_chp_configure
==================

.. c:function:: int sclp_chp_configure(struct chp_id chpid)

    perform configure channel-path sclp command

    :param struct chp_id chpid:
        channel-path ID

.. _`sclp_chp_configure.description`:

Description
-----------

Perform configure channel-path command sclp command for specified chpid.
Return 0 after command successfully finished, non-zero otherwise.

.. _`sclp_chp_deconfigure`:

sclp_chp_deconfigure
====================

.. c:function:: int sclp_chp_deconfigure(struct chp_id chpid)

    perform deconfigure channel-path sclp command

    :param struct chp_id chpid:
        channel-path ID

.. _`sclp_chp_deconfigure.description`:

Description
-----------

Perform deconfigure channel-path command sclp command for specified chpid
and wait for completion. On success return 0. Return non-zero otherwise.

.. _`sclp_chp_read_info`:

sclp_chp_read_info
==================

.. c:function:: int sclp_chp_read_info(struct sclp_chp_info *info)

    perform read channel-path information sclp command

    :param struct sclp_chp_info \*info:
        resulting channel-path information data

.. _`sclp_chp_read_info.description`:

Description
-----------

Perform read channel-path information sclp command and wait for completion.
On success, store channel-path information in \ ``info``\  and return 0. Return
non-zero otherwise.

.. This file was automatic generated / don't edit.

