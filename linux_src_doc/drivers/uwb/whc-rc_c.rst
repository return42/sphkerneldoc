.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/whc-rc.c

.. _`whcrc_cmd`:

whcrc_cmd
=========

.. c:function:: int whcrc_cmd(struct uwb_rc *uwb_rc, const struct uwb_rccb *cmd, size_t cmd_size)

    :param uwb_rc:
        *undescribed*
    :type uwb_rc: struct uwb_rc \*

    :param cmd:
        Buffer containing the RCCB and payload to execute
    :type cmd: const struct uwb_rccb \*

    :param cmd_size:
        Size of the command buffer.
    :type cmd_size: size_t

.. _`whcrc_cmd.description`:

Description
-----------

We copy the command into whcrc->cmd_buf (as it is pretty and
aligned\`and physically contiguous) and then press the right keys in
the controller's URCCMD register to get it to read it. We might
have to wait for the cmd_sem to be open to us.

.. _`whcrc_cmd.note`:

NOTE
----

rc's mutex has to be locked

.. _`whcrc_enable_events`:

whcrc_enable_events
===================

.. c:function:: void whcrc_enable_events(struct whcrc *whcrc)

    :param whcrc:
        *undescribed*
    :type whcrc: struct whcrc \*

.. _`whcrc_enable_events.description`:

Description
-----------

We have read all the events in the event buffer, so we are ready to
reset it to the beginning.

This is only called during initialization or after an event buffer
has been retired.  This means we can be sure that event processing
is disabled and it's safe to update the URCEVTADDR register.

There's no need to wait for the event processing to start as the
URC will not clear URCCMD_ACTIVE until (internal) event buffer
space is available.

.. _`whcrc_irq_cb`:

whcrc_irq_cb
============

.. c:function:: irqreturn_t whcrc_irq_cb(int irq, void *_whcrc)

    :param irq:
        *undescribed*
    :type irq: int

    :param _whcrc:
        *undescribed*
    :type _whcrc: void \*

.. _`whcrc_irq_cb.description`:

Description
-----------

We ack inmediately (and expect the hw to do the right thing and
raise another IRQ if things have changed :)

.. _`whcrc_setup_rc_umc`:

whcrc_setup_rc_umc
==================

.. c:function:: int whcrc_setup_rc_umc(struct whcrc *whcrc)

    map regions, get (shared) IRQ

    :param whcrc:
        *undescribed*
    :type whcrc: struct whcrc \*

.. _`whcrc_release_rc_umc`:

whcrc_release_rc_umc
====================

.. c:function:: void whcrc_release_rc_umc(struct whcrc *whcrc)

    :param whcrc:
        *undescribed*
    :type whcrc: struct whcrc \*

.. _`whcrc_start_rc`:

whcrc_start_rc
==============

.. c:function:: int whcrc_start_rc(struct uwb_rc *rc)

    start a WHCI radio controller

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

.. _`whcrc_start_rc.description`:

Description
-----------

Reset the UMC device, start the radio controller, enable events and
finally enable interrupts.

.. _`whcrc_stop_rc`:

whcrc_stop_rc
=============

.. c:function:: void whcrc_stop_rc(struct uwb_rc *rc)

    stop a WHCI radio controller

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

.. _`whcrc_stop_rc.description`:

Description
-----------

Disable interrupts and cancel any pending event processing work
before clearing the Run/Stop bit.

.. _`whcrc_probe`:

whcrc_probe
===========

.. c:function:: int whcrc_probe(struct umc_dev *umc_dev)

    :param umc_dev:
        *undescribed*
    :type umc_dev: struct umc_dev \*

.. _`whcrc_probe.note`:

NOTE
----

we setup whcrc->uwb_rc before calling \ :c:func:`uwb_rc_add`\ ; in the
IRQ handler we use that to determine if the hw is ready to
handle events. Looks like a race condition, but it really is
not.

.. _`whcrc_remove`:

whcrc_remove
============

.. c:function:: void whcrc_remove(struct umc_dev *umc_dev)

    :param umc_dev:
        *undescribed*
    :type umc_dev: struct umc_dev \*

.. _`whcrc_remove.description`:

Description
-----------

When we up the command semaphore, everybody possibly held trying to
execute a command should be granted entry and then they'll see the
host is quiescing and up it (so it will chain to the next waiter).
This should not happen (in any case), as we can only remove when
there are no handles open...

.. This file was automatic generated / don't edit.

